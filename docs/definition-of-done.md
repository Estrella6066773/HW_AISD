# Definition of Done

> **Provenance**: first written on 2026-09-14 as `agile/definition-of-done.md`, in the initial repository skeleton (commit `c8da046`); deleted in commit `3d114fa`; restored from history on 2026-09-16 into `docs/`. Corrected on 2026-09-16 against the layout the repository actually has: every path below now points at a file or folder that exists, and items that belong to the implementation increment are labelled as such.
>
> This file is the evidence for **PB-29** (first owner Ender, second owner Estrella). Group sign-off is still required before PB-29 is counted as Done.

A user story, task, or work item is considered **Done** when ALL of the following are true.

## How to use this list

The list spans two increments, and not every group applies to both. The 16 September standup delivers a **plan increment only** — no models and no code (see `docs/p6-sprint-backlog.md`).

| Group | Applies to |
|-------|------------|
| BPMN & Process Modeling, External Workers, Camunda Forms, Code Quality | The 28 September implementation increment and later. The folders these items name (`docs/strategic-bpmn/`, `docs/operational-bpmn/`, `forms/`, `src/workers/`) are created when implementation starts; naming follows `docs/requirements-traceability-matrix.md`. |
| Documentation, Delivery Evidence | Every increment, including the 16 September plan increment. |

An item must not be marked Done by ticking items from a group that does not apply to its increment. In the plan increment, the last two groups are the ones that can actually be satisfied.

## BPMN & Process Modeling — implementation increment

- [ ] BPMN model follows BPMN 2.0.2 standard and Camunda 8 best practices
- [ ] Model is executable (all required technical attributes configured)
- [ ] Normal path, alternative paths, and exception paths are modeled
- [ ] Process has been deployed to Camunda 8 successfully
- [ ] Process has been tested end-to-end in Tasklist / Operate
- [ ] Model file sits under `docs/strategic-bpmn/` or `docs/operational-bpmn/`, as applicable

## External Workers — implementation increment

- [ ] Worker subscribes to the correct topic(s)
- [ ] Worker receives variables from the process instance
- [ ] Worker processes variables and returns results correctly
- [ ] Error handling covers: invalid input, service failures, timeouts
- [ ] Worker is idempotent (can safely retry without duplicate side effects) — covers the case rules on no duplicate appointments and no duplicate charges
- [ ] Worker logs meaningful messages for debugging
- [ ] Worker code sits under `src/workers/`

## Camunda Forms — implementation increment

- [ ] Form is connected to the correct user task in BPMN
- [ ] All required fields are present with clear labels
- [ ] Input validation is in place (required fields, data types, ranges)
- [ ] Variables are mapped correctly between form and process
- [ ] Form works for all user roles that access the task
- [ ] Form file sits under `forms/`

## Code Quality — implementation increment

- [ ] Code compiles / runs without errors
- [ ] No hardcoded secrets or credentials; no patient data and no card data committed
- [ ] Code is self-documenting (clear variable names, comments where needed)
- [ ] At least one team member (Second Owner) reviewed the changes

## Documentation — every increment

- [ ] Changes are reflected in the root `README.md` when the repository structure or the deliverable index changes
- [ ] Assumptions are recorded where they belong: group assumptions in the Part 1 case summary (`Ruby/2026-09-14/ruby：part1案例摘要.md`), and item-level assumptions such as mocked external services in the item's own file
- [ ] Known limitations are documented
- [ ] The item's row in `docs/p3-product-backlog.md` shows the correct Status

## Delivery Evidence — every increment

- [ ] Screenshot, log or document evidence is committed to the repository at a path that can be opened, named `PB-xx_name_type_date`
- [ ] That path is written in the item's Evidence column in `docs/p3-product-backlog.md`, and in the Evidence column in `docs/p6-sprint-backlog.md` for sprint tasks
- [ ] Git commit message describes what was changed and references the backlog item, for example `docs(PB-01): add role permission table`
- [ ] Backlog item status is updated in `docs/p3-product-backlog.md`, and in `docs/p6-sprint-backlog.md` for sprint tasks

## Group sign-off

This checklist is the deliverable for PB-29, whose acceptance condition is that the whole group agrees to it. It stays **In progress** in `docs/p3-product-backlog.md` until all four members have signed off; the sign-off record is part of the evidence.
