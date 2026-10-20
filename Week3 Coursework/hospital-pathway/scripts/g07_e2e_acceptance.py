"""G07 end-to-end acceptance: V3 main path (referral -> accept -> visit -> treat ->
letter -> self-pay -> treatment booking -> discharge).

Same method as the 2026-09-29 Group_Final_E2E JSON: Camunda REST /v2 with the Java
workers running (check-slot, request-payment, dispatch-clinic-letter,
reserve-appointment, send-booking-confirmation). Synthetic data only.

Run from hospital-pathway with Camunda and `mvn spring-boot:run` already up:
  python scripts/g07_e2e_acceptance.py

Evidence is written to evidence/Group_Final_E2E_<timestamp>.json. A failed step is
recorded verbatim in the JSON; the assertion list shows which business claims hold.
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
PROCESS = os.environ.get("CAMUNDA_PROCESS_ID", "Hospital_All_Processes_V3_C8")
ROOT = Path(__file__).resolve().parents[1]
STAMP = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
CASE = "GROUP-E2E-" + STAMP
EVIDENCE: dict = {
    "testId": "G07",
    "caseReference": CASE,
    "startedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
    "method": "Camunda 8 REST /v2 with live Java worker application; fictional classroom data",
    "processDefinitionId": PROCESS,
    "tasks": [],
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
        "staffRole": "G07 / acceptance",
        "clinicianId": "DEMO-CLINICIAN",
        "specialty": "general medicine",
        "priority": "routine",
        "timeframeUnit": "weeks",
        "timeframeWeeks": 2,
        "timeframeDays": 14,
        "notes": "Synthetic group acceptance case; no real patient data",
        "decisionReason": "Synthetic teaching scenario",
    }
    values.update(variables)
    submitted_at = dt.datetime.now(dt.timezone.utc).isoformat()
    api(
        "POST",
        f"/user-tasks/{item['userTaskKey']}/completion",
        {"variables": values},
    )
    try:
        completed = api("GET", f"/user-tasks/{item['userTaskKey']}")
    except RuntimeError:
        completed = {}
    record["tasks"].append(
        {
            "elementId": element,
            "userTaskKey": str(item["userTaskKey"]),
            "formKey": item.get("formKey"),
            "submittedAction": values.get("action"),
            "submittedAt": submitted_at,
            "completionDate": completed.get("completionDate"),
        }
    )
    print(f"completed {element} ({item['userTaskKey']})", flush=True)


def start(definition_key):
    instance = api(
        "POST",
        "/process-instances",
        {
            "processDefinitionKey": definition_key,
            "variables": {
                "patientId": CASE,
                "notes": "Synthetic group acceptance case; no real patient data",
                "specialty": "general medicine",
                "priority": "routine",
            },
        },
    )
    record = {
        "case": CASE,
        "processInstanceKey": str(instance["processInstanceKey"]),
        "tasks": [],
        "checks": {},
    }
    print("started", record["processInstanceKey"], flush=True)
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


def main():
    topology = api("GET", "/topology")
    EVIDENCE["engineVersion"] = topology.get("gatewayVersion")

    definitions = api(
        "POST",
        "/process-definitions/search",
        {
            "filter": {"processDefinitionId": PROCESS},
            "sort": [{"field": "version", "order": "DESC"}],
        },
    )["items"]
    assert definitions, "Deploy Hospital_All_Processes_V3.bpmn first"
    definition = definitions[0]
    key = definition["processDefinitionKey"]
    EVIDENCE["definition"] = {
        "processDefinitionId": definition.get("processDefinitionId"),
        "processDefinitionKey": str(key),
        "version": definition.get("version"),
    }

    record = start(key)
    EVIDENCE["processInstanceKey"] = record["processInstanceKey"]
    EVIDENCE["tasks"] = record["tasks"]

    complete(record, "Register", action="referral")
    complete(record, "ReviewReferral", action="accept")
    complete(record, "BookVisit", action="attended", appointmentDate="2026-10-20")
    complete(record, "ClinicalCare", action="treatment")
    complete(record, "DispatchLetter", action="sent")
    complete(
        record,
        "Funding",
        action="patient_payment_required",
        charge_amount="10.01",
        insurerReference="",
    )
    complete(record, "BookTreatment", action="ready")
    complete(record, "ClinicalCare", action="discharge")
    complete(record, "DispatchLetter", action="sent")

    instance = wait_for(
        lambda: (
            p
            if (p := api("GET", "/process-instances/" + record["processInstanceKey"]))[
                "state"
            ]
            == "COMPLETED"
            else None
        ),
        "instance completed",
    )
    decoded = variables(record["processInstanceKey"])
    incidents = active_incidents(record["processInstanceKey"])

    EVIDENCE["finalState"] = instance["state"]
    EVIDENCE["variables"] = decoded
    EVIDENCE["activeIncidents"] = incidents
    EVIDENCE["assertions"] = {
        "referralDecision": decoded.get("referralDecision") == "accept",
        "visitOutcome": decoded.get("visitOutcome") == "attended",
        "careDecision": decoded.get("careDecision") == "discharge",
        "letterStatus": decoded.get("letterStatus") == "sent",
        "fundingStatus": decoded.get("fundingStatus") == "patient_paid",
        "payment_status": decoded.get("payment_status") == "successful",
        "booking_slot_status": decoded.get("booking_slot_status") == "CONFIRMED",
        "confirmation_sent": decoded.get("confirmation_sent") is True,
        "clinicLetterDispatchStatus": decoded.get("clinicLetterDispatchStatus")
        == "dispatched",
        "noActiveIncident": not incidents,
    }
    EVIDENCE["result"] = "PASS" if all(EVIDENCE["assertions"].values()) else "FAIL"
    EVIDENCE["finishedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
    print("result", EVIDENCE["result"], flush=True)


if __name__ == "__main__":
    exit_code = 0
    try:
        main()
    except Exception as error:  # noqa: BLE001 — record the exact failure
        EVIDENCE["result"] = "FAIL"
        EVIDENCE["error"] = str(error)
        exit_code = 1
        print("G07 FAIL:", error, flush=True)
    finally:
        path = ROOT / "evidence" / f"Group_Final_E2E_{STAMP}.json"
        path.write_text(
            json.dumps(EVIDENCE, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("Evidence:", path, flush=True)
    raise SystemExit(exit_code)
