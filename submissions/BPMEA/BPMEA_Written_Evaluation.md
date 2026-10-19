# BPM&EA Written Evaluation

**Requirements alignment and acceptance criteria — second release**

| Field | Value |
| --- | --- |
| Module | UFCEP4-0-3 Business Process Modelling & Enterprise Architecture |
| Assessment | End of Week 6 · Full Portfolio (second release) |
| Group | 10 |
| Members | Hao Zheng (Ruby, 23084382) · Geping Chen (Estrella, 23084393) · Minghao Qin (Ender, 23084402) · Guanyan He (Ryan, 23084395) |
| Date | 2026-10-19 |
| Part 1 owner | Geping Chen (Estrella) — `PB-39` |
| Part 2 owner | Guanyan He (Ryan) — `PB-31` |
| Status | Part 1 complete; Part 2 written 19 October, `PB-31` sign-off not recorded |
| Accompanying deliverables | Strategic BPMN (B-1), i\* SD/SR (B-2), supporting files and readable PDF exports (B-5) |

---

## How the two parts fit together

This document carries both halves of the written evaluation the portfolio asks for.

**Part 1 — requirements alignment.** Takes the 42 business requirements in the case study and asks, one rule at a time, whether the second release moved the rule that the initial release left open. Every answer is tied to a named artefact and a commit.

**Part 2 — acceptance criteria.** Takes the acceptance criteria the group set for itself, the results actually recorded, the evidence behind those results, and the failures that remain. Its owning item is `PB-31`; Section 4 was written from the evidence on 19 October.

Both parts share one evidence set and one status vocabulary, so they are written into one file rather than two. A rule that Part 1 grades Partial because no test exercises it is the same gap Part 2 has to account for.

---

## 1. Purpose and method

### 1.1 The question this evaluation answers

The initial release was submitted on 29 September with a traceability matrix that graded every requirement. That matrix was written **before** the model was improved. The question this evaluation answers is narrower than "is the model better": for each rule the first release marked Partial or Unsupported, **did the artefact the gap depends on actually change in the second release, and if it did not, why not?**

A second release can look substantial — more gateways, more forms, more workers — while leaving the graded gaps exactly where they were. This document is written to make that difference visible, including where the answer is unflattering.

### 1.2 Where a requirement can live

Each requirement is traced across four artefacts, not one:

| Layer | Artefact | What a rule needs from it |
| --- | --- | --- |
| Strategic | `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | The rule is visible as a stage, role or interaction |
| Operational | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` (`Hospital_All_Processes_V3_C8`) | The rule is carried by a task, gateway, event or data object |
| Implementation | `Week6 Coursework/forms/` (the deployed form set) and `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/` | The rule is enforced or recorded, not merely described |
| Acceptance | `pb14_acceptance.py`, `pb18_acceptance.py` and their records | The rule is demonstrated on a running process |

A rule is only as strong as its weakest enforced layer. This is why a rule can be drawn correctly, described correctly in a task's documentation, and still be graded Partial: a sentence in a task description is not an implementation.

### 1.3 The grading scale

| Mark | Meaning | Test applied |
| --- | --- | --- |
| ✅ Supported | Fully addressed in this deliverable | The rule can be completed as written using the artefacts named above |
| ⚠️ Partial | Partly addressed | Part of the rule is enforced or recorded; the limitation is named in the Notes |
| ❌ Unsupported | Not addressed | Justified, with the route it would take in a later release |

The scale is deliberately strict at the artefact level. It does not award a rule for being desirable, for appearing in a task description, or for working only because the operator chose to behave correctly. Where the group chose that reading knowingly, it is stated.

### 1.4 The "moved" test

A rule counts as **moved** only when **the artefact its earlier Notes named actually changed**. It does not count as moved because:

- a task description gained stronger wording (documentation is not enforcement);
- a neighbouring rule was fixed;
- the process now reaches the step more reliably by ordering alone;
- a form gained a field that is not the one the gap named.

This test is what separates 1 grade movement from 4. Section 3.4 uses it to explain each of the 26 rules that stayed put.

### 1.5 Scope limits

The evaluation judges **alignment**, not quality of modelling style. It does not grade whether the BPMN is elegant, whether the naming is consistent, or whether a different modelling choice would have been better. Those belong to the justification of decisions, not to traceability.

It also does not manufacture evidence. Where the second release added a capability but nothing was run, the row says "not exercised", never "passed".

---

## 2. The evidence set

### 2.1 Versions fixed

The second release is graded against these exact artefacts. Every claim in Sections 3 and 4 resolves to one of them.

| Artefact | Version graded | Change since 29 September |
| --- | --- | --- |
| Strategic BPMN | `PB-12_strategic-process_2026-09-29.bpmn` and `PB-12_abstraction-level_2026-09-29.md` | **None.** Both unchanged (`88a5bcc`). |
| Operational BPMN | `Hospital_All_Processes_V3.bpmn`, process `Hospital_All_Processes_V3_C8` | **New model**, built across `8cda78c` … `787375e`, then renamed and extended in `357528e` |
| Initial-release model | `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`, `Hospital_All_Processes_Simple_C8` | Untouched; remains the submitted baseline and is tagged `submission-2026-09-29` (`f6fec99`) |
| Forms | 12 forms in `Week6 Coursework/forms/` (the set the deployment packages) | 4 changed and 1 new in V2; all 12 gained input validation in the 19 October feedback pass; `dispatch_letter` and `book_visit` each gained one field |
| Workers | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/` | `ChargeAmountRules` added (`cb23fdf`); `RefundWorkers` and `HospitalPathwayWorkers` changed. The 20 Java files under `Week6 Coursework/code/` are byte-identical |
| Acceptance tests | `pb14_acceptance.py`, `pb18_acceptance.py`, `g07_e2e_acceptance.py` and their run records | **Re-run against V3 on 19 October.** The two existing scripts changed in one constant: `PROCESS` now reads `CAMUNDA_PROCESS_ID`, defaulting to `Hospital_All_Processes_V3_C8`. `g07_e2e_acceptance.py` is new and repeats the 29 September G07 method. Results, instance keys and limits are in Section 4; the master record is `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`. |

The second release was **added alongside** the first, not substituted for it. The initial-release model stays in the repository and stays executable, so the two versions can be compared directly. This matters for the portfolio: it asks for an identifiable initial release and a revised version, and both now exist as distinct, tagged artefacts.

**V3 replaces V2 as the operational model of record.** Commit `357528e` deleted `Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn` and added the V3 file with the same content plus five further merge gateways, renamed to `Hospital_All_Processes_V3_C8`. V2 now exists only in history (`6c572b3`); an earlier revision of the same model also remains at `Week3 Coursework/hospital-pathway/bpmn/Hospital_All_Processes_V2.bpmn` (127,869 bytes against 126,772 in the deleted file, so not byte-identical) but it is no longer packaged by the build. Every V2 statement in this document has been re-checked against V3, and every path cited below points at the file the repository now deploys.

### 2.2 What the second release actually contains

The V3 model changes that matter for traceability, in one place:

- **Visit outcome split.** `VisitOutcome` carries six conditions — attended, pending/retry (the gateway default), patient cancelled, booked awaiting attendance, declined, did not attend — with `AwaitAttendance`, `RecordDecline` and `RecordDna` as separate steps.
- **Slot check made conditional.** `VisitNeedsSlot` skips the outpatient slot when the visit is not being booked, so a cancellation no longer passes through slot reservation.
- **Requested review period structured.** Stored as a number plus a unit; a past appointment date is rejected (`disallowPassedDates`).
- **Finance.** The finance form shows the original charge; an invalid refund fails once (`retries(0)`) instead of three times.
- **Merge gateways.** Twelve exclusive join gateways are pass-through and change no rule. Seven came from V2 (`Join_BookVisit`, `Join_ClinicalCare`, `Join_Funding`, `Join_BookTreatment`, `Join_ClinicalChange`, `Join_VisitOutcome`, `Join_MarkPaymentInvestigate`); V3 adds five more (`Join_ReviewReferral`, `Join_GetDocuments`, `Join_DispatchLetter`, `Join_FinanceAdjustment`, `Join_Register`). Each has one unconditional outgoing flow and no default. They are recorded here so that a reader counting gateways does not mistake added structure for added coverage.
- **Form input validation.** All 12 forms in the deployed set gained a `patientId` pattern; ten of them carry a second pattern on `staffRole`, `clinicianId` or, in `funding_assessment`, `insurerReference`. The `patientId`, `staffRole` and `clinicianId` patterns require a leading letter, so a value made only of digits is rejected; `insurerReference` accepts a leading digit. All four are format checks, not identity or role checks.
- **Two new form fields.** `book_visit` gained `attendedOn`, the date the patient attended, which now feeds `appointmentDate` when a visit is recorded as attended. `dispatch_letter` gained a required `letterClinicallyApproved` checkbox on the *sent* path.

**What V3 does not add.** The process id and participant names changed and five gateways appeared; no user task, event, sequence-flow condition or assignment did. All 22 user tasks are still `assignee="demo"` with no candidate groups or candidate users, and the model still contains **no timer event of any kind**. Neither of the two questions that decide BR-37 and the four timer-dependent rules is answered by this release.

Forms: in V2, `book_visit` (`e4b2159`, `8a10e24`), `finance_adjustment` (`32e6dbc`, `1816b8e`), `funding_assessment` (`9a0b294`) and `register_request` (`c29df1c`, `8a10e24`) changed, and `await_attendance` (`e4b2159`) was new. The 19 October pass then touched every form. The deployed copies are `Week6 Coursework/forms/`; `Week3 Coursework/hospital-pathway/forms/` holds the pre-validation revision. The two directories contain the same 12 filenames, but all 12 files differ, so a reader must cite the directory they mean.

### 2.3 What did not change

Two facts carry most of Section 3:

1. **The strategic model is byte-identical to 29 September.** Every strategic cell in the matrix therefore keeps its initial release value. Where a strategic stage was missing then, it is still missing.
2. **The executed acceptance run did not move a grade.** The six criteria and the G07 path were re-run against V3 on 19 October and reproduced the 29 September pass/fail pattern exactly, including the `AT-03` failure (Section 4). That is a result about the path the cases cover: none of them drives a branch that a Partial note in Section 3.4 names, so no rule could move on this evidence even where it passed. Section 4.7 explains the connection.

Section 2 of the traceability matrix describes the 29 September executable and must be read as its result, not as a V3 result; Section 4.3 below is the V3 result.

---

## 3. Part 1 — Requirements alignment evaluation

### 3.1 Headline result

| Release | ✅ Supported | ⚠️ Partial | ❌ Unsupported |
| --- | ---: | ---: | ---: |
| Initial release (29 September) | 12 | 26 | 4 |
| Second release (V3, 19 October) | 13 | 25 | 4 |

**One grade moved. Three gaps narrowed. Twenty-six rules are untouched.**

The count is identical to the V2 position recorded earlier on 19 October. That is not a coincidence: V3 added five merge gateways, renamed the process and revalidated the forms, and none of those artefacts carries a rule. The rebase changed paths and descriptions, not grades.

The acceptance run of the same evening (Section 4) does not change it either. Six of the seven criteria pass on V3 and the count stays where it was, for the reason 4.7 sets out: a passing case can only upgrade a rule when the case reaches the gap that rule's Notes name.

That is the honest summary, and it should be read as a statement about the second release's *aim*, not only about its effort. The release was driven by the class feedback on implementation maturity and by the visit-outcome modelling problem, both of which were worth doing. Neither of them was a traceability gap named in the matrix. The result is a release that is genuinely better as a process and barely different as a coverage profile.

The next three sub-sections take the result apart: what moved, what narrowed, and what did not.

### 3.2 The one rule that moved: BR-20

BR-20 requires that an authorised Finance member decides a refund — in full or in part — and that the amount is recorded. The matrix marked it Partial for exactly one reason: *no explicit full versus partial refund amount control*.

| Initial-release gap | What the second release has instead | Where |
| --- | --- | --- |
| Refund decision is coarse (resolved / pending) | The decision selects `refund_full`, `refund_partial`, `transfer`, `retain` or `pending`; `adjustmentAmount` is mandatory on every decision except `pending` | `finance_adjustment.form` (`32e6dbc`; deployed copy `Week6 Coursework/forms/`) |
| No amount control | `resolveAdjustment` maps each decision to its own ledger status; `requirePartialAmount` rejects a partial amount that is not lower than the original charge | `RefundWorkers.java` (`1816b8e`) |
| Original charge could be overwritten | The form displays `charge_amount` as the original charge and the worker never writes it back; an invalid amount or unknown decision fails the job once | `ChargeAmountRules.java` (`cb23fdf`) |

**Why Supported rather than still Partial.** The gap the matrix named — the absence of full/partial selection and of the amount — is closed in both the form and the worker. The rule is now completable as written, which is the test in 1.3. V3 left the refund fields and the worker untouched, so the re-check changes nothing here.

**Two limits, recorded rather than hidden.**

- **No acceptance case reaches the refund path.** BR-20 is Supported without its own acceptance test, following the BR-11 precedent, where a modelled and implemented rule is Supported and the missing test is listed in Notes. `RefundWorkersTest` now holds ten tests at `dbc0a33` (it held five on 29 September), but a worker test is not an acceptance run: `FinanceAdjustment` is never reached by `AT-01`–`AT-06` or by G07.
- **Role enforcement is not part of this grade.** BR-20 asks for an *authorised* Finance member. The matrix consistently grades role enforcement under BR-37 (see the BR-02 and BR-09 notes), so BR-37 remains the row that carries the gap. Moving BR-20 to Supported does not imply that an unauthorised user is blocked; it implies that the refund decision itself is now expressible and validated.

### 3.3 Three gaps narrowed without a grade change

These are the cases where the second release did real work on the named gap but not enough to close it. They are reported separately because a coverage count of 13/25/4 hides them.

| Req | What the second release added | Why the grade did not move |
| --- | --- | --- |
| **BR-36** Cancel / reschedule / DNA | `RecordDecline` and `RecordDna` are separate tasks; `AwaitAttendance` holds the booked visit; `VisitOutcome` carries six distinct conditions; decline and DNA enter `Join_ClinicalChange`, so the pathway decision happens at `ClinicalChange` and paid cases reach `FinanceAdjustment` through `MoneyAffected`; both `book_visit.form` and `await_attendance.form` offer the separate outcomes; `book_visit.form` now records `attendedOn`, the date the patient attended | The split is delivered, but no acceptance case runs DNA → pathway decision → Finance, and **reschedule is still not a recorded outcome of its own** — it is a re-booking through `BookVisit` with `pending`. Both were named in the earlier Notes. |
| **BR-35** Follow-up booking | `book_visit.form` rejects a past appointment date, hides date and time unless the outcome is `booked` or `attended`, and makes `waitReason` mandatory (`no_slot`, `contact_incomplete`, `external_waiting`); the requested period is a number plus a unit. The 19 October validation pass kept all of this and added input patterns | There is still no out-of-timeframe flag or pathway-team notification **separate from** the pending branch, and no follow-up booking test. The booking side is structured; the rule's named gap is not closed. |
| **BR-13** Funding organisation, reference, amount, limits | `funding_assessment.form` requires `charge_amount` as a two-decimal number from 0.01 to 99999.99 on the patient-payment path, and requires `insurerReference` on the insurer path; both are re-checked by `ChargeAmountRules.require` | Amount and reference are now structured, but there is still **no dedicated limitations/restrictions field** — they remain inside `notes`. Partial stands. |

Two further form changes are deliberately **not** counted as narrowing, because they fail the test in 1.4:

- **`dispatch_letter.letterClinicallyApproved`.** The deployed form requires a checkbox confirming that the clinician approved the letter before it can be marked sent. The `DispatchLetter` task maps no input for that variable, and `LetterWorkers.dispatchClinicLetter` never reads it, so the process records a self-declaration rather than an approval it can check. The gap BR-30 names — a letter body, recipients and an approval time — is untouched, and the grade stays Partial.
- **`book_visit.attendedOn`.** It is mapped and does capture an attendance date, which is a real record. It does not supply the reschedule outcome BR-36's Notes named, so it strengthens that row's evidence without moving the rule.

The pattern is consistent: the release structured what could be structured on a form and stopped short of the new step, flag or test that the rule actually needed.

### 3.4 The 26 rules that did not move: six shared causes

The remaining rules are not 26 separate failures. Read together, they fall into a small number of causes, and that is the most useful thing this evaluation can say about the next release.

| Cause | Rules | What the cause is | What one fix would move |
| --- | --- | --- | --- |
| **C1 — no role model** | BR-09, BR-19, BR-21, BR-27, BR-31 | All 22 user tasks in V3 are still `assignee="demo"`. There are no candidate groups, no candidate users, no claims and no login beyond `demo`/`demo` | BR-37 delivered → five rules can be re-graded, and `AT-03` becomes a pass condition |
| **C2 — no timer or scheduled-event capability** | BR-06, BR-32, BR-33, BR-34 | The V3 model contains no timer events at all, so no rule whose substance is "within seven days", "after one month", "unless already sent" or "shorten the timescale" can be enforced | A single timer pattern applied at four places |
| **C3 — records still unstructured** | BR-01, BR-04, BR-05, BR-08, BR-23, BR-25, BR-28, BR-30 | Every rule that asks for a *record* — a contact attempt, a consent, an urgent postponement, a blood-test result, a letter body with recipients and approval time — is still free text in `notes`, or has no field at all | Structured fields plus a validation rule per form; no engine change needed |
| **C4 — modelled and implemented, never exercised** | BR-22 | The formal change path, the unauthorised skip (`SKIPPED_UNAUTHORISED`) and Finance routing all exist, but no acceptance case drives them | Three acceptance cases; no build work |
| **C5 — blocked on a decision the group cannot take alone** | BR-29 | The urgency highlight rules are still a stakeholder clarification; the only mechanism is a manual priority value | A decision from the tutor or client, then a queue or alert |
| **C6 — capability never built** | BR-10, BR-37, BR-38, BR-39, BR-40, BR-41, BR-42 | External treatment/lab/imaging coordination remains mocked; there is no read-only audit API, no patient matching, no offline fallback, no report output and no communication preference | Each is a new capability, not a refinement |

Note that several rules appear in more than one story — BR-19 also lacks test coverage, BR-36 also lacks a test — but each is assigned here to its **primary** cause, which is the one that has to be removed first.

Three observations follow from the grouping.

1. **C1 and C2 are single capabilities with multiple dependants.** One role model unlocks five rules; one timer pattern unlocks four. Nine of the 26 rows are waiting on two pieces of work.
2. **C3 is the largest group and the cheapest to fix.** Eight rules need a form field and a check, not a process redesign. The second release already demonstrated it can do this — BR-13 and BR-20 are both C3-type rules that were partly and fully closed.
3. **Only one rule (BR-22) is blocked purely on test coverage.** That is worth stating plainly, because it means "we have no evidence" is not the general explanation for the coverage profile. In most cases the behaviour is not there to evidence.

### 3.5 Why the second release did not close more rows

The honest answer is that the release was aimed elsewhere, and the reasons were good.

- **The class feedback was about implementation maturity**, not about the traceability matrix: validation, roles, persistence. The second release answered the validation part (`ChargeAmountRules`, date rejection, mandatory `waitReason`, and the input patterns added on 19 October) and left the roles part open — which is exactly why the role-model cause (C1) remains the largest single lever in 3.4.
- **The operational model had a real modelling defect** — a visit outcome that could not express cancellation, decline and DNA separately. Fixing it was more urgent than any single traceability row, and it narrowed BR-36 and BR-35 as a side effect.
- **No one owned the matrix between 29 September and 19 October.** The refresh had to be done after the model changes, which means the changes were never steered by the rule gaps. A matrix refreshed *before* a release would have made C1 and C2 visible as blockers rather than as findings.

That last point is the lesson worth carrying forward: the matrix was used as a record of what happened, not as an input to what was planned.

### 3.6 Two columns, and what happened to them

| Column | State | Consequence |
| --- | --- | --- |
| **Strategic BPMN** | `PB-12` has not changed since 29 September, so this column could not be refreshed | BR-25, BR-29, BR-38, BR-39, BR-40, BR-41 and BR-42 remain ❌ in that column even where V3 implemented part of the operational work. The strategic picture and the operational picture now disagree in seven places. |
| **Acceptance tests** | Refreshed on 19 October from the executed run against V3 (Section 4); it could not be refreshed when 3.1–3.5 were written | The cells in Section 2 describe the 29 September executable and keep that meaning; the V3 verdicts, instance keys and evidence files are in 4.3. The refresh changed no grade, because the same six cases were run and none of them drives a branch the Partial notes name. |

The strategic column is the more serious of the two. A reader comparing the strategic model with the operational model would find stages in the operational model that the strategic model does not show, and a reviewer is entitled to ask which one is the intended design.

### 3.7 Leverage order for the next release

Measured by rules moved per unit of work:

1. **BR-37 — role model and candidate groups.** P0. Unlocks BR-09, BR-19, BR-21, BR-27 and BR-31, and turns `AT-03` from a recorded failure into a pass condition. No other single item comes close.
2. **BR-38 — audit immutability.** P0. The append-only writer exists; what is missing is a read-only audit API and a refusal test. It also underwrites BR-28's enquiry trail.
3. **BR-08 — consent and a structured treatment request.** P0. The artefact did not change at all in the second release; the task text asks for fields that do not exist.
4. **The timer pattern (C2).** One implementation, four rules.
5. **BR-22 — three acceptance cases.** The cheapest row on the list, because the behaviour already exists.

---

## 4. Part 2 — Acceptance criteria evaluation

> **Status: written 19 October; `PB-31` sign-off not recorded.** Part 2 belongs to `PB-31`. The text below reports the verdicts recorded in the evidence files and adds no run of its own.

### 4.1 The criteria, fixed before the results

The group set seven criteria for the executable pathway: six case-level criteria (`AT-01` to `AT-06`) and one end-to-end path (`G07`). They were written for the initial release against `Hospital_All_Processes_Simple_C8`, and they were **not** rewritten for the second release. That is what makes a before-and-after comparison possible at all: same criterion, same driver, two models.

| ID | What the case asks | Pass rule |
| --- | --- | --- |
| `AT-01` | Documents checked, consultant accepts, new-patient booking opens, clinical care reachable | `BookVisit` created after accept; `referralDecision=accept` with a reason; `ClinicalCare` reached; rejected end not taken; no active incident |
| `AT-02` | Consultant rejects; the case closes without a booking | State `COMPLETED`; `referralDecision=reject` with a reason; `BookVisit` never created; no active incident |
| `AT-03` | A Medical Secretary submits Accept, which the case rule forbids | The engine refuses the accept, so `BookVisit` is not created |
| `AT-04` | No suitable slot within the requested period | `BookVisit` reopens as pending; `ClinicalCare` absent; `visitOutcome=pending`; no active incident |
| `AT-05` | Payment fails, then a person retries | Failure routed to investigation and a funding issue; retry succeeds; `BookTreatment` reached; no duplicate charge |
| `AT-06` | Provider may have taken the money, confirmation missing | `payment_status=investigate`; `BookTreatment` not auto-opened; no automatic second charge |
| `G07` | One referral through the whole pathway to discharge | Nine human tasks completed in order; final state `COMPLETED`; the recorded variables set; zero active incidents |

A case passes only when every check listed for it matches. A failure is kept as a failure, with its reason, and is not reworded once a later run behaves differently. The plan behind the first six is `Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf`; the working plans are `PB-14_acceptance-test-plan_2026-09-29.md` and `PB-18_acceptance-test-plan_2026-09-29.md`.

### 4.2 Two runs of the same cases

| | 29 September 2026 | 19 October 2026 |
| --- | --- | --- |
| Model under test | `Hospital_All_Processes_Simple_C8`: definition version 6 for `AT-01`–`AT-06`, version 1 for `G07` | `Hospital_All_Processes_V3_C8`, definition key `2251799813928658`, version 1 |
| Engine | local c8run 8.10.0-alpha5, REST `/v2` on `localhost:8080` | the same, started with `c8run.exe start --disable-connectors`; gRPC `26500`; `demo`/`demo` |
| Workers | `mvn spring-boot:run` from `Week3 Coursework/hospital-pathway` | the same |
| Drivers | `pb14_acceptance.py`, `pb18_acceptance.py` | the same two scripts, whose only change is that `PROCESS` now reads `CAMUNDA_PROCESS_ID` and defaults to V3; plus a new `g07_e2e_acceptance.py` that repeats the 29 September G07 method |
| Repository tree | `fc6293e`, the tree the 29 September runs were made from; the submitted release is tagged `submission-2026-09-29` (`f6fec99`) | `dbc0a33` |
| Deployment | definition version 6 of the simple model | deployment `2251799813928657` of V3, version 1 |

The cases, the data shape and the checks are unchanged; only the process id moved. `g07_e2e_acceptance.py` is new because the 29 September G07 driver was never committed — it drives the same REST `/v2` sequence and asserts the same variables.

### 4.3 Results

| Case | Purpose | 29 September | 19 October (V3) | Evidence file | Instance key (V3) |
| --- | --- | --- | --- | --- | --- |
| `AT-01` | Main path: accept, book, reach clinical care | PASS | **PASS** | `PB-14_acceptance-run-log_2026-10-19.json` | `2251799813930310` |
| `AT-02` | Reject closes the case; no booking | PASS | **PASS** | `PB-14_acceptance-run-log_2026-10-19.json` | `2251799813930247` |
| `AT-03` | Secretary must not decide acceptance | **FAIL** | **FAIL** | `PB-18_acceptance-run-log_2026-10-19.json` | `2251799813930421` |
| `AT-04` | No suitable slot returns to pending booking | PASS (limited scope) | **PASS** | `PB-18_acceptance-run-log_2026-10-19.json` | `2251799813930493` |
| `AT-05` | Failed payment, no duplicate charge, retry | PASS | **PASS** | `PB-18_acceptance-run-log_2026-10-19.json` | `2251799813930607` |
| `AT-06` | Payment taken, confirmation missing, investigate | PASS | **PASS** | `PB-18_acceptance-run-log_2026-10-19.json` | `2251799813930876` |
| `G07` | Full self-pay route to completed care | PASS (selected route, version 1) | **PASS — `COMPLETED`** | `Group_Final_E2E_20261019-214234.json` | `2251799813931091` |

Six of the seven criteria pass on V3; one fails, and it is the same one that failed on 29 September. The 29 September instance keys are `2251799813925318` (`AT-01`), `2251799813925262` (`AT-02`), `2251799813927118` (`AT-03`), `2251799813927181` (`AT-04`), `2251799813927283` (`AT-05`), `2251799813927534` (`AT-06`) and `2251799813685458` (`G07`), so each pair can be opened side by side in Operate.

The G07 run completed nine human tasks in order — `Register`, `ReviewReferral`, `BookVisit`, `ClinicalCare`, `DispatchLetter`, `Funding`, `BookTreatment`, a second `ClinicalCare` and a second `DispatchLetter` — with `activeIncidents: []`. Its final variables show the path the assertions claim: `referralDecision=accept`, `visitOutcome=attended`, `careDecision=discharge`, `letterStatus=sent`, `fundingStatus=patient_paid`, `payment_status=successful`, `booking_slot_status=CONFIRMED`, `confirmation_sent=true`.

The 29 September `AT-01`–`AT-06` run was against **definition version 6** of the simple model and is labelled "historical" in the submitted acceptance record; `G07` was against version 1 of the same model. The V3 run is a single definition, version 1. The comparison is therefore between two models, and on the six exception cases also between two deployments of the first model — a looser control than a laboratory would accept, and the reason the table keeps the model and version columns rather than presenting the two results as interchangeable.

### 4.4 The failure: `AT-03` fails in both releases

`AT-03` asks one thing: that a person labelled as a Medical Secretary cannot decide a referral. It fails on V3 exactly as it failed on 29 September. This is **the same defect observed twice, not a regression**, and the evidence file says so in its own words:

> Case rule: secretaries must not accept referrals. Observed: Accept by staffRole Medical Secretary still created BookVisit. Proposed handling: implement role candidate groups / Identity (PB-22); keep this FAIL visible until then.

The mechanism is unchanged from the first release. All 22 user tasks in V3 are `assignee="demo"`, with zero candidate groups and zero candidate users; there is no login beyond `demo`/`demo`. The `staffRole` the case sets is a free-text field written by the same user it is meant to constrain, so the engine has nothing to check it against. The case cannot pass by behaving differently: it is asking the model to enforce something the model does not contain.

Two consequences are stated rather than softened. First, the second release does not improve the role boundary, and the traceability matrix keeps BR-37 ❌ Unsupported with BR-09, BR-21, BR-27 and BR-31 Partial for the same cause. Second, no acceptance result in this evaluation should be read as evidence that any task is performed by the right person; the cases record who submitted what, not who was entitled to.

### 4.5 An environment event, and why the evidence files look the way they do

The record keeps one failure that is not a test result:

- The first c8run start, without `--disable-connectors`, was shut down at 21:38 because the bundled Connectors runtime never became healthy.
- One G07 attempt, `Group_Final_E2E_20261019-213833.json`, died at 21:38:33 with a connection reset (`[WinError 10054]`). It has an instance key (`2251799813929726`), no completed tasks, and no verdict beyond `FAIL` and the error text.
- Every case was then re-run in one continuous session after restarting at 21:40 with connectors disabled. All results in 4.3 come from that session, and the file timestamps (`214113`, `214159`, `214234`, master record `2145`) reflect it.
- The engine stayed healthy throughout. The shutdown was the connector health check, not the process model.

One further file is worth naming rather than leaving for a reader to find. `Group_Final_E2E_20261019-214113.json` records a G07 instance (`2251799813929943`) that reached `COMPLETED` with the same variables as the cited run but lists no completed tasks. It is not the file behind 4.3: the run recorded there (`2251799813931091`, `214234`) repeats the path and captures the ordered nine-task trail. The instance could not have reached `COMPLETED` with those variables had the nine human tasks not been completed, so the empty list is a task-collection failure in that attempt, not evidence that the path was shorter. It is retained for the same reason as the failed JSON, and it supports no claim on its own.

The failed JSON is deliberately retained. Deleting it would make the record look as though the first attempt never happened, and the difference between "the criterion failed" and "the environment died mid-run" is precisely what an acceptance record has to preserve. It is not counted in 4.3 and is never presented as a pass.

### 4.6 What the evidence does not cover

Each of these is a boundary of the claim, not a defect to be discovered later:

1. **Browser-side form validation.** The drivers submit values through REST `/v2`, which completes the same user tasks and writes the same variables but bypasses the form. Required fields, input patterns, `disallowPassedDates`, the mandatory `waitReason` and conditional visibility are therefore **not exercised** by these runs. No claim about Tasklist behaviour follows from a PASS in 4.3.
2. **Role enforcement.** `AT-03` is the only case aimed at it, and it fails. There is no run with distinct role identities.
3. **Timers.** The model contains no timer event. Nothing here evidences the seven-day letter target or the 7-day / 1-month / 3-month escalation, because nothing in the model measures elapsed time.
4. **Branches that no case drives.** The formal change path and its unauthorised skip (BR-22), decline and DNA through the pathway decision to Finance (BR-36), urgent authorisation (BR-19), letter escalation (BR-33), refund through `FinanceAdjustment` (BR-20), the three enquiry paths (BR-26 to BR-28) and follow-up booking (BR-35). G07 used `visitOutcome=attended`; `AT-04` used `pending` on a first visit. Neither drives a decline or a DNA, so BR-36's record is not strengthened by this run.
5. **Treatment slot unavailability.** G07 confirms the confirmed side (`booking_slot_status=CONFIRMED`, one reservation, one confirmation). No case drives a treatment resource to pending.
6. **Database rows.** The cases assert process variables and worker-log lines. They do not query the H2 tables, so no direct booking, ledger or audit row count is claimed.
7. **External systems.** Payment, scheduling and correspondence are all local mocks. Nothing here is evidence about a live provider.

### 4.7 Assessment

**What the run licenses.** V3 executes the route the cases cover, end to end, with the workers wired to the right job types: nine human tasks in order, ten true assertions on the G07 variables, zero active incidents, and the same verdicts on the six exception cases as the first release. The visit-outcome rebuild, the slot-skip gateway and the twelve pass-through merges did not regress the tested path. At unit level, `mvn -B clean test` at `dbc0a33` is `BUILD SUCCESS` with 19 tests and no failures — `CareChangeWorkersTest` 7, `ChargeAmountRulesTest` 2, `RefundWorkersTest` 10 — and the binding audit resolves 22 user tasks to 12 form ids and 12 files with no orphan.

**What it does not license.** It does not license acceptance of the branches in 4.6, and it does not license a statement that "the tests pass". One criterion fails, and it fails for a reason the release did not address.

**How this connects to Part 1.** The coverage profile stays at **13 Supported / 25 Partial / 4 Unsupported**. That is not in tension with six passing cases; it follows from the grading rule in 1.4. A case can only move a rule when it reaches the gap that rule's Notes name. `BR-22` is the clearest test of this: it was the one rule blocked purely on test coverage, and none of `AT-01`–`AT-06` or G07 enters `ClinicalChange`, submits an invalid change or routes a paid change to Finance, so it stays Partial with the same reason — the path exists and is unexercised. The worker tests that do exercise `SKIPPED_UNAUTHORISED` and `SENT_FINANCE_REVIEW_REQUIRED` were already recorded in the first release's evidence and are not acceptance cases. `BR-36` and `BR-35` stay Partial because the run used `attended` and a first-visit `pending`; `BR-19`, `BR-09`, `BR-21`, `BR-27`, `BR-31` and `BR-37` stay where they were, and `AT-03` failing on V3 is the operational face of that.

**The judgement.** The second release is now demonstrated to work on the route it was tested on, and still not demonstrated anywhere else. The submission's claim should be exactly that: a working, worker-backed V3 pathway with one known, replicated role failure and an acceptance set that has not yet been widened to the branches the traceability review names. That is a stronger claim than the evidence allowed before the run, and a weaker one than "acceptance passed".

### 4.8 What a complete second-release acceptance record would still need

- `AT-07` formal change: authorised change posts `SENT_FINANCE_REVIEW_REQUIRED`; invalid change posts `SKIPPED_UNAUTHORISED`; a paid change reaches `FinanceAdjustment`.
- `AT-08` decline or DNA → `ClinicalChange` pathway decision → `FinanceAdjustment` when money is affected.
- `AT-09` urgent authorisation → `BookTreatment` → `UrgentFinance`.
- `AT-10` refund through `FinanceAdjustment`, asserting the ledger row.
- `AT-11` treatment resource pending, then ready, with one occupancy row.
- One Tasklist walkthrough with screenshots, so form validation and conditional fields have evidence of their own.
- A re-run of `AT-03` with distinct role identities once `PB-22` delivers candidate groups.

---

## 5. Limitations and threats to validity

1. **The count is not a score.** 13 of 42 Supported says nothing about how much of the clinical pathway works. The rules are not equally weighted by business risk, and BR-37 alone blocks four operational rules.
2. **The grading is strict by choice.** A rule that works because the operator behaves correctly is Partial, not Supported. A more generous reading would produce a higher count and a less useful document.
3. **The V3 test evidence is narrow by construction.** One model, one engine build, seven cases and one route; it establishes that the covered path executes and establishes nothing about the branches 4.6 lists. Where a judgement here rests on reading artefacts rather than on a run, the row says so.
4. **The strategic column is stale by construction.** Section 3.6 states this rather than correcting it, because correcting the strategic model was outside this release.
5. **The case study leaves some rules genuinely underdetermined** — BR-29's urgency rules are the clearest example. Grading those Partial rather than Unsupported reflects that the gap is a missing decision, not missing engineering.

---

## 6. Conclusion

The second release improved the process and did not improve its alignment profile. One rule moved to Supported, three narrowed, and 26 are untouched — and the 26 are concentrated in five causes, two of which (the role model and timers) account for nine rules between them.

The defensible claim is therefore not that the second release closed the gaps. It is that the gaps are now **enumerated, attributed and ordered**: the group knows that BR-37 is the highest-leverage item, that BR-38 and BR-08 are the next P0s, that eight rules are waiting on a form field rather than a redesign, and that only one rule is blocked on test coverage alone. That is a more useful position than a higher count produced by grading generously.

---

## Appendix A — All 42 rules, second-release position

Status is the V3 position. "Basis" names where the judgement comes from: a sub-section of the traceability matrix, or the initial-release row carried forward because the artefact did not change. All 42 rows were re-checked against V3 on 19 October; the traceability matrix's §4.8 records that re-check and §4.9 records the executed acceptance run. Only BR-30, BR-35 and BR-36 gained rule-relevant evidence from the model, and none of the three changed grade. The acceptance run moved no row: where it touches a rule it is cited below, and where a row still says "no acceptance case" that remains true after 19 October.

| Req | Requirement (abbreviated) | V3 status | Basis |
| --- | --- | --- | --- |
| BR-01 | Secretaries verify referral documents and request missing items | ⚠️ Partial | §4.5 — `GetDocuments`, `register_request.form`: no rule-relevant change (input patterns only) |
| BR-02 | Consultant accepts / rejects / redirects with reason and ID | ✅ Supported | §2, carried forward; `review_referral.form` gained input patterns only |
| BR-03 | Bookings team arranges appointment via external scheduler | ✅ Supported | §2, carried forward; `book_visit.form` changed but the rule's substance was already met |
| BR-04 | Letter, and telephone within two weeks | ⚠️ Partial | §4.5 — no channel fields, no send task |
| BR-05 | Each contact attempt and outcome recorded | ⚠️ Partial | §4.5 — still `notes` text |
| BR-06 | Urgent referrals skip normal timescales | ⚠️ Partial | §4.5 — priority value only, no skip path, no timers |
| BR-07 | No suitable slot → highlight / refer | ✅ Supported | §2, carried forward |
| BR-08 | Consent and authorised Treatment Booking Request | ⚠️ Partial | §4.5 — `clinical_care.form`: no rule-relevant change (input patterns only) |
| BR-09 | Unauthorised requests blocked from admin processing | ⚠️ Partial | §4.5 — cause is BR-37; `AT-03` reproduced the failure on V3 (§4.4) |
| BR-10 | Coordinate with external treatment / lab / imaging | ⚠️ Partial | §4.5 — remains mocked inside `book_treatment` |
| BR-11 | Pending on unavailable service; no duplicates | ✅ Supported | §2, carried forward; G07 confirms the confirmed-slot side only, no case drives treatment to pending (§4.6) |
| BR-12 | Funding determination: hospital / insurer / patient | ✅ Supported | §2, carried forward |
| BR-13 | Funding organisation, reference, amount, limitations | ⚠️ Partial | §4.4 — amount and reference structured; limitations still free text |
| BR-14 | Secure payment request; no card storage | ✅ Supported | §2, carried forward |
| BR-15 | Payment returned: status, reference, date, amount | ✅ Supported | §2, carried forward |
| BR-16 | No treatment confirmation until payment complete | ✅ Supported | §2, carried forward |
| BR-17 | Payment failure → notify, retry, no duplicate charge | ✅ Supported | §2, carried forward |
| BR-18 | Orphaned payment marked for investigation | ✅ Supported | §2, carried forward |
| BR-19 | Urgent treatment bypass with recorded reason | ⚠️ Partial | §4.5 — no acceptance case; none enters `UrgentAuthorisation`; clinician-only authorisation unenforced |
| BR-20 | Authorised Finance member decides refund, full or partial | ✅ Supported | §4.3 — form and worker both changed; `RefundWorkersTest` holds 10 tests, but no acceptance case reaches `FinanceAdjustment` |
| BR-21 | Financial and clinical responsibilities separated | ⚠️ Partial | §4.5 — `staffRole` is free text; cause is BR-37, and `AT-03` still fails (§4.4) |
| BR-22 | Treatment change only via system, authorised | ⚠️ Partial | §4.5 — path exists, no acceptance case; the 19 October run never enters `ClinicalChange`, so the reason is unchanged (§4.7) |
| BR-23 | Urgent postponement with retrospective authorisation | ⚠️ Partial | §4.5 — free text |
| BR-24 | Financial impact of change → Finance review | ✅ Supported | §2, carried forward |
| BR-25 | Chemotherapy cycle review; clinical decision only | ⚠️ Partial | §4.5 — no blood-test or fitness fields |
| BR-26 | Enquiry classified admin / financial / clinical | ✅ Supported | §2, carried forward |
| BR-27 | Call handlers may not give clinical advice | ⚠️ Partial | §4.5 — policy text only; no acceptance case; cause is BR-37 |
| BR-28 | Every enquiry recorded, classified, prioritised, routed | ⚠️ Partial | §4.5 — priority added; no audit record on enquiry paths |
| BR-29 | Urgent clinical enquiry highlighted immediately | ⚠️ Partial | §4.5 — urgency rules still a stakeholder decision |
| BR-30 | Consultant writes and approves clinic letter | ⚠️ Partial | §4.5, §4.8 — `dispatch_letter.form` gained a `letterClinicallyApproved` checkbox, but no BPMN input or worker reads it; no letter body, recipients or approval time |
| BR-31 | Secretaries fix admin errors, not clinical content | ⚠️ Partial | §4.5 — not enforced; cause is BR-37, and `AT-03` still fails (§4.4) |
| BR-32 | Seven-day completion target for letters | ⚠️ Partial | §4.5 — no dates captured, no timer |
| BR-33 | Delay escalation at 7 days / 1 month / 3 months | ⚠️ Partial | §4.5 — manual task, no timers |
| BR-34 | No duplicate reminders; delay reasons recorded | ⚠️ Partial | §4.5 — no reminder service |
| BR-35 | Follow-up booking; highlight if outside timeframe | ⚠️ Partial | §4.4, §4.8 — booking structured and retained; no out-of-timeframe flag |
| BR-36 | Cancel / reschedule / DNA recording and consequences | ⚠️ Partial | §4.4, §4.8 — split delivered and `attendedOn` added; reschedule not its own outcome; the 19 October runs used `attended` and a first-visit `pending`, so no decline or DNA case exists |
| BR-37 | Role-based access control | ❌ Unsupported | §4.5, §4.8, §4.9 — all 22 user tasks `assignee="demo"`; no candidate groups, no login; `AT-03` fails on V3 exactly as on 29 September |
| BR-38 | Immutable audit records: user, time, action | ⚠️ Partial | §4.5 — writer unchanged; no read-only API or refusal test |
| BR-39 | Patient identity deduplication | ❌ Unsupported | §4.5 — `patientId` free text |
| BR-40 | Availability and fallback for time-sensitive work | ❌ Unsupported | §4.5 — no offline log or catch-up task |
| BR-41 | Management reports on volumes, waits, delays, KPIs | ⚠️ Partial | §4.5 — placeholder human task |
| BR-42 | Communication preferences respected | ❌ Unsupported | §4.5 — no preference field, no worker reads one |

---

## Appendix B — Evidence index

| Reference | Artefact |
| --- | --- |
| Traceability matrix, initial release | `docs/requirements-traceability-matrix.md` §2 |
| Traceability matrix, second release | `docs/requirements-traceability-matrix.md` §3–4 |
| Operational model, second release | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` (`Hospital_All_Processes_V3_C8`) |
| Operational model, V2 (history only) | `git show 6c572b3:"Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn"`; an earlier revision remains at `Week3 Coursework/hospital-pathway/bpmn/Hospital_All_Processes_V2.bpmn` |
| Operational model, initial release | `Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` |
| Strategic model and note | `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`, `PB-12_abstraction-level_2026-09-29.md` |
| Forms | `Week6 Coursework/forms/` (12 files; the set the deployment packages) |
| Workers | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/` |
| Refund and charge rules | `RefundWorkers.java`, `ChargeAmountRules.java` |
| Acceptance scripts | `pb14_acceptance.py`, `pb18_acceptance.py`, `g07_e2e_acceptance.py` (repository root of the technical module) |
| V3 acceptance master record | `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt` |
| V3 acceptance run records | `evidence/PB-14_acceptance-run-log_2026-10-19.json`, `evidence/PB-18_acceptance-run-log_2026-10-19.json`, `evidence/Group_Final_E2E_20261019-214234.json` |
| V3 environment failure, retained | `evidence/Group_Final_E2E_20261019-213833.json` — connection reset at 21:38:33; not a test result (§4.5) |
| V3 G07 attempt without a task trail, retained | `evidence/Group_Final_E2E_20261019-214113.json` — `COMPLETED`, same variables, empty task list; not the cited result (§4.5) |
| Clean build and unit tests, 19 October | `evidence/Java_Clean_Build_Test_2026-10-19.txt` — `mvn -B clean test` at `dbc0a33`, 19 tests, plus the form binding audit |
| Initial-release acceptance record | `submissions/AISD/Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf` |
| V1 → V2 change record | `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` |
| Initial-release tag | `submission-2026-09-29` (`f6fec99`) |
| V2 construction range | `8cda78c` … `787375e` |
| V2 → V3 rename and five further merges | `357528e` |
| Form change commits | `e4b2159`, `8a10e24`, `32e6dbc`, `1816b8e`, `9a0b294`, `c29df1c`, `cb23fdf` |
| Strategic model baseline commit | `88a5bcc` |
