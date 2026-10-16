# Feedback response record (second release)

**Written**: 2026-10-16
**Required by**: the second-release brief, *Changes made in response to feedback*. The module specification also asks for a record identifying the point raised, the agreed response, the first and second owners, and evidence of completion, with a reason where an action was not implemented.

This record lists only points the repository can evidence. Where the point came from the group's own review rather than from an outside comment, the source column says so. Tutor feedback has not been written into any file yet, so it is not guessed at here; section 2 is the place to add it.

## 1. Points recorded so far, and what was done

| ID | Point raised (source) | Decision | Action taken | First owner | Second owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | Merging gateways were called out in review. The comment is recorded in the model itself: "Added in response to Group 10 feedback on merging gateways." | Keep the split paths, but merge them explicitly before each downstream task instead of letting alternatives meet informally | Added exclusive merge gateways in front of `BookVisit`, `ClinicalCare`, `Funding` and `BookTreatment` | Estrella | to confirm | `../bpmn/Hospital_All_Processes_V2.bpmn`, the four gateway `documentation` elements; commits `8cda78c` and `f90d31e` (2026-10-13, 2026-10-14) |
| F-02 | Group review of the visit-outcome branch: decline, patient cancellation and did-not-attend were being treated as if a slot had to be reserved | Only a booked or an attended visit should use the slot worker | Split the visit outcomes and added `VisitNeedsSlot` and `Join_VisitOutcome`, so decline, cancellation and did-not-attend skip slot allocation and rejoin before the outcome decision | Estrella | to confirm | Same model; commits `e4b2159` (2026-10-13) and `305fccb` (2026-10-14) |
| F-03 | Clinical SR review against the case: one encounter records one care decision, so the OR-refinement under the care outcome was wrong | Remove the OR-refinement beneath that outcome | One care decision (treatment / follow-up / discharge) recorded as a single task | Estrella | Ryan | `../istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, diagram description; commit `8ceb854` (2026-10-15) |
| F-04 | Case-alignment review of the i\* dependencies: four of them did not match the case wording | Align them with the case | Dependency names, types and directions corrected | Estrella | Ryan | Commit `25f53f7` (2026-10-14) changed `docs/istar/PB-16_istar-sd-sr.md`, `PB-16_sd.md` and `PB-16_sr.md`; `../istar/V1_SD_diagram.txt` records alignment to the dependency catalogue at `2d09f5a` |
| F-05 | The SD carried detail that belongs in the per-service SR views | Keep one maintained SD and move service detail into the SRs | SD reduced to nine aggregated actors and 13 selected dependencies; `D5` narrowed to new-patient acceptance only; `D10` separated from the scheduling dependency `D9`; `D18` treated as a softgoal | Estrella | Ryan | `../istar/V1_SD_diagram.txt` diagram description; commits `5398f2c` and `13abe30` (2026-10-16) |
| F-06 | The administrative rationale had to be checked against the actual model, not the case alone | Review every goal, task and resource against `Hospital_All_Processes_V2` | Per-element `Evidence` and `V1 status` added; appointment-outcome wording corrected for decline, patient cancellation and did-not-attend | Estrella | Ryan | `../istar/PB-16_V1_Admin_SR_reviewed_2026-10-13.txt`, diagram description; commits `2d09f5a`, `856568d`, `6865b35` (2026-10-14, 2026-10-15) |
| F-07 | Traceability review: the matrix did not separate what the release actually supports from what it only partly supports | Grade every business rule against real evidence rather than intent | BR-01 to BR-42 graded, giving 12 supported, 26 partial and 4 unsupported, plus a second-release plan | Ruby | Ryan | `../requirements/requirements-traceability-matrix.md`, section 3 |

Notes on the owner columns:

- Where the point belongs to a registered backlog item, the owners are the registered pair. `PB-16` (i\* SD/SR) is first owner Estrella, second owner Ryan, from `../docs/p3-product-backlog.md`.
- F-01 and F-02 are not yet registered against a backlog item, so the column names the member whose commits carry the change. Both pairs need confirming.
- The W6 SD commits are by Ryan while `PB-16` is registered to Estrella first. The SD description also says the SR files are separate owners' responsibility. Confirm at SU3 whether the SR views were split between members.

## 2. Tutor feedback to be recorded

Add one row per point as it is given, in the same shape as section 1. Nothing is filled in from memory.

| ID | Point raised (source, date) | Decision | Action taken | First owner | Second owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 | | | | | | |
| T-02 | | | | | | |
| T-03 | | | | | | |

## 3. Points raised and not implemented

The brief asks for the reason and any outstanding implications where an action was not taken.

| ID | Point | Reason not implemented | Outstanding implication | Proposed next step |
| --- | --- | --- | --- | --- |
| None recorded yet | | | | |

## 4. Claims this record does not make

- It does not claim that any tutor has given feedback that is not written above.
- It does not claim that the V1 statuses in the SR files are verified fulfilment. The SR files state the opposite: a dependency records a business need, and the mock or manual status is carried on the element, not on the dependency name.
- It does not claim that the role-permission criterion has been fixed. `AT-03` is still recorded as a fail in `../acceptance/`.
