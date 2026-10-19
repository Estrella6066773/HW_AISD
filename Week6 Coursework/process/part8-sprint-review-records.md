# Part 8 sprint-review records

**Purpose**: one section per sprint review, recording what the group actually showed. The Sprint Review 3 and Sprint Review 4 criteria (10% each) are marked on these records and on the increment presented at each.
**Not backlog items**: these records are coursework process work. They carry no `PB` number; the product backlog lists product work only. See part B of `plan/sprint3-4-plan_2026-10-16.md`.

The workbook's Part 8 asks the group to be ready to show: completed tasks, unfinished tasks, key decisions, evidence of integration, testing or validation evidence, feedback received, and backlog updates. The fields below are those seven, in that order.

The AISD presentation specification adds one requirement the workbook does not list: a brief retrospective after each review, recording the improvements for the next sprint (Section 2, *Agile project delivery*: "Hold a brief retrospective after each review and record improvements for the next sprint"). Each review below therefore carries a retrospective section after the seven workbook fields. It is recorded here rather than in a separate file, so that one review is read in one place.

**Who fills it in**: Ruby, with Ryan as second owner. Written on the day, not reconstructed later.

## Reviews before this file

The specification asks for a record of what each review showed and a version or snapshot for each of the four. Only SR3 and SR4 are handled that way in this file. The two earlier reviews are set out here so that a reader sees what exists and what does not, rather than meeting two empty sections and having to guess.

| Review | When | What exists | What does not |
| --- | --- | --- | --- |
| SR1 | 16 September 2026, a plan increment. The date is the one stated in the preparation record; no September timetable is in the repository, so it is not independently confirmed here | A preparation record in two versions: `../../Ruby/2026-09-15/ruby：part8 Sprint Review.md` (192 lines, English) and `../../Ruby/2026-09-15/ruby：part8 Sprint Review准备.md` (237 lines, Chinese, with the workshop text, a speaking order and per-member answers). Both fill the seven workbook fields and both state that no executable result is claimed | The session record at the foot of that file is blank and labelled "not held / no tutor results recorded": no tutor point, no decision changed at the session, no owner for follow-up |
| SR2 | End of Sprint 2, by 28 September 2026 | The increment it presented is `submission-2026-09-29` (`f6fec99`), the state the initial release was built from | No record and no preparation document. No snapshot was tagged for the review |

**Neither is backfilled, and the blank is deliberate.** A review record answers two questions: what was shown, and what the tutor said. For SR1 and SR2 the first is partly recoverable from the repository and the second is not recoverable at all — no minutes were kept. Writing one now would date a reconstruction before the session that produced it, which is the same objection that keeps the 12 October standup rows at "Not recorded". What the group can do is say at SR4 what the increment was at each point and which of those changes survive into the second release; what it cannot do is invent what a tutor said.

**What the SR1 preparation record is still good for.** It is the only written statement of the plan increment: T01 Done, T02 in progress, T03 not started, no form, no worker, no executable test. That makes it the starting point the V1-to-V2 change note (`../istar/PB-16_V1-V2_review-changes_2026-10-16.md`) is measured from, and the reason the second release can show a real before-and-after rather than a claim of one. Its feedback table runs `F01` to `F06`: `F01` to `F05` are the group's own review points (four from the Part 4 review, one from the case study) and `F06` is the tutor row, left as "Not yet received". That row is why SR1 yields no external point: the second release's response record (`../feedback/feedback-response_2026-10-16.md`) draws its received points from peer review and the whole-class sheet instead, and numbers them `F-01` onwards, so the two schemes are not confused.

### Snapshots across the four reviews

| Review | Snapshot | Note |
| --- | --- | --- |
| SR1 | none made | `standup-1-2026-09-16` points at `93dfaf5` (16 September 04:42), the state that existed on the morning of the review. It was created to mark the standup, so it is the nearest thing to an SR1 snapshot but it is not one and is not claimed as one |
| SR2 | none made | `submission-2026-09-29` (`f6fec99`) is the release tag from the following evening, not a review snapshot |
| SR3 | `sr3-2026-10-14` → `25f53f7` | Taken at the last commit before the session slot; `2d09f5a` (21:01 the same day) came after the review and is excluded |
| SR4 | to be tagged `sr4-<date>` | Tag it on the day, not at submission: a later submission tag does not show what was on screen |

## Sprint Review 3 — 2026-10-14

**Date from the timetable** (12–16 October: Stand-up 03 on Monday 12, Sprint Review 03 on Wednesday 14, Stand-up 04 on Friday 16 — `../../W01/Weekly-Schedule_2026-10-12_16.png`). **Snapshot**: `sr3-2026-10-14`, taken at `25f53f7` (14 October 15:07), the last commit before the session slot; `2d09f5a` (21:01 the same day) came after the review and is not part of the increment shown.

| Field | Record |
| --- | --- |
| Date and who attended | 2026-10-14; attendance to be completed |
| Completed tasks (by `PB` number) | |
| Unfinished tasks, and why | |
| Key decisions | |
| Evidence of integration (the increment shown, and how it holds together) | |
| Testing or validation evidence | |
| Feedback received | The class feedback sheet was in the team's hands before this session: `Group_Feedback_2026-10-13.docx`, dated 13 October 11:35, four byte-identical copies received. Its entry for this submission, quoted verbatim: "1. Implement role-based access control in Camunda. 2. Improve form validation, particularly for date selections, to prevent invalid or inappropriate dates. 3. Implement database integration to support data persistence." Every point is about implementation maturity; none names a model, gateway or flow defect, which only one other entry on the sheet shares. The same themes run across the class — validation in 18 of 20 entries, roles in 14, persistence in 13, merging gateways in 12 — so the three points read as marking criteria rather than one reviewer's preference. Two were settled in the second release and one was deferred: dates and persistence done, access control deferred with `AT-03` still a recorded failure. Detail in `../feedback/feedback-response_2026-10-16.md`, the section "The class feedback sheet", then sections 1 and 3. No tutor point was received in writing, so nothing is recorded as tutor feedback |
| Backlog updates the feedback produced | `PB-13` (forms) took the date and period constraints; `PB-30` (operational model) was not touched for this sheet, because no entry asks this submission for merging gateways — those answer Group 10's review and sit under `F-01`; `PB-22` (access control) is where the deferred point stays, as `F-11` |

### Retrospective after Sprint Review 3

| Field | Record |
| --- | --- |
| What the review showed we should change (process, estimate, ownership or dependency) | |
| What Sprint 4 does differently as a result | |

## Sprint Review 4 — date to be confirmed

**Not in the 12–16 October timetable**: that week carries Stand-up 04 but no Sprint Review 04. The specification sets the last one "by 22 October 2026", so it falls in the week beginning 19 October. Write the date in as soon as it is announced, and tag the snapshot the same day (`sr4-<date>`), for the same reason as SR3: a later submission tag does not show what was on screen at the review.

| Field | Record |
| --- | --- |
| Date and who attended | |
| Completed tasks (by `PB` number) | |
| Unfinished tasks, and why | |
| Key decisions | |
| Evidence of integration (the increment shown, and how it holds together) | |
| Testing or validation evidence | |
| Feedback received | |
| Backlog updates the feedback produced | |

### Retrospective after Sprint Review 4

| Field | Record |
| --- | --- |
| What the review showed we should change (process, estimate, ownership or dependency) | |
| What the next delivery does differently as a result | |
| What carries into the written evaluation of the plan | |
