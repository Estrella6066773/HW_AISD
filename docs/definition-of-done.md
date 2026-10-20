# Definition of Done

> **Provenance**: first written on 2026-09-14 as `agile/definition-of-done.md`, in the initial repository skeleton (commit `c8da046`); deleted in commit `3d114fa`; restored from history on 2026-09-16 into `docs/`. Corrected on 2026-09-16 against the layout the repository actually has: every path below now points at a file or folder that exists, and items that belong to the implementation increment are labelled as such.
>
> This file is the deliverable for **PB-29** (first owner Ender, second owner Estrella). PB-29 was withdrawn from the product backlog on 2026-10-16: a Definition of Done is an agreement about how the group works, not product work, so it carries no backlog ID. Group sign-off is still required before the checklist below can be called agreed.

A user story, task, or work item is considered **Done** when ALL of the following are true.

## How to use this list

The list spans two increments, and not every group applies to both. The 16 September standup delivers a **plan increment only** — no models and no code (see `docs/p6-sprint-backlog.md`).

| Group | Applies to |
|-------|------------|
| BPMN & Process Modeling, External Workers, Camunda Forms, Code Quality | The 28 September implementation increment and later. The folders these items name (`docs/strategic-bpmn/`, `docs/operational-bpmn/`, `forms/`, `src/workers/`) are created when implementation starts; naming follows `docs/requirements-traceability-matrix.md`. |
| Documentation, Delivery Evidence | Every increment, including the 16 September plan increment. |

An item must not be marked Done by ticking items from a group that does not apply to its increment. In the plan increment, the last two groups are the ones that can actually be satisfied.

## BPMN & Process Modeling — implementation increment

- [x] BPMN model follows BPMN 2.0.2 standard and Camunda 8 best practices — deployed and executed on Camunda 8.10.0-alpha5 (`Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`).
- [x] Model is executable (all required technical attributes configured) — 22 user tasks, 8 service tasks, 10 bound job types, 12 form bindings; G07 ran to completion.
- [x] Normal path, alternative paths, and exception paths are modeled — 27 exclusive gateways cover the referral, visit, funding and change branches; AT-02 (rejected referral) and AT-04 (no slot) exercise two alternative paths.
- [x] Process has been deployed to Camunda 8 successfully — deployment key `2251799813928657`, definition key `2251799813928658` (evidence/Camunda_V3_Acceptance_2026-10-19.txt).
- [x] Process has been tested end-to-end in Tasklist / Operate — G07 instance `2251799813931091` reached COMPLETED with 9 human tasks and no active incident (evidence/Camunda_V3_Acceptance_2026-10-19.txt).
- [x] Model file sits under `docs/strategic-bpmn/` or `docs/operational-bpmn/`, as applicable — the strategic model is `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`; the operational model is `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`, the location the second release has used since 19 October.

## External Workers — implementation increment

- [x] Worker subscribes to the correct topic(s) — the ten `@JobWorker` types across five classes match the `zeebe:taskDefinition type` strings in the model.
- [x] Worker receives variables from the process instance — the acceptance logs show the variables arriving per job; see the per-case records in `evidence/`.
- [x] Worker processes variables and returns results correctly — 19 unit tests, 0 failures (evidence/Java_Test_Results_2026-10-20.txt), and the completed G07 route carries the returned values.
- [ ] Error handling covers: invalid input, service failures, timeouts — **partly met**: invalid input is covered by unit tests (`rejectsBlankLettersNegativeAndWrongScale`, `wrongPrecisionFailsWithoutWriting`) and service failure by explicit job failure and retry reuse; **timeouts are not covered**, because the model carries no timer and no timeout path is tested.
- [x] Worker is idempotent (can safely retry without duplicate side effects) — covers the case rules on no duplicate appointments and no duplicate charges — `requestRefund` reuses the ledger row, `requestPayment` reuses when `payment_requested_once` is set, `notifyCareChange` keys the receipt on process and element instance, `upsertBooking` reuses by occupancy key. Tested in `RefundWorkersTest` (`refundRetryReusesSameLedgerRow`) and `CareChangeWorkersTest` (`retriesReuseReceiptButLaterChangesGetNewReceipts`).
- [x] Worker logs meaningful messages for debugging — each worker writes an `audit_event` row carrying the actor prefix for its owner, and the run logs name the failing element on an incident.
- [x] Worker code sits under `src/workers/` — the workers live in `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/`, the module location the second release has used throughout; the folder named here was never created.

## Camunda Forms — implementation increment

- [x] Form is connected to the correct user task in BPMN — 22 `zeebe:formDefinition` bindings resolve to 12 distinct formIds, every one present in `Week6 Coursework/forms/`; audit in `evidence/Java_Clean_Build_Test_2026-10-19.txt`.
- [x] All required fields are present with clear labels — checked in the 19 October validation pass; `review_referral` marks `decisionReason` required, `book_visit` marks date, time and `waitReason`.
- [x] Input validation is in place (required fields, data types, ranges) — constraints are defined and bound, including `adjustmentAmount` limited to 0.01–99999.99 and a partial refund required to be below the original charge. This records definition and binding only; browser-side rejection was not exercised (see the limit below).
- [x] Variables are mapped correctly between form and process — the acceptance runs wrote through the form variables and G07 carried them to completion.
- [ ] Form works for all user roles that access the task — **not met**: all 22 user tasks are `assignee="demo"` with zero `candidateGroups`, so no role distinction exists for a form to satisfy. `AT-03` fails on both releases for this reason and `BR-37` is unsupported.
- [x] Form file sits under `forms/` — the deployed set is `Week6 Coursework/forms/`, twelve `.form` files; the `forms/` folder named here was never created.

## Code Quality — implementation increment

- [x] Code compiles / runs without errors — `mvn -B clean test` reports BUILD SUCCESS, 19 tests (evidence/Java_Test_Results_2026-10-20.txt).
- [x] No hardcoded secrets or credentials; no patient data and no card data committed — `application.yaml` holds the local `demo`/`demo` and an empty-password H2 file; the database file is not committed.
- [x] Code is self-documenting (clear variable names, comments where needed).
- [x] At least one team member (Second Owner) reviewed the changes — Ender, Ryan and Estrella reviewed the worker module on 2026-10-20; record in `Week6 Coursework/process/B-6_worker-review_2026-10-20.md`.

## Documentation — every increment

- [x] Changes are reflected in the root `README.md` when the repository structure or the deliverable index changes — the `Releases` section carries both tags and the second-release layout.
- [x] Assumptions are recorded where they belong: group assumptions in the Part 1 case summary (`Ruby/2026-09-14/ruby：part1案例摘要.md`), and item-level assumptions such as mocked external services in the item's own file — the mocked payment and letter services are stated in the worker notes and in §4.6 of `submissions/BPMEA/BPMEA_Written_Evaluation.pdf`.
- [x] Known limitations are documented — `Limits recorded, not hidden` in `submissions/Submission_Index.pdf` page 2, and §4.6 of the written evaluation.
- [x] The item's row in `docs/p3-product-backlog.md` shows the correct Status — corrected on 20 October for `PB-13` (was `Not started`), `PB-30`, `PB-31` and `PB-16`.

## Delivery Evidence — every increment

- [x] Screenshot, log or document evidence is committed to the repository at a path that can be opened, named `PB-xx_name_type_date` — the acceptance records follow the form (`PB-14_acceptance-run-log_2026-10-19.json`, `PB-18_acceptance-run-log_2026-10-19.json`); the build and test logs are named by subject instead (`Java_Test_Results_2026-10-20.txt`), and both are opened from the evidence column.
- [x] That path is written in the item's Evidence column in `docs/p3-product-backlog.md`, and in the Evidence column in `docs/p6-sprint-backlog.md` for sprint tasks.
- [ ] Git commit message describes what was changed and references the backlog item, for example `docs(PB-01): add role permission table` — **not met**: of 198 commits on `main`, 18 carry a `PB-xx` reference; the commit carrying the 19 October acceptance evidence, `41d2f10`, carries none. Messages describe the change, but the reference convention was not applied.
- [x] Backlog item status is updated in `docs/p3-product-backlog.md`, and in `docs/p6-sprint-backlog.md` for sprint tasks.

## Group sign-off

This checklist is the deliverable for PB-29, whose acceptance condition is that the whole group agrees to it. PB-29 was withdrawn from the product backlog on 2026-10-16 and now carries no backlog ID; it is tracked as planning work in part B of `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md`. The checklist stays **unagreed** until all four members have signed off, and the sign-off record is part of the evidence.

### Sign-off record, 20 October 2026

The four members read this checklist together on the afternoon of 20 October 2026 and agreed to it as it stands: 28 of the 31 items are ticked, each tick naming the file that supports it, and 3 are left unticked with the reason written beside them.

| Member | Signature | Date |
|---|---|---|
| Hao Zheng (Ruby) | Ruby | 2026-10-20 |
| Geping Chen (Estrella) | Estrella | 2026-10-20 |
| Minghao Qin (Ender) | Ender | 2026-10-20 |
| Guanyan He (Ryan) | Ryan | 2026-10-20 |

The three items left unticked are known and accepted rather than outstanding work:

1. **Timeouts** in the worker error handling. The model has no timer, so a timeout path does not exist to handle.
2. **Form works for all user roles.** There is no role layer; every task is assigned to `demo`. This is the same defect `AT-03` records on both releases.
3. **Commit messages referencing the backlog item.** 18 of 198 commits on `main` carry a `PB-xx` reference. The convention was written down and never applied consistently, and rewriting the history to satisfy it would misrepresent what happened.

Signing this checklist means the group agrees the completed items are Done and the three gaps above are recorded truthfully. It does not mean every item on the list is satisfied.
