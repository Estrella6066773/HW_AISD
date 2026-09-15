# Part 1 Discussion Notes

> Meeting summary  
> **Topic**: Case Study — Hospital Patient Referral, Treatment and Administration System  
> **Date**: 2026-09-14  
> **Attendees**:  
> - A: Hao Zheng (Ruby Zheng, 23084382)  
> - B: Geping Chen (Estrella Chen, 23084393)  
> - C: Minghao Qin (Ender Qin, 23084402)  
> - D: Guanyan He (HeGuanYan He, 23084395)  

---

## Meeting overview

The group reviewed Part 1 against the case study text. The patient pathway starts when a patient is referred by a General Practitioner or another hospital, then continues through consultation, diagnosis, treatment, follow-up care and ongoing communication. Information is currently moved through existing hospital systems, electronic forms, emails, telephone calls, letters and manually maintained records, which makes it hard to monitor progress, identify delays and keep a complete audit trail. The hospital therefore intends to introduce a Hospital Patient Administration System.

---

## Contributions

### A · Hao Zheng (Ruby Zheng)
1. Main pathway from the case: Medical Secretaries receive and check the referral → Consultant accepts / rejects / requests further information / redirects → a New Patient Appointment only after acceptance → authorised Treatment Booking Request after consent → treatment booking and funding/payment → Clinic Letter → enquiry routing.  
2. Teams must keep a clear distinction between clinical decisions, administrative responsibilities and financial activities.

### B · Geping Chen (Estrella Chen)
1. Main participants include Medical Secretaries, the Outpatient Bookings Team, the Call Handling Team, the Clinical Nurse Specialist Team and its Administrative Support Team, the Treatment and Chemotherapy Bookings Team, Patient Pathway Coordinators, Consultants, the Finance Team and the Administrative Management Team, plus patients and referring organisations.  
2. Key rules: Medical Secretaries must not assess clinical suitability or decide acceptance; the reason and decision-maker must be recorded; unauthorised treatment requests must not be processed by administrative staff; call handlers must not diagnose, interpret test results, recommend treatment or give clinical advice.

### C · Minghao Qin (Ender Qin)
1. Key needs: support the full pathway and team coordination; auditable significant actions; role-based access; integration with external scheduling, correspondence and payment; visibility of backlogs, delayed letters, incomplete payments and unresolved enquiries.  
2. The case states that urgency rules for clinical concerns are not yet fully agreed; this needs further investigation with stakeholders (tutors) and documented assumptions.

### D · Guanyan He (HeGuanYan He)
1. External services/organisations: external scheduling, correspondence, Payment Service Provider, and external treatment / laboratory / imaging services; also referring organisations and insurers / funding organisations.  
2. Exception handling: if an external service is unavailable, keep the booking pending and avoid duplicates; if payment is taken but confirmation is missing, mark for investigation rather than charging again; treatment changes require an authorised Treatment Modification Request — email/telephone/informal requests must not be processed.

---

## Actions

| Action | Owner |
|--------|--------|
| Finalise the Part 1 case summary | Whole group (see `part1-case-summary.md` / `part1案例摘要.md`) |
| Confirm urgency rules for clinical enquiries | To ask tutor |
| Document mock boundary for scheduling/payment in this phase | Minghao Qin / Guanyan He |
