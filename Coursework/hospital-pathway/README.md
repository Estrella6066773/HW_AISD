# Hospital Pathway

Executable Camunda 8 pathway: BPMN + forms + two Java workers.

Payment follows the Est / Message Example pattern: **send task** `request-payment` publishes BPMN message `payment-result` (correlation key `case_reference`); catch event **Payment result received** continues the path. Booking confirmation is a **send task** worker (no inbound message wait).

## How to run (same for every teammate)

**Order matters: start Camunda first, then Java. Keep both running.**

### 1. Start local Camunda 8 (c8run / starter)

Confirm in browser:

| UI | URL | Login |
|----|-----|-------|
| Operate | http://localhost:8080/operate | demo / demo |
| Tasklist | http://localhost:8080/tasklist | demo / demo |

If your Camunda uses port **8090** instead of **8080**, change `rest-address` in `src/main/resources/application.yaml` to match.

### 2. Start Java workers

Option A — terminal:

```bash
cd Coursework/hospital-pathway
mvn spring-boot:run
```

Option B — IDE: open `HospitalPathwayApplication.java` → Run (Java 21).

Keep the process running after `Started HospitalPathwayApplication`.

### 3. Start a process

Tasklist → Processes → start `Hospital_All_Processes_Simple_C8` (assignee `demo`).

## Do you need Java every time?

| Situation | Need Java? |
|-----------|------------|
| Only user tasks | Optional, but recommended |
| Reaching P7 send payment / P6 send booking confirmation | **Required** — otherwise the instance stays on that job (or on the payment-result catch if the message was never published) |

Closing Java stops the workers. Restart Java to resume waiting jobs. Use a non-empty **Patient / case ID** on the funding form so `case_reference` can correlate `payment-result`.

## Notes

- Do not run this module and `Ruby/hospital-pathway-zh-learn` at the same time (same workers / deploy).
- Coursework English package is the submission/demo copy; the Chinese learn folder is optional.
