# Hospital Patient Referral, Treatment and Administration System

BPM&EA and AISD · Group project · Agile Workshop Parts 1–8

## Team

| ID | Name | Blackboard | UWE ID | Parts led |
|----|------|------------|--------|-----------|
| A | Hao Zheng | Ruby | 23084382 | Parts 1, 6, 8 |
| B | Geping Chen | Estrella | 23084393 | Part 3, contribution record |
| C | Minghao Qin | Dluffy | 23084402 | Parts 2, 4 |
| D | Guanyan He | Ryan | 23084395 | Parts 5, 7 |

Every part has a first owner and a second owner; the full table is in `Ruby/2026-09-14/分工表.md`.

## Structure

| Path | Content |
|------|---------|
| `docs/` | Group-level deliverables: product backlog, task breakdown, sprint backlog, requirements traceability matrix, definition of done |
| `Ruby/`, `Est/`, `Dluffy/`, `Ryan/` | Individual workspaces: drafts, part-level documents, meeting notes |
| `Coursework/` | Agile Workshop workbook transcription |
| `W01/` | Course materials: session slides, case study, assessment specifications |

## Current status

16 September 2026 is the first standup. It is checked against three things:

1. A complete product backlog — `docs/p3-product-backlog.md`
2. The Sprint 1 backlog — `docs/p6-sprint-backlog.md`
3. All four members added to the repository, with both tables uploaded

Sprint 1 covers planning only: no models and no code. The first slice under specification is referral check → doctor decision → first clinic booking, with outside scheduling mocked. Payment, clinic letters and enquiry routing come in later sprints, toward the initial release on 28 September 2026.

## Deliverables

| Part | File |
|------|------|
| 1 Case summary | `Ruby/2026-09-14/ruby：part1案例摘要.md`, discussion notes alongside; individual drafts under `Ryan/2026-09-15/` and `Dluffy/2026-09-15/` |
| 2 Deliverable list | `Dluffy/2026-09-15/Dluffy：part2交付物清单.md` |
| 3 Product backlog | `docs/p3-product-backlog.md` |
| 4 Task breakdown | `docs/p4-work-breakdown.md` |
| 5 Dependency mapping | `Ryan/2026-09-15/Ryan：part5依赖映射.md` |
| 6 Sprint backlog | `docs/p6-sprint-backlog.md`, notes in `Ruby/2026-09-15/ruby：part6 Sprint Backlog-理解.md` |
| 7 Standups | `Ryan/2026-09-15/Ryan：part7 standup.md` and the summary alongside |
| 8 Sprint Review | `Ruby/2026-09-15/ruby：part8 Sprint Review准备.md` |

Supporting documents, not tied to a single part:

| File | Content |
|------|---------|
| `docs/requirements-traceability-matrix.md` | BR-01 to BR-42 with case paragraph sources, and the matrix to fill per release |
| `docs/definition-of-done.md` | Definition of Done and the minimum delivery evidence, across BPMN, workers, forms, code quality and documentation |

## Conventions

- `main` stays in a demonstrable state. Longer work goes on a short-lived branch such as `feature/PB-06-brief`.
- Commit messages carry the item ID where one applies, for example `docs(PB-01): add role permission table`.
- The second owner reviews before merge.
- Evidence is named `PB-xx_name_type_date` and cites a path that can be opened.
- An item is marked Done only when an openable file, screenshot or run log exists. A missing evidence path means the dependency is not cleared.
- Do not commit credentials, patient data or card data.

## Reference

- Agile Workshop workbook: `Coursework/Agile Workshop.md`, with Word copies at `Coursework/Agile Workshop-ZH.docx` and `Coursework/Agile Workshop-EN.docx`
- Defence notes on the case study: `Ruby/2026-09-15/正式作答-答辩批注.md`, `Ruby/2026-09-15/Case Study-批注.docx`
- Session notes: `W01/notes/`
- Case study: `W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
