# Week 6 Coursework — second release working set

Both modules' second-release deliverables are due **20 October 2026 23:59**. This folder holds the material for that submission: the reviewed i\* models, the improved operational BPMN, the strategic model it abstracts from, and the requirement traceability behind them.

The brief for this release asks for four things: the presentation, the updated solution, a feedback response record, and planning evidence. The table below says where each one is.

| What the brief asks for | Where it lives here |
| --- | --- |
| Improved operational BPMN, shown against the 29 September baseline | `bpmn/` |
| Strategic BPMN that the operational model is derived from | `strategic-bpmn/` |
| i\* SD and the three SR views, reviewed against the case | `istar/` |
| Feedback response record: point, decision, owners, evidence | `feedback/` |
| Requirement traceability across models, forms, workers and tests | `requirements/` |
| Acceptance evidence | `acceptance/` |
| Sprint 3 / Sprint 4 plan and the planned-versus-actual draft | `plan/` |

## Which file is authoritative

| Artefact | Authoritative file | Notes |
| --- | --- | --- |
| Executable operational BPMN | `bpmn/Hospital_All_Processes_V2.bpmn` | Process id `Hospital_All_Processes_V2_C8`. This is the improved model: split visit outcomes and four exclusive merge gateways. It is not the model the 29 September submission used. |
| Strategic BPMN | `strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | Not executable. Unchanged since 2026-09-29. |
| Abstraction note | `strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` | Maps the strategic stages to the operational tasks and states the gaps. |
| i\* SD | `istar/V1_SD_diagram.txt` with `istar/V1_SD_diagram.png` | piStar 2.1.0 export. Nine aggregated actors; 13 of the 24 catalogue dependencies are shown. |
| i\* SR | `istar/PB-16_V1_Admin_SR_reviewed_2026-10-13.txt`, `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, `istar/PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` | One SR per reviewed service. Every element carries `Evidence` and a `V1 status`. |
| Requirement traceability | `requirements/requirements-traceability-matrix.md` | BR-01 to BR-42: 12 supported, 26 partial, 4 unsupported, with the second-release plan in section 3. |
| V1 to V2 change note | `istar/PB-16_V1-V2_review-changes_2026-10-16.md` | Says what changed in each model and which commit carries it. |

The Chinese-label copy of the operational diagram is `../Ruby/2026-10-15/Hospital_All_Processes_V2_中文.bpmn`. It changes labels only — the numbered elements, arrows and gateway conditions are identical to the English V2. **Do not deploy it.**

The earlier `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` (process id `Hospital_All_Processes_Simple_C8`) is the model behind the 29 September submission and its exported PDF. It stays valid as that baseline but it does not contain the split visit outcomes, so it is not the second-release model.

## Where the executable package lives now

`Coursework/` was renamed to `Week3 Coursework/` in commit `03180bb` (2026-10-16). The old name `Coursework/` still exists on disk but holds only build output (`target/`, `data/`); nothing under it is tracked any more. Anything still linking to `Coursework/hospital-pathway/` is a dead link.

The shared executable package is therefore `../Week3 Coursework/hospital-pathway/` — BPMN, forms, Java workers, scripts and the 29 September evidence.

Two copies of the operational BPMN exist and are byte-different but element-identical (same element ids, same names and documentation):

- `bpmn/Hospital_All_Processes_V2.bpmn` — this folder
- `../Week3 Coursework/hospital-pathway/bpmn/Hospital_All_Processes_V2.bpmn` — inside the executable package

Decide which one is maintained and keep the other in step, or state that only one is maintained.

## Working note

Two documents in this folder are not submission artefacts. They track the open questions:

- `problems_2026-10-16.md` — what still has to be solved before 20 October, with the evidence for each point and the commands that reproduce it.
- `open-items_2026-10-16.md` — the round-by-round record of what has been changed and the candidate next steps.

**Before editing anything here, pull.** As at 2026-10-16 the local `main` (`de555fd`) is two commits behind `origin/main` (`40297f2`), and those two commits change `bpmn/Hospital_All_Processes_V2.bpmn` and `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt` — both files named as authoritative in the table above. The edge versions on `origin/main` are the newer ones.
