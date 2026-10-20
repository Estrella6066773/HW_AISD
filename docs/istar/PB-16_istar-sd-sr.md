# PB-16 · i\* Strategic Dependency and Strategic Rationale Models

**Backlog item**: PB-16 · i\* SD/SR models  
**First owner**: Estrella  
**Second owner**: Ryan / Guanyan He  
**Scope**: Initial system release of the Hospital Patient Administration System  
**Date**: 2026-09-29  

**Related sources**:

- Assessment Task 02 in `W01/S03 - Assessment Introduction(1).pptx`
- Case study: `W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
- Executable-scope reference only: `Week3 Coursework/hospital-pathway/README.md` and `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn` (the deployed model; the `Hospital_All_Processes_V2.bpmn` kept in the Week3 module is an earlier copy and is no longer packaged)
- Diagram files: [`PB-16_sd.md`](PB-16_sd.md), [`PB-16_sr.md`](PB-16_sr.md), presentation figure [`PB-16_sd-overview.png`](PB-16_sd-overview.png)

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
| D5 | AdministrativeTeam | ClinicalTeam | goal | Authorised acceptance before a new patient appointment | A new patient appointment is arranged only after an authorised consultant has accepted the referral. A later follow-up appointment is requested by a clinician and is not this dependency |
| D6 | AdministrativeTeam | ClinicalTeam | resource | Authorised treatment booking request | Administrative staff must not process an unauthorised treatment request |
| D7 | AdministrativeTeam | ClinicalTeam | goal | Clinic letter clinically approved | Secretaries distribute only after consultant approval; they must not change clinical meaning |
| D8 | ClinicalTeam | AdministrativeTeam | task | Arrange clinic and treatment appointments | Bookings teams use scheduling and external clinical services after clinical authorisation |
| D9 | AdministrativeTeam | ExternalSchedulingService | resource | Available appointment slot | Outpatient and follow-up bookings use the external scheduling service |
| D10 | AdministrativeTeam | ExternalClinicalServices | resource | External treatment, laboratory or imaging availability | Some treatment appointments depend on an external provider. If that provider is unavailable, the booking stays pending and is not duplicated. Assumption A7 keeps treatment, laboratory and imaging as one dependee. Scheduling is D9 |
| D11 | AdministrativeTeam | ExternalCorrespondenceService | task | Send appointment letters and approved clinic letters | The correspondence service sends the appointment letter to the patient, and sends an approved clinic letter to the recipients the consultant named. Those recipients may include the patient, the GP, another hospital or another professional |
| D12 | Patient | ClinicalTeam | goal | Appropriate clinical assessment and care | Consultation, diagnosis, treatment options, CNS advice and fitness-to-continue decisions |
| D13 | ClinicalTeam | Patient | goal | Informed consent to treatment | Treatment proceeds only when the patient agrees and consent is recorded |
| D14 | AdministrativeTeam | FinanceTeam | goal | Normal-route clearance before treatment confirmation | Before a treatment appointment is confirmed on the normal route, Finance records hospital funding, insurer approval, verified patient payment, an exemption, or another authorised arrangement. Urgent treatment that a clinician authorises despite missing payment is D18, not a failure of D14 |
| D15 | FinanceTeam | FundingOrganisation | resource | Funding approval record | Finance records organisation, authorisation reference, amount and limitations |
| D16 | FinanceTeam | PaymentServiceProvider | resource | Verified payment or refund result | Provider returns status, transaction reference, date and amount; missing confirmation is investigated, not auto-retried as a new charge |
| D17 | Patient | FinanceTeam | goal | Charging and refunds follow the recorded rules | The patient is told when a payment fails or remains incomplete. Another attempt must not create a second charge for the same booking. A refund is made only after an authorised finance decision |
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
| Goal | Referral decision recorded | Depends on D2. The decision may be acceptance, rejection, a request for more information, or a redirect |
| Task | Submit referral with supporting documents | Provides D1 |
| Softgoal | Timely feedback on rejection, redirect or DNA | Supported via D3 |

### 6.2 Patient

| Kind | Name | Links |
|------|------|-------|
| Goal | Receive appropriate specialist care | Depends on D12 |
| Goal | Charging and refunds follow the recorded rules | Depends on D17 |
| Task | Attend or respond to appointment contacts | The patient's own response after a contact |
| Goal | Give or withhold informed consent | Provides D13 |
| Softgoal | Timely, understandable communication | Depends on D20. D11 is AdministrativeTeam's dependency on the correspondence service, not the patient's. Preferences stay in Section 8 |

### 6.3 ClinicalTeam

| Kind | Name | Links |
|------|------|-------|
| Goal | Make safe referral and treatment decisions | Uses D4; provides D2, D6 and D7. Provides D5 only when the recorded decision accepts a new patient referral |
| Goal | Clinic and treatment appointments arranged after authorisation | Depends on D8 |
| Goal | Obtain informed consent before treatment | Depends on D13 |
| Task | Review referral and record decision | Provides D2. Provides D5 only when the decision is acceptance |
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
| Goal | Keep the patient pathway moving within clinical authorisations | Uses D6 and D7 on the routes those dependencies cover |
| Goal | Authorised acceptance before a new patient appointment | From D5. Applies when the booking is a new patient appointment, not to a later follow-up |
| Task | Check referral documents and request missing items | Consumes D1; provides D4 |
| Task | Book clinic and treatment appointments | Provides D8. Clinic bookings use D9. Treatment bookings use D10. A new patient appointment also uses D5. Normal-route treatment confirmation uses D14 |
| Task | Notify patient and record contact attempts | Provides D20; uses D11 for the appointment letter |
| Task | Distribute approved clinic letters | Uses D7, and uses D11 for the clinic letter |
| Task | Route enquiries; escalate clinical matters | Uses D21 |
| Task | Communicate pathway outcome to the referrer when required | Provides D3 |
| Resource | Authorised treatment booking request | From D6 |
| Resource | Available appointment slot | From D9 |
| Resource | External treatment, laboratory or imaging availability | From D10 |
| Softgoal | No duplicate bookings when external services fail | Depends on D22 |

### 6.5 FinanceTeam

| Kind | Name | Links |
|------|------|-------|
| Goal | Record normal-route clearance before treatment confirmation | Provides D14; uses D15 and D19. Urgent treatment despite missing payment is D18 |
| Goal | Collect or refund money correctly | Uses D16; provides D17 |
| Task | Record funding approval details | Uses D15 |
| Task | Request payment or refund via the provider | Uses D16 |
| Task | Investigate missing payment confirmation without automatic re-charge | Uses D16, D23 |
| Resource | Treatment and modification context | From D19 |
| Resource | Funding approval record | From D15 |
| Resource | Verified payment or refund result | From D16 |
| Softgoal | Separate financial authority from clinical necessity decisions | Supports D18 and aligns with A6. This softgoal is not a means of the normal-route clearance goal |
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
| Resource | Verified payment or refund result | Provides D16 |

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
| D2 | ReferringOrganisation goal “Referral decision recorded” ↔ ClinicalTeam task “Review referral and record decision” |
| D3 | ReferringOrganisation softgoal “Timely feedback…” ↔ AdministrativeTeam task “Communicate pathway outcome to the referrer when required” |
| D4 | ClinicalTeam resource “Checked referral package” ↔ AdministrativeTeam task “Check referral documents…” |
| D5 | AdministrativeTeam goal “Authorised acceptance before a new patient appointment” ↔ ClinicalTeam task “Review referral and record decision”, only when that decision is acceptance |
| D6 | AdministrativeTeam resource “Authorised treatment booking request” ↔ ClinicalTeam task “Authorise treatment booking request” |
| D7 | AdministrativeTeam letter-distribution task ↔ ClinicalTeam task “Approve clinic letter content” |
| D8 | ClinicalTeam goal “Clinic and treatment appointments arranged after authorisation” ↔ AdministrativeTeam task “Book clinic and treatment appointments” |
| D9 | AdministrativeTeam resource “Available appointment slot” ↔ ExternalSchedulingService resource of the same name |
| D10 | AdministrativeTeam resource “External treatment, laboratory or imaging availability” ↔ ExternalClinicalServices resource of the same name |
| D11 | AdministrativeTeam notification/letter tasks ↔ ExternalCorrespondenceService task “Deliver outbound correspondence” |
| D12 | Patient goal “Receive appropriate specialist care” ↔ ClinicalTeam goal “Make safe referral and treatment decisions” |
| D13 | ClinicalTeam goal “Obtain informed consent…” ↔ Patient goal “Give or withhold informed consent” |
| D14 | AdministrativeTeam task “Book clinic and treatment appointments” ↔ FinanceTeam goal “Record normal-route clearance before treatment confirmation” |
| D15 | FinanceTeam resource “Funding approval record” ↔ FundingOrganisation resource of the same name |
| D16 | FinanceTeam resource “Verified payment or refund result” ↔ PaymentServiceProvider resource of the same name. The provider task “Process payment or refund” produces that resource |
| D17 | Patient goal “Charging and refunds follow the recorded rules” ↔ FinanceTeam goal “Collect or refund money correctly” |
| D18 | ClinicalTeam softgoal “Clinical work not delayed solely by payment…” ↔ FinanceTeam softgoal “Separate financial authority from clinical necessity decisions” |
| D19 | FinanceTeam resource “Treatment and modification context” ↔ ClinicalTeam authorisation/modification tasks |
| D20 | Patient depends on AdministrativeTeam task “Notify patient and record contact attempts”; the patient softgoal “Timely, understandable communication” is only partly carried by this task |
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


## 11. Ryan review record

- Reviewer: **Guanyan He (Ryan)**, second owner.
- Date: **20 October 2026**.
- Reviewed repository version: **b4e0d23**.
- Scope: the selected SD and three SR models in `Week6 Coursework/istar/` (the SD has 9 actors and 13 dependencies), checked against the dependency catalogue. This does not certify every D1-D24 dependency in the older Mermaid views.
- Decision: **Reviewed - changes requested; final approval pending.**

The selected SD matches the catalogue's names, types and directions. Corrections remain in the Finance SR (D18 must be aligned with the Quality dependency in the SD, and D14/D15/D16/D17 labels require alignment) and the Admin SR (nine Contribution links target Goals rather than Qualities; D1/D14 labels require alignment). The older five-item checklist in section 10 must be reconciled with the actual selected-view scope before it can be approved. No unchecked item above has been certified by this record.

*This section records the review as it stood on 20 October. The Admin SR part is superseded by section 12.1, where the nine links were corrected; the Finance SR part is answered in section 12.2, where the labels are found to match the catalogue's meaning; the D1/D14 label question is answered there too.*

Typed review record entered at Ryan's explicit request. SR model files and figures were not modified.


## 12. Final acceptance, 20 October 2026

- Reviewers: **Guanyan He (Ryan)**, second owner, with **Geping Chen (Estrella)** as first owner and the whole group present.
- Decision: **Accepted, with the Admin SR contribution defects corrected.**

### 12.1 Corrections applied to the Admin SR source

The nine contribution links that pointed at goals were rewritten in `Week6 Coursework/istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.txt`. The metamodel requires a contribution link to target a soft goal, and the group's own Clinical and Finance SRs use that form throughout; the Admin SR was the exception.

Five of the nine became valid by typing the top aspiration as a quality. **`Patient pathway coordinated` changed from Goal to Quality.** Nothing refined into it and no dependency targeted it, so the retyping broke no decomposition, and the five node-level links that pointed at it now point at a soft goal.

The other four were not contribution links at all, and changing their target alone would have left them describing the relationship wrongly:

| Link | Was | Now | Why |
|---|---|---|---|
| `Clinical acceptance obtained (if initial visit)` | contribution to `Initial / follow-up visit arranged…` | **AND-refinement** of the same goal | clinical acceptance is a part of arranging the visit, not a soft goal it serves |
| `Appointment slot [X]` | contribution to `Initial / follow-up visit arranged…` | **needed-by** `Book visit; record contact / attendance [M/P]` | the slot is a resource the booking task consumes |
| `Normal-route clearance / arrangement obtained` | contribution to `Treatment booking coordinated` | **AND-refinement** of the same goal | clearance is a part of coordinating the booking |
| `Treatment resources [X/M]` | contribution to `Treatment booking coordinated` | **needed-by** `Record treatment booking outcome [M/P]` | the funded resource is what the recording task consumes |

The file now holds 8 contribution links, every one targeting a quality; and 7 AND-refinement and 5 needed-by links, every one targeting a goal or a task. Nothing else in the source was touched: the diff is 8 lines, 4 link types and 1 node type.

**The PNG has not been re-exported.** `PB-16_V1_Admin_SR_reviewed_2026-10-19.png` still shows the old arrows and does not match the source it is named after. The group re-exports it from piStar; until that is done the figure and the source disagree.

### 12.2 Finance SR: reviewed against the catalogue and left as designed

Section 11 asked for the Finance SR labels to be aligned. Read against the catalogue in section 5, none of the four is a metamodel defect, and the group is not changing them. The reasons differ, so they are separated here rather than dismissed together.

**D18 is a deliberate service-view slice, not a mistake.** The catalogue types D18 as a softgoal, "Urgent care not blocked solely by payment delay". The Finance SR renders it as `Clinical team` depending on the Finance task `Follow up after urgent care [M/P]`; the model's own `Qualification` for that dependency records why: the aspiration belongs to the clinical boundary, and carrying it inside Finance would make Finance look as though it owned the authorisation of urgent treatment. The softgoal is present where it belongs, in the Clinical SR, as `Clinical work not delayed solely by payment confirmation gaps` → `Finance`. Retargeting D18 at a quality in the Finance view would put a clinical softgoal into a service view that has no claim to it, so the reading is correct as drawn and the type difference from the catalogue is the price of it.

**D17 is an addition, not a mismatch.** The piStar SD diagram draws 13 of the 24 catalogued dependencies and D17 is not among them; the Finance SR restores it, which is what brings the patient into this view. Its dependum is the Finance goal `Funding and payment managed` rather than the catalogue's narrower "Charging and refunds follow the recorded rules" — broader than the catalogue, not narrower, and therefore not a misstatement. Section 11's wording, "the `D14`–`D17` labels differ from the SD", cannot apply to D17 at all: the SD has no D17 to differ from.

**D14, D15 and D16 differ in wording only.** Each keeps the catalogue's depender, dependee and direction, and each carries its case basis and qualification in `customProperties`. A reader comparing the labels side by side will see different wording for the same dependency; a reader following the edge will find the same dependency.

**On the ids.** D14, D15 and D16 keep the same id in the SD and in this SR. D18 does not, but it also does not in the Clinical SR, which shares `648f5d89…` with the Finance SR against the SD's `40a913f4…`. Making the Finance id match the SD would break the Finance–Clinical pair instead, so the ids are left as they are. No link in the file resolves to a missing node: all 28 resolve, and all four contribution links target a quality.

That is the difference between this item and the Admin SR. There, nine contribution links pointed at goals, which the metamodel forbids; here every link is of a permitted type. **The Finance figure therefore still matches its source**, and unlike the Admin figure it was not invalidated by any change.

The Admin SR `D1` and `D14` label wording is unchanged: the correction in section 12.1 touched the nine contribution links and one node type, nothing else. That one is a wording question only, and is left for the next revision.

This acceptance is therefore an acceptance of the SD and the Clinical and Finance SRs as they stand, and of the Admin SR after the correction above. Item 2 of the section 10 checklist remains uncertified, as it was in section 11: the piStar sources cover 16 of the 24 catalogued dependencies and `D3, D11, D13, D19, D21, D22, D23, D24` do not appear in them. The five boxes in section 10 are left unticked for that reason; this record does not tick them.
