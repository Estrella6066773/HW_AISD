# PB-12 Strategic BPMN — abstraction level

**Backlog item:** PB-12  
**First owner:** Ruby  
**Second owner:** Estrella  
**Date:** 2026-09-29  
**Model:** `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`  
**Operational model this file connects to:** `Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` (`Hospital_All_Processes_Simple_C8`)

This note explains the abstraction level of the strategic model, how each strategic activity lines up with the executable operational model, and which parts of the full case are left out of the picture.

## 1. What this model is

The file is a BPMN collaboration for the initial release. The hospital process `Strategic_Hospital_Pathway` has `isExecutable="false"`. It has no Camunda form bindings and no job-worker types. It is not a deployment file. Deploy and demonstrate `Hospital_All_Processes_Simple_C8` instead.

The picture shows the wider pathway: who receives a request, who is allowed to decide, and which outside organisations the hospital exchanges messages with. Each task is one business stage. The operational model expands that stage into user tasks, gateways, forms and workers.

## 2. Abstraction rules

1. One strategic task stands for a whole stage. It does not stand for one Camunda user task or one Java worker.
2. A rule that the case states inside a stage is written in that task's BPMN documentation, or on the message flow, instead of becoming another box.
3. The hospital uses three lanes, the same three the operational model uses: Clinical team, Administration, and Finance. Medical secretaries, outpatient bookings, treatment bookings and call handling sit in Administration. The consultant and the clinical nurse specialist sit in the Clinical team.
4. Outside participants are black-box pools. The strategic model does not draw their internal steps.
5. The opening gateway keeps three incoming kinds: referral, enquiry, and change or follow-up. The operational `RequestType` gateway splits those kinds further (for example separate admin, clinical and financial enquiries, and a reports option).
6. After the patient has attended, a parallel gateway starts two results of that attendance: the care plan, and the clinic letter. Payment does not have to finish before the consultant approves the letter. The operational model still runs those steps on one token, with the letter task before the funding task. The strategic split is the business relationship; the operational order is the executable packaging.

## 3. Pools, lanes and responsibilities

| Participant or lane | Responsibility in this model |
|---------------------|-------------------------------|
| Referring organisation | Sends referral documents. Receives requests for missing documents, rejection or redirect notices, and a copy of the clinic letter. |
| Patient or authorised representative | Receives the appointment notice and the approved clinic letter. Receives the reply to an enquiry. |
| External scheduling service | Offers a slot inside the consultant's window, or reports that no suitable slot exists. |
| External treatment, laboratory and imaging | Reports whether the requested resource is available. An unavailable resource stays pending. |
| Insurer or funding organisation | Returns the organisation, approval reference, approved amount and limits. |
| External payment service provider | Accepts a payment or refund request that does not include the card number, and returns status, reference, date and amount. |
| Administration | Checks documents, books and notifies, confirms external treatment resources, distributes the approved letter, and logs enquiries. |
| Clinical team | Decides the referral, authorises treatment, writes and approves the clinic letter, answers clinical enquiries, and authorises a change or follow-up. |
| Finance | Determines funding and payment, answers funding enquiries, and reviews a refund or a retained payment. |

Clinical staff do not approve refunds. Finance staff do not decide whether treatment is clinically necessary. Call handling answers administrative questions only; clinical questions go to the clinical lane.

## 4. How strategic activities connect to the operational model

| Strategic activity | Operational elements that expand it |
|--------------------|-------------------------------------|
| Check referral documents | `Register`, `GetDocuments` |
| Record the clinical decision | `ReviewReferral`, `ReferralDecision`, `Redirect`, `notify-referrer` |
| Notify the referrer and close | `Redirect`, `EndRejected` |
| Book the first appointment and notify the patient | `BookVisit`, `CheckVisitSlot` (`check-slot`), `send-booking-confirmation` |
| Attendance recorded | Not a separate operational gateway. The operational model continues from `BookVisit` into `ClinicalCare` and the letter tasks on one path. |
| Authorise the treatment booking | `ClinicalCare` |
| Determine funding and payment | `Funding`, `FundingOutcome`, `RequestPayment`, `PaymentReceived`, `FundingIssue`, `UrgentAuthorisation`, `mark-payment-investigate` |
| Confirm external treatment resources | `BookTreatment`, `reserve-appointment`, `flag-resource-unavailable`, `send-booking-confirmation` |
| Write and approve the clinic letter | Letter fields on `ClinicalCare`, including the revise path back to clinical care |
| Distribute the approved clinic letter | `DispatchLetter`, `dispatch-clinic-letter`, `MonitorLetters` |
| Log the enquiry and route it | `RequestType` enquiry branches, `AdminEnquiry` |
| Answer the clinical enquiry | `ClinicalEnquiry` |
| Answer the funding enquiry | `FinanceEnquiry` |
| Authorise the change or follow-up | `ClinicalChange`, `notify-care-change` |
| Review the refund or retained payment | `FinanceAdjustment`, `request-refund` |

## 5. What the strategic model collapses on purpose

These rules stay inside a stage. They are not extra boxes.

| Rule | Where the strategic model states it |
|------|--------------------------------------|
| Secretary may request missing documents and must not accept the referral | Check referral documents |
| Accept, reject, request further information, or redirect, with a reason and a decision-maker | Record the clinical decision. Reject and redirect share the close path. |
| Letter by default; telephone as well when the visit is within two weeks | Message from the booking task to the patient |
| No suitable slot stays pending and is not booked outside the clinical window | Message from the scheduling service, and the booking task text |
| No second booking when an external resource is unavailable | Confirm external treatment resources |
| Failed or unconfirmed payment is investigated and is not charged again automatically | Determine funding and payment |
| Urgent care before payment needs a clinical reason and a later finance follow-up | Determine funding and payment. It is not its own branch. |
| Seven-day letter target; escalation around one month and three months; reminders stop when the letter is sent | Distribute the approved clinic letter. The operational model records the time band on `MonitorLetters` and does not run a multi-day timer. |
| Formal change only; an urgent stop for safety can be authorised afterwards | Authorise the change or follow-up |

## 6. Gaps between the full case, this picture, and the running solution

The strategic model does not draw these, and the running solution does not implement them as enforced behaviour:

| Topic | Strategic picture | Running solution |
|-------|-------------------|------------------|
| Eight-role login and minimum access | Three lanes only | Every user task is assigned to `demo`. Acceptance test AT-03 fails on purpose. |
| Immutable audit of every significant action | Not a stage. Audit applies across stages. | Selected workers append `audit_event`. Ordinary users are not refused if they edit the database. |
| Patient identity matching | Not drawn | `patientId` is free text |
| Service-outage back-entry | Not drawn | No offline catch-up path |
| Management reports | Not drawn | `AuditReports` is a human task with a short form |
| Communication preferences | Not drawn | Forms do not capture postal, digital or accessible-format preferences |
| Chemotherapy cycle review limited to clinical staff | Not a separate stage. Folded into treatment authorisation. | `ClinicalCare` text and a free-text form; no blood-test fields and no role check |
| Urgent enquiry highlight | Not drawn | The case has not fixed the urgency rules. The form stores a priority value only. |
| Full versus partial refund amount | The finance review task does not split the amount | `finance_adjustment.form` records a coarse outcome |

External scheduling, treatment resources, funding decisions and card payment are simulated. The strategic pools name those organisations. The operational model draws a pool for the payment provider and the referrer and the patient; scheduling, laboratory, imaging and the funder appear as workers or form fields rather than as further pools.

## 7. Second-owner review

Estrella reviews before this item is marked Done.

- [ ] The three lanes can be told apart, and clinical, administrative and financial decisions are not given to the same lane.
- [ ] Referral, consultant decision, first appointment, treatment authorisation, funding and payment, clinic letter, enquiry, and change or follow-up are all on the diagram.
- [ ] Each external message matches a participant in section 3.
- [ ] The mapping in section 4 matches `Hospital_All_Processes_Simple_C8`.
- [ ] Section 6 still matches the running solution, including AT-03 recorded as Fail.
