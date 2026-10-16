# PB-18 Additional Acceptance Tests (exception paths)

**Module**: UFCEP6-0-3 AISD · Hospital pathway  
**Backlog item**: PB-18 (extends PB-14)  
**First owner**: Ryan · **Second owner**: Ender  
**Purpose**: Four exception-path acceptance tests required by the product backlog and Part 8 must-test list: unauthorised access, no suitable slot (pending), payment failure with retry, and provider payment without confirmation (investigate / no automatic re-charge).

---

## 1. Version under test

| Item | Value |
|------|-------|
| Process id | `Hospital_All_Processes_Simple_C8` |
| BPMN | `Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn` |
| Forms | `register_request`, `review_referral`, `book_visit`, `clinical_care`, `dispatch_letter`, `funding_assessment`, `simple_record` |
| Deployed definition | version **6**, key `2251799813925244` |
| Git baseline | `8c666bf` (at plan write) |
| Execution date | 2026-09-29 |
| Run id | `PB18-20260929-011021` |
| Evidence log | `Ryan/2026-09-26/PB-18_acceptance-run-log_2026-09-29.json` |
| Overall run result | **PASS_WITH_KNOWN_FAILS** (AT-03 Fail as expected for classroom RBAC gap; AT-04/05/06 Pass) |

**Official procedure:** Tasklist form steps below.  
**Recorded execution:** same field values via `Coursework/hospital-pathway/scripts/pb18_acceptance.py` (REST `/v2`).

---

## 2. Business rules under test

| ID | Case rule | Measurable criterion |
|----|-----------|----------------------|
| BR-U | Secretaries must not decide acceptance (para 3–4) | Accept submitted under Medical Secretary role must **not** open Book visit |
| BR-P | No slot in window → pending, notify pathway team, no silent out-of-window booking (para 5–6) | Book visit with **pending** returns to Book visit; Clinical care does **not** start |
| BR-F | Payment failure: notify; retry allowed; no duplicate charge (para 11–12) | Unsuccessful payment reaches Resolve funding issue; retry can then succeed into Book treatment |
| BR-I | Provider may have taken money but confirmation missing → investigate; **never** automatic second charge (para 11–12) | Funding outcome **investigate** → Mark payment investigate → Funding issue; Book treatment not auto-opened |

---

## 3. Test summary

| Test | Path | Verdict (2026-09-29) |
|------|------|----------------------|
| AT-03 | Unauthorised accept (secretary) | **FAIL** (honest; no engine RBAC) |
| AT-04 | No suitable slot / pending | **PASS** |
| AT-05 | Payment fail then retry | **PASS** |
| AT-06 | Missing confirmation / investigate | **PASS** |

Pass/fail: every Expected check must match Actual. Failures stay Fail with reason and proposed handling (Portfolio Task 04).

---

## 4. Shared preconditions

1. Camunda 8 Run up (`demo` / `demo`).
2. Process deployed.
3. For AT-04/05/06: Java workers running (`mvn spring-boot:run`) — needs at least `check-slot`, `request-payment`, `mark-payment-investigate`, `dispatch-clinic-letter`.
4. Unique case IDs per run.

---

## 5. AT-03 — Unauthorised access (secretary accepts)

### Preconditions

Shared 1–2, 4. Java not required.

### Test data

| Task | Field | Value |
|------|-------|-------|
| Register | Request type | New referral - documents checked |
| | Patient / case ID | `PB18-20260929-011021-UNAUTH` |
| Review | Staff name and role | Medical Secretary / not authorised to accept |
| | Referral decision | Accept |
| | Clinician ID | SECRETARY-ATTEMPT |
| | Decision reason | Attempted accept by secretary (should be refused) |

### Steps (Tasklist)

1. Start process → complete Register as referral.  
2. On Consultant review, fill Medical Secretary role and **Accept** → Complete.  
3. Observe whether **Book visit** appears.

### Expected vs Actual

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| U1 | Book visit must **not** appear | Book visit **was** created (instance `2251799813927118`) | **Fail** |

| Verdict | **FAIL** |
|---------|----------|
| Failures / proposed handling | Case rule: secretaries must not accept. Observed: Accept with staffRole Medical Secretary still created BookVisit. Classroom model assigns every task to `demo` with no candidate-group RBAC. **Proposed handling:** implement role enforcement under **PB-22**; keep this Fail visible until then. Do not rewrite as Pass. |

---

## 6. AT-04 — No suitable slot → pending booking

### Preconditions

Shared 1–4. `check-slot` worker active.

### Test data

| Task | Field | Value |
|------|-------|-------|
| Register / Review | referral + Accept | Consultant role |
| Book visit | Outcome | **No suitable slot / contact or service pending** |
| | Case ID | `PB18-20260929-011021-PENDING` |

### Steps

1. Reach Book visit after Accept.  
2. Complete Book visit with **pending**.  
3. Wait for `check-slot`.  
4. Confirm Book visit reappears; Clinical care is absent.

### Expected vs Actual

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| P1 | Book visit created again after pending | Yes (instance `2251799813927181`) | Pass |
| P2 | Clinical care not present | Absent | Pass |
| P3 | `visitOutcome = pending` | `pending` | Pass |
| P4 | No active incident | 0 | Pass |

| Verdict | **PASS** |

---

## 7. AT-05 — Payment failure then retry

### Preconditions

Shared 1–4. Demo rule: amount ending in `0` fails (`10.00`); otherwise succeeds (`10.01`).

### Test data

| Stage | Field | Value |
|-------|-------|-------|
| Case ID | | `PB18-20260929-011021-PAYFAIL` |
| Path to Funding | Accept → attended → treatment → letter **sent** | standard |
| Funding (1st) | Patient payment required; amount | **10.00** |
| Funding issue | Completed and recorded | |
| Funding (retry) | Patient payment required; amount | **10.01** |

### Steps

1. Drive process to Funding.  
2. Submit patient payment with `10.00` → wait for Resolve funding issue.  
3. Complete Funding issue → Funding again.  
4. Retry with `10.01` → expect Book treatment.

### Expected vs Actual

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| F1 | Funding issue after fail; status unsuccessful or investigate | Funding issue reached; `payment_status=investigate` | Pass |
| F2 | After retry: `payment_status = successful` | `successful` | Pass |
| F3 | Book treatment appears | Yes (instance `2251799813927283`) | Pass |

| Verdict | **PASS** |
|---------|----------|
| Note | After unsuccessful provider result the process runs `mark-payment-investigate` before Funding issue (Member A), so status reads `investigate` rather than raw `unsuccessful`. Retry still succeeds. |

---

## 8. AT-06 — Payment taken / confirmation missing (investigate, no auto re-charge)

### Preconditions

Shared 1–4. `mark-payment-investigate` worker active.

### Test data

| Stage | Field | Value |
|-------|-------|-------|
| Case ID | | `PB18-20260929-011021-NOCONF` |
| Funding | Outcome | **Provider success but confirmation missing** (`investigate`) |

### Steps

1. Reach Funding.  
2. Choose investigate → Complete.  
3. Confirm Funding issue appears; Book treatment does **not** auto-open; `payment_status = investigate`.

### Expected vs Actual

| Check | Expected | Actual | Result |
|-------|----------|--------|--------|
| I1 | `payment_status = investigate` | `investigate` | Pass |
| I2 | `payment_investigate = true` | true | Pass |
| I3 | Book treatment not auto-created | Not created; Funding issue waiting | Pass |
| I4 | `payment_requested_once` not forcing auto re-charge | `false` (request-payment not used on this branch) | Pass |

| Verdict | **PASS** | Instance `2251799813927534` |

---

## 9. How to repeat

```text
cd Coursework/hospital-pathway
mvn spring-boot:run
python scripts/pb18_acceptance.py
```

Archive `target/pb18-acceptance-*.json` as `Ryan/2026-09-26/PB-18_acceptance-run-log_<date>.json`.

---

## 10. Traceability

| Test | Case | Backlog | BPMN |
|------|------|---------|------|
| AT-03 | para 3–4 | PB-01 / **PB-22** gap | ReviewReferral Accept without RBAC |
| AT-04 | para 5–6 | PB-03 | BookVisit pending → VisitOutcome → BookVisit |
| AT-05 | para 11–12 | PB-07 | RequestPayment fail → MarkPaymentInvestigate → FundingIssue → Funding retry |
| AT-06 | para 11–12 | PB-07 | Funding investigate → MarkPaymentInvestigate → FundingIssue |

---

## 11. Second-owner review (Ender)

- [ ] Four cases each have Expected / Actual / Result  
- [ ] AT-03 Fail states reason + proposed handling (PB-22)  
- [ ] Evidence path opens in the repo  
- [ ] Version / run id filled  

PB-18 stays **In progress** until second-owner sign-off (group DoD).
