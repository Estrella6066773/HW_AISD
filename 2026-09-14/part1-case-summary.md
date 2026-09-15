# Part 1 Case Study Summary

**Date**: 2026-09-14  
**Participants**: A Hao Zheng, B Geping Chen, C Minghao Qin, D Guanyan He  
**Topic**: Hospital Patient Referral, Treatment and Administration System — group case summary  

---

## 1. Main business processes

1. Referral enters from a GP / another hospital → Medical Secretaries check supporting documents (may request missing information; no clinical judgement).  
2. Consultant review: accept / reject / request further information / redirect to another specialist service; record the reason and the identity of the decision-maker.  
3. After acceptance, Outpatient Bookings arranges a New Patient Appointment via the external scheduling service; patients are normally informed by letter; if the appointment is within two weeks, they must also be contacted by telephone and each attempt/outcome recorded.  
4. After attendance, if the patient agrees to treatment → Consultant records consent and creates an authorised Treatment Booking Request → Treatment / Chemotherapy Bookings coordinates appointments.  
5. Before confirmation, determine funding source; if payment is required, use the external Payment Service Provider; schedule changes require a formal Treatment Modification Request; financially affected changes go to Finance.  
6. After consultation, Clinic Letter: Consultant writes and approves → Medical Secretaries distribute; delays trigger reminders and escalation.  
7. Patient enquiries are routed by Call Handling (administrative / financial / clinical).

## 2. Main participants

| Category | Roles |
|----------|--------|
| Patients and referrers | Patient, GP / other hospital |
| Clinical | Consultant, Clinical Nurse Specialist Team and other clinical professionals |
| Administrative | Medical Secretaries, Outpatient / Treatment Bookings, Call Handling, Patient Pathway Coordinators, Administrative Management |
| Financial | Finance Team |
| External | Scheduling, correspondence and payment providers; laboratory / imaging / external treatment services; insurers / funding organisations |

Principle: keep clinical decisions, administrative responsibilities and financial activities clearly separated.

## 3. Key requirements

- Support the end-to-end pathway (referral → booking → treatment → payment → clinic letters → enquiries) instead of fragmented email / phone / manual records.  
- Provide an audit trail for significant actions (who, when, what); audit records must not be editable by ordinary users.  
- Authenticate users and apply role-based access.  
- Integrate with external scheduling, correspondence and payment services; on failure, keep work pending/traceable and avoid duplicate bookings or charges.  
- Support pathway monitoring (outstanding referrals, delayed letters, incomplete payments/enquiries, etc.) and management reporting.  
- Allow for patient communication preferences (postal / digital / accessible formats, etc.).

## 4. Important business rules

- A New Patient Appointment may only be arranged after an authorised Consultant has accepted the referral.  
- Medical Secretaries must not assess clinical suitability or decide whether a referral is accepted.  
- Unauthorised treatment requests must not be processed by administrative staff; changes made only by email/telephone/informal means must not be processed.  
- The system must not store complete card details; appointments requiring advance payment should not normally be confirmed until payment succeeds, or an authorised exemption / funding approval / payment arrangement is recorded.  
- If payment succeeds at the provider but confirmation is not returned → mark for investigation; do not automatically request another payment.  
- Clinic Letters require Consultant approval before distribution; administrative staff must not change clinical meaning.  
- Letters incomplete/unapproved more than seven days after the appointment are delayed; escalate at about one month and three months.  
- Call handlers must not diagnose, interpret test results, recommend treatment or give clinical advice.

## 5. External services or organisations

- **Scheduling service**: find and confirm outpatient / treatment slots.  
- **Correspondence service**: letters and related patient notifications.  
- **Payment Service Provider**: payment and refund status returned to the hospital system.  
- **Laboratory / imaging / external treatment resources**: dependencies for treatment booking.  
- **Referring organisations; insurers / funding bodies**: source of referrals, missing-document requests, and funding approvals.

## 6. Group assumptions

1. For the first demo, external scheduling and payment may be mocked; the report will state the simulation boundary.  
2. Urgency rules for clinical enquiries are not fully defined in the case; leave as to-be-confirmed with the tutor — do not invent formal policy.  
3. Where working practices conflict across teams, follow the authorisation and audit requirements stated in the case.  
4. This phase prioritises the path “referral check → Consultant decision → new patient booking”; deeper reporting and complex preference handling can follow later.  
5. Audit coverage should at least include: referral decisions, clinical authorisations, letter approvals, payments/refunds, and treatment modifications.  

---

Further detail: `2026-09-14/*-分工内容.md`.
