# Requirements Traceability Matrix

> **Purpose**: Trace each requirement across the entire development lifecycle — from the strategic process model, through the operational BPMN, down to the actual implementation. This is a **grading criterion** (BPM&EA Task 3).
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

> Copy this table and fill in as you build each deliverable. **One row per business requirement**.

| Req ID | **Strategic BPMN** (docs/strategic-bpmn/) | **Operational BPMN** (docs/operational-bpmn/) | **Implementation** (forms/ + src/workers/) | **Initial Release Status** | **Notes** |
|--------|------------------------------------------|-----------------------------------------------|-------------------------------------------|---------------------------|-----------|
| BR-01 | _(e.g., Medical Secretary Verification lane)_ | _(e.g., `ReferralVerification` user task)_ | _(e.g., VerifyReferralForm.json + referral_worker)_ | ✅ / ⚠️ / ❌ | _(limitations, assumptions)_ |
| BR-02 | | | | | |
| BR-03 | | | | | |
| BR-04 | | | | | |
| BR-05 | | | | | |
| BR-06 | | | | | |
| BR-07 | | | | | |
| BR-08 | | | | | |
| BR-09 | | | | | |
| BR-10 | | | | | |
| BR-11 | | | | | |
| BR-12 | | | | | |
| BR-13 | | | | | |
| BR-14 | | | | | |
| BR-15 | | | | | |
| BR-16 | | | | | |
| BR-17 | | | | | |
| BR-18 | | | | | |
| BR-19 | | | | | |
| BR-20 | | | | | |
| BR-21 | | | | | |
| BR-22 | | | | | |
| BR-23 | | | | | |
| BR-24 | | | | | |
| BR-25 | | | | | |
| BR-26 | | | | | |
| BR-27 | | | | | |
| BR-28 | | | | | |
| BR-29 | | | | | |
| BR-30 | | | | | |
| BR-31 | | | | | |
| BR-32 | | | | | |
| BR-33 | | | | | |
| BR-34 | | | | | |
| BR-35 | | | | | |
| BR-36 | | | | | |
| BR-37 | | | | | |
| BR-38 | | | | | |
| BR-39 | | | | | |
| BR-40 | | | | | |
| BR-41 | | | | | |
| BR-42 | | | | | |

---

## 3. Unsupported / Partially Supported Requirements — Second Release Plan

| Req ID | Initial Release Status | Gap Description | Second Release Plan | Priority |
|--------|----------------------|-----------------|---------------------|----------|
| _(e.g., BR-29)_ | ❌ Unsupported | Urgency rules not agreed by stakeholders | Define with stakeholders; add to call handling classification | P1 |
| | | | | |
