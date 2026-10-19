# Part 7 standup records

**Table**: the Part 7 table from `W01/Agile Workshop.docx`, unchanged.
**Purpose**: one row per member per standup, which is what the Standup 3 and Standup 4 criteria (5% each) are marked on.
**Not backlog items**: these records are coursework process work. They carry no `PB` number; the product backlog lists product work only. See part B of `plan/sprint3-4-plan_2026-10-16.md`.
**Personal prep is not a record**: a member's private speaking notes stay private — the draft for the 16 October session is at `notes/SU4_2026-10-16.md`. What belongs here is what was actually said, written up afterwards.

**Who fills it in**: each member writes their own row; Ruby collects and keeps the table complete before each submission date.
**Evidence rule**: every "Evidence" cell names a file, a commit or a screenshot that can be opened. A row without openable evidence does not count.

| Student | Completed Work | Evidence | Next Action | Blocker | Support Needed | Handover Required |
|---------|----------------|----------|-------------|---------|----------------|-------------------|

## Standup 3 — 2026-10-12

| Student | Completed Work | Evidence | Next Action | Blocker | Support Needed | Handover Required |
|---------|----------------|----------|-------------|---------|----------------|-------------------|
| Estrella | Not recorded | None that evidences a standup update | — | — | — | — |
| Ruby | Not recorded | None that evidences a standup update | — | — | — | — |
| Ryan | Not recorded | None that evidences a standup update | — | — | — | — |
| Ender | Not recorded | None that evidences a standup update | — | — | — | — |

> **The 12 October session has no record.** The timetable for 12–16 October places Stand-up 03 on Monday 12 October, Sprint Review 03 on Wednesday 14 October and Stand-up 04 on Friday 16 October (`W01/Weekly-Schedule_2026-10-12_16.png`). The group had been treating the 16 October meeting as Standup 3, so the rows written on 19 October were filed under the wrong session; they now sit under Standup 4.
>
> "Not recorded" is the recorded position, not a gap to be filled later. Two commits do exist on 12 October — `db289ae` and `6ec8191`, both archiving Week 3 course material and the piStar tool — but they are not project work and cannot stand in for what a member said at the session. The SU3 mark was assessed live on the day; this table cannot reconstruct it, and a row back-filled from later work would date that work before it happened.

## Standup 4 — 2026-10-16

| Student | Completed Work | Evidence | Next Action | Blocker | Support Needed | Handover Required |
|---------|----------------|----------|-------------|---------|----------------|-------------------|
| Estrella | The second-release working set and its index: `Week6 Coursework/README.md`, the feedback-response framework, the V1-to-V2 change note, the Sprint 3/4 plan and `problems_2026-10-16.md` → `67badbf` (15:37). Re-pointed the renamed shared package, consolidated the duplicate files, renumbered the sprint plan by backlog item, 46 files changed, and added `open-items_2026-10-16.md` → `151a86d` (15:50) | `git show --stat 67badbf`, `git show --stat 151a86d`; `problems_2026-10-16.md` Section 六 gives one verification command per claim | Fixed the second-release scope at `PB-30`, `PB-31`, `PB-34` and `PB-39` and took the process records out of the product backlog → `2c5252b` (16:13, after this session). Then: keep one row per feedback point actually received and leave the tutor rows blank; carry the traceability grades forward (`PB-39`); name the baseline commit behind every recorded result (`PB-31`); hand the planned-versus-actual draft to Ender | No tutor feedback point was written down anywhere in the repository, so the 20% criterion has no traceable tutor evidence; the BPM&EA (`UFCEP4-0-3`) marking specification is also missing, as `W01/` holds only the two AISD ones | Ryan's signature on `PB-12` and the second-owner review of `PB-16`; the Group 10 review text so that `F-08` can be split into its two points; confirmation of the BPM&EA specification | Two signature requests go to Ryan and Ender; the submission checklist in `Est/est：个人待办.md` Section 4 goes back to the group for the final cross-check |
| Ruby | | | | | | |
| Ryan | | | | | | |
| Ender | | | | | | |
