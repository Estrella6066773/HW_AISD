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
| Status | Part 1 complete; Part 2 not complete in this draft |
| Accompanying deliverables | Strategic BPMN (B-1), i\* SD/SR (B-2), supporting files and readable PDF exports (B-5) |

---

## How the two parts fit together

This document carries both halves of the written evaluation the portfolio asks for.

**Part 1 — requirements alignment.** Takes the 42 business requirements in the case study and asks, one rule at a time, whether the second release moved the rule that the initial release left open. Every answer is tied to a named artefact and a commit.

**Part 2 — acceptance criteria.** Takes the acceptance criteria the group set for itself, the results actually recorded, the evidence behind those results, and the failures that remain. It is owned by Ryan and is not complete here; Section 4 states exactly what it must contain and what evidence already exists.

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
| Acceptance tests | `pb14_acceptance.py`, `pb18_acceptance.py` | **Not re-run.** `PB-31` is still open. |

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
2. **No acceptance test was executed against V3.** No result in this evaluation is a V3 result. Section 2 of the traceability matrix describes the 29 September executable and must be read as "not re-run" for V3, never as "passed".

---

## 3. Part 1 — Requirements alignment evaluation

### 3.1 Headline result

| Release | ✅ Supported | ⚠️ Partial | ❌ Unsupported |
| --- | ---: | ---: | ---: |
| Initial release (29 September) | 12 | 26 | 4 |
| Second release (V3, 19 October) | 13 | 25 | 4 |

**One grade moved. Three gaps narrowed. Twenty-six rules are untouched.**

The count is identical to the V2 position recorded earlier on 19 October. That is not a coincidence: V3 added five merge gateways, renamed the process and revalidated the forms, and none of those artefacts carries a rule. The rebase changed paths and descriptions, not grades.

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

- **No acceptance test was executed.** BR-20 is Supported without its own test, following the BR-11 precedent, where a modelled and implemented rule is Supported and the missing test is listed in Notes. Part 2 has to carry that test forward.
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

### 3.6 Two columns that could not be refreshed

| Column | Why it could not move | Consequence |
| --- | --- | --- |
| **Strategic BPMN** | `PB-12` has not changed since 29 September | BR-25, BR-29, BR-38, BR-39, BR-40, BR-41 and BR-42 remain ❌ in that column even where V3 implemented part of the operational work. The strategic picture and the operational picture now disagree in seven places. |
| **Acceptance tests** | No test was re-run | Nothing moves on test evidence. The cells describe the 29 September executable; for V3 they read as "not re-run". |

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

> **Status: not complete in this draft.** Part 2 is owned by Ryan (`PB-31`). This section states what it must contain and what evidence already exists, so that the two parts can be joined without rework. It does not speak for Part 2's owner.

### 4.1 What Part 2 has to answer

The portfolio asks for an evaluation of the acceptance criteria: the criteria set for the initial and revised versions, the test results actually obtained, the supporting evidence, the failures identified, and a reasoned assessment.

### 4.2 Evidence that already exists

| Evidence | State |
| --- | --- |
| `pb14_acceptance.py`, `pb18_acceptance.py` | Exist; **not re-run against V3** |
| Initial-release results | Recorded for the 29 September executable (`submission-2026-09-29`, `f6fec99`) |
| `AT-03` role enforcement | **Recorded failure** — a Medical Secretary completing Accept still created a Book visit |
| Worker unit tests | Three test classes re-run at `353f988` on 2026-10-19; 19 tests passed. This covers the workers, **not** the process end to end |
| Acceptance plan | `Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf` — the initial-release plan, not a second-release evaluation |

### 4.3 What Part 2 must add

- Acceptance criteria for the revised model, stated before the results.
- A re-run of `pb14_acceptance.py` and `pb18_acceptance.py` against `Hospital_All_Processes_V3_C8`, with the raw output archived.
- An explicit statement that `AT-03` is still a failure, and why (BR-37).
- The cases named in Part 1 as missing: BR-20 refund, BR-36 DNA → pathway decision → Finance, BR-35 out-of-timeframe, BR-22 change path, BR-19 urgent authorisation.
- A reasoned assessment: which criteria are met, which are not, and what that means for the claim that the second release improves the process.

---

## 5. Limitations and threats to validity

1. **The count is not a score.** 13 of 42 Supported says nothing about how much of the clinical pathway works. The rules are not equally weighted by business risk, and BR-37 alone blocks four operational rules.
2. **The grading is strict by choice.** A rule that works because the operator behaves correctly is Partial, not Supported. A more generous reading would produce a higher count and a less useful document.
3. **No V3 test evidence exists,** so every V3 judgement here rests on reading the artefacts — model, form definitions, worker source and commit history — not on observed behaviour.
4. **The strategic column is stale by construction.** Section 3.6 states this rather than correcting it, because correcting the strategic model was outside this release.
5. **The case study leaves some rules genuinely underdetermined** — BR-29's urgency rules are the clearest example. Grading those Partial rather than Unsupported reflects that the gap is a missing decision, not missing engineering.

---

## 6. Conclusion

The second release improved the process and did not improve its alignment profile. One rule moved to Supported, three narrowed, and 26 are untouched — and the 26 are concentrated in five causes, two of which (the role model and timers) account for nine rules between them.

The defensible claim is therefore not that the second release closed the gaps. It is that the gaps are now **enumerated, attributed and ordered**: the group knows that BR-37 is the highest-leverage item, that BR-38 and BR-08 are the next P0s, that eight rules are waiting on a form field rather than a redesign, and that only one rule is blocked on test coverage alone. That is a more useful position than a higher count produced by grading generously.

---

## Appendix A — All 42 rules, second-release position

Status is the V3 position. "Basis" names where the judgement comes from: a sub-section of the traceability matrix, or the initial-release row carried forward because the artefact did not change. All 42 rows were re-checked against V3 on 19 October; the traceability matrix's §4.8 records that re-check. Only BR-30, BR-35 and BR-36 gained rule-relevant evidence, and none of the three changed grade.

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
| BR-09 | Unauthorised requests blocked from admin processing | ⚠️ Partial | §4.5 — cause is BR-37 |
| BR-10 | Coordinate with external treatment / lab / imaging | ⚠️ Partial | §4.5 — remains mocked inside `book_treatment` |
| BR-11 | Pending on unavailable service; no duplicates | ✅ Supported | §2, carried forward |
| BR-12 | Funding determination: hospital / insurer / patient | ✅ Supported | §2, carried forward |
| BR-13 | Funding organisation, reference, amount, limitations | ⚠️ Partial | §4.4 — amount and reference structured; limitations still free text |
| BR-14 | Secure payment request; no card storage | ✅ Supported | §2, carried forward |
| BR-15 | Payment returned: status, reference, date, amount | ✅ Supported | §2, carried forward |
| BR-16 | No treatment confirmation until payment complete | ✅ Supported | §2, carried forward |
| BR-17 | Payment failure → notify, retry, no duplicate charge | ✅ Supported | §2, carried forward |
| BR-18 | Orphaned payment marked for investigation | ✅ Supported | §2, carried forward |
| BR-19 | Urgent treatment bypass with recorded reason | ⚠️ Partial | §4.5 — no test; clinician-only authorisation unenforced |
| BR-20 | Authorised Finance member decides refund, full or partial | ✅ Supported | §4.3 — form and worker both changed |
| BR-21 | Financial and clinical responsibilities separated | ⚠️ Partial | §4.5 — `staffRole` is free text; cause is BR-37 |
| BR-22 | Treatment change only via system, authorised | ⚠️ Partial | §4.5 — path exists, no acceptance case |
| BR-23 | Urgent postponement with retrospective authorisation | ⚠️ Partial | §4.5 — free text |
| BR-24 | Financial impact of change → Finance review | ✅ Supported | §2, carried forward |
| BR-25 | Chemotherapy cycle review; clinical decision only | ⚠️ Partial | §4.5 — no blood-test or fitness fields |
| BR-26 | Enquiry classified admin / financial / clinical | ✅ Supported | §2, carried forward |
| BR-27 | Call handlers may not give clinical advice | ⚠️ Partial | §4.5 — policy text only; cause is BR-37 |
| BR-28 | Every enquiry recorded, classified, prioritised, routed | ⚠️ Partial | §4.5 — priority added; no audit record on enquiry paths |
| BR-29 | Urgent clinical enquiry highlighted immediately | ⚠️ Partial | §4.5 — urgency rules still a stakeholder decision |
| BR-30 | Consultant writes and approves clinic letter | ⚠️ Partial | §4.5, §4.8 — `dispatch_letter.form` gained a `letterClinicallyApproved` checkbox, but no BPMN input or worker reads it; no letter body, recipients or approval time |
| BR-31 | Secretaries fix admin errors, not clinical content | ⚠️ Partial | §4.5 — not enforced; cause is BR-37 |
| BR-32 | Seven-day completion target for letters | ⚠️ Partial | §4.5 — no dates captured, no timer |
| BR-33 | Delay escalation at 7 days / 1 month / 3 months | ⚠️ Partial | §4.5 — manual task, no timers |
| BR-34 | No duplicate reminders; delay reasons recorded | ⚠️ Partial | §4.5 — no reminder service |
| BR-35 | Follow-up booking; highlight if outside timeframe | ⚠️ Partial | §4.4, §4.8 — booking structured and retained; no out-of-timeframe flag |
| BR-36 | Cancel / reschedule / DNA recording and consequences | ⚠️ Partial | §4.4, §4.8 — split delivered and `attendedOn` added; reschedule not its own outcome, no test |
| BR-37 | Role-based access control | ❌ Unsupported | §4.5, §4.8 — all 22 user tasks `assignee="demo"`; no candidate groups, no login |
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
| Acceptance scripts | `pb14_acceptance.py`, `pb18_acceptance.py` (repository root of the technical module) |
| V1 → V2 change record | `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` |
| Initial-release tag | `submission-2026-09-29` (`f6fec99`) |
| V2 construction range | `8cda78c` … `787375e` |
| V2 → V3 rename and five further merges | `357528e` |
| Form change commits | `e4b2159`, `8a10e24`, `32e6dbc`, `1816b8e`, `9a0b294`, `c29df1c`, `cb23fdf` |
| Strategic model baseline commit | `88a5bcc` |
