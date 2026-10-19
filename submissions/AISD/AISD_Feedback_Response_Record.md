# Feedback response record (second release)

**Written**: 2026-10-16

**Refreshed**: 2026-10-19. Every point the repository can evidence now has a row. Nothing is filled in from memory, and no point that was not received is written down.

**Prepared by**: Estrella (Geping Chen 陈格平, UWE ID 23084393), first owner of this record

**Release**: the revised release, tagged `submission-2026-10-20`

**Required by**: the second-release brief, *Changes made in response to feedback*. The module specification also asks for a record identifying the point raised, the agreed response, the first and second owners, and evidence of completion, with a reason where an action was not implemented.

**What a row carries.** Every row in section 1 gives the six elements the brief asks for, each labelled: the point raised and its source, the decision, the action taken, the outcome, the evidence, and the owner pair. Section 3 carries the one point that was not implemented, with its reason, its residual risk and its next step, kept apart from the rows that were accepted and done.

**On the paths in this record.** Every path is written from the repository root, so it resolves from the same place as the pack's submission index. Where one row names several files from the same folder, the folder is given once and the remaining names follow bare. Every root-relative path was checked against the working tree on 2026-10-19; none is a remembered path.

## Where the points come from

| Source | Received or internal | Where the point is written down |
| --- | --- | --- |
| Group 10 peer review of the operational model | Received (peer), 4 items | The four items are transcribed one per row in `Ruby/2026-10-19/group10-feedback/README.md`. Item 3 is also named in four merge-gateway `documentation` elements (`Join_BookVisit`, `Join_ClinicalCare`, `Join_Funding`, `Join_BookTreatment`), which say the gateway was added in response to Group 10's merging-gateway feedback; item 4 is not named in the model. The mapping from each item to the boxes it changed is `Ruby/V2-临床SR与BPMN对照-第10组.md` §9 |
| Whole-class feedback sheet, filed at `Week6 Coursework/feedback/Group_Feedback_2026-10-13.docx` (originally received as `Group Feedback(1)(3).docx`) | Received (peer), 3 points, entry G07 | The document itself. Sourced in the repository on 2026-10-19; MD5 `5E1C42B0DC30D683575A2D51FED149BF`. Its G07 entry is quoted verbatim under "The class feedback sheet" below |
| The group's own review of the models and the matrix | Internal, not outside feedback | Per-element `Evidence` fields in the reviewed SR files; `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` |
| Tutor review | **Not received in writing** | Nothing. Section 2 is left blank on purpose |

Three consequences follow, and they are used below rather than left implicit. F-03 to F-07 are the group's own review points, not comments from outside, and each of those rows says so. The class feedback sheet is held in this folder, so F-09 and F-10 rest on the document rather than on a transcription. The four Group 10 items are held as a four-item transcription written on 19 October, not as the reviewer's own file; section 5 states what that leaves open.

## The class feedback sheet, and what it says beyond G07

The original is `Group_Feedback_2026-10-13.docx` in this folder. Four copies of the same file arrived (`Group Feedback.docx`, `Group Feedback(2).docx`, `Group Feedback(1)(1).docx`, `Group Feedback(1)(3).docx`) and all four are byte-identical, MD5 `5E1C42B0DC30D683575A2D51FED149BF`, dated 2026-10-13 11:35. Only one copy is filed, under a name that carries the date.

The G07 entry, verbatim:

> 1. Implement role-based access control in Camunda. 2. Improve form validation, particularly for date selections, to prevent invalid or inappropriate dates. 3. Implement database integration to support data persistence.

**When it arrived.** The file is dated 13 October 11:35, the day before SR3 on 14 October. That establishes the sheet was in the team's hands before SR3; it does not establish which session it was discussed in, and this record does not claim one.

**What the rest of the sheet shows.** The sheet holds 21 numbered entries, one per submission, of which 20 carry suggestions; entry 13 reads only "No marksheet was present." Counting the theme in each entry gives how the same three points were put to the class:

| Theme | Entries naming it (of 20) |
| --- | --- |
| Form or input validation | 18 |
| Role-based access, roles or cardinality | 14 |
| Database or persistence | 13 |
| Merging gateways | 12 |
| BPMN model correctness, task types or business logic | 9 |
| Data types or field types | 7 |
| More options or outcomes | 6 |
| Testing or acceptance criteria | 3 |

Two readings follow, and both are used in section 1 rather than left implicit:

1. **G07's three points are the three most repeated points on the sheet.** They read as marking criteria applied across the class, not as one reviewer's preference, which is why F-09 and F-10 were treated as must-do work for the second release rather than as optional improvements.
2. **The G07 entry names no BPMN, gateway or business-logic defect.** Every point addressed to this submission is about implementation maturity — constraints on the forms, access control, persistence. Only one other entry on the sheet reads the same way (entry 19: roles and input validation only); the remaining 18 all name a model, gateway, task-type or flow problem. The merge gateways in F-01 therefore answer Group 10's review, not this sheet: no entry asks this group for merging gateways, although 12 other entries ask their groups for them. The two feedback streams are separate and are not counted twice.

Who wrote the sheet is not stated in its body. It carries no reviewer column, and the phrase "No marksheet was present" reads as an assessor's note. Its document properties name a single author, but nothing else in the repository ties that name to a role, so the metadata settles nothing either way; the repository records the sheet as received (peer) feedback because that is how it was handed over. That classification is not settled by the document and is listed in section 5.

## 1. Points received, and what was done

Twelve points are recorded: F-01 to F-10 in this section, and F-11 in section 3 because it was not implemented. Seven of them rest on feedback received from outside the group (F-01, F-02, F-08a, F-08b, F-09, F-10, F-11); the other five (F-03 to F-07) are the group's own review, and each of those rows says so. F-08 arrived as two separate Group 10 items — first the data type of each input, then the refusal of missing or illegal input — and is recorded as F-08a and F-08b so that each rests on its own wording. Where one change answers two points, the outcome says so instead of counting the change twice.

### F-01 Merging gateways

| Element | Record |
| --- | --- |
| Point raised | Alternative paths met informally before a task instead of converging on one flow. (Group 10 review, item 3; transcribed in `Ruby/2026-10-19/group10-feedback/README.md`, row 3) |
| Decision | Accepted. Keep the split paths, but merge them explicitly before each downstream task instead of letting alternatives meet informally. |
| Action taken | Added seven pass-through exclusive merge gateways: `Join_BookVisit`, `Join_ClinicalCare`, `Join_Funding`, `Join_BookTreatment`, `Join_ClinicalChange`, `Join_VisitOutcome`, `Join_MarkPaymentInvestigate`; five more (`Join_ReviewReferral`, `Join_GetDocuments`, `Join_DispatchLetter`, `Join_FinanceAdjustment`, `Join_Register`) were added in V3. They carry no condition, default, synchronisation or deduplication. |
| Outcome | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` holds twelve `Join_*` gateways, each an `exclusiveGateway` whose `documentation` says it is a pass-through merge (counted in the file on 2026-10-19). Ten deliver into a user task; `Join_MarkPaymentInvestigate` delivers into that service task, and `Join_VisitOutcome` into the `VisitOutcome` gateway. The G07 instance of 2026-10-19 completed all nine of its human tasks through this model with no active incident, so the merges are in the model that ran, not only in a diagram. |
| Evidence | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`, the twelve `Join_*` gateway `documentation` elements; commits `8cda78c` (four merges, Ryan), `f90d31e` (three more, Estrella) and `357528e` (V3 rename plus five more); `Ruby/V2-临床SR与BPMN对照-第10组.md` §9; `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt` |
| Owners | First: Estrella. Second: Ruby. |

### F-02 Visit outcome

| Element | Record |
| --- | --- |
| Point raised | The options offered must cover the relevant business situations. On the original model one **Cancel / DNA** flow carried both a cancellation and a did-not-attend, so neither had its own outcome. (Group 10 review, item 4; transcribed in `Ruby/2026-10-19/group10-feedback/README.md`, row 4; the team's mapping of the item to the changed boxes is `Ruby/V2-临床SR与BPMN对照-第10组.md` §9) |
| Decision | Accepted. Only a booked or attended visit uses the slot worker, and each outcome is recorded as its own outcome rather than as a booking. |
| Action taken | Split `VisitOutcome` into attended, booked, pending/retry, patient cancelled, declined and did not attend. Added `AwaitAttendance`, `RecordDecline` and `RecordDna`. Added `VisitNeedsSlot` and `Join_VisitOutcome`, so decline, cancellation and DNA skip `CheckVisitSlot`. `book_visit.form` and the new `await_attendance.form` offer the same separate outcomes. |
| Outcome | `VisitOutcome` now has six outgoing flows and `VisitNeedsSlot` decides whether the slot worker runs at all. The G07 instance of 2026-10-19 recorded `visitOutcome=attended`, so the attended branch is evidenced by an executed case; the decline, cancellation and DNA branches are evidenced by the model and the forms only, because no executed case takes them. |
| Evidence | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`, `VisitOutcome` flows, `VisitNeedsSlot`, `Join_VisitOutcome`; `Week6 Coursework/forms/book_visit.form` and `await_attendance.form`; commits `e4b2159` (2026-10-13) and `305fccb` (2026-10-14) |
| Owners | First: Estrella. Second: Ruby. |

### F-03 Clinical SR: one care decision

| Element | Record |
| --- | --- |
| Point raised | One encounter records one care decision, so the OR-refinement under the care outcome was wrong. (Group review) |
| Decision | Accepted. Remove the OR-refinement beneath that outcome. |
| Action taken | One care decision (treatment / follow-up / discharge) recorded as a single task. |
| Outcome | The reviewed Clinical SR contains eleven `AndRefinementLink` and no `OrRefinementLink` (counted in the file on 2026-10-19), so there is no OR-refinement left under the care outcome. Commit `8ceb854` is the change, and its message states the intent. |
| Evidence | `Week6 Coursework/istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, diagram description; commit `8ceb854` (2026-10-15) |
| Owners | First: Estrella. Second: Ryan. |

### F-04 i\* dependencies against the case

| Element | Record |
| --- | --- |
| Point raised | Four of the i\* dependencies did not match the case wording. (Group review) |
| Decision | Accepted. Align them with the case. |
| Action taken | Dependency names, types and directions corrected. |
| Outcome | The three model notes and the SD were re-issued in the same commit, whose subject names the change as "Align four strategic dependencies with the case". The SD now expresses 13 of the 24 catalogue dependencies, and the four corrections are part of what the SD carries. |
| Evidence | Commit `25f53f7` (2026-10-14), which changed `docs/istar/PB-16_istar-sd-sr.md`, `docs/istar/PB-16_sd.md` and `docs/istar/PB-16_sr.md`; `Week6 Coursework/istar/V1_SD_diagram.txt`, which records alignment to the dependency catalogue at `2d09f5a` |
| Owners | First: Estrella. Second: Ryan. |

### F-05 SD scope

| Element | Record |
| --- | --- |
| Point raised | The SD carried detail that belongs in the per-service SR views. (Group review) |
| Decision | Accepted. Keep one maintained SD and move service detail into the SRs. |
| Action taken | SD reduced to nine aggregated actors and 13 selected dependencies; `D5` narrowed to new-patient acceptance only; `D10` separated from the scheduling dependency `D9`; `D18` treated as a softgoal. |
| Outcome | The SD file in the repository holds 9 actors and 13 dependencies (parsed on 2026-10-19), and the service detail sits in the three SR files. The figure `V1_SD_diagram.png` is the export of that same file, so the picture and the model cannot drift apart. |
| Evidence | `Week6 Coursework/istar/V1_SD_diagram.txt` and `Week6 Coursework/istar/V1_SD_diagram.png`; commits `5398f2c` and `13abe30` (2026-10-16) |
| Owners | First: Estrella. Second: Ryan. |

### F-06 Administrative rationale against the model

| Element | Record |
| --- | --- |
| Point raised | The administrative rationale had to be checked against the actual model, not the case alone. (Group review) |
| Decision | Accepted. Review every goal, task and resource against the operational model that was current at the time, `Hospital_All_Processes_V2`. |
| Action taken | Per-element `Evidence` and `V1 status` added; appointment-outcome wording corrected for decline, patient cancellation and did-not-attend. |
| Outcome | The Admin SR was re-exported on 2026-10-19: 29 elements each carry an `Evidence` field and a `V1 status` (counted in the file), and its figure was re-exported with it. The older `_2026-10-13` Admin file was renamed rather than kept beside the new one, so only one version is reachable. |
| Evidence | `Week6 Coursework/istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.txt` and its figure `Week6 Coursework/istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.png`; commits `2d09f5a`, `856568d`, `6865b35` (2026-10-14, 2026-10-15) |
| Owners | First: Estrella. Second: Ryan. |

### F-07 Traceability grading

| Element | Record |
| --- | --- |
| Point raised | The matrix did not separate what the release actually supports from what it only partly supports. (Group review) |
| Decision | Accepted. Grade every business rule against real evidence rather than intent. |
| Action taken | BR-01 to BR-42 graded, giving 12 supported, 26 partial and 4 unsupported, plus a second-release plan; the V2 refresh (13 supported, 25 partial, 4 unsupported) is carried in section 4 of the matrix. |
| Outcome | `docs/requirements-traceability-matrix.md` now grades all 42 rules, and each grade names the model element, form, worker or test behind it. Section 4 of the matrix states which of the 26 partial and 4 unsupported rules moved in the second release and which did not, so the refresh is auditable row by row rather than as a percentage. |
| Evidence | `docs/requirements-traceability-matrix.md`, sections 3 and 4 |
| Owners | First: Ruby. Second: Ryan. |

### F-08a Data type of each input

| Element | Record |
| --- | --- |
| Point raised | Every input box must use the right data type. (Group 10 review, item 1; transcribed in `Ruby/2026-10-19/group10-feedback/README.md`, row 1) |
| Decision | Accepted. Put a concrete type on the form each task opens, not a free-text box in the diagram. |
| Action taken | Appointments are date and time pickers (`book_visit`, `await_attendance`); the charge is a two-decimal number from 0.01 to 99999.99 (`funding_assessment.charge_amount`); the requested period is a number plus a unit, 1–365 days or 1–52 weeks (`register_request`); decisions and outcomes are selects whose values match the gateway conditions (`review_referral.action`, `clinical_care.action`, `funding_assessment.action`, `book_visit.action`). |
| Outcome | All 12 forms parse as JSON, each form's internal id equals its filename, and the 22 user tasks resolve to 12 distinct form ids with no orphan (form-binding audit, 2026-10-19). The acceptance runs set values through REST rather than through the Tasklist, so the types are inspected and bound, not exercised in a browser. |
| Evidence | `Week6 Coursework/forms/` (12 `.form` files); commits `c29df1c` (period as number and unit), `9a0b294` (numeric charge) and `357528e` (the V3 form set); `Week3 Coursework/hospital-pathway/evidence/Java_Clean_Build_Test_2026-10-19.txt`, form-binding audit |
| Owners | First: Estrella. Second: Ruby. |

### F-08b Missing or illegal input cannot be submitted

| Element | Record |
| --- | --- |
| Point raised | Missing or illegal input must not be submitted. (Group 10 review, item 2; transcribed in `Ruby/2026-10-19/group10-feedback/README.md`, row 2) |
| Decision | Accepted. Make the refusal happen on the form, and do not add a shape to the diagram for it. |
| Action taken | 58 of the 60 input fields across the twelve forms are `required`; the two exceptions are `finance_adjustment.charge_amount` and the free-text `review_referral.notes`. Required notes carry a minimum length of 2; patient, clinician and staff identifiers carry a format pattern; a new booking rejects a passed date and hides the date and time unless the outcome needs them; a pending booking requires a `waitReason`; a dispatch can only be marked `sent` with the clinical-approval box ticked. |
| Outcome | The constraints are visible in the form files and every one of them is bound to a task (same audit as F-08a). No acceptance case drives the form UI, so what is claimed is that the rules are written and bound, not that a browser was seen refusing a field. |
| Evidence | `Week6 Coursework/forms/book_visit.form`, `funding_assessment.form`, `register_request.form`, `review_referral.form`, `clinical_care.form`, `dispatch_letter.form`; commits `8a10e24`, `9a0b294`, `c29df1c`, `357528e`; `Ruby/V2-临床SR与BPMN对照-第10组.md` §9 |
| Owners | First: Estrella. Second: Ruby. |

### F-09 Dates cannot be unreasonable or past

| Element | Record |
| --- | --- |
| Point raised | Dates must not allow an unreasonable or past date. (Whole-class feedback, G07 entry, point 2) |
| Decision | Accepted. Enforce on the forms; the diagram gains no shape for it. |
| Action taken | `book_visit.form` sets `disallowPassedDates` on `appointmentDate` and shows that field only for a new booking; `register_request.form` bounds the requested period to 1–365 days or 1–52 weeks and requires it. The constraint is on the date being booked, not on the date a visit was attended, which is by definition in the past. |
| Outcome | The two form changes are in the V3 form set and are the same change recorded under F-08b. This row is kept because the point arrived from a different source, not because it needed a second change; the two rows are not counted as two fixes. |
| Evidence | `Week6 Coursework/forms/book_visit.form` and `register_request.form`; commit `8a10e24` (2026-10-14); `Week6 Coursework/feedback/Group_Feedback_2026-10-13.docx`, G07 entry, point 2 |
| Owners | First: Estrella. Second: Ruby. |

### F-10 Persist through a database

| Element | Record |
| --- | --- |
| Point raised | Store the data in a database rather than only in process variables. (Whole-class feedback, G07 entry, point 3) |
| Decision | Accepted, with one refusal: persist through the domain entities in an H2 file database, but do not add a database lane to the BPMN, because a data store is not a business actor or a stage. |
| Action taken | Domain schema landed with `AuditEvent`, `BookingSlot`, `PaymentLedger` and their repositories; `application.yaml` points JPA at `jdbc:h2:file:./data/hospital-domain` with `ddl-auto: update`. The workers write those tables. No database lane was added, deliberately. |
| Outcome | The schema and the file datasource are in the tree, and the 19 October run's worker log records the slot and payment workers completing (`booking_slot_status=CONFIRMED`, `tx=TX-6A6C28A4`). The run reads those values back as process variables, not as database rows, so persistence is evidenced by code and configuration, not by a query against the tables. |
| Evidence | `Week3 Coursework/hospital-pathway/src/main/resources/application.yaml`; `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/domain/` (`DomainDatabaseConfig.java`, `AuditEvent.java`, `BookingSlot.java`, `PaymentLedger.java`); commit `d95b79f` (2026-09-28); `Ender/2026-09-28/C_外部工作器与数据库说明.md`; `Week6 Coursework/feedback/Group_Feedback_2026-10-13.docx`, G07 entry, point 3 |
| Owners | First: Estrella. Second: Ender. |

How the owners are filled: the **first owner** carried the change in commits, and the **second owner** accepts the artefact, taken from the registered first owner of the backlog item the point belongs to — `PB-13` (forms) and `PB-30` (operational model) are both first owner Ruby. Where no backlog item covers the point, the second owner is the member who documented the area (F-10: the domain database). No name is left as "to confirm": a pair that cannot be named is a defect in this record, not a placeholder to carry.

## 2. Tutor feedback to be recorded

No tutor point has been received in writing as of 2026-10-19, so the rows stay blank. Only the peer feedback in section 1 has been received, and it is recorded there rather than here. A blank row is the honest state; it is not an omission to fill in later from memory.

| ID | Point raised (source, date) | Decision | Action taken | Outcome | First owner | Second owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-01 | | | | | | | |
| T-02 | | | | | | | |
| T-03 | | | | | | | |

## 3. Points raised and not implemented

The brief asks for the reason and any outstanding implications where an action was not taken. One point is in this position. It is kept out of section 1 so that nothing accepted and done is mixed with it, and so that no reader can take the role gap for a solved item.

The 19 October execution changes nothing in this section: the revised model was run, G07 reached `COMPLETED`, `AT-01`, `AT-02`, `AT-04`, `AT-05` and `AT-06` passed, and `AT-03` failed. The failure is recorded in `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`, which is the master record for the run.

| Element | Record |
| --- | --- |
| Point raised | Role-gated access: Camunda should enforce who may complete which task. (Whole-class feedback, G07 entry, point 1) |
| Decision | **Declined for this release.** Recorded as not implemented, not as partially done. |
| Reason not implemented | All 22 user tasks are `assignee="demo"` and the model declares no candidate groups or users (counted in the BPMN on 2026-10-19; the candidate-group count is zero). Delivering it needs the login and role matrix, an engine-side claim mapping and a re-run of the role test; the second release did not schedule that work. |
| Action taken | None. No candidate group, claim, login or role check was added. |
| Outcome | No change. `AT-03` failed again on the V3 model on 2026-10-19, exactly as it failed on 29 September: a Medical Secretary `Accept` still created `BookVisit` (`processInstanceKey` 2251799813930421). |
| Residual risk | Role enforcement does not exist at runtime. The three lanes on the diagram and the free-text `staffRole` field are labels, not checks, so any user who can reach the Tasklist can complete any task, including a Consultant decision. `BR-37` is Unsupported in the traceability matrix, and `BR-09`, `BR-21`, `BR-27` and `BR-31` stay Partial behind it. The risk is not confined to the demonstration: no part of the model refuses an action on the ground of who is performing it. |
| Evidence | `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`; `Week3 Coursework/hospital-pathway/evidence/PB-18_acceptance-run-log_2026-10-19.json`; `Ryan/2026-09-26/PB-18_acceptance-test-plan_2026-09-29.md` §5; `docs/requirements-traceability-matrix.md`, BR-37 row |
| Outstanding work | `PB-22` (first owner Ruby, second owner Estrella): role matrix, candidate groups on the user tasks, an engine-side claim mapping, then re-run `AT-03` expecting Pass. Until that is done the failure stays on the record. |

## 4. Claims this record does not make

- It does not claim that any tutor has given feedback that is not written above.
- It does not claim that the class feedback sheet is the work of one named source. The document is filed, but its body names no author and its document properties name someone the repository cannot tie to a role; the entry is attributed to peer review because that is how it was handed over.
- It does not claim that Group 10's items 1 and 2 were exercised through the Tasklist. The constraints sit in the form files and every form is bound to its task; no acceptance case drives the browser form, so the claim is that the rules are written and bound, not that a user was seen stopped.
- It does not claim that the 19 October run tested the forms, the role layer or the branches no case takes. The run set values through REST, and it recorded one path per case; the form-binding audit proves the twelve forms parse and bind, not that they refuse input.
- It does not claim that the V1 statuses in the SR files are verified fulfilment. The SR files state the opposite: a dependency records a business need, and the mock or manual status is carried on the element, not on the dependency name.
- It does not claim that the role-permission criterion has been fixed. `AT-03` is still a recorded failure; section 3 is where the gap and its handling now sit.

## 5. What is still open in this record

| Open point | Why it is open | What would close it |
| --- | --- | --- |
| The four Group 10 items survive as a transcription | `Ruby/2026-10-19/group10-feedback/README.md` gives each item one line under the heading "原文", written by the group on 19 October. The reviewer's own document is not in the repository, so the wording of items 1 and 2 is quoted from that transcription | Add the reviewer's file; check the four lines against it |
| The class feedback sheet names no author | The document is filed as `Group_Feedback_2026-10-13.docx`, but its body carries no reviewer column, and "No marksheet was present" in entry 13 reads as an assessor's note. Its document properties name one author, but the repository records nothing about that person's role, so the metadata is not enough to reclassify the sheet. The record calls it peer feedback because that is how it was handed over | Confirm with the module team whether the sheet is peer or tutor feedback; if tutor, move F-09 and F-10 into section 2 and leave section 1 as peer points only |
| The identifier "G07" | The sheet numbers its entries 1 to 21 and says nothing about which submission each number belongs to. The link to this group comes from `Ruby/2026-10-15/问题咨询总结.md`, which keys entry 7 to this repository; the three points there also match entry 7 word for word. The same string is a test id in the acceptance run (`Week3 Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json`), so one confirmation covers both uses | Confirm at SR4 that entry 7 is this group's review entry |
| Tutor points (section 2) | None received in writing | Record each point as given, on its own row |

The split of F-08, open on 16 October, is now closed. The earlier draft could not separate the two items without guessing which asked for what; the 19 October transcription gives them separately, so F-08a and F-08b rest on their own wording and no evidence had to be added to make the split.
