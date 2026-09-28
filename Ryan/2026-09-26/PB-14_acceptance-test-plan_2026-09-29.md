# PB-14 Acceptance Test Plan and Results

**Module**: UFCEP6-0-3 AISD · Hospital Patient Referral, Treatment and Administration System  
**Backlog item**: PB-14 (Part 4 task T19)  
**First owner**: Ryan · **Second owner**: Ender  
**Purpose**: Meet the Portfolio **Project & Test Plan** requirement (LO5) and Presentation **Task 02 Acceptance Test Plan** fields for the referral slice: two executable acceptance tests with preconditions, test data, steps, expected results, actual results and pass/fail verdicts.

---

## 1. Version under test (must be identifiable)

| Item | Value |
|------|-------|
| Process id | `Hospital_All_Processes_Simple_C8` |
| BPMN file | `Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` |
| Forms used | `register_request.form`, `review_referral.form`, `book_visit.form` |
| Deployed definition | version **6**, processDefinitionKey `2251799813925244` |
| Git baseline when planned | commit `275ab9f` |
| Execution date | 2026-09-29 |
| Run id | `PB14-20260929-004206` |
| Camunda | local c8run 8.10.0-alpha5 · Operate/Tasklist `http://localhost:8080` · user `demo` |

This is the version against which Actual results below were recorded. Re-runs must update this table.

---

## 2. Requirements / business rules under test

| ID | Rule (from case study) | Measurable acceptance criterion |
|----|------------------------|---------------------------------|
| BR-A | After documents are checked, the consultant records a decision with **reason** and **identity** (case para 4) | Review task cannot be treated as complete for the path unless `decisionReason` and `clinicianId` are present; variables retain the decision |
| BR-B | A **New Patient Appointment may only be arranged after** an authorised consultant has **accepted** (case para 4–5) | After `accept`, the next user task is **Book visit**; after `reject`, **Book visit** is never created and the process ends at **Referral rejected** |

PB-14 does **not** claim to prove production role login (secretary cannot accept). That is PB-22 / PB-18.

---

## 3. Test design summary

| Test ID | Scenario type | Covers |
|---------|---------------|--------|
| AT-01 | Main / normal path | Documents checked → Accept → New-patient booking entered → slot check → clinical care reachable |
| AT-02 | Exception path | Documents checked → Reject → process ends; no new-patient booking |

Pass/fail: a test **passes** only if every Expected check in its table matches Actual. Failures must be left as Fail with a reason (Portfolio Task 04).

---

## 4. Shared preconditions

1. Camunda 8 Run is running; Operate and Tasklist open at port 8080; login `demo` / `demo`.
2. Process `Hospital_All_Processes_Simple_C8` is deployed (Modeler deploy or existing classroom deployment).
3. For **AT-01 only**: Java workers are running from `Coursework/hospital-pathway` (`mvn spring-boot:run`) so job type `check-slot` can finish.
4. Use a unique Patient / case ID for each run so results can be found in Operate.

**Official student procedure (what the test plan describes):** complete the steps in **Tasklist** using the bound Camunda Forms.  
**Recorded execution for this file:** the same form field values were submitted through Camunda REST `/v2` (script `scripts/pb14_acceptance.py`), which completes the same user tasks and writes the same process variables. Operate instance keys below are the verification handles for the live demo.

---

## 5. AT-01 — Main path (accept → book)

### 5.1 Preconditions

Shared items 1–4. Worker `check-slot` active.

### 5.2 Test data (enter on forms)

| Task (Tasklist title) | Form field | Value used |
|-----------------------|------------|------------|
| P1 Register request | Patient / case ID | `PB14-20260929-004206-MAIN` |
| | Specialty | Oncology |
| | Priority | Routine |
| | Requested timeframe | within 2 weeks |
| | Request type | New referral - documents checked |
| | Registration notes | PB-14 AT-01 documents checked |
| P2 Consultant reviews referral | Patient / case ID | same as above |
| | Clinician ID / name | CONSULTANT-PB14-01 |
| | Referral decision | Accept |
| | Decision reason | Clinically appropriate for new-patient clinic |
| P3 Book visit | Patient / case ID | same |
| | Staff name and role | Outpatient Bookings / PB-14 |
| | Outcome / next action | Booked, notified and attended |
| | Booking / contact notes | Slot confirmed within requested timeframe; letter and phone recorded |

### 5.3 Actions (Tasklist)

| Step | Action | Expected at that step |
|------|--------|------------------------|
| 1 | Tasklist → Processes → start `Hospital_All_Processes_Simple_C8` | Task **Register request** appears |
| 2 | Complete Register with data above → Complete task | Task **Consultant reviews referral** appears |
| 3 | Complete Review with **Accept** + reason + clinician → Complete task | Task **Book visit** appears (proves BR-B accept branch) |
| 4 | Complete Book visit with **Booked, notified and attended** | Service task Check / reserve outpatient slot runs (`check-slot`) |
| 5 | Wait for worker (few seconds) | Task **Consult / treat / review** appears |
| 6 | Open Operate for this instance | State Active (or later Completed if continued); end event **Referral rejected** was not taken |

### 5.4 Expected vs Actual vs Verdict

| Check | Expected | Actual (2026-09-29 run) | Result |
|-------|----------|-------------------------|--------|
| E1 | After Accept, Book visit task exists | Book visit created; userTaskKey `2251799813925371` | Pass |
| E2 | Variables: `referralDecision=accept` and non-empty `decisionReason` | `accept` / `Clinically appropriate for new-patient clinic` | Pass |
| E3 | After Book visit + check-slot, Consult/treat/review task exists | ClinicalCare reached | Pass |
| E4 | Referral rejected end event not used | Not reached | Pass |
| E5 | No active incident | 0 incidents | Pass |

| Verdict | **PASS** |
|---------|----------|
| Process instance key | `2251799813925318` |
| Operate URL (local) | `http://localhost:8080/operate/processes/2251799813925318` |
| Evidence log | `Ryan/2026-09-26/PB-14_acceptance-run-log_2026-09-29.json` |
| Failures | None on E1–E5. Instance left open at clinical care (payment/letters out of PB-14 scope). Classroom assignee is `demo` (not a role-RBAC proof). |

---

## 6. AT-02 — Rejected referral (no booking)

### 6.1 Preconditions

Shared items 1, 2, 4. Java workers **not** required.

### 6.2 Test data

| Task | Form field | Value used |
|------|------------|------------|
| Register | Patient / case ID | `PB14-20260929-004206-REJECT` |
| | Request type | New referral - documents checked |
| | Other required fields | Same shape as AT-01; notes = PB-14 AT-02 documents checked |
| Review | Clinician ID / name | CONSULTANT-PB14-02 |
| | Referral decision | **Reject** |
| | Decision reason | Referral not appropriate for this specialty |

### 6.3 Actions (Tasklist)

| Step | Action | Expected at that step |
|------|--------|------------------------|
| 1 | Start process | Register request appears |
| 2 | Complete Register as referral | Consultant reviews referral appears |
| 3 | Complete Review with **Reject** + reason | Process finishes; Tasklist shows no Book visit for this case |
| 4 | Open Operate | State **Completed**; ended at **Referral rejected** |
| 5 | Confirm history | No Book visit user task for this instance |

### 6.4 Expected vs Actual vs Verdict

| Check | Expected | Actual (2026-09-29 run) | Result |
|-------|----------|-------------------------|--------|
| R1 | Process completed | state `COMPLETED` | Pass |
| R2 | `referralDecision=reject` and non-empty reason | `reject` / `Referral not appropriate for this specialty` | Pass |
| R3 | Book visit never created | `BookVisit_created = false` | Pass |
| R4 | No active incident | 0 | Pass |

| Verdict | **PASS** |
|---------|----------|
| Process instance key | `2251799813925262` |
| Operate URL (local) | `http://localhost:8080/operate/processes/2251799813925262` |
| Evidence log | `Ryan/2026-09-26/PB-14_acceptance-run-log_2026-09-29.json` |
| Failures | None on R1–R4. |

---

## 7. How to repeat (for second owner / demo)

**Preferred for viva / Sprint Review (forms visible):** follow sections 5.3 and 6.3 in Tasklist with new case IDs; paste screenshots into this folder named `PB-14_at01-operate_YYYY-MM-DD.png` and `PB-14_at02-operate_YYYY-MM-DD.png`.

**Repeatable automated check (same variables as forms):**

```text
cd Coursework/hospital-pathway
mvn spring-boot:run
python scripts/pb14_acceptance.py
```

Copy the new `target/pb14-acceptance-*.json` here as `PB-14_acceptance-run-log_<date>.json` and update Actual columns.

---

## 8. Traceability

| Test | Case paragraphs | Backlog | BPMN path |
|------|-----------------|---------|-----------|
| AT-01 | 3–6 | PB-01, PB-02, PB-03 (slice) | Register → ReviewReferral → BookVisit → CheckVisitSlot → ClinicalCare |
| AT-02 | 4 | PB-02 reject | Register → ReviewReferral → EndRejected |

---

## 9. Known limitations (stated honestly)

1. This PB-14 run proves **routing and recorded decision variables**, not eight-role security.
2. Slot confirmation is the classroom **mock** worker `check-slot`, not a live hospital scheduler.
3. AT-01 stops when clinical care is reachable; funding/payment/letter paths are other backlog items.
4. Operate UI screenshots were not captured in-repo on 2026-09-29 (browser in this environment could not open localhost). The run log and Operate instance keys are the committed execution evidence; add screenshots before the marked demonstration if the tutor expects image evidence.

---

## 10. Second-owner review (Ender)

- [ ] Steps match deployed gateways (`referral` / `accept` / `reject`)
- [ ] Each test has Expected, Actual and Pass/Fail
- [ ] Failures (if any) are not rewritten as pass
- [ ] Evidence path opens in the shared repository
- [ ] Can open Operate keys above (or a fresh Tasklist re-run) during review

PB-14 remains **In progress** until this checklist is signed off (group Definition of Done: second-owner review).
