"""PB-18 验收辅助脚本：四条异常路径（越权 / 无号挂起 / 支付失败重试 / 无回执调查）。

正式步骤见 Ryan/2026-09-26/PB-14 同风格的
`PB-18_acceptance-test-plan_2026-09-29.md`（以 Tasklist 表单为准）。

联动：REST 完成用户任务；AT-04/05/06 需 Java（check-slot、request-payment、
mark-payment-investigate、dispatch-clinic-letter）。AT-03 故意用秘书角色提交
Accept，预期引擎应拒绝——教室 demo 无 RBAC 时如实记 FAIL。

Run (Camunda + mvn spring-boot:run already up):
  python scripts/pb18_acceptance.py
"""
from __future__ import annotations

import base64
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = os.environ.get("CAMUNDA_REST_URL", "http://localhost:8080").rstrip("/")
AUTH = base64.b64encode(
    (
        os.environ.get("CAMUNDA_USERNAME", "demo")
        + ":"
        + os.environ.get("CAMUNDA_PASSWORD", "demo")
    ).encode()
).decode()
PROCESS = "Hospital_All_Processes_Simple_C8"
ROOT = Path(__file__).resolve().parents[1]
STAMP = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
PREFIX = "PB18-" + STAMP
EVIDENCE: dict = {
    "run": PREFIX,
    "item": "PB-18",
    "method": "Camunda REST /v2; labelled synthetic instances",
    "tests": [],
}


def api(method: str, path: str, body=None):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(
        BASE + "/v2" + path,
        data=data,
        method=method,
        headers={
            "Authorization": "Basic " + AUTH,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            raw = response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise RuntimeError(
            f"{method} {path}: {error.code} {error.read().decode()}"
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Camunda REST unreachable at {BASE}: {error}") from error


def wait_for(fn, description: str, timeout: float = 90):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        value = fn()
        if value:
            return value
        time.sleep(0.5)
    raise AssertionError("Timed out: " + description)


def find_task(instance: str, element: str):
    def lookup():
        tasks = api(
            "POST",
            "/user-tasks/search",
            {"filter": {"processInstanceKey": instance, "state": "CREATED"}},
        )["items"]
        return next((t for t in tasks if t["elementId"] == element), None)

    return wait_for(lookup, element + " in " + instance)


def complete(record: dict, element: str, **variables):
    item = find_task(record["processInstanceKey"], element)
    values = {
        "patientId": record["case"],
        "staffRole": "PB-18 / acceptance",
        "clinicianId": "CONSULTANT-PB18",
        "specialty": "oncology",
        "priority": "routine",
        "timeframe": "within 2 weeks",
        "notes": "PB-18 acceptance run",
        "decisionReason": "PB-18 recorded reason",
        "action": "recorded",
        "charge_amount": "10.01",
    }
    values.update(variables)
    api(
        "POST",
        f"/user-tasks/{item['userTaskKey']}/completion",
        {"variables": values},
    )
    record["tasks"].append(
        {
            "element": element,
            "userTaskKey": item["userTaskKey"],
            "action": values.get("action"),
            "staffRole": values.get("staffRole"),
            "charge_amount": values.get("charge_amount"),
        }
    )


def start(definition_key, test_id: str, scenario: str):
    case = PREFIX + "-" + scenario
    instance = api(
        "POST",
        "/process-instances",
        {
            "processDefinitionKey": definition_key,
            "variables": {"patientId": case},
        },
    )
    record = {
        "id": test_id,
        "scenario": scenario,
        "case": case,
        "processInstanceKey": str(instance["processInstanceKey"]),
        "tasks": [],
        "checks": {},
    }
    EVIDENCE["tests"].append(record)
    return record


def variables(instance: str) -> dict:
    items = api(
        "POST",
        "/variables/search",
        {"filter": {"processInstanceKey": instance}, "page": {"limit": 200}},
    )["items"]
    decoded = {}
    for item in items:
        if item.get("isTruncated", False):
            continue
        try:
            decoded[item["name"]] = json.loads(item["value"])
        except json.JSONDecodeError:
            decoded[item["name"]] = item["value"]
    return decoded


def active_incidents(instance: str) -> list:
    return api(
        "POST",
        "/incidents/search",
        {"filter": {"processInstanceKey": instance, "state": "ACTIVE"}},
    )["items"]


def task_exists_now(instance: str, element: str) -> bool:
    tasks = api(
        "POST",
        "/user-tasks/search",
        {"filter": {"processInstanceKey": instance, "state": "CREATED"}},
    )["items"]
    return any(t["elementId"] == element for t in tasks)


def reach_after_accept_booked(record: dict):
    complete(record, "Register", action="referral", notes="PB-18 docs checked")
    complete(
        record,
        "ReviewReferral",
        action="accept",
        clinicianId="CONSULTANT-PB18",
        decisionReason="Accepted for PB-18 path",
        staffRole="Consultant / PB-18",
    )
    find_task(record["processInstanceKey"], "BookVisit")


def reach_funding(record: dict):
    """Accept → attend → treat → letter sent → Funding user task."""
    reach_after_accept_booked(record)
    complete(
        record,
        "BookVisit",
        action="attended",
        staffRole="Outpatient Bookings / PB-18",
        notes="Slot confirmed for PB-18 payment path",
    )
    find_task(record["processInstanceKey"], "ClinicalCare")
    complete(
        record,
        "ClinicalCare",
        action="treatment",
        staffRole="Consultant / PB-18",
        notes="Authorise treatment for funding tests",
    )
    find_task(record["processInstanceKey"], "DispatchLetter")
    complete(
        record,
        "DispatchLetter",
        action="sent",
        staffRole="Medical Secretary / PB-18",
        notes="Approved letter sent",
    )
    find_task(record["processInstanceKey"], "Funding")


def wait_task_or_none(instance: str, element: str, timeout: float = 20):
    """Return task if it appears within timeout, else None (no AssertionError)."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if task_exists_now(instance, element):
            return True
        time.sleep(0.4)
    return False


def run_at03(definition_key):
    """Unauthorised: Medical Secretary submits Accept — case requires refusal."""
    record = start(definition_key, "AT-03", "UNAUTH")
    complete(record, "Register", action="referral", notes="PB-18 AT-03")
    complete(
        record,
        "ReviewReferral",
        action="accept",
        staffRole="Medical Secretary / not authorised to accept",
        clinicianId="SECRETARY-ATTEMPT",
        decisionReason="Attempted accept by secretary (should be refused)",
    )
    # Wait long enough for the Accept gateway to create BookVisit if the engine allows it.
    booked = wait_task_or_none(record["processInstanceKey"], "BookVisit", timeout=20)
    record["checks"]["U1_BookVisit_created_after_secretary_accept"] = booked
    record["checks"]["U1_referralDecision"] = variables(record["processInstanceKey"]).get(
        "referralDecision"
    )
    record["checks"]["U2_limitation"] = (
        "All user tasks assignee=demo; no Camunda candidate-group RBAC in classroom model"
    )
    # Case rule PASS = engine refused (no BookVisit). Classroom demo currently allows it → FAIL.
    if not booked:
        record["verdict"] = "PASS"
        record["checks"]["U1_engine_refused_unauthorised_accept"] = True
    else:
        record["verdict"] = "FAIL"
        record["checks"]["U1_engine_refused_unauthorised_accept"] = False
        record["failure_reason"] = (
            "Case rule: secretaries must not accept referrals. "
            "Observed: Accept by staffRole Medical Secretary still created BookVisit. "
            "Proposed handling: implement role candidate groups / Identity (PB-22); "
            "keep this FAIL visible until then."
        )
    print(record["id"], record["verdict"], record["processInstanceKey"], flush=True)
    return record


def run_at04(definition_key):
    """No suitable slot → pending; return to BookVisit; no ClinicalCare yet."""
    record = start(definition_key, "AT-04", "PENDING")
    reach_after_accept_booked(record)
    complete(
        record,
        "BookVisit",
        action="pending",
        staffRole="Outpatient Bookings / PB-18",
        notes="No suitable slot in requested timeframe; pathway team flagged; no duplicate",
    )
    # After check-slot, VisitOutcome default returns to BookVisit
    find_task(record["processInstanceKey"], "BookVisit")
    record["checks"]["P1_BookVisit_again_after_pending"] = True
    clinical = task_exists_now(record["processInstanceKey"], "ClinicalCare")
    record["checks"]["P2_ClinicalCare_absent"] = not clinical
    visit_outcome = wait_for(
        lambda: (
            v
            if (v := variables(record["processInstanceKey"]).get("visitOutcome"))
            == "pending"
            else None
        ),
        "visitOutcome=pending",
        timeout=30,
    )
    record["checks"]["P3_visitOutcome"] = visit_outcome
    assert not clinical
    assert not active_incidents(record["processInstanceKey"])
    record["checks"]["P4_incidents"] = 0
    record["verdict"] = "PASS"
    print(record["id"], "PASS", record["processInstanceKey"], flush=True)
    return record


def run_at05(definition_key):
    """Payment unsuccessful (amount ends with 0) → investigate task → retry success."""
    record = start(definition_key, "AT-05", "PAYFAIL")
    reach_funding(record)
    complete(
        record,
        "Funding",
        action="patient_payment_required",
        charge_amount="10.00",
        staffRole="Finance / PB-18",
        notes="First attempt — expect unsuccessful (demo rule ends with 0)",
    )
    find_task(record["processInstanceKey"], "FundingIssue")
    vars_fail = variables(record["processInstanceKey"])
    record["checks"]["F1_payment_status_after_fail"] = vars_fail.get("payment_status")
    record["checks"]["F1b_payment_investigate"] = vars_fail.get("payment_investigate")
    assert vars_fail.get("payment_status") in ("unsuccessful", "investigate"), vars_fail
    complete(
        record,
        "FundingIssue",
        action="recorded",
        staffRole="Finance / PB-18",
        notes="Failure recorded; retry allowed; no duplicate charge claimed",
    )
    find_task(record["processInstanceKey"], "Funding")
    complete(
        record,
        "Funding",
        action="patient_payment_required",
        charge_amount="10.01",
        staffRole="Finance / PB-18",
        notes="Retry after failure — expect successful",
    )
    find_task(record["processInstanceKey"], "BookTreatment")
    vars_ok = variables(record["processInstanceKey"])
    record["checks"]["F2_payment_status_after_retry"] = vars_ok.get("payment_status")
    record["checks"]["F3_BookTreatment_reached"] = True
    assert vars_ok.get("payment_status") == "successful", vars_ok
    assert not active_incidents(record["processInstanceKey"])
    record["verdict"] = "PASS"
    print(record["id"], "PASS", record["processInstanceKey"], flush=True)
    return record


def run_at06(definition_key):
    """Provider success but confirmation missing → investigate; no auto re-charge."""
    record = start(definition_key, "AT-06", "NOCONF")
    reach_funding(record)
    complete(
        record,
        "Funding",
        action="investigate",
        charge_amount="10.01",
        staffRole="Finance / PB-18",
        notes="Provider may have taken money; confirmation missing — investigate only",
    )
    find_task(record["processInstanceKey"], "FundingIssue")
    vars_ = variables(record["processInstanceKey"])
    record["checks"]["I1_payment_status"] = vars_.get("payment_status")
    record["checks"]["I2_payment_investigate"] = vars_.get("payment_investigate")
    record["checks"]["I3_payment_requested_once"] = vars_.get("payment_requested_once")
    # Default FundingOutcome path to MarkPaymentInvestigate must not call request-payment.
    # Funding form resets payment_requested_once=false; worker sets payment_status=investigate.
    assert vars_.get("payment_status") == "investigate", vars_
    assert vars_.get("payment_investigate") is True, vars_
    # Must not have auto-completed a successful provider charge on this path
    assert vars_.get("payment_status") != "successful"
    assert not task_exists_now(record["processInstanceKey"], "BookTreatment")
    record["checks"]["I4_BookTreatment_not_auto"] = True
    assert not active_incidents(record["processInstanceKey"])
    record["verdict"] = "PASS"
    print(record["id"], "PASS", record["processInstanceKey"], flush=True)
    return record


def main():
    definitions = api(
        "POST",
        "/process-definitions/search",
        {
            "filter": {"processDefinitionId": PROCESS},
            "sort": [{"field": "version", "order": "DESC"}],
        },
    )["items"]
    assert definitions, "Deploy Coursework/hospital-pathway BPMN first"
    definition = definitions[0]
    EVIDENCE["definition"] = {
        "processDefinitionId": definition.get("processDefinitionId"),
        "processDefinitionKey": definition.get("processDefinitionKey"),
        "version": definition.get("version"),
    }
    key = definition["processDefinitionKey"]
    run_at03(key)
    run_at04(key)
    run_at05(key)
    run_at06(key)
    fails = [t for t in EVIDENCE["tests"] if t.get("verdict") == "FAIL"]
    EVIDENCE["result"] = "PASS_WITH_KNOWN_FAILS" if fails else "PASS"
    EVIDENCE["failed_tests"] = [t["id"] for t in fails]


if __name__ == "__main__":
    exit_code = 0
    try:
        main()
    except Exception as error:  # noqa: BLE001
        EVIDENCE["result"] = "FAIL"
        EVIDENCE["error"] = str(error)
        exit_code = 1
        print("PB-18 FAIL:", error, flush=True)
    finally:
        path = ROOT / "target" / f"pb18-acceptance-{STAMP}.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(
            json.dumps(EVIDENCE, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("Evidence:", path, flush=True)
        # Script exit 0 even when AT-03 is the expected classroom FAIL,
        # so long as other executable paths completed without crash.
        if EVIDENCE.get("result") == "FAIL":
            exit_code = 1
    raise SystemExit(exit_code)
