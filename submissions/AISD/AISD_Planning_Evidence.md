---
title: "AISD Planning Evidence"
subtitle: "Initial release, 29 September 2026 · Revised release, 20 October 2026"
author: "Group project · UFCEP6-0-3 AISD"
date: "20 October 2026"
---

| | |
|---|---|
| Module | UFCEP6-0-3 AISD (Presentation and Assessment) |
| Project | Hospital Patient Referral, Treatment and Administration System |
| Team | Ruby (Hao Zheng) · Estrella (Geping Chen) · Ender (Minghao Qin) · Ryan (Guanyan He) |
| Releases | `submission-2026-09-29` — initial release · `submission-2026-10-20` — revised release and current state |
| Repository | https://github.com/Estrella6066773/HW_AISD |

This document is the planning evidence for both releases: the plan for each and what the record shows actually happened, the task and standup records, the two sprint reviews, a risk register for each release, and the lessons the group draws from its own delivery. Where a claim rests on a file, the file is named, so that it can be opened against the repository.

## 1. Timeline of the two releases

| Date | What the record shows | Where it is recorded |
|---|---|---|
| 15 September | Product backlog and task breakdown written: 26 initial-release items with priorities, owner pairs, estimates and dependencies. | `docs/p3-product-backlog.md`, `docs/p4-work-breakdown.md` |
| 16 September | Sprint 1 delivered the plan increment: product backlog, task breakdown, Sprint 1 backlog and traceability matrix, with four members in the repository. No diagram and no code, as the Sprint Goal states. | `docs/p6-sprint-backlog.md`; commits `2b92733`, `2216d66` |
| 17–28 September | Executable model, Java workers and Camunda forms built; acceptance plans written on 26 September and executed on 29 September. | `Ryan/2026-09-26/`; commits `6bac5af` to `43b3f22` |
| 29 September | Acceptance results recorded for AT-01 to AT-06 and the G07 route; initial release tagged at 22:07. | `Week3 Coursework/hospital-pathway/evidence/`; tag `submission-2026-09-29` (`f6fec99`) |
| 13 October | Whole-class feedback sheet issued, 11:35, entry G07 addressed to this submission. | `Week6 Coursework/feedback/Group_Feedback_2026-10-13.docx` |
| 14 October | Sprint Review 3; the snapshot is the last commit before the session slot. | `Week6 Coursework/process/part8-sprint-review-records.md`; tag `sr3-2026-10-14` (`25f53f7`) |
| 16 October | Stand-up 4; Sprint 3 and Sprint 4 plan written; repository consistency pass (34 references re-pointed, 12 duplicate files consolidated). | `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md`; commits `2c5252b`, `151a86d` |
| 19 October | V3 model and readable exports completed; revised model executed against a live engine in the evening; revised release tagged at 23:49. | commits `357528e`, `6ff91a0`; `Camunda_V3_Acceptance_2026-10-19.txt`; tag `submission-2026-10-20` |
| 20 October | Second-release deliverables due, 23:59. | Module notification |

## 2. Plan for the initial release

The 29 September delivery was planned from the P0 list of the product backlog. Note 4 of that file states the rule: *P0 is the scope to be closed in the initial release (28 September)*. Sprint 1, to 16 September, took the first slice only — referral check, consultant decision and first clinic booking, `PB-01` to `PB-04` — and its goal was the plan increment itself. The remaining P0 items were built in the dependency order Part 4 sets out, and the release was packaged on 29 September.

No separate Sprint 2 backlog table exists. The P0 list, with its owner pairs, estimates and dependencies, is the plan of record, and Part 4 supplies the task cards behind it.

| Item | Scope as planned | Owner pair · est. | Depends on | What the 29 September tree holds |
|---|---|---|---|---|
| `PB-01` | Referral receipt and document check; secretaries may request missing papers but not decide | Ruby / Estrella · 5h | — | Permission rule in the Part 1 summary; no engine check |
| `PB-02` | Consultant review, four outcomes, reason and decision-maker mandatory | Ruby / Ryan · 5h | `PB-01` | `review_referral.form`; `ReferralDecision` gateway with accept, reject, redirect, more information |
| `PB-03` | Clinic booking only after acceptance; no out-of-window booking | Ruby / Ender · 8h | `PB-02` | `book_visit.form`; `check-slot`, `reserve-appointment` workers; scheduler mocked |
| `PB-04` | Letter, plus telephone within two weeks, with each call outcome recorded | Estrella / Ruby · 3h | `PB-03` | Notification steps in the model; no case exercises the letter-and-phone rule |
| `PB-05` | Treatment authorisation; administration cannot process an unauthorised request | Ruby / Estrella · 3h | `PB-03` | `book_treatment.form` and the authorisation gate; G07 passes through it, with no check on who authorises |
| `PB-06` | Pending booking when a service is unavailable, with retries and no duplicates | Ender / Ryan · 4h | `PB-05` | `flag-resource-unavailable` worker and the pending path; no case drives treatment to pending |
| `PB-07` | Funding, payment request, failure and retry, missing confirmation | Ender / Estrella · 9h | `PB-05` | `request-payment`, `mark-payment-investigate`; AT-05 and AT-06 pass; self-pay completed in G07 |
| `PB-11` | Audit of significant actions, immutable to ordinary users | Ryan / Ruby · 3h | `PB-02`, `PB-05`, `PB-07` | Workers write `audit_event`; immutability not enforced |
| `PB-12` | Strategic BPMN with abstraction note | Ruby / Estrella · 4h | `PB-01`–`PB-08` | `PB-12_strategic-process_2026-09-29.bpmn` and the note |
| `PB-16` | i\* SD and SR models | Estrella / Ryan · 5h | `PB-01`, `PB-12` | SD and three SR files dated 29 September; checklist unsigned |
| `PB-22` | Login and eight-role permissions enforced by the system | Ruby / Estrella · 6h | `PB-01` | Not delivered: every task `assignee="demo"`, no candidate groups |
| `PB-28` | Traceability matrix as the basis of the alignment review | Ruby / Ryan · 3h | `PB-01`–`PB-14` | 12 Supported, 26 Partial, 4 Unsupported of 42 rules |

The scope was set by priority, not by case sequence: role permissions and audit sat in the release beside the clinical main path, so the release was always wider than the route it could demonstrate. Against the backlog's own status column the record is also thinner than the delivery: on 20 October nine of these items still read *Not started* and one *In progress*, although the tagged tree holds the model, eleven forms and ten worker types. The column was not maintained after 16 September, so item status cannot be read from it; what was delivered is read from the tagged tree and the acceptance record.

## 3. Plan for the revised release

The revised release was planned on 16 October in `sprint3-4-plan_2026-10-16.md`, in two parts kept deliberately apart. Part A carried product work with a backlog number on every row: `PB-30` the improved model and readable export, `PB-31` verification, `PB-34` the change note, `PB-39` the traceability refresh. Part B carried the coursework records — feedback response, standup and review records, plan evaluation, deck, contribution record, Definition of Done — with no backlog number, because none of them produces or verifies the solution. The Sprint 3 goal was an improved model integrated with the reviewed i\* views and the strategic model, with the change written down; the Sprint 4 goal was verification against a named baseline with the traceability grades carried forward.

| Work | Plan of 16 October | What was done | Position at 20 October |
|---|---|---|---|
| `PB-30` model | Revise against the strategic model and reviewed i\* views; split visit outcomes, add the skipping slot, merge redundant gateways; export a readable PDF. Ruby / Ender, 4h, Sprint 3 | V3 completed 19 October with five further pass-through merge gateways; operational and strategic exports produced the same day | Done; `Hospital_All_Processes_V3.bpmn`, process id `Hospital_All_Processes_V3_C8` |
| `PB-31` verification | Run the model and workers where the environment allows; record each result against its commit; keep `AT-03` a failure. Ryan / Ruby, 5h, Sprint 4 | Unit tests re-run at `353f988` (19 passed); end-to-end run at `dbc0a33` on 19 October: G07 completed, AT-01/02/04/05/06 pass, AT-03 fails | Done, with one criterion failing and recorded as failing |
| `PB-34` change note | Per artefact, with the file and commit carrying each change. Estrella / Ryan, 2h, Sprint 3 | Completed 16 October | Done |
| `PB-39` traceability | State which of the 26 partial and 4 unsupported rules moved. Estrella / Ryan, 2h, Sprint 4 | Refreshed against V3: 13 Supported, 25 Partial, 4 Unsupported | Done |
| Feedback response | One row per received point, with decision, owners, evidence; unreceived points blank. Estrella / Ruby, 2h | Twelve rows: seven peer points, five internal; `F-11` recorded as not implemented with its residual risk | Done; eleven-page PDF |
| Standup records | One row per member for Stand-up 3 and 4 | SU3: four rows *Not recorded*. SU4: one of four rows written | Partly done |
| Review records | Seven fields plus retrospective, for SR3 and SR4 | SR3 dated with the feedback and backlog-update fields filled; SR4 opened with one decision | Partly done; see section 5 |
| Plan evaluation | Every difference from plan with a cause, consequence and lesson. Ender / Ruby, 4h | Planned-versus-actual comparison in this record: sections 2, 3 and 8 | Done, within this record |
| Second-release deck | Ordered to the increment delivered; each member able to explain their part. Ruby / Estrella, 4h | Thirteen slides with speaker notes; reviewed by its owner 19 October | Done |
| Contribution record and DoD | Every member's evidence, openable and matched to the owner; four signatures. Estrella / Ender, 2h; Ender / Estrella, 1h | Contribution record filled from the repository 20 October; checklist in place | Record done; checklist unsigned |

**The model revision did not follow the plan's timetable.** The plan named the revision but described its evidence as *V2 content, renamed and extended*. The change that made the revision — five further merge gateways, the split visit outcomes and the readable exports — landed on 19 October, after the Group 10 review items had been transcribed into the repository and the class feedback sheet had been filed. Both were review findings, not scheduled work: Group 10's third item asked for alternative paths to converge explicitly before a task, and twelve of the class sheet's twenty entries asked for merging gateways. The plan supplied the frame and the review supplied the content. Read as a schedule, the plan was overtaken on its last working day; read as a statement of intent, it held.

Two limits belong here. `PB-31` budgeted five hours in Sprint 4 for verification, and the first execution of the revised model happened on the evening of 19 October, the day before the deadline. Part B had no estimate beyond one hour per review record, and the review records are the part of the release that finished least complete.

## 4. Task records

**Sprint 1, to 16 September.** The Sprint 1 backlog records eight task cards drawn from `PB-01` to `PB-04` and `PB-15` (withdrawn as process work on 16 October; the card remains). Statuses are the 16 September position.

| Card | Task | Owner pair · est. | Status at 16 September |
|---|---|---|---|
| T01 (`PB-01`) | Roles and permission boundary for referral check | Ruby / Estrella · 2h | Done |
| T02 (`PB-01`) | Referral main path: receive, check, send to consultant | Ruby / Ryan · 3h | In progress |
| T03 (`PB-02`) | Four consultant outcomes, reason and decision-maker mandatory | Ruby / Estrella · 3h | Not started |
| T04 (`PB-02`) | End or redirect path after rejection or redirection | Ryan / Ruby · 2h | Not started |
| T05 (`PB-03`) | Booking request only after acceptance | Ruby / Ender · 3h | Not started |
| T06 (`PB-03`) | Simulate the external scheduler; flag when no slot suits | Ender / Ryan · 5h | Not started |
| T07 (`PB-04`) | Notification rules, including the telephone record within two weeks | Estrella / Ruby · 3h | Not started |
| T20 | Upload the product backlog and this table; four members in the repository | Ruby / Estrella · 2h | In progress |

The Sprint Goal was met and no executable result was claimed for it: Sprint 1 was a planning sprint, and implementation evidence begins on 17 September.

**Standup records.** Stand-up 3 on 12 October has four rows, all reading *Not recorded*, with the evidence cell stating that no file evidences a standup update. Stand-up 4 on 16 October has one completed row — the second-release working set, the consistency pass and the scope decision that followed the session — and three empty rows. The record explains its own refiling: the 12–16 October timetable places Stand-up 03 on Monday 12, Sprint Review 03 on Wednesday 14 and Stand-up 04 on Friday 16, and the group had been treating the 16 October meeting as Stand-up 3 until the timetable was checked. The rows were moved under Stand-up 4 rather than dated back to the 12th. Two commits do exist on 12 October, both archiving W03 course material; the record states they are not project work and do not stand in for what a member said.

**Revised release.** The task record for this release is the plan table in section 3, because Part B of the plan is the tracker for the process work the product backlog deliberately does not carry.

## 5. The two sprint reviews

The specification asks for a record of what each review showed, with a version or snapshot for each of the four. The repository handles SR3 and SR4 in one file and accounts for the two earlier reviews at its head.

| Review | Date | What the record holds | Snapshot |
|---|---|---|---|
| SR1 | 16 September, as stated in the preparation record; no September timetable exists to confirm it | A preparation record in two versions, both filling the seven fields and both stating that no executable result is claimed. The session record at the foot is blank and marked *not held / no tutor results recorded*: no tutor point, no decision changed, no owner for follow-up | None. `standup-1-2026-09-16` marks the standup and is the nearest state, not a review snapshot |
| SR2 | End of Sprint 2, by 28 September | No record and no preparation document. The increment is the initial release, tagged the following evening | None. `submission-2026-09-29` is the release tag, not a review snapshot |
| SR3 | 14 October | Dated, attendance still to be completed. Completed tasks, unfinished tasks, key decisions, integration evidence and testing evidence are empty. The feedback field quotes the class sheet's G07 entry and the backlog-update field records what it produced. The retrospective is empty | `sr3-2026-10-14` at `25f53f7` (15:07), the last commit before the session slot; `2d09f5a` (21:01) came after the review and is excluded |
| SR4 | Not fixed | One field is filled: the key decision of 19 October, that `PB-12`'s second-owner review was signed after the first owner confirmed the corrected abstraction text. Date and attendance, completed and unfinished tasks, integration, testing, feedback, backlog changes and retrospective are empty | No `sr4-` tag exists |

**Whether a fourth review took place cannot be established from the repository's records, and the record is left as it stands.** The specification places the last review by 22 October; the 12–16 October timetable carries Stand-up 04 but no Sprint Review 04, so the review was expected in the week beginning 19 October. The record shows a section opened for SR4 with one decision logged and no date. It shows no attendance list, no increment and no retrospective, and no snapshot was tagged. A decision taken on 19 October and recorded under SR4 is a fact; a completed review is not. The group's own position, written into the same file, is that a review record answers what was shown and what the tutor said, and neither can be supplied after the session, so the blank stays a blank.

## 6. Risk register — initial release

The initial release closed without a risk register. The register below sets out the risks that were live in that period, each with what was done and what was not.

| Risk | Evidence that it was live | What was done, and what was not |
|---|---|---|
| **Role enforcement did not exist.** Any user who could reach the Tasklist could complete any task, including a consultant decision. | `PB-18_acceptance-test-plan_2026-09-29.md` §5: AT-03 **FAIL**, instance `2251799813927118`, "Book visit was created"; the plan names the cause as "no candidate-group RBAC". `Group_Project_and_Test_Plan_2026-09-29.pdf` §3 repeats it; `BR-37` is Unsupported in the traceability matrix | Recorded as a failure, with the handling proposed against `PB-22` and the instruction not to rewrite it as a pass. `PB-22` was never scheduled into Sprint 3 or 4, no candidate group or login was added, and the same case failed again on 19 October |
| **Results were bound to a working copy and a local engine build, not to something a reader could re-create.** | The acceptance plans name deployed definition version 6 and a baseline of `8c666bf` *at plan write*; the scripts hard-code `Hospital_All_Processes_Simple_C8`; the plan's baseline `fc6293e` is reachable from no branch or tag, while the release tag `f6fec99` is the state a reader can check out | Results archived with instance keys and JSON logs; the baseline was re-pointed to the release tag on 16 October. No re-run followed before the second release, and the scripts could not be pointed at another model without editing |
| **Delivery depended on a small part of the team, and handovers were not written down.** | 120 commits between 15 and 29 September, 103 under two of the four members' accounts; the `PB-16` second-owner review open from September and still unsigned on 20 October | First and second owners on every item, and a review required before an item was marked Done. Handovers were never recorded in the standup table, and the `PB-16` review did not close |
| **Time-dependent rules could not be enforced.** | Zero `timerEventDefinition` elements in the 29 September model; `BR-32`, `BR-33` and `BR-34` graded Partial for this reason | Recorded as Partial with the missing capability named. No timer was added in either release; V3 contains none |
| **The demonstration depended on services that do not exist and a local stack started by hand.** | `AISD-3_Justification_of_Decisions.md` §7, assumption 3: send, notify and pay steps write an audit row and produce no real email, letter or fund movement; the test plan calls the external services "classroom simulations" | Stated as a boundary in the justification and the test plan; a self-pay route was chosen that the mocks could carry end to end. No fallback demonstration was prepared for an engine that would not start, and that risk materialised on 19 October |
| **Acceptance coverage was narrow.** | The test plan marks the redirected-referrer branch, the direct audit-row count and the cross-member change-and-refund route as **NOT EVIDENCED** | Gaps listed in the test plan and carried into the written evaluation rather than counted as passes. Coverage was not widened in the second release; the same six cases were re-run |

## 7. Risk register — revised release

The revised release kept its risks in the plan of 16 October, each with an effect and a response. This is that record with the position at 20 October added.

| Risk | Effect if it happened | Response in the plan | Position at 20 October |
|---|---|---|---|
| The C8 environment does not start | No fresh run to demonstrate; only recorded evidence | Record the attempt and the failure honestly; demonstrate from the G07 JSON and the logs | Resolved. c8run 8.10.0-alpha5 starts with `--disable-connectors`; the model was deployed and run |
| `AT-03` is still a fail | One acceptance criterion unmet | Keep it recorded as a fail with its handling; show the cause is understood | Materialised. Failed again on V3 with the same cause, and stays recorded |
| Tutor feedback is not written down | The 20% criterion has no tutor evidence | Record the peer points received; leave tutor rows blank until a point arrives | Partly resolved. Seven peer points recorded, including the class sheet filed 19 October; no tutor point received in writing |
| The indexes point at a renamed folder | A marker following the links finds nothing | Re-point every reference and check file by file | Resolved 16 October: 34 references re-pointed; the evidence captures left at their recorded paths |
| Recorded results describe the 29 September state | The evidence describes a state other than the current tree | State the tagged baseline and say which conclusions still hold | Resolved 19 October: the revised model was re-run at `dbc0a33` and results recorded against it |
| Part B is not in the product backlog, so nothing there tracks it | The graded process artefacts could be overlooked | Part B of the plan is the tracker; the backlog points to it from Note 9 | Partly resolved. Feedback record, plan evaluation, deck and contribution record in place; standup and review records incomplete |

Three of the six closed, one materialised, two are partly closed. The register earned its place on the environment risk, which was named before it happened: when the bundled Connectors health check shut c8run down at 21:38 on 19 October, the run was restarted with connectors disabled and every case re-run in one continuous session rather than reported from the interrupted attempt. It did less well on a risk that was not on it at all — that the revised model would not be executed until the last evening.

## 8. Lessons learned

| What the record shows | What we take into the next delivery |
|---|---|
| `AT-03` was known on 29 September and failed again on 19 October. The September test record named `PB-22` as the handling, and the second-release plan never scheduled `PB-22`. | A known defect needs a dated item, an owner and a sprint. A proposed handling written inside a test record is not a plan, and a defect that is understood but unscheduled stays exactly where it was. |
| The revised model was first executed at 21:38 on 19 October; the release was tagged at 23:49 the same evening. | The acceptance position for a whole release rested on one late run. Run the model when the model changes, not when the release is due; a run made under deadline pressure cannot be repeated if it fails. |
| One run was lost when the Connectors health check shut c8run down mid-run at 21:38, and every case was re-run after a restart at 21:40. | The environment is part of the test rig. Start it before the run slot, record the exact start command, and write an environment failure down as a test result — which the evidence file does. |
| On 28 September, run evidence for the member D notification work was committed at 19:09 and deleted at 19:42 after the worker was simplified. No replacement run was recorded. | Refactoring invalidates the run that preceded it. When work is simplified or replaced, regenerate the evidence in the same change; deleting a run log leaves code that no run supports. |
| At 16 October none of the six graded process records existed. SU3 is four rows of *Not recorded*; SU4 has one row of four; SR3 has one field of seven; SR4 has one field and no date. | The records are part of the deliverable, not a by-product. A record written on the day costs minutes; a record written a week later cannot be written at all without inventing what was said. |
| The initial release had no risk register. Two of the six risks in section 6 then materialised — the role gap and the environment — and neither was visible as a tracked item during the sprint. | Keep the register in the plan, give each risk an owner, and review it at the standup. A risk that is only understood is not managed. |

Two things are deliberately not here. The uneven spread of work is recorded in section 6 as a delivery risk, but not turned into a lesson about individuals: the records show where delivery concentrated, not why, and a lesson that reads as an assessment of a named member would not be a lesson. The choice of a single merged model is also not a lesson: it was deliberate, it deployed, and G07 completed through it. The cost it carried is recorded as a trade-off in the justification of decisions.

## 9. What this record cannot show

- **SR2 has no minutes.** The increment is identifiable — the tagged initial release — but nothing records what was shown or said.
- **Stand-up 3 has no rows.** The 12 October session was assessed live; the table records that position rather than dating later work back to it.
- **SR4 has one field and no date.** A decision taken on 19 October is recorded under it; the review itself is not.
- **The initial release closed without a risk register.** Section 6 sets out the risks that the September records show were live, and what was and was not done about each.
- **The backlog status column stopped being maintained after 16 September**, so item status is read from the tagged trees and the acceptance record, not from that column.
