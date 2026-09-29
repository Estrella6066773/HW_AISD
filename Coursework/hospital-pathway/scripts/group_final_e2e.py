"""Run one labelled, synthetic start-to-end Camunda 8 acceptance case.

Start c8run and `mvn spring-boot:run` from this module directory first. This
uses the deployed final process, its bound forms and live Java workers. It
does not claim real payment, letter delivery or hospital scheduling.
"""

from __future__ import annotations

import base64
import datetime as dt
import hashlib
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


MODULE = Path(__file__).resolve().parents[1]
REPO = MODULE.parents[1]
BASE = os.environ.get("CAMUNDA_REST_URL", "http://127.0.0.1:8080").rstrip("/")
AUTH = base64.b64encode(
    (os.environ.get("CAMUNDA_USERNAME", "demo") + ":" + os.environ.get("CAMUNDA_PASSWORD", "demo")).encode()
).decode()
PROCESS_ID = "Hospital_All_Processes_Simple_C8"
STAMP = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
CASE_ID = f"GROUP-E2E-{STAMP}"
EVIDENCE_PATH = MODULE / "evidence" / f"Group_Final_E2E_{STAMP}.json"
BPMN = MODULE / "bpmn" / "W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn"
worker_logs = list((MODULE / "target").glob("spring-boot-run-*.log"))
LOG = max(worker_logs, key=lambda item: item.stat().st_mtime) if worker_logs else None


def api(method: str, path: str, body=None):
    data = None if body is None else json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        BASE + "/v2" + path,
        data=data,
        method=method,
        headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"{method} {path}: {error.code} {error.read().decode()}") from error


def wait_for(callback, description: str, seconds: int = 90):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        result = callback()
        if result:
            return result
        time.sleep(0.5)
    raise AssertionError(f"Timed out waiting for {description}")


def open_tasks(instance_key: str):
    response = api("POST", "/user-tasks/search", {"filter": {"processInstanceKey": instance_key, "state": "CREATED"}})
    return response.get("items", [])


def active_incidents(instance_key: str):
    response = api("POST", "/incidents/search", {"filter": {"processInstanceKey": instance_key, "state": "ACTIVE"}})
    return response.get("items", [])


def variables(instance_key: str):
    response = api("POST", "/variables/search", {"filter": {"processInstanceKey": instance_key}, "page": {"limit": 200}})
    result = {}
    for item in response.get("items", []):
        if not item.get("isTruncated", False):
            result[item["name"]] = json.loads(item["value"])
    return result


def complete(record: dict, element: str, action: str, **extra):
    key = record["processInstanceKey"]
    task = wait_for(
        lambda: next((item for item in open_tasks(key) if item.get("elementId") == element), None),
        element,
    )
    values = {
        "patientId": CASE_ID,
        "specialty": "general medicine",
        "priority": "routine",
        "timeframe": "within two weeks",
        "notes": "Synthetic group acceptance case; no real patient data",
        "staffRole": "demo authorised classroom staff",
        "clinicianId": "DEMO-CLINICIAN",
        "decisionReason": "Synthetic teaching scenario",
        "action": action,
    }
    values.update(extra)
    api("POST", f"/user-tasks/{task['userTaskKey']}/completion", {"variables": values})
    record["tasks"].append(
        {
            "elementId": element,
            "userTaskKey": task["userTaskKey"],
            "formKey": task.get("formKey"),
            "submittedAction": action,
            "submittedFields": {key: values[key] for key in extra},
        }
    )
    print(f"completed {element}: {action}", flush=True)


def run(record: dict):
    topology = api("GET", "/topology")
    if not topology.get("brokers"):
        raise RuntimeError("Camunda topology has no broker")
    definitions = api(
        "POST",
        "/process-definitions/search",
        {"filter": {"processDefinitionId": PROCESS_ID}, "sort": [{"field": "version", "order": "DESC"}]},
    ).get("items", [])
    if not definitions:
        raise RuntimeError("The final BPMN has not been deployed")
    definition = definitions[0]
    record["definition"] = {
        "processDefinitionId": definition.get("processDefinitionId"),
        "processDefinitionKey": definition.get("processDefinitionKey"),
        "version": definition.get("version"),
    }
    instance = api(
        "POST",
        "/process-instances",
        {"processDefinitionKey": definition["processDefinitionKey"], "variables": {"patientId": CASE_ID}},
    )
    record["processInstanceKey"] = instance["processInstanceKey"]
    print(f"started case={CASE_ID} instance={record['processInstanceKey']} version={definition.get('version')}", flush=True)

    complete(record, "Register", "referral")
    complete(record, "ReviewReferral", "accept")
    complete(record, "BookVisit", "attended")
    complete(record, "ClinicalCare", "treatment")
    complete(record, "DispatchLetter", "sent")
    complete(record, "Funding", "patient_payment_required", charge_amount="10.01", insurerReference="")
    complete(record, "BookTreatment", "ready")
    complete(record, "ClinicalCare", "discharge")
    complete(record, "DispatchLetter", "sent")

    def completed_instance():
        current = api("GET", "/process-instances/" + record["processInstanceKey"])
        return current if current.get("state") == "COMPLETED" else None

    final = wait_for(completed_instance, "process instance COMPLETED")
    record["finalState"] = final["state"]
    record["variables"] = variables(record["processInstanceKey"])
    record["activeIncidents"] = active_incidents(record["processInstanceKey"])
    expected = {
        "referralDecision": "accept",
        "visitOutcome": "attended",
        "careDecision": "discharge",
        "letterStatus": "sent",
        "fundingStatus": "patient_paid",
        "payment_status": "successful",
        "confirmation_sent": True,
        "booking_slot_status": "CONFIRMED",
        "clinicLetterDispatchStatus": "dispatched",
    }
    record["assertions"] = {key: record["variables"].get(key) == value for key, value in expected.items()}
    record["assertions"]["noActiveIncident"] = not record["activeIncidents"]
    if LOG and LOG.exists():
        record["workerLogFile"] = str(LOG.relative_to(REPO)).replace("\\", "/")
        record["workerLogEvidence"] = [
            line.strip()
            for line in LOG.read_text(encoding="utf-8", errors="replace").splitlines()
            if CASE_ID in line and any(
                token in line
                for token in ("check-slot", "dispatch-clinic-letter", "request-payment", "reserve-appointment", "send-booking-confirmation")
            )
        ]
    if not all(record["assertions"].values()):
        raise AssertionError(f"Final assertions failed: {record['assertions']}")


def main():
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, check=True, capture_output=True, text=True
    ).stdout.strip()
    record = {
        "testId": "G07",
        "caseReference": CASE_ID,
        "startedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "method": "Camunda 8 REST /v2 with live Java worker application; fictional classroom data",
        "repositoryCommitBeforeDocumentation": revision,
        "bpmnSha256": hashlib.sha256(BPMN.read_bytes()).hexdigest(),
        "tasks": [],
        "result": "IN_PROGRESS",
    }
    try:
        run(record)
        record["result"] = "PASS"
    except Exception as exc:
        record["result"] = "FAIL"
        record["error"] = f"{type(exc).__name__}: {exc}"
        if record.get("processInstanceKey"):
            try:
                record["openTasksAtFailure"] = open_tasks(record["processInstanceKey"])
                record["activeIncidentsAtFailure"] = active_incidents(record["processInstanceKey"])
                record["variablesAtFailure"] = variables(record["processInstanceKey"])
            except Exception as capture_error:
                record["captureError"] = str(capture_error)
        raise
    finally:
        record["finishedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
        EVIDENCE_PATH.parent.mkdir(parents=True, exist_ok=True)
        EVIDENCE_PATH.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"evidence: {EVIDENCE_PATH} result={record['result']}", flush=True)


if __name__ == "__main__":
    main()
