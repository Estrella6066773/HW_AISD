# Part 7 standup records

**Table**: the Part 7 table from `W01/Agile Workshop.docx`, unchanged.
**Purpose**: one row per member per standup, which is what the Standup 3 and Standup 4 criteria (5% each) are marked on.
**Not backlog items**: these records are coursework process work. They carry no `PB` number; the product backlog lists product work only. See part B of `plan/sprint3-4-plan_2026-10-16.md`.
**Personal prep is not a record**: a member's private speaking notes stay private — the draft for the 16 October session is at `notes/SU4_2026-10-16.md`. What belongs here is what was actually said, written up afterwards.
**Where a session left no minute**: the row keeps what the repository can prove and marks the rest. *Completed Work* and *Evidence* are then taken from the commits the member made that day and named so each one opens; the spoken columns are left as "—" rather than inferred, because a commit records what someone did, not what they said. Both tables below say which cells rest on which evidence.

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
> "Not recorded" is the recorded position, not a gap to be filled later. Two commits do exist on 12 October — `db289ae` and `6ec8191`, both archiving Week 3 course material and the piStar tool — but they are not project work and cannot stand in for what a member said at the session. Nor can rows be derived the way the Standup 4 rows are, because no project commit exists on 12 October to derive them from: the two commits above are the whole of the day. The SU3 mark was assessed live, and this table does not reconstruct it.

## Standup 4 — 2026-10-16

| Student | Completed Work | Evidence | Next Action | Blocker | Support Needed | Handover Required |
|---------|----------------|----------|-------------|---------|----------------|-------------------|
| Estrella | The second-release working set and its index: `Week6 Coursework/README.md`, the feedback-response framework, the V1-to-V2 change note, the Sprint 3/4 plan and `problems_2026-10-16.md` → `67badbf` (15:37). Re-pointed the renamed shared package, consolidated the duplicate files, renumbered the sprint plan by backlog item, 46 files changed, and added `open-items_2026-10-16.md` → `151a86d` (15:50) | `git show --stat 67badbf`, `git show --stat 151a86d`; `problems_2026-10-16.md` Section 六 gives one verification command per claim | Fixed the second-release scope at `PB-30`, `PB-31`, `PB-34` and `PB-39` and took the process records out of the product backlog → `2c5252b` (16:13, after this session). Then: keep one row per feedback point actually received and leave the tutor rows blank; carry the traceability grades forward (`PB-39`); name the baseline commit behind every recorded result (`PB-31`); hand the planned-versus-actual draft to Ender | No tutor feedback point was written down anywhere in the repository, so the 20% criterion has no traceable tutor evidence; the BPM&EA (`UFCEP4-0-3`) marking specification is also missing, as `W01/` holds only the two AISD ones | Ryan's signature on `PB-12` and the second-owner review of `PB-16`; the Group 10 review text so that `F-08` can be split into its two points; confirmation of the BPM&EA specification | Two signature requests go to Ryan and Ender; the submission checklist in `Est/est：个人待办.md` Section 4 goes back to the group for the final cross-check |
| Ruby | Working V2 material for the clinical view on the day before the session: the Chinese V2 pathway (`Hospital_All_Processes_V2_中文.bpmn`) together with a comparison note against the Clinical SR and the strategic view → `03180bb` (14:26, 67 files, of which 61 are the Week 3 working set arriving in the repository for the first time). Then the Chinese visit-outcome labels were moved off the flow lines so the skip-slot and booked paths read separately → `787375e` (14:26, 1 file). Refactored both BPMN diagrams with actor positions and waypoints redrawn, and rewrote the clinical SR figure explanation → `8fb64c4` (15:27, 6 files, +1108/−251). After the session: clinical SR goal descriptions rewritten, redundant tasks removed from the BPMN, and the Group 10 V2-to-BPMN comparison written up → `086a33f` (16:42, 5 files) | `git show --stat 03180bb`, `git show 787375e`, `git show --stat 8fb64c4`, `git show --stat 086a33f`; the comparison note is `Week6 Coursework/V2-临床SR与BPMN对照-第10组.md`; the student's own account of the day is `Ruby/2026-10-15/问题咨询总结.md` | — | — | — | — |
| Ryan | Week 6 SD model brought up to the dependencies verified in the case → `5398f2c` (14:59, `PB-16_V1_SD_reviewed_2026-10-13.txt`, +223/−256). The model then renamed to `V1_SD_diagram.txt` with the matching PNG exported beside it → `13abe30` (15:03) | `git show --stat 5398f2c`, `git show --stat 13abe30`; the PNG is `Week6 Coursework/istar/V1_SD_diagram.png` | — | — | — | — |
| Ender | No commit on 16 October. The next commit under this name is `e098d2c` on 17 October 15:42, the Finance SR reviewed PNG | `git log --author=DLuffy --format='%h %ci %s'` | — | — | — | — |

> **Which cells are derived, and which are not.** The session left no minute, so on 16 October the table above carries only what the repository can prove: *Completed Work* and *Evidence* name the commits a member made that day, and every one of them opens. The five spoken columns — *Next Action*, *Blocker*, *Support Needed*, *Handover Required*, and the discussion behind each — are left as "—" for Ruby, Ryan and Ender rather than written from inference: a commit shows what someone did, not what they promised or what stopped them. Estrella's row is the one written on the day and keeps its full text. Where an inference would have been possible it was still not written, because a standup row is a record of a conversation and the conversation is the part that is missing.

> **Added after the session, 2026-10-19 — the class feedback sheet.** The sheet the blocker above treats as missing for the class-feedback half has been found and filed: `../feedback/Group_Feedback_2026-10-13.docx`, dated 13 October 11:35, four byte-identical copies received (MD5 `5E1C42B0DC30D683575A2D51FED149BF`). It holds 21 numbered entries, one per submission. Entry 7 is the one this repository treats as its own — keyed to it by `../../Ruby/2026-10-15/问题咨询总结.md`, with the three points there matching entry 7 word for word: "Implement role-based access control in Camunda; improve form validation, particularly for date selections; implement database integration to support data persistence."
>
> This closes the class-feedback part of the blocker and leaves the tutor part untouched. The sheet names no author and carries no tutor comment, so the recorded position at SU4 — that no tutor point exists in writing — stands as it was written. The sheet is a feedback source, not a standup record.
