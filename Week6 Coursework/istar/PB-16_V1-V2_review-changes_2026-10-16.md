# PB-16 · What the review changed, V1 to V2

**Written**: 2026-10-16
**Scope**: the i\* SD and SR views, the strategic BPMN and the operational BPMN, from the 29 September initial release to the current state.
**Companion**: `../../Ruby/2026-10-15/V2流程-临床SR-战略图对照.md` explains how to read the three views and where they disagree.

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
| Admin | `PB-16_V1_Admin_SR_reviewed_2026-10-13.txt` | Rationale checked against the case *and* `Hospital_All_Processes_V2`, not the case alone. The visit goal now covers recording the outcome when no visit takes place: decline, patient cancellation and did-not-attend are recorded and passed on rather than booked. A slot helps that goal only when the visit is a booking. `D5` applies only to a new patient appointment. `D7` is the clinical-approval goal, and the depender is the letter-processing goal rather than the already-approved letter resource. `D20` keeps the appointment letter and the recorded contact attempts, and does not assign clinical explanation to Admin. |
| Finance | `PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` | Refunds, transfers and retained fees reviewed as separate finance decisions; 13 elements left at `V1 manual/partial` and 2 recorded as `V1 mock`. |

Every element in the three views carries an `Evidence` field naming the case paragraph, the model task or the worker it rests on, and a `V1 status` field. That pairing is the point of the review: it separates what the case requires from what the initial release actually supported.

A constraint the views state explicitly, and one that should be repeated when presenting: a dependency records a business need, not verified fulfilment. The mock or manual status is carried on the element, not on the dependency name.

## 5. Requirement traceability

`../requirements/requirements-traceability-matrix.md` grades every business rule from BR-01 to BR-42 against the models, forms, workers and tests: **12 supported, 26 partial, 4 unsupported**, with the second-release plan in section 3.

## 6. What the review did not change

- The strategic BPMN, and the abstraction level it claims.
- The 29 September executable baseline, `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` (process id `Hospital_All_Processes_Simple_C8`). The V2 model is added alongside it, not substituted for it. This is the model behind the submitted PDF export, and it does not contain the split visit outcomes.
- The role-permission gap. `AT-03` is still recorded as a fail; the reviewed SR views do not claim role enforcement.
- The workers. The V2 work changed the model, the forms and the finance rules; it is not a rewrite of the worker set.
