# Hospital Pathway

Executable Camunda 8 pathway: BPMN + 11 forms + Java job types (shared payment/booking communication; member A refund/investigate; member B slots; member C letters/referrer notification; member D care-change).

This module is the shared implementation for both courses. The course-specific written submission indexes are in [BPM&EA](../../submissions/BPMEA/README.md) and [AISD](../../submissions/AISD/README.md); the same BPMN, forms and worker source are not duplicated there.

The runnable classroom configuration is [`src/main/resources/application.yaml`](src/main/resources/application.yaml). A separate [configuration template](config/application.example.yaml) shows which connection and database settings can be supplied through environment variables. Start the application from this module directory so `./data/hospital-domain` resolves to the intended H2 file.

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
| Running changes, booking, or payment | **Required** — otherwise the instance waits at its next worker job (or the payment-result catch) |

Closing Java stops the workers. Restart Java to resume waiting jobs. Use a non-empty **Patient / case ID** on the funding form so `case_reference` can correlate `payment-result`.

## Notes

- Do not run this module and `Ruby/hospital-pathway-zh-learn` at the same time (same workers / deploy).
- Coursework English package is the submission/demo copy; the Chinese learn folder is optional.
- The 28 September member D changes are maintained in this English package only. The learning package has not received these workers, database changes, or BPMN nodes.

## Refund workers

`RefundWorkers.java` owns:

| Type | BPMN hang point | Writes |
|------|-----------------|--------|
| `request-refund` | After `FinanceAdjustment`, before `AdjustmentOutcome` | `payment_ledger` + `audit_event` |
| `mark-payment-investigate` | Before `FundingIssue` (unpaid / funding pending) | `payment_ledger` (INVESTIGATE) + `audit_event` |

Resolved finance adjustments record a successful refund row; pending keeps INVESTIGATE. Retries reuse the same idempotency key. Existing `request-payment` is unchanged.

```sql
SELECT id, case_reference, idempotency_key, amount, status, transaction_reference, payment_date
FROM payment_ledger
ORDER BY id;
```

## Care-change workers

`CareChangeWorkers.java` subscribes only to `notify-care-change`. One service task follows the human `ClinicalChange` task. It reads four mapped form variables, determines the notification status, saves a mock receipt in H2, and returns the result. The three enquiry routes finish after their human response. Existing forms still apply.

The student version removes the optional enquiry worker, failure switches, payment statistics and custom transaction/concurrency handling. A regular transaction and unique receipt key retain basic retry protection.

See [D's explanation, variable contract and demonstration](../../Ryan/2026-09-28/D_外部工作器与数据库说明.md). A/B second-owner review is pending.

## Shared domain database

Run Java from this module directory so the file is `data/hospital-domain.mv.db`. The file is ignored by Git and persists across restarts. The engine's database is separate.

- `payment_ledger`: payment / refund / investigate facts (member A writes refund and investigate rows).
- `booking_slot`: B's appointment occupancy records.
- `audit_event`: append-only business audit; A/B/D append; D may use an optional unique `idempotency_key`. Old four-argument append callers remain compatible.

The configured H2 file uses `AUTO_SERVER=FALSE`. Stop the Java worker application before opening this same file in an IDE database tool, then restart Java after inspection. Use JDBC URL `jdbc:h2:file:<absolute-path-to-module>/data/hospital-domain;IFEXISTS=TRUE`, user `sa`, empty password. `IFEXISTS=TRUE` prevents silently creating a new database at the wrong path.

```sql
SELECT id, actor, action, case_reference, occurred_at, payload_summary
FROM audit_event
WHERE action IN ('notify-care-change', 'notify-care-change-skipped')
ORDER BY id;
```

## Verify member D

Java 21, Maven and Python 3 are required. Run from this directory:

```text
mvn test
python scripts/test_member_d_bpmn.py
```

The Java tests use a separate in-memory H2 database. After starting Camunda and the formal Java application, run `python scripts/smoke_member_d.py` for seven real-engine scenarios (four change cases and three enquiry regression checks). This creates labelled synthetic process instances and submits user tasks through the API; it does not exercise browser form validation. Evidence is written under `target/`. Running it again creates a new set of test cases.

## Verify PB-14 acceptance (main path + reject)

Official test procedure is Tasklist form steps in `Ryan/2026-09-26/PB-14_acceptance-test-plan_2026-09-29.md`. Optional repeat:

```text
python scripts/pb14_acceptance.py
```

AT-02 (reject) needs only Camunda; AT-01 also needs the Java `check-slot` worker. Archive any new JSON from `target/` as `Ryan/2026-09-26/PB-14_acceptance-run-log_<date>.json`.

## Verify PB-18 additional acceptance (four exception paths)

See `Ryan/2026-09-26/PB-18_acceptance-test-plan_2026-09-29.md`. With Camunda and Java up:

```text
python scripts/pb18_acceptance.py
```

AT-03 is expected to **FAIL** on the classroom model (no role RBAC) and must stay recorded as Fail with handling → PB-22. AT-04/05/06 should Pass.
