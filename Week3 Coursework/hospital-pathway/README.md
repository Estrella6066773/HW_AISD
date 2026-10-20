# Hospital Pathway

Executable Camunda 8 pathway: BPMN + 12 forms + Java job types (shared payment/booking communication; member A refund/investigate; member B slots; member C letters/referrer notification; member D care-change).

This module is the shared implementation for both courses. The course-specific written submissions are in [BPM&EA](../../submissions/BPMEA/) and [AISD](../../submissions/AISD/), indexed by [`Submission_Index.pdf`](../../submissions/Submission_Index.pdf); the same BPMN, forms and worker source are not duplicated there.

`Week6 Coursework/code/` is a trimmed second copy of this module, kept so the Week 6 folder can be read on its own: its Java sources, tests and test resources are identical, but its `pom.xml` packages `../bpmn` and `../forms` from that folder. This module is the one the evidence and the commands below refer to; run one copy at a time, because both deploy the same model and subscribe to the same job types.

The runnable classroom configuration is [`src/main/resources/application.yaml`](src/main/resources/application.yaml). A separate [configuration template](config/application.example.yaml) shows which connection and database settings can be supplied through environment variables. Start the application from this module directory so `./data/hospital-domain` resolves to the intended H2 file.

Payment follows the Est / Message Example pattern: **send task** `request-payment` publishes BPMN message `payment-result` (correlation key `case_reference`); catch event **Payment result received** continues the path. Booking confirmation is a **send task** worker (no inbound message wait).

## How to run (same for every teammate)

**Order matters: start Camunda first, then Java. Keep both running.**

### 1. Start local Camunda 8 (c8run)

The recorded runs use Camunda **8.10.0-alpha5** through c8run. Start it from the tool directory with connectors disabled:

```powershell
cd D:\OneDrive\MyProjects\AISD_Toolbox\tools\c8run-8.10.0-alpha5
.\c8run.exe start --disable-connectors
```

**`--disable-connectors` matters.** Without it, the bundled Connectors runtime fails its health check and c8run shuts the whole engine down mid-run: that happened at 21:38 on 19 October and the run was restarted at 21:40 with the flag. The process model does not use connectors, so nothing is lost. The environment note in [`evidence/Camunda_V3_Acceptance_2026-10-19.txt`](evidence/Camunda_V3_Acceptance_2026-10-19.txt) records the event.

Wait until Operate answers, then confirm in the browser:

| UI | URL | Login |
|----|-----|-------|
| Operate | http://localhost:8080/operate | demo / demo |
| Tasklist | http://localhost:8080/tasklist | demo / demo |

The worker application connects to REST at `http://127.0.0.1:8080` and gRPC at `127.0.0.1:26500`; both are checked in `src/main/resources/application.yaml`. If your Camunda uses port **8090** instead of **8080**, change `rest-address` (and the gRPC port if it moves) to match.

### 2. Start Java workers

Option A — terminal:

```bash
cd "Week3 Coursework/hospital-pathway"
mvn -B spring-boot:run
```

Option B — IDE: open `HospitalPathwayApplication.java` → Run.

Keep the process running after `Started HospitalPathwayApplication`.

`pom.xml` sets `java.version` to 21 and pulls Spring Boot 4.0.5 with `camunda-spring-boot-starter` 8.9.0, so the sources target Java 21. The 19 October acceptance run used **JDK 23.0.1** (`JAVA_HOME D:\Java\jdk-23`); any JDK from 21 up should work.

### 3. Start a process

Tasklist → Processes → start `Hospital_All_Processes_V3_C8` (assignee `demo`). This is the full pathway diagram with the exclusive merge gateways. The module's `pom.xml` packages the model and the forms from `../../Week6 Coursework/`, so the V3 file is what gets deployed; the local `bpmn/Hospital_All_Processes_V2.bpmn` is kept as an earlier copy and is no longer packaged. The 29 September model, process id `Hospital_All_Processes_Simple_C8`, is `bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`; it does not contain the split visit outcomes and is not packaged either.

On startup the application deploys `Hospital_All_Processes_V3.bpmn` plus the 12 forms, and refuses to start if fewer than 11 forms are found.

### 4. Acceptance drivers

Run these from this module directory, with Camunda and the Java workers already up:

| Script | Cases | Needs |
|--------|-------|-------|
| `python scripts/pb14_acceptance.py` | AT-01 main path, AT-02 reject | Camunda; AT-01 also needs the Java `check-slot` worker |
| `python scripts/pb18_acceptance.py` | AT-03 to AT-06 | Camunda and Java; AT-03 is expected to FAIL |
| `python scripts/g07_e2e_acceptance.py` | G07 full path to `COMPLETED` | Camunda and Java; writes `evidence/Group_Final_E2E_<timestamp>.json` |

All three read `CAMUNDA_PROCESS_ID` (default `Hospital_All_Processes_V3_C8`), `CAMUNDA_REST_URL` (default `http://localhost:8080`) and `CAMUNDA_USERNAME` / `CAMUNDA_PASSWORD` (default `demo` / `demo`).

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

`request-refund` records a full or partial refund as SUCCESSFUL, a transfer as TRANSFERRED, and a retained fee as RETAINED. Pending stays INVESTIGATE and does not invent an amount. Retries reuse the same idempotency key. `request-payment` rejects a missing or wrongly scaled `charge_amount` instead of substituting `10.01`. A valid amount that ends in 0, such as `10.00`, is still the classroom unsuccessful payment. Funding-pending investigation with no amount records `unspecified`.

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

JDK 21 or newer, Maven and Python 3 are required. Run from this directory:

```text
mvn test
python scripts/test_member_d_bpmn.py
```

The Java tests use a separate in-memory H2 database. The 19 October clean build ran 19 tests with no failures.

`python scripts/smoke_member_d.py` is a live-engine script for seven change and enquiry scenarios (four change cases and three enquiry regression checks). It hard-codes `Hospital_All_Processes_Simple_C8`, the 29 September model, and takes no override, so it does **not** run against the V3 deployment this module now starts; it is kept for the initial-release record. Run it only against a deployment of `bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`. When it does run, it creates labelled synthetic process instances and submits user tasks through the API, does not exercise browser form validation, and writes evidence under `target/`; each run creates a new set of cases.

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
