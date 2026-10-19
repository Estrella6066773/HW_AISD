# Feedback response record (second release)

**Written**: 2026-10-16
**Refreshed**: 2026-10-19. Every point the repository can evidence now has a row. Nothing is filled in from memory, and no point that was not received is written down.
**Required by**: the second-release brief, *Changes made in response to feedback*. The module specification also asks for a record identifying the point raised, the agreed response, the first and second owners, and evidence of completion, with a reason where an action was not implemented.

## Where the points come from

| Source | Received or internal | Where the point is written down |
| --- | --- | --- |
| Group 10 peer review of the operational model | Received (peer), 4 items | Item 3 is quoted in the model itself: "Added in response to Group 10 feedback on merging gateways." All four are set out in `../V2-临床SR与BPMN对照-第10组.md` §9 |
| Whole-class feedback sheet `Group Feedback(1)(1).docx`, the entry keyed to this repository as G07 | Received (peer), 3 points | The sheet is not in the repository. Its three points are transcribed in `../../Ruby/2026-10-15/问题咨询总结.md`, section "第 7 组反馈" |
| The group's own review of the models and the matrix | Internal, not outside feedback | Per-element `Evidence` fields in the reviewed SR files; `../istar/PB-16_V1-V2_review-changes_2026-10-16.md` |
| Tutor review | **Not received in writing** | Nothing. Section 2 is left blank on purpose |

Two consequences. F-03 to F-07 are the group's own review points, not comments from outside; each row says so. The class feedback sheet is reached through a repository transcription, and Group 10's items 1 and 2 only through the repository's summary of them — section 5 states what that leaves open.

## 1. Points received, and what was done

| ID | Point raised (source) | Decision | Action taken | First owner | Second owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | Merging gateways: alternative paths met informally before a task instead of converging on one flow. (Group 10 review, item 3) | Keep the split paths, but merge them explicitly before each downstream task instead of letting alternatives meet informally | Added seven pass-through exclusive merge gateways: `Join_BookVisit`, `Join_ClinicalCare`, `Join_Funding`, `Join_BookTreatment`, `Join_ClinicalChange`, `Join_VisitOutcome`, `Join_MarkPaymentInvestigate`. They carry no condition, default, synchronisation or deduplication | Estrella | Ruby | `../bpmn/Hospital_All_Processes_V2.bpmn`, the seven `Join_*` gateway `documentation` elements; commits `8cda78c` (four merges, Ryan) and `f90d31e` (three more, Estrella); `../V2-临床SR与BPMN对照-第10组.md` §9 |
| F-02 | Visit outcome: decline, patient cancellation and did-not-attend were treated as if a slot had to be reserved. (Group 10 review, item 4) | Only a booked or attended visit uses the slot worker, and each outcome is recorded as its own outcome rather than as a booking | Split `VisitOutcome` into attended, booked, pending/retry, patient cancelled, declined and did not attend. Added `AwaitAttendance`, `RecordDecline` and `RecordDna`. Added `VisitNeedsSlot` and `Join_VisitOutcome`, so decline, cancellation and DNA skip `CheckVisitSlot`. `book_visit.form` and the new `await_attendance.form` offer the same separate outcomes | Estrella | Ruby | Same model, `VisitOutcome` conditions, `VisitNeedsSlot`, `Join_VisitOutcome`; `../../Week3 Coursework/hospital-pathway/forms/book_visit.form` and `await_attendance.form`; commits `e4b2159` (2026-10-13) and `305fccb` (2026-10-14) |
| F-03 | Clinical SR review against the case: one encounter records one care decision, so the OR-refinement under the care outcome was wrong. (Group review) | Remove the OR-refinement beneath that outcome | One care decision (treatment / follow-up / discharge) recorded as a single task | Estrella | Ryan | `../istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, diagram description; commit `8ceb854` (2026-10-15) |
| F-04 | Case-alignment review of the i\* dependencies: four of them did not match the case wording. (Group review) | Align them with the case | Dependency names, types and directions corrected | Estrella | Ryan | Commit `25f53f7` (2026-10-14) changed `../../docs/istar/PB-16_istar-sd-sr.md`, `PB-16_sd.md` and `PB-16_sr.md`; `../istar/V1_SD_diagram.txt` records alignment to the dependency catalogue at `2d09f5a` |
| F-05 | The SD carried detail that belongs in the per-service SR views. (Group review) | Keep one maintained SD and move service detail into the SRs | SD reduced to nine aggregated actors and 13 selected dependencies; `D5` narrowed to new-patient acceptance only; `D10` separated from the scheduling dependency `D9`; `D18` treated as a softgoal | Estrella | Ryan | `../istar/V1_SD_diagram.txt` diagram description; commits `5398f2c` and `13abe30` (2026-10-16) |
| F-06 | The administrative rationale had to be checked against the actual model, not the case alone. (Group review) | Review every goal, task and resource against `Hospital_All_Processes_V2` | Per-element `Evidence` and `V1 status` added; appointment-outcome wording corrected for decline, patient cancellation and did-not-attend | Estrella | Ryan | `../istar/PB-16_V1_Admin_SR_reviewed_2026-10-13.txt`, diagram description; commits `2d09f5a`, `856568d`, `6865b35` (2026-10-14, 2026-10-15) |
| F-07 | Traceability review: the matrix did not separate what the release actually supports from what it only partly supports. (Group review) | Grade every business rule against real evidence rather than intent | BR-01 to BR-42 graded, giving 12 supported, 26 partial and 4 unsupported, plus a second-release plan; the V2 refresh (13 supported, 25 partial, 4 unsupported) is recorded in section 4 | Ruby | Ryan | `../../docs/requirements-traceability-matrix.md`, sections 3 and 4 |
| F-08 | Form-level: dates, decisions and amounts should be entered through constrained controls and required fields rather than free text. (Group 10 review, items 1 and 2 — the repository records the two items together, so they share this row; see section 5) | Put the constraints on the form each task opens, not on a shape in the diagram | Added or tightened in V2: `appointmentDate` rejects a past date, and a pending booking hides date and time and requires a `waitReason` (`book_visit`); `charge_amount` is a two-decimal number from 0.01 to 99999.99 and is required on the patient-payment path, with `insurerReference` required on the insurer path (`funding_assessment`); the requested period is a bounded number plus a unit (`register_request`). The decision and care-plan dropdowns that the review also covers already existed as required selects in `review_referral` and `clinical_care` on 29 September and are unchanged | Estrella | Ruby | `../../Week3 Coursework/hospital-pathway/forms/book_visit.form`, `funding_assessment.form`, `register_request.form`, `review_referral.form`, `clinical_care.form`; commits `8a10e24`, `9a0b294`, `c29df1c`; `../V2-临床SR与BPMN对照-第10组.md` §9 |
| F-09 | Dates must not allow an unreasonable or past date. (Whole-class feedback, G07 entry, point 2) | Enforce on the forms; the diagram gains no shape for it | `book_visit.form` sets `disallowPassedDates` on `appointmentDate`; `register_request.form` bounds the requested period to 1–365 days or 1–52 weeks and requires it | Estrella | Ruby | `../../Week3 Coursework/hospital-pathway/forms/book_visit.form`, `register_request.form`; commit `8a10e24` (2026-10-14); `../../Ruby/2026-10-15/问题咨询总结.md` |
| F-10 | Store the data in a database rather than only in process variables. (Whole-class feedback, G07 entry, point 3) | Persist through the domain entities in an H2 file database; do not add a database lane to the BPMN, because a data store is not a business actor or a stage | Domain schema landed with `AuditEvent`, `BookingSlot`, `PaymentLedger` and their repositories; `application.yaml` points JPA at `jdbc:h2:file:./data/hospital-domain` with `ddl-auto: update`. The workers write those tables. No database lane was added, deliberately | Estrella | Ender | `../../Week3 Coursework/hospital-pathway/src/main/resources/application.yaml`; `../../Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/domain/` (`DomainDatabaseConfig.java`, `AuditEvent.java`, `BookingSlot.java`, `PaymentLedger.java`); commit `d95b79f` (2026-09-28); `../../Ender/2026-09-28/C_外部工作器与数据库说明.md` |

How the owner columns are filled: the **first owner** carried the change in commits, and the **second owner** accepts the artefact, taken from the registered first owner of the backlog item the point belongs to — `PB-13` (forms) and `PB-30` (operational model) are both first owner Ruby. Where no backlog item covers the point, the second owner is the member who documented the area (F-10: the domain database). No name is left as "to confirm": a pair that cannot be named is a defect in this record, not a placeholder to carry.

## 2. Tutor feedback to be recorded

No tutor point has been received in writing as of 2026-10-19, so the rows stay blank. Only the peer feedback in section 1 has been received, and it is recorded there rather than here. A blank row is the honest state; it is not an omission to fill in later from memory.

| ID | Point raised (source, date) | Decision | Action taken | First owner | Second owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 | | | | | | |
| T-02 | | | | | | |
| T-03 | | | | | | |

## 3. Points raised and not implemented

The brief asks for the reason and any outstanding implications where an action was not taken.

| ID | Point | Reason not implemented | Outstanding implication | Proposed next step |
| --- | --- | --- | --- | --- |
| F-11 | Role-gated access: Camunda should enforce who may complete which task. (Whole-class feedback, G07 entry, point 1) | Deferred. All 22 user tasks are still `assignee="demo"` and the model declares no candidate groups or users. Delivering it needs the login and role matrix, an engine-side claim mapping and a re-run of the role test; the second release did not schedule that work | `AT-03` still fails: a Medical Secretary can still accept a referral and open `BookVisit` (`../../Ryan/2026-09-26/PB-18_acceptance-test-plan_2026-09-29.md` §5). `BR-37` stays Unsupported in the traceability matrix, and `BR-09`, `BR-21`, `BR-27` and `BR-31` stay Partial behind it | `PB-22` (first Ruby, second Estrella): role matrix, candidate groups on the user tasks, then re-run `AT-03` expecting Pass |

## 4. Claims this record does not make

- It does not claim that any tutor has given feedback that is not written above.
- It does not claim that the class feedback sheet is held in the repository. Its three points are a member's transcription from that sheet, and F-09 to F-11 rest on the transcription, not on the sheet itself.
- It does not claim that Group 10's items 1 and 2 were fully implemented. Dates and amounts were added or tightened; the decision, care-plan and other required selects they also cover were already in place on 29 September.
- It does not claim that the V1 statuses in the SR files are verified fulfilment. The SR files state the opposite: a dependency records a business need, and the mock or manual status is carried on the element, not on the dependency name.
- It does not claim that the role-permission criterion has been fixed. `AT-03` is still a recorded failure; F-11 is where the gap and its handling now sit.

## 5. What is still open in this record

| Open point | Why it is open | What would close it |
| --- | --- | --- |
| Group 10's items 1 and 2 are one row (F-08) | The review's original wording is not in the repository; only the summary in `../V2-临床SR与BPMN对照-第10组.md` §9 records the two items together. Splitting them here would mean guessing which item asked for what | Add the original review text; then split F-08 into one row per item, keeping the same evidence |
| The class feedback sheet itself is not in the repository | The record rests on a transcription in `问题咨询总结.md`, made by one member | Add `Group Feedback(1)(1).docx` (or a saved copy) under `feedback/`, and quote its G07 entry directly |
| The identifier "G07" | The transcription keys the sheet's entry to this repository as G07. The same string is also a test id in the acceptance run (`Group_Final_E2E_20260929-135729.json`), so the link between the two uses needs one confirmation | Confirm at SU4 that the G07 entry in the sheet is this group's review entry |
| Tutor points (section 2) | None received in writing | Record each point as given, on its own row |
