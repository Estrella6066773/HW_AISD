# Second-owner review checklist — 20 October 2026

> **Closed.** All the reviews this checklist was written to drive were signed and recorded on 20 October 2026. Section 12 carries the outcomes; the authoritative record for each item is the file named in its own section, not this sheet. Sections 1–11 are kept as written that evening, so their `Unsigned` and `Status today` cells describe the starting position, not the state at close.

**Status**: internal working document, written on the evening of 20 October 2026. It is not a submission deliverable and does not go into either pack. Each reviewer signs their own line; nobody signs for anyone else.

**Deadline**: 23:59 tonight. Every item below can be finished by opening files that already exist. Nothing here asks anyone to restart c8run, re-run Maven, redeploy a model or export a PDF.

**What "reviewed" means here.** `docs/definition-of-done.md` line 53 says `At least one team member (Second Owner) reviewed the changes`. It does not ask for a reproduction, a re-run or a fresh log. A reviewer who opens the named files, answers the check points below and writes a dated line is doing the review the rule asks for.

---

## 1. Scope ruling

`docs/definition-of-done.md` line 53 sits inside **Code Quality — implementation increment** (lines 48–53). Lines 13–16 scope the groups: BPMN & Process Modeling, External Workers, Camunda Forms and Code Quality apply to the implementation increment; Documentation and Delivery Evidence have no review row at all (lines 55–60 and 62–67). Read strictly, line 53 binds one of the eight B items, **B-6**, because B-6 is the only one that is code. The other items are not excused: B-2, B-5, B-7 and B-4 each carry a declared Second Owner in `docs/p3-product-backlog.md`, so the review is owed under that declaration rather than under line 53. B-3 and B-8 carry neither, and are left unsigned.

| Item | Does line 53 bind it? | Reason |
|------|----------------------|--------|
| B-2 i\* SD/SR | No | A model, not code; the Code Quality group does not reach it. Bound instead by PB-16, whose Second Owner column names Ryan, and by the five-item checklist already written at `docs/istar/PB-16_istar-sd-sr.md` section 10. |
| B-5 operational model | No | BPMN & Process Modeling (lines 22–27) has six items and none of them is a review. Bound instead by PB-30, whose Second Owner column names Ender. |
| B-6 Java workers | **Yes** | Code. Line 53 is the only place the review is written as a requirement. The External Workers group (lines 29–36) adds no review row. |
| B-7 twelve forms | No | Camunda Forms (lines 38–46) has six items and none of them is a review. Bound instead by PB-13, whose Second Owner column names Ruby. |
| B-4 written evaluation, Part 2 | No | A document. Documentation (55–60) and Delivery Evidence (62–67) carry no review row. Bound instead by PB-31, whose Second Owner column names Ruby. |
| B-3 written evaluation, Part 1 | No | Same document, same reason. No reviewer is required. One caution: PB-39, the item Part 1 rests on, does name Ryan as Second Owner, so a reader may ask. The group can leave B-3 unsigned and say so. |
| B-8 project and test plan | No | A planning record. No review row, and no Second Owner is declared anywhere for it. |

**B-1 is closed.** The strategic model's second-owner review was signed on 2026-10-19 and recorded in section 7 of `docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md`. Do not re-open it and do not sign it again.

---

## 2. Summary

| Item | Deliverable | First owner | Reviewer | Files to open | Minutes | Status today |
|------|-------------|-------------|----------|---------------|---------|--------------|
| B-2 | i\* SD and three service SR views | Estrella | Ryan | `docs/istar/PB-16_istar-sd-sr.md`, `PB-16_sd.md`, `PB-16_sr.md`, four piStar sources and four PNGs | 50 | Unsigned. Checklist item 2 cannot honestly be ticked (section 3). |
| B-5 | V3 operational model and two readable exports | Ruby | Ender | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`, two readable PDFs | 35 | Unsigned. No defect known. |
| B-6 | Java workers, 17 files, 10 job types, 19 tests | Split across four | Cross-review, table in section 5 | `src/main/java/.../hospital/` and `src/test/java/.../hospital/` | 70 | No review recorded for any file. Four files have no documented owner. |
| B-7 | 12 Camunda forms | Estrella | Ruby | `Week6 Coursework/forms/` | 30 | Unsigned. PB-13 still reads `Not started`, which understates the artefact. |
| B-4 | `BPMEA_Written_Evaluation`, Part 2 | Ryan | Ruby | `submissions/BPMEA/BPMEA_Written_Evaluation.pdf` pages 12–17 | 50 | Unsigned. The pack states `PB-31 sign-off not recorded`. |
| B-3 | Same file, Part 1 | Estrella | Not required | `submissions/BPMEA/BPMEA_Written_Evaluation.pdf` pages 7–11 | 0 | Leave unsigned (section 8). |
| B-8 | `Group_Project_and_Test_Plan_2026-10-20` | Ruby | Not required | `submissions/BPMEA/Group_Project_and_Test_Plan_2026-10-20.pdf` | 0 | Leave unsigned (section 8). |

---

## 3. B-2 — i\* SD and three service SR views

**Deliverable.** `docs/istar/PB-16_istar-sd-sr.md` (24.4 KB, nine sections plus the section 10 checklist), `docs/istar/PB-16_sd.md` (3.4 KB, one Mermaid diagram), `docs/istar/PB-16_sr.md` (11.3 KB, eleven Mermaid diagrams). The delivered diagrams are piStar files in `Week6 Coursework/istar/`:

| Source | Figure | Size |
|--------|--------|------|
| `V1_SD_diagram.txt` (22.0 KB) | `V1_SD_diagram.png`, 5020 × 2748 | 1056.7 KB |
| `PB-16_V1_Admin_SR_reviewed_2026-10-19.txt` (32.6 KB) | `PB-16_V1_Admin_SR_reviewed_2026-10-19.png`, 7672 × 3636 | 1968.7 KB |
| `PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt` (25.9 KB) | `PB-16_V1_Clinical_SR_reviewed_2026-10-13.png`, 1416 × 730 | 153.9 KB |
| `PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` (22.8 KB) | `PB-16_V1_Finance_SR_reviewed.png`, 5700 × 2944 | 1246.3 KB |

The presentation figure `docs/istar/PB-16_sd-overview.png` (104.7 KB) is a JPEG with a `.png` extension. It is not one of the review assets.

**Reviewer**: Ryan (Guanyan He). **First owner**: Estrella.

**What to open.** Section 10 of the notes; section 4 (actors), section 5 (the 24-row dependency catalogue), section 7 (the D1–D24 corroboration table) and section 8 (out of scope); the four `.txt` sources in a text editor; the four PNGs at 100 % zoom.

**Check points.**

1. Section 10 carries exactly five items and none of the boxes is ticked. Yes or no.
2. The SD source declares nine actors; section 4 lists eleven. Is the explanation for the difference (section 4 is a catalogue, the figure is aggregated) written down anywhere the reviewer can read, and does it hold? Yes or no. An inconsistency here is a defect for the author, not something the reviewer edits.
3. Item 2 of section 10 reads "every SD dependency D1–D24 appears in the SR diagrams". Search the three SR `.txt` sources for `D3`, `D11`, `D13`, `D19`, `D21`, `D22`, `D23`, `D24`: none of the eight appears. Yes or no.
4. The SD figure itself draws thirteen dependencies: `D1, D2, D4, D5, D7, D9, D10, D12, D14, D15, D16, D18, D20`. Each of those thirteen appears in at least one of the three SR sources. Yes or no.
5. Section 8 lists five out-of-scope topics and includes forced role-based login; no line in the SD or SR text claims that role enforcement is implemented, which matches AT-03 recorded as FAIL. Yes or no.
6. All four PNGs open and their edge labels are legible at 100 %. Note that the Clinical figure is 1416 × 730, an order of magnitude smaller than the Admin figure. Yes or no.

**Where the sign-off goes.** Section 10 of `docs/istar/PB-16_istar-sd-sr.md`, under the five items, then the PB-16 Status cell in `docs/p3-product-backlog.md`. No re-export is needed for a Markdown signature.

**Blocker.** Check point 3 cannot be answered yes. The piStar sources cover 16 of the 24 catalogued dependencies. The reviewer has three honest routes: ask the author to add the eight to the sources and re-export the PNGs from piStar (the group's own work, not this checklist's), ask the author to reword section 10 item 2 to the thirteen drawn on the figure, or sign with the gap recorded. Signing while the box is ticked is not one of the routes. The preparation note `Est/est：PB-16二责复核备料_2026-10-19.md` sets out the same three options in more detail.

**Also record**: the PB-16 row is marked `Done` although its own second-owner checklist is unsigned and its Evidence cell says so. One of the two has to change, and only the first owner should change the row.

**Reading time**: 50 minutes, most of it on the four figures and the 24-row catalogue.

---

## 4. B-5 — V3 operational model and the two readable exports

**Deliverable.** `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` (131.7 KB, process id `Hospital_All_Processes_V3_C8`); `submissions/BPMEA/BPMEA_Operational_Process_Readable_2026-10-19.pdf` (2074.9 KB, 16 pages, A3 landscape) and `submissions/BPMEA/BPMEA_Strategic_Process_Readable_2026-10-19.pdf` (1582.5 KB, 8 pages). The deployment configuration named in the B-5 slot is `Week3 Coursework/hospital-pathway/src/main/resources/application.yaml` (0.9 KB) with `config/application.example.yaml` (1.2 KB).

**Reviewer**: Ender. **First owner**: Ruby.

**What to open.** Page 1 (model-of-record cover), page 3 (legend with job types) and pages 5–16 (twelve detail tiles) of the operational export; page 1 of the strategic export; the `.bpmn` file in a text editor for the counts that the cover does not print.

**Check points.**

1. The cover element summary reads 22 user tasks, 8 service tasks, 2 send tasks, 27 exclusive gateways (12 `Join_*` merges), 1 message catch event, 97 sequence flows. Do those six numbers match the `.bpmn` you opened? Yes or no.
2. The cover prints SHA-256 `17c59a8934a3a9552bf183c517017a09df46824fb53e7fbc30383dc20aeeace1`. Does `Get-FileHash` on the `.bpmn` return the same value? Yes or no.
3. The model contains no timer. The cover summary has no timer row and `timerEventDefinition` occurs zero times in the `.bpmn`. Yes or no. This is the count that matters for the letter deadline: the model cannot measure elapsed time.
4. The model carries 22 `zeebe:formDefinition` bindings resolving to 12 distinct formIds. The export does **not** print this count; it is in the `.bpmn` and in the audit block of `Week3 Coursework/hospital-pathway/evidence/Java_Clean_Build_Test_2026-10-19.txt`. Does the reviewer see 22 bindings and 12 ids? Yes or no.
5. Page 3 lists eight service-task job types. Added to the two send-task types on the same page (`request-payment`, `send-booking-confirmation`) they equal the ten `@JobWorker` types in the Java module. Yes or no.
6. The strategic cover names `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`, prints SHA-256 `8162a524b455f83c1e1def79c1c876a372a12e51a163d640dd41381a28a5716b`, and states that the model is not executable. Does `Get-FileHash` match, and does the export say it is non-executable? Yes or no.

**Where the sign-off goes.** The PB-30 Status cell in `docs/p3-product-backlog.md`, which currently reads `In progress`. No re-export is needed.

**Blocker.** None known. The diagram pages of both exports are raster content, so a reviewer judges layout by eye; the counts above are on the vector cover and legend pages and can be checked without reading pixels.

**Reading time**: 35 minutes.

---

## 5. B-6 — Java workers

**Deliverable.** `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/`: 17 Java files, 47.5 KB. `Week3 Coursework/hospital-pathway/src/test/java/io/camunda/demo/hospital/`: 3 files, 14.9 KB, 19 test methods. `pom.xml` (2.4 KB) and `src/main/resources/application.yaml` (0.9 KB). Evidence: `evidence/Java_Clean_Build_Test_2026-10-19.txt` (11.1 KB, `mvn -B clean test` at `dbc0a33`, 19 tests, BUILD SUCCESS) and `evidence/Java_Test_Results_2026-10-20.txt` (10.8 KB).

**Reviewers and first owners, by file.** Ownership is taken from section 5 of `Group_Project_and_Test_Plan_2026-10-20.pdf`, cross-checked against the module `README.md` and the actor strings the workers write into the audit table. No document assigns reviewers to worker files, so the reviewer column is a proposal that keeps reviewer ≠ author; record whoever actually reads.

| File | Job types | First owner (basis) | Reviewer | Test methods |
|------|-----------|--------------------|----------|--------------|
| `HospitalPathwayWorkers.java` | `request-payment`, `send-booking-confirmation` | Ruby (plan §5 names the file) | Ender | none |
| `RefundWorkers.java` | `request-refund`, `mark-payment-investigate` | Ruby (plan §5 names the file) | Ender | `RefundWorkersTest`, 10 |
| `ChargeAmountRules.java` | none; helper used by the two Ruby workers | **unknown** (plan §5 names only `ChargeAmountRulesTest`; commit `cb23fdf` is Estrella's) | Ender | `ChargeAmountRulesTest`, 2 |
| `BookingWorkers.java` | `check-slot`, `reserve-appointment`, `flag-resource-unavailable` | Estrella (plan §5; README "member B slots"; audit actor `member-B`) | Ryan | none |
| `LetterWorkers.java` | `dispatch-clinic-letter`, `notify-referrer` | Ender (plan §5; README "member C letters/referrer notification"; audit actor `member-C`) | Estrella | none |
| `CareChangeWorkers.java` | `notify-care-change` | Ryan (plan §5; audit key prefix `member-D`) | Estrella | `CareChangeWorkersTest`, 7 |
| `HospitalPathwayApplication.java` | none; loads the model and forms at startup | **unknown** | Ender | none |
| `domain/AuditEvent.java` | none | Ryan (plan §5) | Estrella | covered indirectly by `CareChangeWorkersTest` |
| `domain/AuditEventWriter.java` | none | Ryan (plan §5) | Estrella | `memberBOriginalAppendStillWorks` |
| `domain/AuditEventRepository.java` | none | **unknown** (plan gives domain repositories to Estrella and `AuditEvent.java` to Ryan) | Estrella | none |
| `domain/BookingSlot.java`, `BookingSlotRepository.java`, `BookingSlotStatus.java` | none | Estrella (plan §5 "the domain/ entities and repositories") | Ryan | none |
| `domain/PaymentLedger.java`, `PaymentLedgerRepository.java`, `PaymentLedgerStatus.java` | none | Estrella (same clause) | Ryan | none |
| `domain/DomainDatabaseConfig.java` | none | **unknown** (neither owner statement names a configuration class) | Ryan | none |

`unknown` means what it says. The reviewer still reads the file, but the group has to decide who answers for it before the signature claims a review of the whole module.

**What to open.** The five worker classes, the three test classes, and page 3 of the operational export for the job-type list. The 19 test methods are: `CareChangeWorkersTest` — `approvedChangeSavesNotification`, `missingApprovalSkipsNotification`, `paidChangeStillNeedsHumanFinanceReview`, `invalidInputCanBeCorrectedAndRetried`, `retriesReuseReceiptButLaterChangesGetNewReceipts`, `unknownTargetIsRejected`, `memberBOriginalAppendStillWorks`; `ChargeAmountRulesTest` — `acceptsTwoDecimalAmountsInsideRange`, `rejectsBlankLettersNegativeAndWrongScale`; `RefundWorkersTest` — `resolvedRefundWritesSuccessfulLedger`, `pendingRefundWritesInvestigateLedger`, `refundRetryReusesSameLedgerRow`, `markInvestigateWritesInvestigateAndSkipsAutoChargeFlag`, `missingAmountFailsWithoutWritingOrDefaulting`, `wrongPrecisionFailsWithoutWriting`, `investigateWithoutAmountDoesNotInventDemoCharge`, `partialRefundMustBeLowerThanTheOriginalCharge`, `transferAndRetainDoNotCountAsRefunds`, `missingCaseIdFailsWithoutWriting`.

**Check points.**

1. Every `@JobWorker(type = ...)` string matches a `zeebe:taskDefinition type` in `Hospital_All_Processes_V3.bpmn`: ten types across five classes. Do all ten match? Yes or no.
2. Every test method calls a public method of the class it is filed under, except one: `memberBOriginalAppendStillWorks` in `CareChangeWorkersTest` exercises `AuditEventWriter.append`, not `CareChangeWorkers`. Pair the rest: the 10 in `RefundWorkersTest` against `requestRefund` and `markPaymentInvestigate`; the 6 remaining in `CareChangeWorkersTest` against `notifyCareChange`; the 2 in `ChargeAmountRulesTest` against `ChargeAmountRules.require`. Is that the only exception, and does every method land on a named method? Yes or no.
3. Seven of the ten job types have no unit test: `check-slot`, `reserve-appointment`, `flag-resource-unavailable`, `request-payment`, `send-booking-confirmation`, `dispatch-clinic-letter`, `notify-referrer`. In `Camunda_V3_Acceptance_2026-10-19.txt` five of the seven appear on the G07 route; `flag-resource-unavailable` and `notify-referrer` appear in no run at all. Does the reviewer agree that the coverage claimed in the plan and in `BPMEA_Written_Evaluation` §4.7 is limited to those five? Yes or no.
4. Retry safety is visible in the source: `RefundWorkers.requestRefund` reuses the ledger row, `HospitalPathwayWorkers.requestPayment` reuses when `payment_requested_once` is true, `CareChangeWorkers.notifyCareChange` keys the receipt on `member-D|notify-care-change|<processInstanceKey>|<elementInstanceKey>`, and `BookingWorkers.upsertBooking` reuses by `occupancyKey`. Confirm that none of the four writes a second row on a retry with the same key. Yes or no.
5. The two `autoComplete = false` workers (`request-payment`, `request-refund`) complete explicitly after publishing or writing; the other eight complete automatically. Is that true for all ten job types? Yes or no.
6. No hardcoded secret and no patient or card data: `application.yaml` holds `demo`/`demo` for Camunda and `sa` with an empty password for the local H2 file, and the H2 file under `data/` is not committed. Yes or no.

**Where the sign-off goes.** No file currently records a B-6 review, and line 53 is a single group-level checkbox with nowhere to write a name. Two workable options, both of which the group performs itself: add a `reviewed by` line per file to section 5 of `Group_Project_and_Test_Plan_2026-10-20.docx` and re-export the PDF from Word, or write a short Markdown record under `Week6 Coursework/process/` and point the index at it. Tick line 53 of `docs/definition-of-done.md` only when every file above has a named reviewer and a date.

**Blockers.** Four files have no documented owner: `ChargeAmountRules.java`, `HospitalPathwayApplication.java`, `AuditEventRepository.java`, `DomainDatabaseConfig.java`. The reviewer cannot be shown to be independent of an author who is not recorded. Decide those four owners tonight, or sign the rest and list the four as unreviewed.

**Reading time**: 70 minutes.

---

## 6. B-7 — twelve Camunda forms

**Deliverable.** `Week6 Coursework/forms/`: 12 `.form` files, 38.3 KB in total — `await_attendance`, `book_treatment`, `book_visit`, `clinical_care`, `clinical_change`, `dispatch_letter`, `finance_adjustment`, `funding_assessment`, `register_request`, `review_referral`, `simple_record`, `urgent_authorisation`. The copies in `Week3 Coursework/hospital-pathway/forms/` are older, from before the 19 October validation pass, and are not the set to review.

**Reviewer**: Ruby. **First owner**: Estrella.

**What to open.** The twelve files in `Week6 Coursework/forms/`; the binding-audit block at the end of `Week3 Coursework/hospital-pathway/evidence/Java_Clean_Build_Test_2026-10-19.txt`; the `zeebe:formDefinition` bindings in `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`.

**Check points.**

1. Twelve files exist, and each file's internal `id` equals its filename. Yes or no.
2. The audit reports 22 user tasks, 12 distinct formIds, every formId resolving to a file, and no orphan file. Does the reviewer reach the same numbers from the BPMN? Yes or no.
3. `simple_record` is bound to eleven tasks: `Redirect`, `RecordDecline`, `RecordDna`, `FundingIssue`, `AdminEnquiry`, `ClinicalEnquiry`, `FinanceEnquiry`, `AuditReports`, `UrgentFinance`, `MonitorLetters`, `GetDocuments`. Are those the eleven listed in the audit? Yes or no.
4. Mandatory fields are present where the business rule needs them: `review_referral.form` marks `decisionReason` required (4 of 7 fields); `book_visit.form` marks `appointmentDate`, `appointmentTime` and `waitReason` required (8 of 10); `register_request.form` marks the timeframe fields required (8 of 10); every form marks `patientId` and `action` required. Yes or no.
5. No form carries a role check. All 22 user tasks are `assignee="demo"`, with zero `candidateGroups` and zero `candidateUsers`, so "form works for all user roles that access the task" cannot be asserted from these files. Does the reviewer say so rather than tick it? Yes or no.
6. Browser behaviour is not demonstrated: the 19 October acceptance drivers post JSON through REST `/v2` and bypass Tasklist, so required-field blocking is defined and bound but has never been shown to reject anything. Does the reviewer avoid claiming otherwise? Yes or no.

**Where the sign-off goes.** The PB-13 Status cell in `docs/p3-product-backlog.md`, which currently reads `Not started` and understates the artefact. The first owner should correct that row; the reviewer must not edit it. A signature inside the audit log would mean editing generated output or re-running the audit script, which is the group's decision, not part of this checklist.

**Reading time**: 30 minutes.
---

## 7. B-4 — `BPMEA_Written_Evaluation`, Part 2

**Deliverable.** `submissions/BPMEA/BPMEA_Written_Evaluation.docx` (36.6 KB) and `submissions/BPMEA/BPMEA_Written_Evaluation.pdf` (4500.8 KB, 23 pages). Part 2 is section 4, pages 12–17. Part 1 is section 3, pages 7–11.

**Reviewer**: Ruby. **First owner**: Ryan (PB-31).

**What to open.** Pages 12–17; the master record `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`; the three per-case JSON logs named in the results table; `submissions/AISD/Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf` (10 pages) for the earlier run.

**Check points.**

1. The field table on page 2 has `Part 2 owner: Guanyan He (Ryan) — PB-31` and `Status: Part 1 complete; Part 2 written 19 October, PB-31 sign-off not recorded`. Is there still no sign-off anywhere in the document, so the reviewer is not signing over an earlier one? Yes or no.
2. §4.3 carries seven rows with instance keys. Two spot checks against the master record: `2251799813930310` (AT-01) and `2251799813931091` (G07). Do both appear there, and does the G07 key come from `Group_Final_E2E_20261019-214234.json`? Yes or no.
3. AT-03 is recorded FAIL in both date columns and §4.4 gives the mechanism: 22 user tasks with `assignee="demo"`, zero candidate groups, no login beyond `demo`/`demo`. Does that match the model you opened for B-5? Yes or no.
4. The seven 29 September keys in §4.3 (`2251799813925318`, `2251799813925262`, `2251799813927118`, `2251799813927181`, `2251799813927283`, `2251799813927534`, `2251799813685458`) all appear in the initial-release acceptance record. Yes or no.
5. §4.7 gives the unit-test count as 19, split 7 / 2 / 10. Do the three test classes hold 19 methods in that split? Yes or no.
6. §4.6 lists seven limits, including browser-side validation, role enforcement, timers, the branches no case drives, treatment-slot unavailability, database rows and external systems. Is each of those limits kept out of the claims in §4.7? Yes or no.

**Where the sign-off goes.** The PB-31 Status cell in `docs/p3-product-backlog.md`, which currently reads `Done (sign-off not recorded)`. The document has no second-owner block of its own; if the group wants the signature inside the report, the first owner edits the `Status` row in the `.docx` and re-exports the PDF from Word. That re-export is the group's own work.

**Blocker.** None beyond the signature itself. Note that this is the second release of a section first drafted on 19 October; the reviewer reviews the text as it stands today, not the run it describes.

**Reading time**: 50 minutes.

---

## 8. B-3 and B-8 — not required by the rule

**B-3**, Part 1 of the same `BPMEA_Written_Evaluation` (pages 7–11; `.docx` 36.6 KB, `.pdf` 4500.8 KB, 23 pages). The rule does not reach it: Documentation has no review row (lines 55–60). No reviewer is declared for B-3 itself. Leave it unsigned unless the group decides otherwise tonight; if it does, PB-39 is the row that already names Ryan, because Part 1 rests on the traceability refresh. The honest wording for the index is "no second-owner review is required for Part 1; it is unsigned".

**B-8**, `submissions/BPMEA/Group_Project_and_Test_Plan_2026-10-20.pdf` (428.1 KB, 9 pages) with the `.docx` (26.9 KB) beside it. The rule does not reach it either: Delivery Evidence has no review row (lines 62–67), and no Second Owner is declared for it in `docs/p3-product-backlog.md` or in the sprint plan. Do not sign it and do not write a review claim into it. The honest wording for the index is "no second-owner review is required or recorded".

---

## 9. Before anyone signs

**A review is reading, not re-running.** Line 53 says `reviewed`. It does not say reproduced or re-executed. Reading the exports, the source and the evidence logs and answering the check points is the review. Nobody needs to start c8run, re-run Maven or redeploy anything tonight, and nobody should claim in a signature that they did.

**`README.md` line 93 says `The second owner reviews before merge`.** Everything in this checklist is already merged and tagged. A signature dated 20 October cannot claim a pre-merge review, and should not try. Write the signature as a review of the artefact at the time it was read: name the file, the date, and what was checked.

**Do not repeat the B-1 pattern.** In that review the reviewer wrote `Not yet accepted`, then edited the first owner's text herself (corrections A–D), then signed accepted, while the first owner's confirmation was oral only. Section 7 of the abstraction note records it. Tonight: if you find something wrong, report it to the author and let the author change it. Do not edit the text you are signing, and do not sign on behalf of anyone.

**Self-review is visible.** Page 1 of `submissions/AISD/AISD_Presentation_2026-10-19.pdf` carries `reviewed by Ruby 2026-10-19` on a deck whose first owner is Ruby. That is an A-series item and outside this checklist; the group may want to correct it.

---

## 10. What the index should say afterwards

`submissions/Submission_Index.pdf` (2 pages) and its `.docx` currently name B-2 as unsigned and B-4 as having no PB-31 sign-off, and say nothing about the review status of B-5, B-6 and B-7. Silence there reads as review by default. After tonight the `Limits recorded, not hidden` list should carry one line per item — signed by whom and when, or not required by the rule, or unsigned with the reason — so that no item, signed or not, is passed over in silence. Editing the index means editing the `.docx` and re-exporting it; that is the group's own work.

---

## 11. Sign-off sheet

Working record only. The record that counts is the file named in each section above.

| Item | Reviewer | Date | Outcome | Initials |
|------|----------|------|---------|----------|
| B-2 | Ryan | | Accepted / accepted with the item-2 gap recorded / not signed | |
| B-5 | Ender | | Accepted / not signed | |
| B-6 | Ender, Ryan, Estrella (by file) | | Accepted / accepted with the four unowned files listed / not signed | |
| B-7 | Ruby | | Accepted / not signed | |
| B-4 | Ruby | | Accepted / not signed | |
| B-3 | — | | Not required (section 8) | — |
| B-8 | — | | Not required (section 8) | — |

---

## 12. Outcomes at close, 20 October 2026

Every review above was completed and recorded on the day. This table is an index to the records; where it and a section above disagree, the section above was written earlier and the record named here wins.

| Item | Reviewer | Outcome | Where the record lives |
|------|----------|---------|------------------------|
| B-2 | Ryan | Reviewed; changes requested, then the Admin correction applied. Item 2 of the five-item checklist stays unticked and says why. | `docs/istar/PB-16_istar-sd-sr.md` sections 11 and 12 |
| B-5 | Ender | Accepted | PB-30 Status cell, `docs/p3-product-backlog.md` |
| B-6 | Ender, Ryan, Estrella, by file | Accepted for 13 of 17 files; the four with no recorded author are left unmarked rather than claimed | `Week6 Coursework/process/B-6_worker-review_2026-10-20.md` |
| B-7 | Ruby | Accepted | PB-13 Status cell, `docs/p3-product-backlog.md` |
| B-4 | Ruby | Accepted | PB-31 Status cell, `docs/p3-product-backlog.md` |
| B-3 | — | Not required by the rule; left unsigned | This section, and section 8 above |
| B-8 | — | Not required by the rule; left unsigned | This section, and section 8 above |

Two things this checklist asked for were **not** done, and are recorded as gaps rather than closed:

1. **The eight dependencies missing from the piStar sources** were not added. Item 2 of the five-item checklist therefore remains unticked in the model notes, and the reviewer's signature records the gap instead of hiding it.
2. **The Admin SR figure was not re-exported** after the nine contribution links were corrected in the source. The source and the PNG disagree until it is.

The Finance SR labels were checked against the catalogue in section 12.2 of the model notes and left as drawn: no link there is of a forbidden type, D18's task-level slice is the documented way this service view states a softgoal that belongs to the clinical boundary, and D17 restores a dependency the SD diagram omits. That figure still matches its source.
