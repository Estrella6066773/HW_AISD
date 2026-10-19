# Hospital Patient Referral, Treatment and Administration System

BPM&EA and AISD · Group project · Agile Workshop Parts 1–8

## Team

| ID | Name | Blackboard | UWE ID | Parts led |
|----|------|------------|--------|-----------|
| A | Hao Zheng | Ruby | 23084382 | Parts 1, 6, 8 |
| B | Geping Chen | Estrella | 23084393 | Part 3, contribution record |
| C | Minghao Qin | Ender | 23084402 | Parts 2, 4 |
| D | Guanyan He | Ryan | 23084395 | Parts 5, 7 |

Every part has a first owner and a second owner; the full table is in `Ruby/2026-09-14/分工表.md`.

## Structure

| Path | Content |
|------|---------|
| `docs/` | Group-level deliverables: product backlog, task breakdown, sprint backlog, requirements traceability matrix, definition of done, i* models in `docs/istar/` |
| `Ruby/`, `Est/`, `Ender/`, `Ryan/` | Individual workspaces: drafts, part-level documents, meeting notes |
| `Week3 Coursework/` | Shared executable pathway package in `hospital-pathway/` (BPMN + forms + Java workers + test logs); workbook Word copies. Renamed from `Coursework/` in `03180bb`; anything still linking to `Coursework/hospital-pathway/` is a dead link. |
| `Week6 Coursework/` | Second-release working set: operational BPMN V3, strategic BPMN, reviewed i\* SD and the three service SR views, feedback response record, requirements traceability, acceptance evidence, Sprint 3 and 4 plan. See its [README](Week6%20Coursework/README.md). |
| [`submissions/BPMEA/`](submissions/BPMEA/README.md) | BPM&EA-specific Project and Test Plan and submission index |
| [`submissions/AISD/`](submissions/AISD/README.md) | AISD-specific Design Decisions and Acceptance Test Plan/Results |
| `W01/` | Course materials: session slides, case study, assessment specifications |
| `W02/` | Week 2 slides and Camunda class examples |
| `W03/` | October 2026 slides and the piStar i* tool. The decks do not print a week number |

## Current status

**20 October 2026 23:59** is the deadline for the second-release deliverables in both modules. The 29 September initial release remains the recorded baseline, tagged `submission-2026-09-29` (`f6fec99`): the Java tests and one final-model self-pay route to `COMPLETED` are recorded against that state, and worker source, forms and the executable BPMN have changed since then, so those results describe that tagged baseline rather than the current tree. The executable package is `Week3 Coursework/hospital-pathway/`; `Coursework/` was renamed to `Week3 Coursework/` in `03180bb`. The 16 September Sprint 1 table in `docs/p6-sprint-backlog.md` remains the historical planning record. The second-release working set is in `Week6 Coursework/`.

Present:

- Executable Camunda 8 BPMN, twelve forms, Java workers and configuration
- Strategic BPMN and abstraction note in `docs/strategic-bpmn/`
- i\* SD/SR in `docs/istar/` (second-owner checklist still unsigned)
- Requirements traceability matrix, with 12 supported, 26 partial and 4 unsupported business rules for the initial release, and 13 / 25 / 4 after the second-release re-check
- Course indexes in `submissions/BPMEA/` and `submissions/AISD/`
- The initial-release presentation and demonstration were given on 29 September. The second-release presentation is still to be delivered.

Still open:

- Second-owner review of the submission documents
- Role-permission test AT-03 remains FAIL, on both releases
- Exception routes stay unevidenced even after the 19 October run: the formal change path, DNA to Finance, urgent authorisation, the refund adjustment and letter escalation are modelled but no case drives them
- Contribution record `Est/est：PB-17贡献记录表.md` is still a blank template

**Second release was executed on 19 October.** `Hospital_All_Processes_V3_C8` was deployed to a local Camunda 8.10.0-alpha5 (c8run, started with `--disable-connectors`) and the six acceptance cases plus a full G07 path were re-run against it: five of the six pass, G07 reached `COMPLETED` with nine human tasks and no active incident, and `AT-03` fails exactly as it did on 29 September. A clean `mvn -B clean test` passes 19 unit tests. The master record is [`Camunda_V3_Acceptance_2026-10-19.txt`](<Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt>); the evaluation is Part 2 of [`BPMEA_Written_Evaluation.md`](submissions/BPMEA/BPMEA_Written_Evaluation.md).

## Deliverables

| Part | File |
|------|------|
| 1 Case summary | `Ruby/2026-09-14/ruby：part1案例摘要.md`, discussion notes alongside; individual drafts under `Ryan/2026-09-15/` and `Ender/2026-09-15/` |
| 2 Deliverable list | `Ender/2026-09-15/Ender：part2交付物清单.md` |
| 3 Product backlog | `docs/p3-product-backlog.md` |
| 4 Task breakdown | `docs/p4-work-breakdown.md` |
| 5 Dependency mapping | `Ryan/2026-09-15/Ryan：part5依赖映射.md` |
| 6 Sprint backlog | `docs/p6-sprint-backlog.md`, notes in `Ruby/2026-09-15/ruby：part6 Sprint Backlog-理解.md` |
| 7 Standups | `Ryan/2026-09-15/Ryan：part7 standup.md` and the summary alongside |
| 8 Sprint Review | `Ruby/2026-09-15/ruby：part8 Sprint Review准备.md` |

Supporting documents, not tied to a single part:

28 September implementation addition: [Member D single notification worker and demo guide](Ryan/2026-09-28/D_外部工作器与数据库说明.md). Formal English package only; second-owner review pending.

| File | Content |
|------|---------|
| `docs/requirements-traceability-matrix.md` | PB-28 traceability for BR-01 to BR-42 across the strategic BPMN, operational BPMN, forms, workers and acceptance tests, plus the second-release gap plan |
| `docs/istar/PB-16_istar-sd-sr.md` | PB-16 i* SD/SR notes, with diagrams in `PB-16_sd.md`, `PB-16_sd-overview.png` and `PB-16_sr.md`. Second-owner review is still unsigned. |
| `docs/definition-of-done.md` | Definition of Done and the minimum delivery evidence, across BPMN, workers, forms, code quality and documentation |
| `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | PB-12 strategic BPMN for the initial release. Not executable. |
| `docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` | Abstraction level, mapping to the operational model, and gaps |

## Conventions

- `main` stays in a demonstrable state. Longer work goes on a short-lived branch such as `feature/PB-06-brief`.
- Commit messages carry the item ID where one applies, for example `docs(PB-01): add role permission table`.
- The second owner reviews before merge.
- Evidence is named `PB-xx_name_type_date` and cites a path that can be opened.
- An item is marked Done only when an openable file, screenshot or run log exists. A missing evidence path means the dependency is not cleared.
- Do not commit credentials, patient data or card data.

## Reference

- Agile Workshop workbook: `W01/Agile Workshop.docx`; English copy: `Week3 Coursework/Agile Workshop-EN.docx`
- Defence notes on the case study: `Ruby/2026-09-15/正式作答-答辩批注.md`, `Ruby/2026-09-15/Case Study-批注.docx`
- Case study: `W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
