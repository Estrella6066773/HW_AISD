# Product Backlog — Hospital Patient Administration System

> Prioritised list of all features/work items. Items are pulled into Sprint Backlogs based on sprint goals and team capacity.
>
> Legend:
> - **P0** = Must have (blocks core workflow)
> - **P1** = Should have (important but not blocking)
> - **P2** = Nice to have (can defer to later sprint)
> - **Size** = Story points (fibonacci: 1, 2, 3, 5, 8, 13, 21)

---

## Epic 1: Referral Intake & Booking

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-01 | Medical Secretaries verify referral documents | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Missing doc detection; request-missing-doc flow |
| PB-02 | Consultant reviews and accepts/rejects/redirects referral | P0 | 8 | _TBD_ | _TBD_ | 📋 Todo | Decision form; mandatory reason + author ID |
| PB-03 | Outpatient Bookings Team arranges new patient appointment | P0 | 8 | _TBD_ | _TBD_ | 📋 Todo | External scheduler integration; priority handling |
| PB-04 | Patient notification (letter + phone for <2 weeks) | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | External correspondence service; call attempt logging |
| PB-05 | Urgent referral handling | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Skip normal timescales; flag urgency |

---

## Epic 2: Treatment Booking & Payment

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-10 | Consultant authorises Treatment Booking Request | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Auth check; incomplete requests blocked |
| PB-11 | Treatment Bookings Team coordinates appointments | P0 | 8 | _TBD_ | _TBD_ | 📋 Todo | External services (treatment, lab, imaging); pending state |
| PB-12 | Payment Service Provider integration | P0 | 13 | _TBD_ | _TBD_ | 📋 Todo | Secure payment request; no card storage; payment status return |
| PB-13 | Funding approval workflow | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Finance Team records org, ref, amount, limitations |
| PB-14 | Payment failure handling & re-attempt | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | No duplicate charges; no duplicate bookings |
| PB-15 | Orphaned payment (provider success, no confirmation) | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Mark for investigation; do not auto-charge again |
| PB-16 | Refund processing | P1 | 8 | _TBD_ | _TBD_ | 📋 Todo | Finance Team approval; external refund request |
| PB-17 | Urgent treatment bypass (no confirmed payment) | P1 | 3 | _TBD_ | _TBD_ | 📋 Todo | Clinician records reason; referred to Finance |

---

## Epic 3: Treatment Modification & Clinical Reviews

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-20 | Treatment Modification Request form (authorised only) | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Non-clinical staff blocked; audit trail |
| PB-21 | Finance review for financially-impacting modifications | P0 | 3 | _TBD_ | _TBD_ | 📋 Todo | Refer to Finance Team |
| PB-22 | Chemotherapy cycle review & blood test check | P1 | 8 | _TBD_ | _TBD_ | 📋 Todo | Clinical decision only; medical fitness check |
| PB-23 | Urgent treatment postponement (patient safety) | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Quick action; clinician records retrospectively |

---

## Epic 4: Clinic Letters

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-30 | Consultant writes & approves Clinic Letter | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Clinical content approval; recipient selection |
| PB-31 | Medical Secretaries process & distribute | P0 | 3 | _TBD_ | _TBD_ | 📋 Todo | Admin checks only; no clinical edits; external channels |
| PB-32 | 7-day monitoring reminder | P1 | 3 | _TBD_ | _TBD_ | 📋 Todo | Auto-check; weekly reminder; avoid duplicate |
| PB-33 | Escalation hierarchy (1 month → Admin Mgr; 3 months → higher) | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Correct escalation level per delay duration |

---

## Epic 5: Patient Enquiries

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-40 | Call Handling Team receives & classifies enquiry | P0 | 3 | _TBD_ | _TBD_ | 📋 Todo | Categories: admin / financial / clinical |
| PB-41 | Route to correct team based on classification | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Clinical → CNS Team; Financial → Finance; Admin → relevant |
| PB-42 | Enquiry record (received, handled, assigned, resolved) | P0 | 3 | _TBD_ | _TBD_ | 📋 Todo | Full audit trail of each enquiry |
| PB-43 | Urgent clinical enquiry highlight | P1 | 3 | _TBD_ | _TBD_ | 📋 Todo | Immediate flagging |

---

## Epic 6: Follow-up & Cancellation

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-50 | Follow-up appointment booking | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | External scheduler; highlight if outside requested window |
| PB-51 | Cancellation / reschedule handling | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | Record event; decide re-offer; Finance referral if paid |
| PB-52 | DNA (Did Not Attend) handling | P1 | 3 | _TBD_ | _TBD_ | 📋 Todo | Record; pathway review; refer to Finance if paid |

---

## Epic 7: Non-Functional — Security, Audit, Reporting

| ID | Item | Priority | Size | First Owner | Second Owner | Status | Acceptance Criteria |
|----|------|----------|------|-------------|--------------|--------|---------------------|
| PB-60 | Role-based access control | P0 | 8 | _TBD_ | _TBD_ | 📋 Todo | Staff only sees role-required info |
| PB-61 | Audit logging (immutable records) | P0 | 5 | _TBD_ | _TBD_ | 📋 Todo | User + date/time + action; non-editable |
| PB-62 | Patient ID deduplication / matching | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Reduce wrong-association risk |
| PB-63 | System unavailability fallback procedure | P1 | 5 | _TBD_ | _TBD_ | 📋 Todo | Record activities completed during outage |
| PB-64 | Management reports (referral volumes, waiting times, ...) | P2 | 13 | _TBD_ | _TBD_ | 📋 Todo | Dashboard of key KPIs |

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 📋 Todo | Not started |
| 🚧 In Progress | Currently being worked on |
| ✅ Done | Completed |
| 🚫 Blocked | Cannot proceed (waiting on something) |
