"""PB-14 验收辅助脚本：用与 Tasklist 表单相同的变量完成 AT-01/AT-02。

正式对学生要求的写法与步骤见：
`Ryan/2026-09-26/PB-14_acceptance-test-plan_2026-09-29.md`
（以 Tasklist 表单操作为官方测试步骤；本脚本仅用于可重复执行与跑日志）。

联动：Camunda REST `/v2` → Register / ReviewReferral / BookVisit；
AT-01 依赖 Member B `check-slot`（需 `mvn spring-boot:run`）。
证据 JSON 在 `target/`（gitignore），需复制到 Ryan 目录并按
`PB-14_acceptance-run-log_<date>.json` 命名。

Run from hospital-pathway after Camunda (and for AT-01, Java) are up:
  python scripts/pb14_acceptance.py
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
PREFIX = "PB14-" + STAMP
EVIDENCE = {
    "run": PREFIX,
    "item": "PB-14",
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
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise RuntimeError(
            f"{method} {path}: {error.code} {error.read().decode()}"
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Camunda REST unreachable at {BASE}: {error}"
        ) from error


def wait_for(fn, description: str, timeout: float = 60):
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
        "staffRole": "PB-14 / acceptance",
        "clinicianId": "CONSULTANT-PB14",
        "specialty": "oncology",
        "priority": "routine",
        "timeframe": "within 2 weeks",
        "notes": "PB-14 acceptance run",
        "decisionReason": "PB-14 recorded reason",
        "action": "recorded",
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
            "formKey": item.get("formKey"),
            "action": values.get("action"),
            "decisionReason": values.get("decisionReason"),
        }
    )


def start(definition_key, scenario: str):
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
        "id": "AT-01" if scenario == "MAIN" else "AT-02",
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
        {
            "filter": {"processInstanceKey": instance},
            "page": {"limit": 200},
        },
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


def book_visit_ever_created(instance: str) -> bool:
    created = api(
        "POST",
        "/user-tasks/search",
        {"filter": {"processInstanceKey": instance, "elementId": "BookVisit"}},
    )["items"]
    return len(created) > 0


def run_at01(definition_key):
    """Main path: accept then enter booking and continue past check-slot."""
    record = start(definition_key, "MAIN")
    complete(
        record,
        "Register",
        action="referral",
        notes="PB-14 AT-01 documents checked",
    )
    complete(
        record,
        "ReviewReferral",
        action="accept",
        clinicianId="CONSULTANT-PB14-01",
        decisionReason="Clinically appropriate for new-patient clinic",
    )
    # E1: booking task must appear after accept
    find_task(record["processInstanceKey"], "BookVisit")
    record["checks"]["E1_BookVisit_after_accept"] = True
    vars_after_accept = variables(record["processInstanceKey"])
    record["checks"]["E2_referralDecision"] = vars_after_accept.get(
        "referralDecision"
    )
    record["checks"]["E2_decisionReason"] = vars_after_accept.get(
        "decisionReason"
    )
    assert vars_after_accept.get("referralDecision") == "accept", vars_after_accept
    assert vars_after_accept.get("decisionReason"), vars_after_accept

    complete(
        record,
        "BookVisit",
        action="attended",
        staffRole="Outpatient Bookings / PB-14",
        notes="Slot confirmed within requested timeframe; letter and phone recorded",
    )
    # E3: clinical care after check-slot worker
    find_task(record["processInstanceKey"], "ClinicalCare")
    record["checks"]["E3_ClinicalCare_after_slot"] = True
    record["checks"]["E4_not_EndRejected"] = not any(
        t["element"] == "EndRejected" for t in record["tasks"]
    )
    incidents = active_incidents(record["processInstanceKey"])
    record["checks"]["E5_activeIncidents"] = len(incidents)
    assert not incidents, incidents
    record["verdict"] = "PASS"
    print("AT-01 PASS", record["processInstanceKey"], flush=True)
    return record


def run_at02(definition_key):
    """Reject path: must complete without ever creating BookVisit."""
    record = start(definition_key, "REJECT")
    complete(
        record,
        "Register",
        action="referral",
        notes="PB-14 AT-02 documents checked",
    )
    complete(
        record,
        "ReviewReferral",
        action="reject",
        clinicianId="CONSULTANT-PB14-02",
        decisionReason="Referral not appropriate for this specialty",
    )
    state = wait_for(
        lambda: (
            p
            if (p := api("GET", "/process-instances/" + record["processInstanceKey"]))[
                "state"
            ]
            == "COMPLETED"
            else None
        ),
        "AT-02 completed",
    )
    record["checks"]["R1_state"] = state["state"]
    decoded = variables(record["processInstanceKey"])
    record["checks"]["R2_referralDecision"] = decoded.get("referralDecision")
    record["checks"]["R2_decisionReason"] = decoded.get("decisionReason")
    assert decoded.get("referralDecision") == "reject", decoded
    assert decoded.get("decisionReason"), decoded
    booked = book_visit_ever_created(record["processInstanceKey"])
    record["checks"]["R3_BookVisit_created"] = booked
    assert booked is False, "BookVisit must not be created after reject"
    incidents = active_incidents(record["processInstanceKey"])
    record["checks"]["R4_activeIncidents"] = len(incidents)
    assert not incidents, incidents
    record["verdict"] = "PASS"
    print("AT-02 PASS", record["processInstanceKey"], flush=True)
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
    run_at02(key)
    run_at01(key)
    EVIDENCE["result"] = "PASS"


if __name__ == "__main__":
    exit_code = 0
    try:
        main()
    except Exception as error:  # noqa: BLE001 — surface into evidence JSON
        EVIDENCE["result"] = "FAIL"
        EVIDENCE["error"] = str(error)
        exit_code = 1
        print("PB-14 FAIL:", error, flush=True)
    finally:
        path = ROOT / "target" / f"pb14-acceptance-{STAMP}.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(
            json.dumps(EVIDENCE, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("Evidence:", path, flush=True)
    raise SystemExit(exit_code)
