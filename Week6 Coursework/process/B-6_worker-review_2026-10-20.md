# B-6 second-owner review — Java workers

**Item**: B-6, the Java worker module for `Hospital_All_Processes_V3_C8`.
**Deliverable under review**: `Week3 Coursework/hospital-pathway/`, 17 source files under `src/main/java/io/camunda/demo/hospital/` (47.5 KB) and 3 test classes under `src/test/java/io/camunda/demo/hospital/` (14.9 KB).
**Rule this satisfies**: `docs/definition-of-done.md` line 53, `At least one team member (Second Owner) reviewed the changes`, under Code Quality — implementation increment. B-6 is the only B item that line 53 binds directly.

**Reviewers**: Ender (Minghao Qin), Ryan (Guanyan He), Estrella (Geping Chen). **13 of the 17 source files carry a named reviewer. The other four carry none** — see Limits recorded.
**Date**: 20 October 2026.
**Basis of the review**: each reviewer read the files assigned below, together with the two build records `evidence/Java_Clean_Build_Test_2026-10-19.txt` (`mvn -B clean test` at `dbc0a33`, 19 tests, BUILD SUCCESS) and `evidence/Java_Test_Results_2026-10-20.txt` (`mvn -B clean test`, 19 tests, 0 failures, 0 errors, 0 skipped). No reviewer re-ran the build or the acceptance drivers to produce this record, and none is claimed to have done so.

## What was reviewed

| File | Job types | Author per plan §5 | Reviewer | Tests that name it |
|------|-----------|--------------------|----------|--------------------|
| `HospitalPathwayWorkers.java` | `request-payment`, `send-booking-confirmation` | Ruby | Ender | none |
| `RefundWorkers.java` | `request-refund`, `mark-payment-investigate` | Ruby | Ender | `RefundWorkersTest`, 10 methods |
| `ChargeAmountRules.java` | helper used by the two Ruby workers | not recorded | — not marked | `ChargeAmountRulesTest`, 2 methods |
| `BookingWorkers.java` | `check-slot`, `reserve-appointment`, `flag-resource-unavailable` | Estrella | Ryan | none |
| `LetterWorkers.java` | `dispatch-clinic-letter`, `notify-referrer` | Ender | Estrella | none |
| `CareChangeWorkers.java` | `notify-care-change` | Ryan | Estrella | `CareChangeWorkersTest`, 6 methods |
| `HospitalPathwayApplication.java` | startup: loads model and forms | not recorded | — not marked | none |
| `domain/AuditEvent.java` | none | Ryan | Estrella | indirect, via `CareChangeWorkers` |
| `domain/AuditEventWriter.java` | none | Ryan | Estrella | `memberBOriginalAppendStillWorks` |
| `domain/AuditEventRepository.java` | none | not recorded | — not marked | none |
| `domain/BookingSlot.java`, `BookingSlotRepository.java`, `BookingSlotStatus.java` | none | Estrella | Ryan | none |
| `domain/PaymentLedger.java`, `PaymentLedgerRepository.java`, `PaymentLedgerStatus.java` | none | Estrella | Ryan | none |
| `domain/DomainDatabaseConfig.java` | none | not recorded | — not marked | none |

## What the review established

- Every `@JobWorker(type = ...)` string in the five worker classes matches a `zeebe:taskDefinition type` in `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`: ten job types across five classes.
- The 19 test methods split 7 / 2 / 10 across `CareChangeWorkersTest`, `ChargeAmountRulesTest` and `RefundWorkersTest`, matching the count in both build records. Every test method calls a public method of the class it is filed under, with one exception: `memberBOriginalAppendStillWorks` exercises `AuditEventWriter.append` rather than `CareChangeWorkers`.
- Retry safety is visible in the source: `RefundWorkers.requestRefund` reuses the ledger row, `HospitalPathwayWorkers.requestPayment` reuses when `payment_requested_once` is true, `CareChangeWorkers.notifyCareChange` keys the receipt on the process and element instance, and `BookingWorkers.upsertBooking` reuses by occupancy key. None writes a second row on a retry with the same key.
- `application.yaml` holds `demo`/`demo` for the Camunda connection and `sa` with an empty password for the local file-backed H2 database. The H2 file under `data/` is not committed. No patient data and no card data are present.

## Limits recorded

- Four of the 17 files have no individually recorded author: `ChargeAmountRules.java`, `HospitalPathwayApplication.java`, `domain/AuditEventRepository.java` and `domain/DomainDatabaseConfig.java`. Without an author, reviewer independence cannot be shown, so **no reviewer is marked against them** and they are not counted as reviewed. Naming someone there would assert a review the group cannot stand behind. The files exist and the build compiles them; what is missing is the record of who wrote them, and the group did not reconstruct one.
- Seven of the ten job types carry no unit test: `check-slot`, `reserve-appointment`, `flag-resource-unavailable`, `request-payment`, `send-booking-confirmation`, `dispatch-clinic-letter`, `notify-referrer`. Five of those seven appear on the G07 route in `evidence/Camunda_V3_Acceptance_2026-10-19.txt`; `flag-resource-unavailable` and `notify-referrer` appear in no recorded run.
- This record reviews the source as it stands. It is dated after the module was merged, so it does not claim the pre-merge review described in `README.md` line 93.
