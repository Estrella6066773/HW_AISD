# Week 6 Coursework — second release working set

Both modules' second-release deliverables are due **20 October 2026 23:59**. This folder holds the material that the second release adds or changes. Material that already has a home elsewhere is **linked, not copied** — see "One copy of each artefact" below.

The brief for this release asks for four things: the presentation, the updated solution, a feedback response record, and planning evidence. The table below says where each one is.

| What the brief asks for | Where it is |
| --- | --- |
| Improved operational BPMN | `bpmn/` |
| Feedback response record: point, decision, owners, evidence | `feedback/` |
| V1-to-V2 change note | `istar/` |
| Reviewed i\* SD and the three SR views | `istar/` |
| Sprint 3 / Sprint 4 plan, in two parts: product work, then process work | `plan/` |
| Standup and sprint-review records (Part 7 table, Part 8 record) | `process/` |
| Standup 4 speaking cards — personal notes, not a submission artefact | `process/notes/` |
| What still has to be solved before the deadline | `problems_2026-10-16.md` |
| Strategic BPMN and the abstraction note | `../docs/strategic-bpmn/` |
| Requirement traceability matrix | `../docs/requirements-traceability-matrix.md` |
| i\* SD/SR modelling notes | `../docs/istar/` |
| Acceptance plans and run logs | `../Ryan/2026-09-26/` |
| Acceptance PDF, as submitted | `../submissions/AISD/` |
| Product backlog: `PB-30`, `PB-31`, `PB-34` and `PB-39` for this release | `../docs/p3-product-backlog.md` |
| Executable package: BPMN, forms, workers, scripts, 29 September evidence | `../Week3 Coursework/hospital-pathway/` |

## One copy of each artefact

On 2026-10-16 the duplicate copies that had accumulated were consolidated, so that no artefact has two maintained versions:

| Removed | Kept |
| --- | --- |
| `PB-16_V1_Admin_SR_reviewed_2026-10-13.txt` and the Clinical and Finance files in the repository root (byte-identical copies) | `istar/PB-16_V1_*_SR_reviewed_2026-10-13.txt` (the Admin file was later renamed to `_2026-10-19` when it was re-exported; the name here is the one this consolidation kept) |
| `PB-16_V1_SD_reviewed_2026-10-13.txt` in the repository root (identical to the file below) | `istar/V1_SD_diagram.txt` |
| `acceptance/` — the acceptance PDF, both plans and both run logs (copies) | `../Ryan/2026-09-26/` for the plans and logs; `../submissions/AISD/` for the PDF |
| `requirements/requirements-traceability-matrix.md` (identical copy) | `../docs/requirements-traceability-matrix.md` |
| `strategic-bpmn/` — the strategic model and the abstraction note (copies) | `../docs/strategic-bpmn/` |

Nothing was lost: every removed file is in the history.

Still held in more than one place, and **not** consolidated here because the copies are different versions rather than copies:

- The SD diagram: `istar/V1_SD_diagram.png` (newest), `../Ryan/2026-10-15/PB-16_V1_SD_reviewed_2026-10-13.png` (15 October), `../docs/istar/PB-16_sd-overview.png` (13 October, the figure the initial-release submission refers to).
- The forms: `forms/`, `../Week3 Coursework/hospital-pathway/forms/` and `../Ruby/2026-10-19/group10-feedback/forms/` hold the same 12 filenames. `forms/` and the Ruby copy are byte-identical; both differ from the Week3 copy in every file (the 19 October input-validation pass, plus one new field each on `dispatch_letter` and `book_visit`). Only `forms/` is packaged by either build.
- The operational BPMN: V2 is no longer part of this set. `bpmn/Hospital_All_Processes_V3.bpmn` is the only model here; V2 was deleted in `357528e` and survives in history (`6c572b3`). An earlier revision of V2 also remains at `../Week3 Coursework/hospital-pathway/bpmn/Hospital_All_Processes_V2.bpmn` (127,869 bytes against 126,772 at deletion, differing on 180 lines); it is not deployed.

## Which file is authoritative

| Artefact | Authoritative file | Notes |
| --- | --- | --- |
| Executable operational BPMN | `bpmn/Hospital_All_Processes_V3.bpmn` | Process id `Hospital_All_Processes_V3_C8`. This is the improved model: split visit outcomes, twelve exclusive merge gateways, and the form set the build packages. It is not the model the 29 September submission used. V2 was superseded in `357528e`. |
| Strategic BPMN | `../docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | Not executable. Unchanged since 2026-09-29. |
| Abstraction note | `../docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` | Maps the strategic stages to the operational tasks and states the gaps. |
| i\* SD | `istar/V1_SD_diagram.txt` with `istar/V1_SD_diagram.png` | piStar 2.1.0 export. Nine aggregated actors; 13 of the 24 catalogue dependencies are shown. |
| i\* SR | `istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.txt`, `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, `istar/PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` | One SR per reviewed service. Every element carries `Evidence` and a `V1 status`. The Admin review was re-exported on 2026-10-19 and its model file took that date in its name; the older `_2026-10-13` Admin file was renamed, not kept alongside it. |
| i\* figures | `istar/V1_SD_diagram.png`, `istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.png`, `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.png`, `istar/PB-16_V1_Finance_SR_reviewed.png` | One PNG per model, all four in this folder. The Finance PNG was copied in from `../Ender/2026-10-17/` on 2026-10-19 and keeps its undated name. |
| Requirement traceability | `../docs/requirements-traceability-matrix.md` | BR-01 to BR-42: initial release 12 supported, 26 partial, 4 unsupported; second-release refresh in section 4, 13 supported, 25 partial, 4 unsupported. Section 3 keeps the plan. |
| V1 to V2 change note | `istar/PB-16_V1-V2_review-changes_2026-10-16.md` | Says what changed in each model and which commit carries it. Section 7 counts the change (tasks, gateways, forms, evidence, grades, tests) and records what the figures themselves do and do not show. |
| Backlog numbering | `../docs/p3-product-backlog.md` | The single authoritative numbering. It lists product work only; `PB-30`, `PB-31`, `PB-34` and `PB-39` are this release. Coursework process work carries no `PB` number and is tracked in `plan/sprint3-4-plan_2026-10-16.md`, part B. |

The Chinese-label copy of the operational diagram is `../Ruby/2026-10-15/Hospital_All_Processes_V2_中文.bpmn`. It is a V2-era copy: it changes labels only, and its numbered elements, arrows and gateway conditions match the English V2, not V3. **Do not deploy it.**

**What the build deploys.** `../Week3 Coursework/hospital-pathway/pom.xml` packages `../../Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` and `../../Week6 Coursework/forms/*.form`; `HospitalPathwayApplication` deploys `classpath*:bpmn/Hospital_All_Processes_V3.bpmn`. `code/` is a trimmed second copy of the same Java module — its sources, tests and test resources are byte-identical to the Week3 module (20 Java files plus one Mockito resource), and its `pom.xml` points at `../bpmn` and `../forms` instead. The one difference is a comment in `src/main/resources/application.yaml` that names its own working directory. Neither module deploys the 29 September model or the Week3 V2 copy.

The earlier `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` (process id `Hospital_All_Processes_Simple_C8`) is the model behind the 29 September submission and its exported PDF. It stays valid as that baseline but it does not contain the split visit outcomes, so it is not the second-release model.

## Encoding of the i\* model files

The four piStar model files — `istar/V1_SD_diagram.txt`, `istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.txt`, `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt` and `istar/PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` — are UTF-8 **without a byte-order mark**. Their `V1 status`, `Evidence` and `Qualification` values mix English and Chinese: the earlier sections are in English, the reviewed sections are in Chinese.

**Open them in a viewer set to UTF-8.** On a Windows machine whose default code page is GBK, some viewers — Notepad, and Excel if the file is opened as a table — render those Chinese values as mojibake. That is a viewer setting, not file damage. Checked on 2026-10-16: all four files pass a strict UTF-8 validation and each parses as valid JSON.

No byte-order mark is added, and the values are not translated by hand. These files are piStar model exports: a mark would make them invalid JSON under RFC 8259 and risks the importer, while editing the annotation text directly would desynchronise the model from `V1_SD_diagram.png`. If the group wants the annotations in English only, make that change in piStar and re-export.

## Where the executable package lives now

`Coursework/` was renamed to `Week3 Coursework/` in commit `03180bb` (2026-10-16). The old name `Coursework/` still exists on disk but holds only build output (`target/`, `data/`); nothing under it is tracked any more. Every reference to the old path was re-pointed on 2026-10-16, except the captures under `evidence/`, which are left as recorded.

The shared executable package is `../Week3 Coursework/hospital-pathway/` — BPMN, forms, Java workers, scripts and the 29 September evidence.

## Working notes

These documents are not submission artefacts. They track the open questions:

- `problems_2026-10-16.md` — what still has to be solved before 20 October, with the evidence for each point and the commands that reproduce it.
- `open-items_2026-10-16.md` — the round-by-round record of what has been changed and the candidate next steps.
- `process/notes/SU4_2026-10-16.md` — a member's private speaking draft for Stand-up 04 (the 16 October session). Personal preparation, not a record and not evidence; the record is `process/part7-standup-records.md`.

## Which work is a backlog item and which is not

Since 2026-10-16, `../docs/p3-product-backlog.md` lists **product work only** — what produces the solution or verifies it. The graded process artefacts of this release (the feedback response record, the standup and sprint-review records, the plan evaluation, the presentation deck, the contribution record, the Definition of Done sign-off) are **not** backlog items and carry no `PB` number. They are tracked in part B of `plan/sprint3-4-plan_2026-10-16.md`, and the standup and review records have their own tables in `process/`. Note 9 of the backlog lists the IDs that were withdrawn for this reason, so that references in documents dated 15 to 17 September do not dangle.

**Pull before editing.** The pull that was outstanding on 2026-10-16 has been done: the changes on `origin/main` (`40297f2`) were merged in as `2f9264b`, and local `main` and `origin/main` are level. Those commits carry the newer copies of what was then `bpmn/Hospital_All_Processes_V2.bpmn` and `istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`, both named as authoritative above at the time. The BPMN was superseded by V3 in `357528e` and the V2 file is no longer in this folder. They also brought in `Ruby/2026-10-15/~$SR-中文图解.docx`, a Word lock file; it has since been removed from version control and from disk, and `~$*` is now in `.gitignore`.
