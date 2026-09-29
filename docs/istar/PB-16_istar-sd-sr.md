# PB-16 · i\* Strategic Dependency and Strategic Rationale Models

**Backlog item**: PB-16 · i\* SD/SR models  
**First owner**: Estrella  
**Second owner**: Ryan / Guanyan He  
**Scope**: Initial system release of the Hospital Patient Administration System  
**Date**: 2026-09-29  

**Related sources**:

- Assessment Task 02 in `W01/notes/S03 - Assessment Introduction.md`
- Case study: `W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
- Executable-scope reference only: `Coursework/hospital-pathway/README.md` and `Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`
- Diagram files: [`PB-16_sd.md`](PB-16_sd.md), [`PB-16_sr.md`](PB-16_sr.md)

---

## 1. Purpose

This document presents the i\* (pronounced “i star”) models for the initial release. i\* is a socio-technical modelling language. The SD (Strategic Dependency) model shows which actor depends on which other actor for what. The SR (Strategic Rationale) model expands each actor’s internal goals, softgoals, tasks and resources, and shows how those elements justify the dependencies in the SD model.

The assessment requires the team to identify key actors, goals, softgoals, tasks, resources and dependencies; to explain modelling choices and assumptions; and to keep the SD and SR models consistent with each other.

---

## 2. Modelling choices

1. **Abstraction for the initial release.** Actors are grouped by strategic responsibility rather than by every named job title in the case. Medical Secretaries, Outpatient Bookings, Treatment and Chemotherapy Bookings, Call Handling, Patient Pathway Coordinators and Administrative Management appear together as `AdministrativeTeam`. Consultants, the Clinical Nurse Specialist Team and other authorised clinical professionals appear together as `ClinicalTeam`. Distinct external services remain separate actors because their failure modes and dependums differ.
2. **Five dependency kinds required by PB-16.** The SD model includes dependencies that involve the referring organisation, clinical actors, administrative actors, financial actors and external organisations. Patient and the Hospital Patient Administration System are also modelled because the case centres on patient pathway coordination.
3. **Dependum types.** Each SD edge is labelled with one i\* dependum type: goal, softgoal, task or resource.
4. **Executable BPMN is not the strategic model.** The Camunda pathway is used only to confirm which pathway stages the initial release intends to support. It does not replace SD/SR, and classroom mocks (external scheduling, payment, correspondence) are stated as assumptions rather than as real external capability.
5. **Capabilities not promised in this release.** Management reports, identity de-duplication, patient communication preferences and offline catch-up recording are listed in Section 8 as out of scope for this SR, even where the case mentions them.

---

## 3. Assumptions

| ID | Assumption |
|----|------------|
| A1 | The initial release supports the main referral-to-treatment pathway: referral check, consultant decision, clinic booking, treatment authorisation, funding determination, payment handling (including failure and missing confirmation), formal treatment modification with finance follow-up, clinic-letter administration, and enquiry routing. |
| A2 | External scheduling and payment interfaces are simulated in the classroom implementation. The i\* models still treat the external organisations as real dependees; the simulation is an implementation boundary, not a denial of the dependency. |
| A3 | Role-based login enforcement is a backlog requirement (PB-22) and is **not** treated as an already delivered capability in this SR. The models record the softgoal of role-appropriate access; they do not claim that forced authentication is implemented. |
| A4 | Ordinary users must not be able to alter audit records of significant actions. Achieving immutable audit storage in production may exceed the classroom store; the softgoal remains. |
| A5 | The hospital has not finished a full urgency rule set for clinical enquiries. The models require urgent clinical concerns to be escalated to clinical staff; they do not invent a complete grading policy. |
| A6 | Clinical decisions, administrative execution and financial approval remain separate. No administrative or finance actor may accept a referral, authorise treatment or approve a refund without the authority the case assigns to that role. |
| A7 | “ExternalClinicalServices” groups external treatment, laboratory and imaging providers that supply availability for treatment bookings. |
| A8 | The same actor set and the same assumptions A1–A8 apply to both the SD and the SR models. |

---

## 4. Actors

| Actor ID | Actor name | Category for PB-16 coverage | Rationale |
|----------|------------|-------------------------------|-----------|
| RO | ReferringOrganisation | Referring organisation | General Practitioner or other hospital that submits the referral and may need outcome information |
| PT | Patient | Stakeholder (patient pathway) | Receives care, appointments, letters, charges and clinical advice |
| CL | ClinicalTeam | Clinical | Consultant and authorised clinical professionals who decide referrals, care, letters and modifications |
| AD | AdministrativeTeam | Administrative | Secretaries, bookings, call handling and pathway coordination that execute non-clinical pathway work |
| FI | FinanceTeam | Financial | Funding determination, payment requests, refunds and finance enquiries |
| ESS | ExternalSchedulingService | External organisation | Supplies appointment slots for outpatient and related bookings |
| ECS | ExternalClinicalServices | External organisation | Supplies external treatment, laboratory or imaging availability |
| ECSND | ExternalCorrespondenceService | External organisation | Delivers approved letters and related outbound correspondence |
| PSP | PaymentServiceProvider | External organisation | Processes payment and refund transactions and returns verified results |
| FO | FundingOrganisation | External organisation | Insurer or funding body that issues funding approvals |
| HPAS | HospitalPatientAdministrationSystem | Socio-technical system | Coordinates pathway work, records decisions and mediates external requests |

---

## 5. SD dependency catalogue

Reading rule: **Depender** depends on **Dependee** for the **dependum**. Every row below appears in [`PB-16_sd.md`](PB-16_sd.md) and is mirrored in [`PB-16_sr.md`](PB-16_sr.md).

| ID | Depender | Dependee | Type | Dependum | Case basis (summary) |
|----|----------|----------|------|----------|----------------------|
| D1 | AdministrativeTeam | ReferringOrganisation | resource | Supporting referral documents | Secretaries check letters, results and reports; may request missing items from the referrer |
| D2 | ReferringOrganisation | ClinicalTeam | goal | Referral decision recorded | Consultant accepts, rejects, requests further information or redirects; reason and identity are recorded |
| D3 | ReferringOrganisation | AdministrativeTeam | task | Communicate pathway outcome to referrer when required | Reject, redirect, DNA or discharge pathways may require the referrer to be informed |
| D4 | ClinicalTeam | AdministrativeTeam | resource | Checked referral package | Clinical review starts after administrative document checking |
| D5 | AdministrativeTeam | ClinicalTeam | goal | Authorised referral acceptance | New Patient Appointment may be arranged only after authorised acceptance |
| D6 | AdministrativeTeam | ClinicalTeam | resource | Authorised treatment booking request | Administrative staff must not process an unauthorised treatment request |
| D7 | AdministrativeTeam | ClinicalTeam | goal | Clinic letter clinically approved | Secretaries distribute only after consultant approval; they must not change clinical meaning |
| D8 | ClinicalTeam | AdministrativeTeam | task | Arrange clinic and treatment appointments | Bookings teams use scheduling and external clinical services after clinical authorisation |
| D9 | AdministrativeTeam | ExternalSchedulingService | resource | Available appointment slot | Outpatient and follow-up bookings use the external scheduling service |
| D10 | AdministrativeTeam | ExternalClinicalServices | resource | External treatment, laboratory or imaging availability | Some treatment appointments depend on external providers; outages leave bookings pending without duplicates |
| D11 | AdministrativeTeam | ExternalCorrespondenceService | task | Send outbound patient correspondence | Appointment letters and approved clinic letters go through approved channels |
| D12 | Patient | ClinicalTeam | goal | Appropriate clinical assessment and care | Consultation, diagnosis, treatment options, CNS advice and fitness-to-continue decisions |
| D13 | ClinicalTeam | Patient | goal | Informed consent to treatment | Treatment proceeds only when the patient agrees and consent is recorded |
| D14 | AdministrativeTeam | FinanceTeam | goal | Funding or payment cleared before confirmation | Treatment appointments that need advance payment are not normally confirmed until funding, payment, exemption or arrangement is recorded |
| D15 | FinanceTeam | FundingOrganisation | resource | Funding approval record | Finance records organisation, authorisation reference, amount and limitations |
| D16 | FinanceTeam | PaymentServiceProvider | resource | Verified payment or refund result | Provider returns status, transaction reference, date and amount; missing confirmation is investigated, not auto-retried as a new charge |
| D17 | Patient | FinanceTeam | goal | Fair charging and refund handling | Patient is notified of failed or incomplete payment; refunds follow authorised finance decisions |
| D18 | ClinicalTeam | FinanceTeam | softgoal | Urgent care not blocked solely by payment delay | Clinicians may authorise urgent treatment with a recorded reason; Finance resolves afterwards |
| D19 | FinanceTeam | ClinicalTeam | resource | Treatment and modification context for charges | Finance needs the clinical treatment or modification facts to decide funding, payment or refund |
| D20 | Patient | AdministrativeTeam | task | Recorded appointment notification and contact attempts | Letters plus telephone contact within two weeks; each attempt and outcome is recorded |
| D21 | AdministrativeTeam | ClinicalTeam | task | Handle escalated clinical enquiry | Call handlers must not diagnose or advise; clinical enquiries go to CNS or authorised clinicians |
| D22 | AdministrativeTeam | HospitalPatientAdministrationSystem | softgoal | Traceable pathway without duplicate bookings | System supports pending bookings, retries and pathway visibility without inventing duplicate appointments |
| D23 | FinanceTeam | HospitalPatientAdministrationSystem | softgoal | Auditable payment trail without full card storage | System must not store complete card numbers; significant payment actions remain auditable |
| D24 | ClinicalTeam | HospitalPatientAdministrationSystem | softgoal | Recorded clinical authorisations for ordinary-user immutability | Referral decisions, treatment authorisations, letter approvals and modifications are recorded so ordinary users cannot alter them |

**Dependency count**: 24.

Coverage of the five PB-16 kinds:

| Kind | Example dependency IDs |
|------|------------------------|
| Referring organisation | D1, D2, D3 |
| Clinical | D2, D4–D8, D12, D13, D18, D19, D21, D24 |
| Administrative | D1, D3–D11, D14, D20–D22 |
| Financial | D14–D19, D23 |
| External organisations | D9–D11, D15, D16 |

---

## 6. Goals, softgoals, tasks and resources by actor

Elements below are the SR vocabulary. Softgoals that the initial release does **not** commit to delivering as product features are listed again in Section 8.

### 6.1 ReferringOrganisation

| Kind | Name | Links |
|------|------|-------|
| Goal | Patient accepted onto an appropriate specialist pathway | Contributes to D2 |
| Task | Submit referral with supporting documents | Provides D1 |
| Softgoal | Timely feedback on rejection, redirect or DNA | Supported via D3 |

### 6.2 Patient

| Kind | Name | Links |
|------|------|-------|
| Goal | Receive appropriate specialist care | Depends on D12 |
| Goal | Fair and clear charging | Depends on D17 |
| Task | Attend or respond to appointment contacts | Supports D20 |
| Goal | Give or withhold informed consent | Provides D13 |
| Softgoal | Timely, understandable communication | Partially via D11, D20; preferences deferred (Section 8) |

### 6.3 ClinicalTeam

| Kind | Name | Links |
|------|------|-------|
| Goal | Make safe referral and treatment decisions | Uses D4; provides D2, D5, D6, D7 |
| Goal | Obtain informed consent before treatment | Depends on D13 |
| Task | Review referral and record decision | Provides D2, D5 |
| Task | Authorise treatment booking request | Provides D6 |
| Task | Approve clinic letter content | Provides D7 |
| Task | Respond to escalated clinical enquiries | Provides D21 |
| Task | Authorise treatment modification when care must change | Feeds D19 |
| Resource | Checked referral package | From D4 |
| Softgoal | Clinical work not delayed solely by payment confirmation gaps | Depends on D18 |
| Softgoal | Clinical authorisations remain recorded and protected from ordinary alteration | Depends on D24 |

### 6.4 AdministrativeTeam

| Kind | Name | Links |
|------|------|-------|
| Goal | Keep the patient pathway moving within clinical authorisations | Uses D5, D6, D7, D14 |
| Task | Check referral documents and request missing items | Consumes D1; provides D4 |
| Task | Book clinic and treatment appointments | Provides D8; uses D9, D10 |
| Task | Notify patient and record contact attempts | Provides D20; uses D11 |
| Task | Distribute approved clinic letters | Uses D7, D11 |
| Task | Route enquiries; escalate clinical matters | Uses D21 |
| Resource | Authorised referral acceptance | From D5 |
| Resource | Authorised treatment booking request | From D6 |
| Resource | Available appointment slot | From D9 |
| Resource | External clinical service availability | From D10 |
| Softgoal | No duplicate bookings when external services fail | Depends on D22 |

### 6.5 FinanceTeam

| Kind | Name | Links |
|------|------|-------|
| Goal | Determine funding before treatment confirmation | Provides D14; uses D15, D19 |
| Goal | Collect or refund money correctly | Uses D16; provides D17 |
| Task | Record funding approval details | Uses D15 |
| Task | Request payment or refund via the provider | Uses D16 |
| Task | Investigate missing payment confirmation without automatic re-charge | Uses D16, D23 |
| Resource | Treatment and modification context | From D19 |
| Resource | Funding approval record | From D15 |
| Resource | Verified payment or refund result | From D16 |
| Softgoal | Separate financial authority from clinical necessity decisions | Aligns with A6 |
| Softgoal | Auditable payments without storing full card data | Depends on D23 |

### 6.6 ExternalSchedulingService

| Kind | Name | Links |
|------|------|-------|
| Resource | Available appointment slot | Provides D9 |
| Softgoal | Return availability reliably enough for pending/retry handling | Supports D22 |

### 6.7 ExternalClinicalServices

| Kind | Name | Links |
|------|------|-------|
| Resource | External treatment, laboratory or imaging availability | Provides D10 |
| Softgoal | Signal unavailability so bookings stay pending without duplicates | Supports D22 |

### 6.8 ExternalCorrespondenceService

| Kind | Name | Links |
|------|------|-------|
| Task | Deliver outbound correspondence | Provides D11 |

### 6.9 PaymentServiceProvider

| Kind | Name | Links |
|------|------|-------|
| Task | Process payment or refund | Supports D16 |
| Resource | Verified transaction result | Provides D16 |

### 6.10 FundingOrganisation

| Kind | Name | Links |
|------|------|-------|
| Resource | Funding approval record | Provides D15 |

### 6.11 HospitalPatientAdministrationSystem

| Kind | Name | Links |
|------|------|-------|
| Goal | Coordinate referral, booking, funding, payment and letter stages | Supports D22–D24 |
| Softgoal | Traceable pathway without duplicate bookings | Anchors D22 |
| Softgoal | Auditable payment trail without full card storage | Anchors D23 |
| Softgoal | Recorded clinical authorisations with ordinary-user immutability | Anchors D24 |
| Softgoal | Role-appropriate access (requirement acknowledged; enforcement not claimed delivered) | See A3 and Section 8 |

---

## 7. SD–SR corroboration table

Every SD dependency must appear in the SR. The table maps each dependency to the SR location that carries it.

| SD ID | SR location (actor internal element ↔ dependum) |
|-------|--------------------------------------------------|
| D1 | AdministrativeTeam task “Check referral documents…” ↔ ReferringOrganisation task “Submit referral with supporting documents” |
| D2 | ReferringOrganisation goal “Patient accepted onto an appropriate specialist pathway” ↔ ClinicalTeam task “Review referral and record decision” |
| D3 | ReferringOrganisation softgoal “Timely feedback…” ↔ AdministrativeTeam pathway-outcome communication tasks |
| D4 | ClinicalTeam resource “Checked referral package” ↔ AdministrativeTeam task “Check referral documents…” |
| D5 | AdministrativeTeam resource “Authorised referral acceptance” ↔ ClinicalTeam goal/task for referral acceptance |
| D6 | AdministrativeTeam resource “Authorised treatment booking request” ↔ ClinicalTeam task “Authorise treatment booking request” |
| D7 | AdministrativeTeam letter-distribution task ↔ ClinicalTeam task “Approve clinic letter content” |
| D8 | ClinicalTeam care goals ↔ AdministrativeTeam task “Book clinic and treatment appointments” |
| D9 | AdministrativeTeam resource “Available appointment slot” ↔ ExternalSchedulingService resource of the same name |
| D10 | AdministrativeTeam resource “External clinical service availability” ↔ ExternalClinicalServices resource |
| D11 | AdministrativeTeam notification/letter tasks ↔ ExternalCorrespondenceService task “Deliver outbound correspondence” |
| D12 | Patient goal “Receive appropriate specialist care” ↔ ClinicalTeam goal “Make safe referral and treatment decisions” |
| D13 | ClinicalTeam goal “Obtain informed consent…” ↔ Patient goal “Give or withhold informed consent” |
| D14 | AdministrativeTeam goal “Keep the patient pathway moving…” ↔ FinanceTeam goal “Determine funding before treatment confirmation” |
| D15 | FinanceTeam resource “Funding approval record” ↔ FundingOrganisation resource of the same name |
| D16 | FinanceTeam resource “Verified payment or refund result” ↔ PaymentServiceProvider resource/task |
| D17 | Patient goal “Fair and clear charging” ↔ FinanceTeam goal “Collect or refund money correctly” |
| D18 | ClinicalTeam softgoal “Clinical work not delayed solely by payment…” ↔ FinanceTeam separation-of-duties softgoal and urgent-care follow-up |
| D19 | FinanceTeam resource “Treatment and modification context” ↔ ClinicalTeam authorisation/modification tasks |
| D20 | Patient softgoal for timely communication ↔ AdministrativeTeam task “Notify patient and record contact attempts” |
| D21 | AdministrativeTeam task “Route enquiries…” ↔ ClinicalTeam task “Respond to escalated clinical enquiries” |
| D22 | AdministrativeTeam softgoal “No duplicate bookings…” ↔ HospitalPatientAdministrationSystem softgoal “Traceable pathway without duplicate bookings” |
| D23 | FinanceTeam softgoal “Auditable payments without storing full card data” ↔ HospitalPatientAdministrationSystem softgoal of the same intent |
| D24 | ClinicalTeam softgoal “Clinical authorisations remain recorded…” ↔ HospitalPatientAdministrationSystem softgoal “Recorded clinical authorisations…” |

Diagram cross-check: open [`PB-16_sd.md`](PB-16_sd.md) and [`PB-16_sr.md`](PB-16_sr.md) and confirm each `D1`–`D24` label appears in both files.

---

## 8. Explicitly out of scope for this SR (initial release)

These topics appear in the case or backlog but are **not** modelled as committed initial-release capabilities inside the SR graphs:

| Topic | Why excluded from this SR as a committed capability |
|-------|-----------------------------------------------------|
| Management reports (volumes, waiting times, pathway dashboards) | P2 backlog item; not promised as delivered capability for the initial-release SR |
| Patient identity de-duplication across organisations | Case concern; initial release does not claim a dedicated identity-matching capability |
| Patient communication preferences (postal vs digital, accessible formats, representatives) | P2 backlog; conflicting preferences remain unresolved hospital practice |
| Offline catch-up recording after system or external-service outage | Case mentions the need; initial release does not commit a full offline catch-up procedure |
| Forced role-based login enforcement | Required by the case and by PB-22; classroom pathway currently assigns demo tasks without mandatory role login. Softgoal is acknowledged; delivery is not claimed |

External scheduling and payment remain real strategic dependees (D9, D16) even though the classroom workers simulate them.

---

## 9. Consistency statement

- The SD and SR models use the same eleven actors and the same assumptions A1–A8.
- Every dependency D1–D24 in the SD catalogue appears in Section 7 and in the SR Mermaid diagrams.
- Softgoals that are requirements but not yet enforced in the classroom build are labelled as such (especially role-based login under A3).

---

## 10. Second-owner review

Second owner: **Ryan / Guanyan He**. Items below are left unchecked for human review.

- [ ] Second owner confirms the actor set matches the case and the initial-release boundary
- [ ] Second owner confirms every SD dependency D1–D24 appears in the SR diagrams
- [ ] Second owner confirms out-of-scope items in Section 8 match the agreed release boundary
- [ ] Second owner confirms the models do not claim forced role login as already implemented
- [ ] Second owner confirms Mermaid diagrams render and edge labels remain readable
