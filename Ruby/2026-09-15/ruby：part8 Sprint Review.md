# Part 8: Prepare For Sprint Reviews

**Group project:** Hospital Patient Referral, Treatment and Administration System  
**First owner:** Hao Zheng (Ruby, 23084382)  
**Second owner:** Geping Chen (Estrella, 23084393)  
**Date:** 15 September 2026  
**Review:** Sprint 1 / 16 September 2026 (plan increment)  
**Backlog:** PB-15 / T20

This record prepares the group to demonstrate the **current integrated increment**, as required by Agile Workshop Part 8. On 16 September the increment is the agreed **plan**: case understanding, deliverables, product backlog, task breakdown, dependency map, Sprint 1 backlog, standup preparation, and this review. No BPMN diagram, Camunda form, worker or executable test is claimed as complete.

---

## Sprint 1 Goal

Finish and upload the Product Backlog and the Sprint 1 Backlog by 16 September. Specify the first delivery slice: referral check → consultant decision → first clinic booking (external scheduling may be mocked). Payment, clinic letters and enquiry routing are out of this sprint.

---

## Demonstration order

All four members present their own contribution.

| Order | Member | Focus |
|-------|--------|--------|
| 1 | Hao Zheng | Case summary, sprint goal, completed and unfinished work |
| 2 | Geping Chen | Business rules and Product Backlog |
| 3 | Minghao Qin | Deliverable list and Sprint 1 selected tasks |
| 4 | Guanyan He | Exceptions, external services, validation plan |

---

## 1. Completed tasks

Evidence is the artefact shown to the tutor at the review (the Part 1–8 tables and GitHub), not a local folder path.

| ID | Item | First owner | Second owner | Evidence | Status |
|----|------|-------------|--------------|----------|--------|
| Part 1 | Case study summary and eight discussion questions | Hao Zheng | Geping Chen | Part 1 summary table | Done |
| Part 2 | Deliverable list | Minghao Qin | Hao Zheng | Part 2 deliverable table | Done |
| Part 3 | Product Backlog (PB-01 to PB-29, twelve fields) | Geping Chen | Guanyan He | Part 3 Product Backlog table | Done (plan) |
| Part 4 | Task breakdown T01–T20 | Minghao Qin | Guanyan He | Part 4 task table | Done (draft) |
| Part 5 | Dependency mapping | Guanyan He | Geping Chen | Part 5 dependency table | Done (plan) |
| Part 6 | Sprint 1 Backlog and goal | Hao Zheng | Minghao Qin | Part 6 Sprint Backlog table | Done |
| T01 | Roles and permissions for referral check: secretaries may request missing papers; they must not accept a referral | Hao Zheng | Geping Chen | T01 row in Part 6; secretary vs consultant rule in Part 1 | Done |
| T02 | Main referral path: receive → check papers → send to consultant | Hao Zheng | Guanyan He | Path described in Part 1; T02 row in Part 6 | In progress |
| T20 | Upload Product Backlog and Sprint Backlog; all members on GitHub; plan only | Hao Zheng | Geping Chen | GitHub with four members; Part 3 and Part 6 uploaded | In progress |
| Part 7 | Individual standup format | Guanyan He (summary) | Hao Zheng (format) | Part 7 standup table | In progress |

---

## 2. Unfinished tasks

Unfinished work is reported with a reason. It is not marked as done.

| ID | Item | Reason | Next action |
|----|------|--------|-------------|
| T03 | Four consultant outcomes: accept / reject / request further information / redirect; reason and decision-maker required | Plan increment only; no form implementation on 16 Sep | Record decision fields after the review; bind Camunda Form by 28 Sep |
| T04 | Reject / redirect path: no new-patient booking after reject | Depends on T03 | Exception-path notes; rejected referrals must not enter booking |
| T05 | First clinic booking request only after accept | Depends on T03 | Gate rule: administration cannot book before accept |
| T06 | External scheduling (may mock): confirm a slot or set pending and flag the pathway team; do not book outside the requested window | Depends on T05; no worker on 16 Sep | Mock worker by 28 Sep |
| T07 | Notification: letter as normal; telephone if the visit is within two weeks; log every call result | Depends on a confirmed booking | Notification rule table |
| T08–T16 | Treatment authorisation, payment, clinic letters, enquiries, audit implementation | Outside Sprint 1 Goal | Remain on the Product Backlog for a later sprint |
| PB-12 / PB-13 / PB-16 | Strategic BPMN, Camunda Forms, i* SD/SR | 16 Sep is documents only | 28 Sep implementation increment |
| T19 / PB-14 | Executable acceptance tests | No running process yet | Test plan on 16 Sep; actual results on 28 Sep |
| Part 7 | Full set of individual standup records | Summary still waiting for remaining personal updates | Each member files their own standup |

---

## 3. Key decisions

Each decision is taken from the case study. The group does not invent clinical or urgency policy.

| ID | Decision | Case study basis | Effect on this sprint |
|----|----------|------------------|------------------------|
| D01 | Clinical decisions, administrative work and financial activity stay separate. The system enforces the boundary. | The service must maintain a clear distinction between clinical decisions, administrative responsibilities and financial activities. | Secretaries cannot accept a referral. Finance cannot decide treatment. |
| D02 | Sprint 1 covers only referral check → consultant decision → first clinic booking. | A New Patient Appointment may only be arranged after an authorised Consultant has accepted the referral. | Sprint 1 tasks are T01–T07 and T20. Treatment, payment, letters and enquiries stay on the Product Backlog. |
| D03 | External scheduling, correspondence and payment may be mocked in the first release, but mocked failures must still follow the case. | If an external service is temporarily unavailable, the booking must remain pending, the responsible team must be notified, and further attempts must be recorded without creating duplicate appointments. | No-slot and unavailable-service paths are kept. The mock boundary is stated in the plan. |
| D04 | Where the case is incomplete, the gap is logged and referred to tutors. No unofficial policy is written. | The hospital has not yet agreed a complete set of rules for determining urgency. | Enquiry urgency (PB-10) is not in Sprint 1. |
| D05 | Every task has a first owner and a different second owner. Done requires evidence. | Workshop ownership rule; Part 5 handover rule. | T01 is Done. T03 is Not started. |
| D06 | An unconfirmed successful payment is marked for investigation. The system must not automatically request another payment. Urgent treatment without confirmed payment requires a recorded clinical reason and referral to Finance. | Payment confirmation failure and urgent-treatment rules in the case study. | Held for later tests. Not demonstrated as software on 16 Sep. |

---

## 4. Evidence of integration

On 16 September, integration means one identifier scheme, one sprint slice and one repository. It does not mean a running Camunda process.

| Integration point | What is aligned | Evidence shown to the tutor |
|-------------------|-----------------|-----------------------------|
| Identifiers | PB-01 ↔ T01/T02; PB-02 ↔ T03/T04; PB-03 ↔ T05/T06; PB-04 ↔ T07; PB-15 ↔ T20 | Same IDs in Part 3, Part 4 and Part 6 |
| Scope | Sprint Goal matches the case path as far as first booking | Part 1 summary and Part 6 Goal |
| Authority | Medical Secretaries check documents; only an authorised Consultant accepts; Outpatient Bookings act after accept | T01 in Part 6; referral rules in Part 1 |
| Exception paths | Reject does not book; no suitable slot stays pending and is flagged; duplicates are not created | T04 and T06 in Part 6; exception list in Part 1 |
| Repository | Four members added; Part 3 and Part 6 uploaded | GitHub organisation / project page |

The 28 September increment will add process-level integration: referral form → consultant decision → mocked scheduling on one deployed model, with commits attributable to each member.

---

## 5. Testing or validation evidence

No executable test result is claimed for 16 September. Validation against the case study text is recorded below. Actual run results will be added when the process exists. Failed or unrun checks will remain visible.

### 5.1 Case-study validation (document increment)

| Rule | Expected behaviour | Current check | Actual result (16 Sep) |
|------|--------------------|---------------|-------------------------|
| Secretaries must not accept a referral | Secretary role cannot accept or reject | T01 permission notes match the case | Pass (document) |
| Reason and decision-maker required | Consultant decision cannot proceed without both | T03 acceptance condition agreed | Not executed |
| Booking only after accept | Rejected or redirected referrals do not enter new-patient booking | T04 / T05 gate agreed | Not executed |
| No slot inside the requested window | Booking stays pending; pathway team is flagged; no silent booking outside the window | T06 mock rule agreed | Not executed |
| Visit within two weeks | Letter plus telephone; each attempt and outcome recorded | T07 rule agreed | Not executed |

### 5.2 Planned executable tests (28 September)

| ID | Scenario | Expected result |
|----|----------|-----------------|
| TC-01 | Unauthorised role attempts accept or treatment booking | Action refused |
| TC-02 | Normal path: papers complete → consultant accepts → booking request → mock slot available → confirm | Appointment confirmed in the hospital system |
| TC-03 | Consultant rejects the referral | No new-patient booking is created |
| TC-04 | No suitable slot in the requested period | Status pending or escalated; no duplicate booking |
| TC-05 | Later sprint: payment declined, then retry | Second attempt allowed; no duplicate booking or charge |
| TC-06 | Later sprint: provider takes payment, hospital receives no confirmation | Marked for investigation; no automatic second charge |

---

## 6. Feedback received

Tutor feedback from the live review is not yet available. Only feedback that has already occurred is recorded. Invented tutor comments are not entered.

| ID | Source | Issue | Decision | Owner | Outcome |
|----|--------|-------|----------|-------|---------|
| F01 | Group | Do not plan the happy path only | Adopted | Hao Zheng / Guanyan He | Exception tasks T04, T09, T11, T12 remain on the Product Backlog |
| F02 | Group | Real external services cannot be connected in Sprint 1 | Adopted; mock with labelled boundary | Minghao Qin | Scheduling mock in Sprint 1; payment mock after first booking |
| F03 | Group (Part 4 review) | Some dependencies named only “Part 1 summary” | Adopted | Guanyan He | Part 5 maps predecessors to Task IDs |
| F04 | Group (Part 4 review) | Done requires an evidence path | Adopted | Hao Zheng | A Done status without evidence does not clear a dependency |
| F05 | Case study | Urgency rules for clinical enquiries are undefined | Do not invent policy; ask tutors | Geping Chen | PB-10 stays out of Sprint 1 |
| F06 | Tutor | Not yet received | To be recorded at the review | Hao Zheng | After the session: decision, owner, backlog change |

---

## 7. Backlog updates

Items are not deleted. Scope changes move work between the Product Backlog and the Sprint Backlog.

| Update | Reason | Current placement |
|--------|--------|-------------------|
| Sprint 1 pulls only the first-booking slice from P0 | 16 Sep is a plan review; the sprint goal must stay small | Part 6: T01–T07, T20 |
| Treatment authorisation, external treatment failure and payment (T08–T11 / PB-05–PB-07) are not in this demonstration | The case places them after the New Patient Appointment | Product Backlog; later sprint |
| Clinic-letter delay rules and enquiry routing are deferred | Required by the case, not by the first slice | PB-09, PB-10 (P1) |
| Rejected referral, no-slot escalation, uncertain payment and urgent treatment-without-payment stay visible | F01; explicit case rules | T04, T06, T11, T12 on the Product Backlog |
| Audit should at least cover referral decisions and treatment authorisation in release one | Significant actions listed in the case | PB-11; not implemented on 16 Sep |
| Wider Sprint 1 coverage only if tutors require it | F06 | Add T13–T15 and revise the Sprint Goal; do not expand scope informally |

---

## Member contribution for this increment

| Member | Completed work | Evidence shown to the tutor | Next action |
|--------|----------------|-----------------------------|-------------|
| Hao Zheng | Part 1 summary; Part 6 Sprint Backlog; this Part 8 record; T01 permission rules | Part 1, Part 6 and this Part 8 | Close T02 path notes; T03 decision fields after the review |
| Geping Chen | Part 3 Product Backlog; review of Parts 1, 5 and 8 | Part 3 Product Backlog table | Upload the backlog; T07 notification rules |
| Minghao Qin | Part 2 deliverables; Part 4 breakdown and review; T06 mock agreement | Part 2 and Part 4 tables | Scheduling mock worker by 28 Sep |
| Guanyan He | Part 1 exceptions and external systems; Part 5 dependencies; Part 7 summary format | Part 1 exception list; Part 5 table; Part 7 standup | T04 reject path; T19 test plan |

---

## Review session record

To be completed at the 16 September session. Current status: **not held / no tutor results recorded**.

| Field | Entry |
|-------|--------|
| Date and session | TBC |
| Version shown | Plan increment (Parts 1–8) |
| Completed task IDs shown | |
| Unfinished task IDs shown | |
| Integration evidence shown | |
| Validation evidence shown | |
| Decisions confirmed or changed | |
| Tutor feedback IDs | |
| Resulting backlog changes | |
| Owners for follow-up | |

---

## Sources

- Agile Workshop, Part 8  
- Case Study: Hospital Patient Referral, Treatment and Administration System  
- Group Parts 1–7 shown at this review
