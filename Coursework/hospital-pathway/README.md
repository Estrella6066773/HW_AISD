# Hospital Pathway

Executable Camunda 8 pathway: BPMN + 11 forms + seven Java job types (the original two, three owned by B, and two owned by D).

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
| Editing BPMN / previewing forms without running a process | No |
| Running enquiries, changes, booking, or payment | **Required** — otherwise the instance waits at its next worker job (or the payment-result catch) |

Closing Java stops the workers. Restart Java to resume waiting jobs. Use a non-empty **Patient / case ID** on the funding form so `case_reference` can correlate `payment-result`.

## Notes

- Do not run this module and `Ruby/hospital-pathway-zh-learn` at the same time (same workers / deploy).
- Coursework English package is the submission/demo copy; the Chinese learn folder is optional.
- The 28 September member D changes are maintained in this English package only. The learning package has not received these workers, database changes, or BPMN nodes.

## Member D: care-change notifications and enquiry receipts

`MemberDPathwayWorkers.java` subscribes to `notify-care-change` and `ack-enquiry-routed`. The BPMN inserts one service task after `ClinicalChange` and one after each of the three enquiry user tasks. Existing forms still collect human decisions; no extra form is required. Notifications are classroom mocks, recorded in the shared domain database.

See [D's explanation, variable contract and demonstration](../../Ryan/2026-09-28/D_外部工作器与数据库说明.md) and [verified evidence](../../evidence/PB-10_PB-21_member-D_workers_2026-09-28/README.md). A/B second-owner review is pending.

## Shared domain database

Run Java from this module directory so the file is `data/hospital-domain.mv.db`. The file is ignored by Git and persists across restarts. The engine's database is separate.

- `payment_ledger`: payment facts; D only reads it for financial changes.
- `booking_slot`: B's appointment occupancy records.
- `audit_event`: append-only business audit; D adds an optional unique `idempotency_key`. Old four-argument append callers remain compatible.

The configured H2 file uses `AUTO_SERVER=FALSE`. Stop the Java worker application before opening this same file in an IDE database tool, then restart Java after inspection. Use JDBC URL `jdbc:h2:file:<absolute-path-to-module>/data/hospital-domain;IFEXISTS=TRUE`, user `sa`, empty password. `IFEXISTS=TRUE` prevents silently creating a new database at the wrong path.

```sql
SELECT id, actor, action, case_reference, occurred_at, payload_summary
FROM audit_event
WHERE action IN ('notify-care-change', 'notify-care-change-skipped', 'ack-enquiry-routed')
ORDER BY id;
```

## Verify member D

Java 21, Maven and Python 3 are required. Run from this directory:

```text
mvn test
python scripts/test_member_d_bpmn.py
```

The Java tests use a separate in-memory H2 database. After starting Camunda and the formal Java application, run `python scripts/smoke_member_d.py` for eight real-engine scenarios. This creates labelled synthetic process instances and submits user tasks through the API; it does not exercise browser form validation. Evidence is written under `target/`. Running it again creates a new set of test cases.

The optional process variable `memberDNotificationFailure="once"` demonstrates a transient notification failure followed by a successful retry. Leave it absent for normal demonstrations. `"always"` exhausts retries and needs an operator to clear the variable and retry the incident. These switches affect only D's mocked notifications.
