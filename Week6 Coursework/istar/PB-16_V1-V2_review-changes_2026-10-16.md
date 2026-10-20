# PB-16 · What the review changed, V1 to V2

**Written**: 2026-10-16
**Scope**: the i\* SD and SR views, the strategic BPMN and the operational BPMN, from the 29 September initial release to the current state.
**Companion**: `../../Ruby/2026-10-15/V2流程-临床SR-战略图对照.md` explains how to read the three views and where they disagree.

> **Status note added 2026-10-19.** Later on 19 October, `357528e` replaced the operational model with `bpmn/Hospital_All_Processes_V3.bpmn` (`Hospital_All_Processes_V3_C8`): the V2 content plus five further pass-through `Join_*` gateways, a renamed process, and no change to any task, event, condition or assignment. Sections 2 and 7 below remain the V1→V2 record and are left as written; where they call V2 the current model, read that as the V2 step in the history. The model of record is V3.

## How to read "V1" and "V2" here

- **V1** is the 29 September initial release: the first version of each model, as submitted.
- **V2** is the improved operational BPMN. The name comes from the file: `bpmn/Hospital_All_Processes_V2.bpmn`, process id `Hospital_All_Processes_V2_C8`.
- The i\* files are named `V1_...` and carry per-element `V1 status` values. "V1" there means "this element describes the initial release", and the status says how well the initial release supported it: `V1 manual/partial`, `V1 mock`, or a business goal / business quality that is not a support claim at all.

## 1. Strategic BPMN — unchanged

`strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` and `strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` have not changed since 2026-09-29 (`88a5bcc`). Nothing in the review altered the strategic model.

What it does: three lanes (clinical, administrative, finance), one stage per task, external organisations shown outside, non-executable. The abstraction note maps each stage to the operational tasks and states what the model leaves out.

## 2. Operational BPMN — the V2 changes

The V2 model was built during the review. Each change below is a separate commit.

| Change | Commit | Date |
| --- | --- | --- |
| Created a separate V2 model with four exclusive merge gateways | `8cda78c` | 2026-10-13 |
| Split the visit outcomes so decline, patient cancellation and did-not-attend are not treated as bookings | `e4b2159` | 2026-10-13 |
| Three further exclusive merges added before the remaining downstream tasks | `f90d31e` | 2026-10-14 |
| Slot reservation skipped when the visit is not being booked (`VisitNeedsSlot`, `Join_VisitOutcome`) | `305fccb` | 2026-10-14 |
| Review period constrained, past appointment dates rejected | `8a10e24` | 2026-10-14 |
| Finance form shows the original charge; an invalid refund fails once | `1816b8e` | 2026-10-14 |
| Chinese-label copy: visit-outcome labels moved off the flow lines | `787375e` | 2026-10-16 |

The four merge gateways are recorded in the model itself as a response to a review comment: their `documentation` reads "Added in response to Group 10 feedback on merging gateways." Two lead-in notes are worth keeping in mind when explaining the diagram:

- The merges are pass-through. They carry no condition, default, synchronisation or deduplication.
- `Ryan's Join_BookVisit` stays upstream of `BookVisit`, separately from these merges.

## 3. i\* SD — what changed

| Change | Evidence |
| --- | --- |
| Four dependencies re-aligned with the case wording | `25f53f7` (2026-10-14), touching `docs/istar/PB-16_istar-sd-sr.md`, `PB-16_sd.md` and `PB-16_sr.md` |
| SD reduced to nine aggregated actors and 13 selected dependencies out of the 24-item catalogue | `istar/V1_SD_diagram.txt`, diagram description |
| `D5` narrowed to new-patient acceptance only | same |
| `D10` separated from the scheduling dependency `D9`, so external treatment, laboratory and imaging availability is no longer mixed with slot availability | same |
| `D14` read as normal-route treatment confirmation | same |
| `D20` includes recorded contact attempts, including the two-week telephone | same |
| `D7` typed as a goal, `D18` as a quality | same |
| Model and PNG re-exported | `5398f2c`, `13abe30` (2026-10-16) |

The SD file records that it was aligned on 2026-10-15 with the group dependency catalogue at commit `2d09f5a`, and that it is the only SD maintained in this folder.

## 4. i\* SR — three separate views

The single SR view in `docs/istar/PB-16_sr.md` was replaced by three service-level SR views, added in `a7386e6` (2026-10-14) and refined through 2026-10-15 and 2026-10-16.

| View | File | What the review settled |
| --- | --- | --- |
| Clinical | `PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt` | The OR-refinement under the care outcome was removed, because one encounter records one care decision (treatment / follow-up / discharge) as a single task. `D5` narrowed to new-patient acceptance. `D7` is a goal. `D8` added for appointment arrangement after authorisation. `D18` is a softgoal, not a finance follow-up task. |
| Admin | `PB-16_V1_Admin_SR_reviewed_2026-10-19.txt` | Rationale checked against the case *and* `Hospital_All_Processes_V2`, not the case alone. The visit goal now covers recording the outcome when no visit takes place: decline, patient cancellation and did-not-attend are recorded and passed on rather than booked. A slot helps that goal only when the visit is a booking. `D5` applies only to a new patient appointment. `D7` is the clinical-approval goal, and the depender is the letter-processing goal rather than the already-approved letter resource. `D20` keeps the appointment letter and the recorded contact attempts, and does not assign clinical explanation to Admin. Re-exported on 2026-10-19: 20 nodes, 9 dependencies, layout re-laid on a 2013x1063 canvas, all 20 elements still carrying `Evidence` and a `V1 status`. |
| Finance | `PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` | Refunds, transfers and retained fees reviewed as separate finance decisions; 13 elements left at `V1 manual/partial` and 2 recorded as `V1 mock`. |

Every element in the three views carries an `Evidence` field naming the case paragraph, the model task or the worker it rests on, and a `V1 status` field. That pairing is the point of the review: it separates what the case requires from what the initial release actually supported.

A constraint the views state explicitly, and one that should be repeated when presenting: a dependency records a business need, not verified fulfilment. The mock or manual status is carried on the element, not on the dependency name.

## 5. Requirement traceability

`../../docs/requirements-traceability-matrix.md` grades every business rule from BR-01 to BR-42 against the models, forms, workers and tests: **12 supported, 26 partial, 4 unsupported** for the 29 September release, with the second-release plan in section 3. The V2 refresh of those grades is in the same file, section 4: **13 supported, 25 partial, 4 unsupported** as of 2026-10-19.

## 6. What the review did not change

- The strategic BPMN, and the abstraction level it claims.
- The 29 September executable baseline, `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` (process id `Hospital_All_Processes_Simple_C8`). The V2 model is added alongside it, not substituted for it. This is the model behind the submitted PDF export, and it does not contain the split visit outcomes.
- The role-permission gap. `AT-03` is still recorded as a fail; the reviewed SR views do not claim role enforcement.
- The workers. The V2 work changed the model, the forms and the finance rules; it is not a rewrite of the worker set.

## 7. What the changes amount to, counted

**Written**: 2026-10-19. **Method**: the counts below are taken from the artefacts, not from memory. Model files are the piStar exports parsed as JSON; BPMN counts use namespace-qualified XPath, so `zeebe:userTask` extension elements are not mistaken for tasks; "before" is `f6fec99` (29 September) and "after" is the state at `353f988` (19 October). Element-level figure differences are matched by element id.

The purpose of this section is narrow: this file has said what changed; this says how much, so the increment can be described without adjectives. It adds no claim about what anyone said at a review — the points received are in `../feedback/feedback-response_2026-10-16.md`.

| Dimension | 29 September | 19 October | Change |
| --- | --- | --- | --- |
| Strategic BPMN | one model, `88a5bcc` | the same model | none; `151a86d` changed one line of the abstraction note, not the model |
| Operational BPMN — user tasks | 19 | 22 | +3 (`AwaitAttendance`, `RecordDecline`, `RecordDna`) |
| Operational BPMN — service tasks | 8 | 8 | none |
| Operational BPMN — exclusive gateways | 14 | 22 | +8 (seven `Join_*`, one `VisitNeedsSlot`) |
| Operational BPMN — sequence flows | 76 | 91 | +15 |
| Operational BPMN — `documentation` elements | 31 | 42 | +11 |
| Forms | 11 | 12 | 4 changed, 1 new (`await_attendance`, 93 lines), 7 untouched |
| Mandatory fields, the four changed forms | 4 / 3 / 4 / 6 | 7 / 5 / 5 / 8 | +8 in total (`book_visit`, `funding_assessment`, `finance_adjustment`, `register_request`) |
| Value and date constraints | none stated | 9 numeric bounds, 1 `disallowPassedDates` | +10 |
| i\* SD — actors in the figure | 11 | 9 | −2, aggregated |
| i\* SD — dependencies in the figure | 24 | 13 | −11; the 24-item catalogue is kept in `../../docs/istar/PB-16_istar-sd-sr.md` |
| i\* SR — structure | one document, 11 actor sections, about 52 nodes | three service views, 53 nodes, 21 dependencies | rebuilt by service |
| i\* SR — per-element evidence | none | 74 elements, each with `Evidence` and a `V1 status` | +74 |
| Traceability grades | 12 / 26 / 4 | 13 / 25 / 4 | one grade moved (BR-20); three gaps narrowed |
| Unit tests | 12 | 19 | +7, all passing at `353f988` |

### 7.1 What the figures show, element by element

| Figure | Change |
| --- | --- |
| Admin, re-exported 2026-10-19 | 29 elements, **all 29 moved**, 0 text changes, 0 property changes, canvas 1520×760 → 2013×1063. The re-export is a re-layout, and nothing else |
| Clinical | 23 → 22 elements. Four nodes removed: the separate treatment-plan, discharge-decision and follow-up tasks were folded into one `Record care decision` task, and "obtain later finance follow-up" was dropped. Three added: the dependency `D8`, one goal (appointments arranged after authorisation) and one quality (clinical work not delayed by payment confirmation gaps). 5 text changes, 9 status changes; canvas 1340×643 → 1400×745 |
| Finance | 22 → 23 elements: `D17` added, the other 22 moved, no text or status change; canvas 1420×702 → 1464×1123 |
| SD | the current PNG is byte-identical to `../../Ryan/2026-10-15/PB-16_V1_SD_reviewed_2026-10-13.png`, so the re-export produced no visual change |
| Export scale | SD 3.8×, Admin 3.8×, Finance 3.9×, Clinical 1.0× (1416×730). Clinical is the only figure that would blur when projected |

### 7.2 Five readings

1. **The increment is evidence, not features.** Seven of the eight new gateways are `Join_*`, each with one unconditional outgoing flow and no default, so they change no decision. The traceability grades moved by one row. What grew is documentation (+11), per-element evidence (+74) and form constraints (+8 mandatory fields, +10 constraints).
2. **There is exactly one functional expansion**: the visit outcome is split into attended, booked-awaiting-attendance, pending, patient-cancelled, declined and did-not-attend. That accounts for all three new tasks, `VisitNeedsSlot`, `await_attendance.form` and six outcome conditions.
3. **The strategic layer is unchanged, and that is a result.** The review confirmed it did not need to change; a reader should not read its silence as an omission.
4. **The review quantified how much of V1 was automated.** Of the 53 nodes in the three SR views, 43 carry a support claim, 4 of those are `V1 mock` or `V1 mock/manual`, and none is labelled as fully supported. The remaining 10 are not support claims: 3 business goals and 7 business qualities. This is a statement about the initial release, not about V2.
5. **The figures cannot show the improvement themselves.** All three views carry `V1 status` and no `V2 status`, so what V2 added is evidenced by the operational model, the forms, the tests and the matrix rather than by the SR figures. The status field is also not one vocabulary: the 53 nodes use eight fixed English labels, while the 21 dependencies carry 15 different free Chinese phrases, so the two cannot be counted together. Anyone quoting a coverage figure should say which of the two they mean.

### 7.3 What this cannot reconstruct

- What a tutor said at SR1 or SR2, and how either review was marked. No minutes were kept, and `../process/part8-sprint-review-records.md` records that gap rather than filling it.
- Why each change was made, except where the model itself says so: the seven `Join_*` gateways carry "Added in response to Group 10 feedback on merging gateways" in their `documentation`, and the rest is inference from commit messages.
- Why each of the 11 dependencies left the SD figure. The figure states the 13 it uses and the catalogue keeps all 24, but no per-dependency reason for the selection is recorded.
