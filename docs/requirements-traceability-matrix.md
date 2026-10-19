# Requirements Traceability Matrix

> **Provenance**: first written on 2026-09-14 as `docs/requirements/traceability-matrix.md`, in the initial repository skeleton (commit `c8da046`); deleted in commit `3d114fa`; restored from history on 2026-09-16 into `docs/`. Paths inside follow the repository layout of that time; the current layout is in the root `README.md`. The BR numbers are used in this file only.

> **Purpose**: Trace each requirement across the entire development lifecycle — from the strategic process model, through the operational BPMN, down to the actual implementation. This is a **grading criterion** (BPM&EA Task 3).
>
> **Current status (2026-10-19)**: the grades in section 2 are the 29 September snapshot and are left as written. Section 4 is the refreshed second-release position: **13 Supported / 25 Partial / 4 Unsupported**.
>
> **Status Legend**:
> - ✅ **Supported** — The requirement is fully addressed in this deliverable
> - ⚠️ **Partial** — Partially addressed; limitations documented in Notes
> - ❌ **Unsupported** — Not addressed; justify why and how it will be handled in a later release

---

## 1. Business Requirements (from Case Study)

| Req ID | Requirement Description (abbreviated) | Case Study Source Para |
|--------|--------------------------------------|------------------------|
| BR-01 | Medical Secretaries verify referral documents and request missing info | Para 3 |
| BR-02 | Consultant accepts / rejects / redirects referral with mandatory reason + author ID | Para 4 |
| BR-03 | Outpatient Bookings Team arranges appointment via external scheduler | Para 5 |
| BR-04 | Patient notified by letter; phone call if appointment within 2 weeks | Para 5 |
| BR-05 | Each contact attempt and outcome recorded; unanswered / wrong number / alternative request | Para 6 |
| BR-06 | Urgent referral handling (skip normal timescales) | Para 6 |
| BR-07 | No suitable appointment within Consultant-requested period → highlight/refer | Para 6 |
| BR-08 | Consultant records patient consent + authorises Treatment Booking Request | Para 7 |
| BR-09 | Unauthorised Treatment Booking Request blocked from admin processing | Para 7 |
| BR-10 | Treatment Bookings Team coordinates with external treatment / lab / imaging / scheduling services | Para 8 |
| BR-11 | Pending booking + notification if external service unavailable; no duplicates | Para 8 |
| BR-12 | Funding determination: hospital / approved insurer / patient pays | Para 9 |
| BR-13 | Finance Team records funding org, ref, amount, limitations | Para 9 |
| BR-14 | Secure payment request to Payment Service Provider; no card storage | Para 10 |
| BR-15 | Payment returned: status, transaction ref, date, amount | Para 10 |
| BR-16 | Treatment appointment not confirmed until payment complete (or exemption/funding/arrangement) | Para 11 |
| BR-17 | Payment failure notification + re-attempt without duplicate booking or charge | Para 11 |
| BR-18 | Orphaned payment (provider success, no confirmation) → mark for investigation | Para 12 |
| BR-19 | Urgent treatment bypass (no confirmed payment) with recorded reason + Finance referral | Para 12 |
| BR-20 | Authorised Finance member decides refund (full / partial) | Para 13 |
| BR-21 | Financial vs clinical responsibilities separated (clinical ≠ finance decisions) | Para 13 |
| BR-22 | Treatment Modification Request: only via system, authorisation required | Para 15 |
| BR-23 | Urgent treatment postponement (patient safety) + retrospective clinician authorisation | Para 15 |
| BR-24 | Treatment modifications affecting finances → Finance Team review | Para 15 |
| BR-25 | Chemotherapy cycle review + blood test; clinical decision only | Para 14 |
| BR-26 | Call Handling Team classifies enquiry: admin / financial / clinical | Para 17 |
| BR-27 | Call handlers may NOT diagnose, interpret results, recommend treatment | Para 19 |
| BR-28 | Every enquiry recorded, classified, prioritised, routed → full audit trail | Para 20 |
| BR-29 | Urgent clinical enquiry highlighted immediately | Para 20 |
| BR-30 | Consultant writes Clinic Letter; approves before distribution | Para 21 |
| BR-31 | Medical Secretaries process/distribute; may fix admin errors but NOT clinical content | Para 22 |
| BR-32 | 7-day completion target for Clinic Letters | Para 23 |
| BR-33 | Delayed letter monitoring: 7 days → 1 month → 3 months escalation chain | Para 24-25 |
| BR-34 | No duplicate reminders after letter completed; valid delay reasons recorded | Para 26 |
| BR-35 | Follow-up appointment booking; highlight if outside requested timeframe | Para 27 |
| BR-36 | Cancellation / reschedule / DNA recording + pathway decision + Finance referral (if paid) | Para 28 |
| BR-37 | Role-based access control; staff only sees role-required info | Para 29 |
| BR-38 | Immutable audit records: user + date/time + action | Para 30 |
| BR-39 | Patient ID deduplication to prevent wrong-association | Para 30 |
| BR-40 | System availability for time-sensitive work; unavailability fallback procedure | Para 30 |
| BR-41 | Management reports: referral volumes, waiting times, delays, KPIs | Para 31 |
| BR-42 | Patient communication preferences respected (postal / digital / accessible formats) | Para 32 |

---

## 2. Traceability Matrix — Initial Release

> Evidence baseline: operational BPMN `Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`; forms under `Week3 Coursework/hospital-pathway/forms/`; JobWorkers under `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/`; acceptance evidence `Ryan/2026-09-26/PB-14_acceptance-test-plan_2026-09-29.md` and `Ryan/2026-09-26/PB-18_acceptance-test-plan_2026-09-29.md`. Strategic BPMN: `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` with notes `docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md`. Every user task is assigned to `demo`.

| Req ID | **Strategic BPMN** (docs/strategic-bpmn/) | **Operational BPMN** (executable W02) | **Implementation** (forms/ + JobWorkers) | **Acceptance tests** | **Initial Release Status** | **Notes** |
|--------|------------------------------------------|----------------------------------------|------------------------------------------|----------------------|---------------------------|-----------|
| BR-01 | ✅ Check referral documents; message asks the referrer for missing documents | ✅ Supported — `Register` (document check) and `GetDocuments` (missing material); gateway `RequestType` for `referral_incomplete` | ⚠️ Partial — `register_request.form` (documents checked / missing); `simple_record.form` on `GetDocuments`; no outbound referrer request | AT-01, AT-02 cover the documents-checked path; missing-documents branch has no acceptance test | ⚠️ Partial | Classroom completes `GetDocuments` to simulate a reply; there is no real message wait or correspondence integration. |
| BR-02 | ✅ Record the clinical decision; reject and redirect share Notify the referrer and close | ✅ Supported — `ReviewReferral`, gateways `ReferralDecision` (accept / reject / redirect / more_information), `Redirect`, service task `NotifyReferrer` | ✅ Supported — `review_referral.form` captures `clinicianId`, decision and mandatory `decisionReason`; worker `notify-referrer` records redirect notification in `audit_event` | AT-01 (accept), AT-02 (reject); redirect path has no acceptance test | ✅ Supported | Accept/reject with reason and clinician identity are proven. Role enforcement that only a Consultant may accept is BR-37 / AT-03 Fail, not this rule. |
| BR-03 | ✅ Book the first appointment; messages to and from External scheduling service | ✅ Supported — `BookVisit` then service task `CheckVisitSlot` (`check-slot`) before `VisitOutcome` | ✅ Supported — `book_visit.form`; worker `check-slot` writes `booking_slot` (classroom mock of external scheduling) | AT-01 | ✅ Supported | Slot check is a local mock worker, not a live hospital scheduler (`Week3 Coursework/hospital-pathway/README.md`). |
| BR-04 | ✅ Booking message: appointment letter, and telephone when the visit is within two weeks | ⚠️ Partial — `BookVisit` documentation requires letter and, within two weeks, telephone; classroom completion stands in for elapsed correspondence | ⚠️ Partial — `book_visit.form` free-text notes only; no letter/phone workers or structured contact fields | no acceptance test (AT-01 notes mention letter/phone but do not assert them) | ⚠️ Partial | Notification channels are documented on the task, not implemented as separate send tasks. |
| BR-05 | ⚠️ Partial — contact outcomes stay inside the booking task; each outcome is not its own box | ⚠️ Partial — `BookVisit` documentation requires each contact attempt and outcome to be recorded | ⚠️ Partial — outcomes are free-text in `book_visit.form` notes; no structured attempt list | no acceptance test | ⚠️ Partial | Contact outcomes are not modelled as discrete variables. |
| BR-06 | ⚠️ Partial — urgent referrals are not a separate skip-timescale path | ⚠️ Partial — `Register` / `ReviewReferral` documentation pass urgent referrals and timeframes to booking; no dedicated skip-timescale gateway or timer | ⚠️ Partial — `register_request.form` Priority includes Urgent and Two-week wait; no automatic timescale override | no acceptance test | ⚠️ Partial | Urgency is captured as data; normal administrative timescales are not automatically shortened. |
| BR-07 | ✅ Scheduling message: slot offered, or no suitable slot; booking task forbids a silent out-of-window booking | ✅ Supported — `BookVisit` outcome pending loops via `VisitOutcome` back to booking; documentation requires highlight / pathway referral and no silent out-of-window booking | ✅ Supported — `book_visit.form` pending option; `check-slot` runs on the pending path | AT-04 | ✅ Supported | Pending outpatient path is acceptance-tested. |
| BR-08 | ✅ Authorise the treatment booking | ✅ Supported — `ClinicalCare` documentation requires consent and an authorised Treatment Booking Request before treatment | ⚠️ Partial — `clinical_care.form` can authorise treatment / next cycle; no explicit consent field or structured treatment-request payload (dates, cycles, resources) | no acceptance test (AT-01 reaches ClinicalCare but does not complete authorisation) | ⚠️ Partial | Consent and detailed booking-request fields are not captured on the form. |
| BR-09 | ✅ Authorise task states that administration cannot continue an unauthorised request | ⚠️ Partial — process order reaches `BookTreatment` only after clinical care and funded / urgent paths; documentation forbids unauthorised admin processing | ⚠️ Partial — no engine check that the actor is a clinician; all tasks assignee `demo` | no acceptance test | ⚠️ Partial | Sequence reduces accidental skip, but RBAC does not block an unauthorised user from completing clinical tasks (see BR-37 / AT-03). |
| BR-10 | ✅ Confirm external treatment resources; messages to External treatment, laboratory and imaging | ✅ Supported — `BookTreatment`, `ReserveTreatmentSlot`, `FlagResourceUnavailable`, `SendBookingConfirmation` | ⚠️ Partial — `book_treatment.form`; workers `reserve-appointment`, `flag-resource-unavailable`, `send-booking-confirmation` mock external coordination | AT-05 reaches Book treatment after payment; lab/imaging outage scenarios have no acceptance test | ⚠️ Partial | External treatment / lab / imaging services are mocked locally. |
| BR-11 | ✅ Same task: unavailable resource stays pending and the request is not booked twice | ✅ Supported — `TreatmentOutcome` pending path through `FlagResourceUnavailable` returns to `BookTreatment` | ✅ Supported — worker `flag-resource-unavailable` sets PENDING and increments retry; occupancy key limits duplicate slots | no acceptance test (AT-04 covers outpatient pending, not treatment) | ✅ Supported | Treatment pending/retry is implemented; no PB-14/PB-18 case yet. |
| BR-12 | ✅ Determine funding and payment | ✅ Supported — `Funding` and gateway `FundingOutcome` (hospital / insurer / patient payment / arrangement / investigate / urgent) | ✅ Supported — `funding_assessment.form` funding outcome options | AT-05, AT-06 | ✅ Supported | |
| BR-13 | ✅ Message from Insurer or funding organisation: organisation, reference, amount and limits | ✅ Supported — `Funding` documentation requires organisation, reference, amount and restrictions | ⚠️ Partial — `funding_assessment.form` has `insurerReference`, `charge_amount` and notes; no dedicated limitations field | AT-05 / AT-06 exercise amount and outcome, not full funding metadata | ⚠️ Partial | Limitations / restrictions are free-text only. |
| BR-14 | ✅ Message to External payment service provider without the card number | ✅ Supported — send task `RequestPayment` to external Payment Service Provider participant | ✅ Supported — worker `request-payment`; forms warn never to enter a full card number; worker stores no card data | AT-05 | ✅ Supported | Classroom mock publishes `payment-result`; not a live PSP. |
| BR-15 | ✅ Return message: status, reference, date and amount | ✅ Supported — catch event `PaymentReceived` consumes message variables for status, transaction reference and date | ✅ Supported — `request-payment` returns `payment_status`, `transaction_reference`, `payment_date`; amount via `charge_amount` | AT-05 | ✅ Supported | |
| BR-16 | ✅ Funding task completes before Confirm external treatment resources | ✅ Supported — `FundingOutcome` opens `BookTreatment` only for funded / paid / arrangement statuses; unpaid paths go to issue or urgent review | ✅ Supported — gateway conditions and funding / payment workers enforce the classroom rule | AT-05 (Book treatment after success), AT-06 (Book treatment not auto-opened on investigate) | ✅ Supported | |
| BR-17 | ✅ Stated on Determine funding and payment: retry allowed, no automatic second charge | ✅ Supported — unsuccessful payment → `MarkPaymentInvestigate` → `FundingIssue` → return to `Funding` for retry | ✅ Supported — `request-payment` idempotent when `payment_requested_once`; `mark-payment-investigate` writes INVESTIGATE ledger row | AT-05 | ✅ Supported | |
| BR-18 | ✅ Stated on Determine funding and payment: missing confirmation is investigated | ✅ Supported — funding outcome investigate → `MarkPaymentInvestigate` → `FundingIssue`; documentation forbids automatic second charge | ✅ Supported — `funding_assessment.form` option Provider success but confirmation missing; worker `mark-payment-investigate` | AT-06 | ✅ Supported | |
| BR-19 | ⚠️ Partial — urgent care before payment is stated on the funding task, not drawn as its own branch | ✅ Supported — `UrgentAuthorisation`, gateway `UrgentDecision`, `UrgentFinance` follow-up | ✅ Supported — `urgent_authorisation.form` (clinicianId, reason, authorise / not authorised) | no acceptance test | ⚠️ Partial | Path and form exist; not covered by PB-14/PB-18; no RBAC proving only a clinician may authorise. |
| BR-20 | ⚠️ Partial — Review the refund or retained payment; full versus partial amount is not split | ✅ Supported — `FinanceAdjustment` then service task `RequestRefund` | ⚠️ Partial — `finance_adjustment.form` records authorised outcome or pending; no explicit full versus partial refund amount control; worker `request-refund` writes ledger | no acceptance test | ⚠️ Partial | Refund decision is coarse (resolved / pending), not full/partial amount selection. |
| BR-21 | ✅ Clinical, Administration and Finance lanes; money gateway sends affected changes to Finance | ⚠️ Partial — clinical / finance / admin lanes and task documentation separate clinical and financial decisions | ⚠️ Partial — separate forms and tasks; every task still assignee `demo`, so separation is organisational on the diagram only | AT-03 Fail demonstrates missing role enforcement | ⚠️ Partial | Responsibility split is modelled, not enforced at runtime. |
| BR-22 | ✅ Authorise the change or follow-up; telephone, email or a verbal request is not enough | ✅ Supported — `ClinicalChange`, gateway `ChangeValid` (rejects `invalid`), `GetDocuments` for formal authorised records; documentation rejects email/phone-only changes | ✅ Supported — `clinical_change.form`; worker `notify-care-change` skips unauthorised (`SKIPPED_UNAUTHORISED`) | no acceptance test | ⚠️ Partial | Formal change path exists; PB-14/PB-18 do not exercise it. |
| BR-23 | ⚠️ Partial — urgent stop with later authorisation is stated on the change task, not a separate branch | ⚠️ Partial — `ClinicalChange` documentation requires urgent safety postponement to be documented and authorised | ⚠️ Partial — free-text notes only; no dedicated urgent-postpone flag or retrospective-authorisation control | no acceptance test | ⚠️ Partial | Urgent postponement is policy text, not a structured workflow state. |
| BR-24 | ✅ Money affected? leads to Review the refund or retained payment | ✅ Supported — gateway `MoneyAffected` routes to `FinanceAdjustment` when `moneyAffected = true` | ✅ Supported — `clinical_change.form` Finance-review options; `notify-care-change` status `SENT_FINANCE_REVIEW_REQUIRED` | no acceptance test | ✅ Supported | Finance review flag and route are implemented; refund approval remains a separate Finance task. |
| BR-25 | ❌ Not a strategic stage; folded into Authorise the treatment booking | ⚠️ Partial — `ClinicalCare` documentation requires blood-test / fitness review before subsequent chemotherapy cycles and clinical-only decisions | ⚠️ Partial — `clinical_care.form` can authorise next cycle; no blood-test result fields; RBAC not enforced | no acceptance test | ⚠️ Partial | Cycle review is a free-text clinical step, not a structured fitness check. |
| BR-26 | ✅ Enquiry class gateway: administrative, clinical, financial | ✅ Supported — `RequestType` routes to `AdminEnquiry`, `ClinicalEnquiry` or `FinanceEnquiry` | ✅ Supported — `register_request.form` request types Administrative / Clinical / Financial enquiry; enquiry tasks use `simple_record.form` | no acceptance test | ✅ Supported | Classification is by request type at registration. |
| BR-27 | ✅ Log the enquiry states call handling answers administrative questions only; clinical answers go to the clinical lane | ⚠️ Partial — `AdminEnquiry` documentation forbids diagnosis, result interpretation and clinical advice | ⚠️ Partial — policy text only; no field or RBAC blocking clinical content on the admin path | no acceptance test | ⚠️ Partial | Call-handler limits are documented, not enforced. |
| BR-28 | ⚠️ Partial — the enquiry is logged and routed; priority, owner and resolution are not separate tasks | ⚠️ Partial — `Register` plus enquiry tasks record and route; documentation requires priority, owner and resolution | ⚠️ Partial — `register_request.form` priority and notes; enquiry responses in `simple_record.form`; no dedicated enquiry audit worker on those paths | no acceptance test | ⚠️ Partial | Enquiry trail is process variables / notes, not a full enquiry audit trail. |
| BR-29 | ❌ Urgent highlight is not drawn; the case has not fixed the urgency rules | ⚠️ Partial — `Register` / `ClinicalEnquiry` documentation require immediate highlight; documentation also states urgency rules remain a stakeholder clarification | ⚠️ Partial — Priority field only; no automatic urgent queue or alert | no acceptance test | ⚠️ Partial | Case study urgency rules are incomplete; classroom capture is manual priority only. |
| BR-30 | ✅ Write and approve the clinic letter, then Distribute the approved clinic letter | ✅ Supported — `ClinicalCare` prepares/approves letter; `DispatchLetter` gates distribution; revise path returns to clinical care | ⚠️ Partial — letter approval/content is free-text notes; `dispatch_letter.form` sent / clinical-error / delayed; worker `dispatch-clinic-letter` writes `audit_event` only | AT-05 drives letter sent to reach funding; letter-content rules have no acceptance test | ⚠️ Partial | No structured letter body, recipient list or approval timestamp fields. |
| BR-31 | ✅ Distribute task: secretaries correct formatting and administrative errors only | ✅ Supported — `DispatchLetter` documentation: admin checks only; clinical errors return to Consultant | ⚠️ Partial — `dispatch_letter.form` and `dispatch-clinic-letter` worker; clinical-edit prohibition is not enforced by the engine | Path used in AT-05; secretary-vs-consultant edit rules have no acceptance test | ⚠️ Partial | Policy is on the task; demo assignee can complete any step. |
| BR-32 | ✅ Distribute task states the seven-day target | ⚠️ Partial — `DispatchLetter` documentation states seven-day complete/approve/send target; process documentation states there are no timers | ⚠️ Partial — no appointment / approval / dispatch date fields on forms | no acceptance test | ⚠️ Partial | Seven-day target is documented, not measured or timed. |
| BR-33 | ✅ Distribute task states escalation around one month and three months | ⚠️ Partial — `MonitorLetters` user task documents 7-day / 1-month / 3-month escalation; classroom records the time band without a real multi-day timer | ⚠️ Partial — `simple_record.form` only; no timer events or escalation automation | no acceptance test | ⚠️ Partial | Escalation is a manual demo task, not a timer-driven chain. |
| BR-34 | ✅ Distribute task states that reminders stop once the letter is complete | ⚠️ Partial — `MonitorLetters` documentation: stop reminders after completion; record valid delay reasons | ⚠️ Partial — free-text notes; no reminder engine or completion-linked suppression | no acceptance test | ⚠️ Partial | Reminder suppression is undocumented behaviour of a missing reminder service. |
| BR-35 | ⚠️ Partial — follow-up sits on Authorise the change or follow-up; the out-of-window rule is drawn only on the first booking | ⚠️ Partial — `ClinicalCare` / `CarePlan` follow-up and `BookVisit` pending path can highlight unavailable slots; documentation requires referral when outside requested timeframe | ⚠️ Partial — follow-up request and pending booking exist; no dedicated outside-timeframe highlight field | no acceptance test for follow-up booking | ⚠️ Partial | Follow-up reuses outpatient booking; out-of-window highlight is the pending outcome, not a separate alert. |
| BR-36 | ⚠️ Partial — cancellation sits on the change task; did-not-attend is not its own gateway | ✅ Supported — `BookVisit` cancelled/DNA outcome; `ClinicalChange` for pathway decisions; `MoneyAffected` → `FinanceAdjustment` when paid items are affected | ⚠️ Partial — `book_visit.form`, `clinical_change.form`, `finance_adjustment.form` cover the branches; DNA versus cancel are one combined option | no acceptance test | ⚠️ Partial | End-to-end cancel/DNA + finance referral is not acceptance-tested. |
| BR-37 | ⚠️ Partial — three lanes show the split; eight-role login is not drawn | ❌ Unsupported — lanes group admin / clinical / finance, but every user task is assignee `demo`; process documentation states demo assignment is not production RBAC | ❌ Unsupported — no login beyond Camunda `demo`/`demo`; PB-22 (eight-role permissions) not delivered | AT-03 Fail — Medical Secretary Accept still created Book visit | ❌ Unsupported | Initial release has no role-based access control. Second release: implement PB-22 candidate groups / role checks so secretaries cannot complete Consultant decisions; re-run AT-03 expecting Pass. |
| BR-38 | ❌ Audit is not drawn as a stage | ⚠️ Partial — `AuditReports` and process documentation require user / time / action audit and that ordinary users must not edit history | ⚠️ Partial — `AuditEventWriter` append-only API writes `audit_event` for selected workers (A/B/C/D); not every significant user-task action is audited; no application check refusing ordinary users who edit the H2 table | no acceptance test (PB-11 refusal evidence not delivered) | ⚠️ Partial | Append-only writer is not the same as immutable, access-controlled audit storage. |
| BR-39 | ❌ Patient identity matching is not drawn | ⚠️ Partial — `Register` documentation requires identify patient and existing case | ❌ Unsupported — `patientId` is free text; no matching / deduplication logic against prior records or external IDs | no acceptance test | ❌ Unsupported | No patient-identity reconciliation service in the initial release. |
| BR-40 | ❌ Outage back-entry is not drawn | ⚠️ Partial — `AuditReports` documentation mentions downtime recovery; no operational fallback process model | ❌ Unsupported — no offline recording procedure, queue or availability controls in forms or workers | no acceptance test | ❌ Unsupported | Availability and fallback remain undocumented classroom assumptions only. |
| BR-41 | ❌ Management reports are not drawn | ⚠️ Partial — `AuditReports` user task for authorised manager review of pathway reports | ⚠️ Partial — `simple_record.form` only; no generated referral-volume, waiting-time or KPI report | no acceptance test | ⚠️ Partial | Reporting is a placeholder human task, not analytics. |
| BR-42 | ❌ Communication preferences are not drawn | ❌ Unsupported — no task, gateway or documentation for postal / digital / accessible communication preferences | ❌ Unsupported — no preference fields on forms; correspondence workers do not read preferences | no acceptance test | ❌ Unsupported | Communication preferences are out of scope for the initial executable pathway. |

---

## 3. Unsupported / Partially Supported Requirements — Second Release Plan

> **What the second release actually did (2026-10-19)**: BR-20 is delivered and now Supported (section 4.3). BR-36, BR-35 and BR-13 are partly delivered and keep their grade (section 4.4). Every other row below is unchanged, and section 4.5 states why for each rule. The plan text is left as written so the gap that was planned can be compared with what was built.
| Req ID | Initial Release Status | Gap Description | Second Release Plan | Priority |
|--------|----------------------|-----------------|---------------------|----------|
| BR-01 | ⚠️ Partial | Missing-document request is a classroom user-task simulation | Strategic task Check referral documents is delivered; add a real or stubbed outbound request record and an acceptance test for the `referral_incomplete` path | P1 |
| BR-04 | ⚠️ Partial | Letter and two-week phone contact are documentation only | Add structured contact-channel fields (letter / phone) on booking; optionally a correspondence send task; acceptance-test letter-plus-phone when timeframe is within two weeks | P1 |
| BR-05 | ⚠️ Partial | Contact attempts are free-text notes | Add a repeatable contact-attempt structure (channel, outcome, timestamp) on the booking form and assert it in acceptance tests | P1 |
| BR-06 | ⚠️ Partial | Urgent priority is data only; timescales are not shortened | Strategic model leaves urgent timescale as data inside booking; add an operational skip path and an urgent-referral acceptance case | P1 |
| BR-08 | ⚠️ Partial | No explicit consent field or structured Treatment Booking Request payload | Extend `clinical_care.form` with consent confirmation and treatment request fields (start date, cycles, resources); block `BookTreatment` unless those variables are present | P0 |
| BR-09 | ⚠️ Partial | Unauthorised treatment requests are not blocked by role checks | Implement PB-22 so only clinical roles can complete treatment-authorisation tasks; add an acceptance test that admin cannot open `BookTreatment` without authorised clinical variables | P0 |
| BR-10 | ⚠️ Partial | External treatment / lab / imaging coordination is mocked | Keep mocks for coursework, but record service identity and attempt log on the form; add an acceptance case for laboratory/imaging unavailable separate from outpatient pending | P2 |
| BR-13 | ⚠️ Partial | Funding limitations are free-text only | Add dedicated funding-limitation fields (approved amount, restrictions, organisation) and validate them before confirming treatment | P1 |
| BR-19 | ⚠️ Partial | Urgent unpaid treatment path untested; clinician-only authorisation not enforced | Add PB-18-style acceptance for `UrgentAuthorisation` → `BookTreatment` → `UrgentFinance`; bind the task to clinical candidate groups under PB-22 | P1 |
| BR-20 | ⚠️ Partial | Refund form lacks full versus partial amount decision | Extend `finance_adjustment.form` with refund type (full / partial) and amount; assert ledger row fields in an acceptance test | P1 |
| BR-21 | ⚠️ Partial | Clinical / finance separation is lane documentation only | Enforce separate candidate groups for clinical versus finance tasks (PB-22); re-run AT-03 and add a finance-cannot-authorise-treatment case | P0 |
| BR-22 | ⚠️ Partial | Formal modification path exists but has no PB-14/PB-18 coverage | Add acceptance tests for authorised change, invalid/unauthorised skip (`notify-care-change`), and Finance-review routing | P1 |
| BR-23 | ⚠️ Partial | Urgent safety postponement has no structured retrospective authorisation | Add urgent-postpone outcome plus mandatory retrospective authorisation fields; escalate if authorisation remains empty | P1 |
| BR-25 | ⚠️ Partial | Blood-test / fitness review before chemotherapy cycles is documentation only | Add blood-test and fitness fields on `clinical_care.form`; prevent next-cycle authorisation when fitness is not recorded | P2 |
| BR-27 | ⚠️ Partial | Call-handler clinical prohibition is policy text only | Restrict `AdminEnquiry` content and block clinical advice fields; route symptom/side-effect text to `ClinicalEnquiry` under PB-22 | P1 |
| BR-28 | ⚠️ Partial | Enquiry audit trail is incomplete | Persist enquiry receive time, handler, team, priority, response and resolution to `audit_event` (or an enquiry table) on every enquiry path | P1 |
| BR-29 | ⚠️ Partial | Urgency highlight rules are undecided; only a Priority field exists | Agree urgency rules with tutors/stakeholders; implement highlight / clinical-queue routing and an urgent-enquiry acceptance case | P1 |
| BR-30 | ⚠️ Partial | Clinic letter content, recipients and approval timestamps are unstructured | Add letter draft / approval fields and recipient list; require Consultant approval variable before `dispatch-clinic-letter` runs | P1 |
| BR-31 | ⚠️ Partial | Secretaries can complete any demo task; clinical-edit ban not enforced | PB-22 candidate groups for Medical Secretaries on `DispatchLetter` only; acceptance test that clinical-error return reopens `ClinicalCare` | P1 |
| BR-32 | ⚠️ Partial | Seven-day target has no dates or timers | Capture appointment, approval and dispatch dates on forms; report overdue when elapsed days exceed seven | P1 |
| BR-33 | ⚠️ Partial | Escalation is a manual `MonitorLetters` task without timers | Add timer boundary events or a scheduled monitor for 7-day / 1-month / 3-month escalation; keep classroom short timers for demo | P1 |
| BR-34 | ⚠️ Partial | No reminder service to suppress after completion | Implement reminder records linked to letter status; stop creating reminders when letter status is sent; require a delay-reason field when overdue | P2 |
| BR-35 | ⚠️ Partial | Follow-up outside-timeframe highlight is only the pending booking outcome | Add an explicit out-of-timeframe flag and pathway-team notification when the booked slot exceeds the requested review window | P2 |
| BR-36 | ⚠️ Partial | Cancel / DNA / finance referral path untested; DNA and cancel share one option | Split cancel, decline and DNA outcomes; add acceptance covering DNA → clinical pathway decision → Finance when payment exists | P1 |
| BR-37 | ❌ Unsupported | No eight-role login or engine RBAC; AT-03 Fail | Deliver PB-22 role matrix and Camunda candidate groups / claims; refuse Medical Secretary Accept; re-run AT-03 to Pass | P0 |
| BR-38 | ⚠️ Partial | Selected workers append `audit_event`; ordinary users are not refused if they alter storage; many user tasks are unaudited | Extend audit coverage to referral decisions, letter approvals, payments and refunds; add read-only audit API and an acceptance test that an ordinary user cannot update or delete audit rows (PB-11) | P0 |
| BR-39 | ❌ Unsupported | No patient-identity deduplication | Add patient match rules (name/DOB/NHS-style id stub) at `Register`; block or warn on ambiguous matches; acceptance-test wrong-association prevention | P1 |
| BR-40 | ❌ Unsupported | No availability or downtime fallback procedure | Document and implement an offline activity log / catch-up task for system or external-service outages; add it to the strategic model and to an operational fallback path | P2 |
| BR-41 | ⚠️ Partial | `AuditReports` is a placeholder human task | Produce management report views or exports for referral volumes, waits, letter delays, payment exceptions and pathway progress from domain tables | P2 |
| BR-42 | ❌ Unsupported | No communication-preference capture or use | Add preference fields (postal / digital / accessible) and pass them into correspondence workers; add the preference to the strategic model and the operational model | P2 |
| Strategic column remainder | ⚠️ Partial | PB-12 now draws the main stages. Still undrawn: chemotherapy cycle review (BR-25), urgent enquiry highlight (BR-29), audit as a stage (BR-38), identity matching (BR-39), outage back-entry (BR-40), management reports (BR-41), communication preferences (BR-42) | Keep those items out of the initial strategic picture unless a later release adds the stage; implementation gaps stay in the rows above | P2 |

---

## 4. Second Release Refresh — V2 (2026-10-19)

> Refreshed for `PB-39` / `Est-01`. Section 2 is the 29 September snapshot and is left as written. This section answers one question per rule: did the second release move it, and if not, why not. A rule counts as **moved** only when the artefact its section 2 Notes named actually changed. A rule that only gained better wording in a task description has not moved.

### 4.1 Evidence set

| Artefact | Version graded here | What changed since 2026-09-29 |
|----------|---------------------|------------------------------|
| Strategic BPMN | `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | Nothing. The file and its abstraction note are unchanged (`88a5bcc`; stated in `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` §1). |
| Operational BPMN | `Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`, process `Hospital_All_Processes_V2_C8` | New model, built in `8cda78c` … `787375e`. The 29 September model (`Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`, `Hospital_All_Processes_Simple_C8`) is untouched and remains the submitted baseline; V2 is added alongside it, not substituted for it. |
| Forms | `Week3 Coursework/hospital-pathway/forms/` (12 forms; 11 at baseline) | 4 changed: `book_visit` (`e4b2159`, `8a10e24`), `finance_adjustment` (`32e6dbc`, `1816b8e`), `funding_assessment` (`9a0b294`), `register_request` (`c29df1c`, `8a10e24`). 1 new: `await_attendance` (`e4b2159`), which records the booked visit before the outcome decision. 7 unchanged: `book_treatment`, `clinical_care`, `clinical_change`, `dispatch_letter`, `review_referral`, `simple_record`, `urgent_authorisation`. |
| Workers | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/` | `ChargeAmountRules` added (`cb23fdf`); `RefundWorkers` and `HospitalPathwayWorkers` changed (`cb23fdf`, `1816b8e`). `BookingWorkers`, `CareChangeWorkers`, `LetterWorkers` and the domain classes are unchanged. |
| Acceptance tests | `pb14_acceptance.py`, `pb18_acceptance.py` | **Not re-run.** `PB-31` is still open. No test result below is a V2 result. |

The V2 model changes that matter for traceability, in one place: the visit outcome is split into attended, pending/retry, patient-cancelled, booked-awaiting-attendance, declined and did-not-attend (`VisitOutcome`, `AwaitAttendance`, `RecordDecline`, `RecordDna`); the outpatient slot is skipped when the visit is not being booked (`VisitNeedsSlot`); the requested review period is stored as a number plus a unit and a past appointment date is rejected; the finance form shows the original charge and an invalid refund fails once. The seven exclusive merge gateways (`Join_BookVisit`, `Join_ClinicalCare`, `Join_Funding`, `Join_BookTreatment`, `Join_ClinicalChange`, `Join_VisitOutcome`, `Join_MarkPaymentInvestigate`) are pass-through and change no rule.

### 4.2 Result

| Release | ✅ Supported | ⚠️ Partial | ❌ Unsupported |
|---------------|---:|---:|---:|
| Initial release (29 September) | 12 | 26 | 4 |
| Second release (V2, 19 October) | 13 | 25 | 4 |

One grade moved: **BR-20** Partial → Supported. Of the other 29, three gaps narrowed without a grade change — **BR-36, BR-35, BR-13** (4.4) — and 26 were untouched (4.5, one reason per rule).

### 4.3 The grade that moved — BR-20

BR-20 asks that an authorised Finance member decides a refund, in full or in part, and that the amount is recorded. Section 2 marked it Partial for one reason: "no explicit full versus partial refund amount control".

| Section 2 gap | What V2 has instead |
|---------------|---------------------|
| Refund decision is coarse (resolved / pending) | `finance_adjustment.form` selects `refund_full`, `refund_partial`, `transfer`, `retain` or `pending` (`32e6dbc`); `adjustmentAmount` is mandatory on every decision except `pending`. |
| No amount control | `RefundWorkers.resolveAdjustment` maps each decision to its own ledger status, and `requirePartialAmount` rejects a partial amount that is not lower than the original charge (`1816b8e`). |
| Original charge could be overwritten | The form displays `charge_amount` as the original charge and the worker does not write it back. An invalid amount or unknown decision fails the job once with `retries(0)` instead of failing three times (`cb23fdf`). |

Evidence: `Week3 Coursework/hospital-pathway/forms/finance_adjustment.form`; `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/RefundWorkers.java` (job-failure path lines 44–55, decision mapping 115–156); `ChargeAmountRules.java`; `Hospital_All_Processes_V2.bpmn`, `FinanceAdjustment` documentation; commits `32e6dbc`, `1816b8e`, `cb23fdf`.

Why Supported rather than still Partial: the decision, the amount, and the rejection of an invalid amount now exist in both the form and the worker, so the gap the matrix named is closed rather than restated. Two limits are recorded rather than hidden. First, no acceptance test was executed; this follows the BR-11 precedent, where a modelled and implemented rule is Supported without its own test and the missing test is listed in Notes. Second, role enforcement is not part of this grade — the matrix consistently grades it under BR-37 (see the BR-02 and BR-09 notes), so BR-37 remains the row that carries that gap.

### 4.4 Gaps narrowed, grade unchanged

| Req ID | What V2 added | Why the grade did not move |
|--------|---------------|----------------------------|
| BR-36 | `RecordDecline` and `RecordDna` are separate tasks; `AwaitAttendance` holds the booked visit; `VisitOutcome` has six distinct conditions (attended, pending/retry, patient cancelled, booked, declined, dna); decline and DNA enter `Join_ClinicalChange`, so the pathway decision is made at `ClinicalChange` and paid cases reach `FinanceAdjustment` through `MoneyAffected`. `book_visit.form` and `await_attendance.form` offer the same separate outcomes. | The split is delivered, but no acceptance case runs DNA → pathway decision → Finance, and reschedule is still not a recorded outcome of its own: it is a re-booking through `BookVisit` with `pending`. Both were named in section 2's Notes, so the rule stays Partial. |
| BR-35 | `book_visit.form` rejects a past appointment date (`disallowPassedDates`), hides date and time while `pending`, and makes `waitReason` mandatory (`no_slot`, `contact_incomplete`, `external_waiting`); the requested period is stored as a number plus a unit (`c29df1c`, `8a10e24`). | There is still no out-of-timeframe flag or pathway-team notification separate from the pending branch, and no follow-up booking test. The booking side is structured; the rule's named gap is not closed. |
| BR-13 | `funding_assessment.form` requires `charge_amount` as a two-decimal number from 0.01 to 99999.99 on the patient-payment path and requires `insurerReference` on the insurer path (`9a0b294`), re-checked by `ChargeAmountRules.require` (`cb23fdf`). | Amount and reference are now structured, but there is still no dedicated limitations/restrictions field: they remain inside `notes`. Partial stands. |

### 4.5 Rules that did not move, and why

Each row names the artefact the rule actually depends on and what that artefact looks like in V2. "Unchanged" means byte-identical to the 29 September baseline except where a commit is named.

| Req ID | Status | Artefact checked | Why it did not move |
|--------|--------|------------------|---------------------|
| BR-01 | ⚠️ Partial | `GetDocuments`, `register_request.form` | The missing-document path is unchanged: no outbound request record and still no acceptance case for `referral_incomplete`. The registration change (`c29df1c`) only adds the requested period. |
| BR-04 | ⚠️ Partial | `BookVisit`, `book_visit.form` | The V2 form records one outcome plus free-text `notes`; there is no letter or phone channel field, no separate send task, and no test asserting a letter plus a two-week phone call. |
| BR-05 | ⚠️ Partial | `book_visit.form` | Contact attempts are still `notes` text. The form has no repeatable attempt record (channel, outcome, timestamp). |
| BR-06 | ⚠️ Partial | `Register`, `register_request.form` | Urgency is still a priority value (`routine`, `urgent`, `two_week_wait`). No skip-timescale path was added, and the model has no timer events at all. |
| BR-08 | ⚠️ Partial | `clinical_care.form` | The form is unchanged from 29 September. V2 strengthened the task text to require consent and an authorised request with dates, cycles and resources, but no such field exists, so the rule still cannot be completed as written. |
| BR-09 | ⚠️ Partial | `ClinicalCare`, `BookTreatment`, `book_treatment.form` | Process order still prevents most accidental skips, but every task remains `assignee="demo"`. The blocking cause is BR-37. |
| BR-10 | ⚠️ Partial | `BookTreatment`, `ReserveTreatmentSlot`, `FlagResourceUnavailable` | Task and worker set unchanged. Laboratory and imaging outages remain inside the same mocked `book_treatment` step. |
| BR-19 | ⚠️ Partial | `UrgentAuthorisation`, `urgent_authorisation.form` | Form unchanged. The path is still not exercised by PB-14 / PB-18, and clinician-only authorisation is still unenforced (BR-37). |
| BR-21 | ⚠️ Partial | Three lanes, all forms | Lane separation is unchanged, and `staffRole` is a free-text field, not a role check. Cause is BR-37. |
| BR-22 | ⚠️ Partial | `ClinicalChange`, `clinical_change.form`, `NotifyCareChange` | Form and worker unchanged. No acceptance case was added for an authorised change, the unauthorised skip, or Finance routing. |
| BR-23 | ⚠️ Partial | `clinical_change.form` | Urgent postponement is still free text in `notes`; there is no dedicated urgent-postpone outcome or retrospective-authorisation field. |
| BR-25 | ⚠️ Partial | `ClinicalCare`, `clinical_care.form` | Form unchanged: no blood-test or fitness fields. The stage is still absent from the strategic model. |
| BR-27 | ⚠️ Partial | `AdminEnquiry` | Task text unchanged. No field or role restriction separates administrative content from clinical content. |
| BR-28 | ⚠️ Partial | `Register`, three enquiry tasks | The form now carries priority, but owner and receipt time exist only in the task text, and no enquiry path writes an audit record. |
| BR-29 | ⚠️ Partial | `Register`, `ClinicalEnquiry` | The urgency rules are still a stakeholder clarification. The only mechanism remains the manual priority field. |
| BR-30 | ⚠️ Partial | `ClinicalCare`, `DispatchLetter`, `dispatch_letter.form` | Form unchanged: letter body, recipient list and approval timestamp are still free text or absent. |
| BR-31 | ⚠️ Partial | `dispatch_letter.form`, `DispatchClinicLetter` | Unchanged. The clinical-edit ban is still policy text, because any `demo` user can complete the task. |
| BR-32 | ⚠️ Partial | `dispatch_letter.form` | Unchanged. No appointment, approval or dispatch date is captured, so the seven-day target cannot be measured. |
| BR-33 | ⚠️ Partial | `MonitorLetters` | Task text unchanged. The model still has no timer or scheduled monitor. |
| BR-34 | ⚠️ Partial | `MonitorLetters` | Unchanged. Reminder suppression still has no reminder service behind it, and no delay-reason field was added. |
| BR-38 | ⚠️ Partial | `AuditReports`, `AuditEventWriter` | The writer is unchanged. There is no read-only audit API, no refusal test, and the same selected workers are audited. |
| BR-41 | ⚠️ Partial | `AuditReports` | Still a placeholder human task. No report view or export was built. |
| BR-37 | ❌ Unsupported | Assignment of every user task | No candidate groups, claims or login were added. `AT-03` remains a recorded fail. |
| BR-39 | ❌ Unsupported | `Register` | `patientId` is still free text. No match, duplicate check or ambiguous-match warning exists. |
| BR-40 | ❌ Unsupported | `AuditReports`, fallback path | No offline log, catch-up task or availability control was added. |
| BR-42 | ❌ Unsupported | `register_request.form`, correspondence workers | No preference field exists, and no worker reads one. |

### 4.6 Two columns that were not refreshed

- **Strategic BPMN** — `PB-12` has not changed since 29 September, so every strategic cell keeps its 29 September value. BR-25, BR-29, BR-38, BR-39, BR-40, BR-41 and BR-42 therefore remain ❌ in that column even where V2 implemented part of the operational work.
- **Acceptance tests** — no test was re-run, so nothing moves on test evidence. The section 2 cells describe the 29 September executable; for V2 they must be read as "not re-run", never as "passed".

### 4.7 What section 3 still covers

Of the 30 rules section 3 plans for, one row is closed (BR-20), three are partly delivered (BR-36, BR-35, BR-13), and 26 are unchanged, of which 4 are still Unsupported. `BR-37` remains the highest-leverage item: it is P0, and it blocks BR-09, BR-21, BR-27 and BR-31 as well as `AT-03`. `BR-38` (audit immutability) and `BR-08` (consent and a structured treatment request) are the next P0 items whose artefacts did not change at all in V2.
