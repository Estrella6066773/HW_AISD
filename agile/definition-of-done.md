# Definition of Done

A user story, task, or work item is considered **Done** when ALL of the following are true:

## BPMN & Process Modeling

- [ ] BPMN model follows BPMN 2.0.2 standard and Camunda 8 best practices
- [ ] Model is executable (all required technical attributes configured)
- [ ] Normal path, alternative paths, and exception paths are modeled
- [ ] Process has been deployed to Camunda 8 successfully
- [ ] Process has been tested end-to-end in Tasklist / Operate

## External Workers

- [ ] Worker subscribes to the correct topic(s)
- [ ] Worker receives variables from the process instance
- [ ] Worker processes variables and returns results correctly
- [ ] Error handling covers: invalid input, service failures, timeouts
- [ ] Worker is idempotent (can safely retry without duplicate side effects)
- [ ] Worker logs meaningful messages for debugging

## Camunda Forms

- [ ] Form is connected to the correct user task in BPMN
- [ ] All required fields are present with clear labels
- [ ] Input validation is in place (required fields, data types, ranges)
- [ ] Variables are mapped correctly between form and process
- [ ] Form works for all user roles that access the task

## Code Quality

- [ ] Code compiles / runs without errors
- [ ] No hardcoded secrets or credentials
- [ ] Code is self-documenting (clear variable names, comments where needed)
- [ ] At least one team member (Second Owner) reviewed the changes

## Documentation

- [ ] Changes are reflected in this README (if structure or setup changed)
- [ ] Assumptions are recorded in the README "Case Study Assumptions" table
- [ ] Known limitations are documented

## Delivery Evidence

- [ ] Screenshot or log saved in `tests/test-results/` showing the feature working
- [ ] Git commit message describes what was changed and references the backlog item
- [ ] Backlog item status updated in `agile/sprint-backlogs/`
