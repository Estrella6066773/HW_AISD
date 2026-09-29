# AISD-3 Justification of Decisions


## Model Facts at a Glance (for traceability)

| Dimension | Count / Value | Note |
|---|---|---|
| Executable process | 1 (`Hospital_All_Processes_Simple_C8`) | Carried only inside the HOSPITAL pool |
| Participants (pools) | 4 | HOSPITAL + 3 external black-box participants |
| Lanes | 3 | Finance / Clinical team / Administration |
| Exclusive gateways | 28 | **Every gateway has a `default` branch** |
| Message flows | 5 | Cross-pool interaction |
| External worker task types | 10 (`zeebe:taskDefinition`) | Java JobWorker / send connector |
| User tasks | 38 | Manual steps |
| Form bindings | 19 (`zeebe:formDefinition` / `formId`) | Linked to 11 `.form` files |
| Intermediate catch events | 2 | `PaymentReceived` correlates the external payment receipt |

---

## 1. Process structure

**Decision**: Use a **single executable process** to carry the "patient pathway main thread + supporting services (finance, enquiry, audit)" rather than splitting the business into several disconnected processes.

**Justification**:
- Entry is `Start request` → `Register request` (P1/P10/P13, Administration lane) → `Request type?` exclusive gateway, which dispatches by request category into 7 workflows: referral (P2), supplementary documents (P1/P11), administrative enquiry (P10), clinical enquiry (P10), financial enquiry (P10), change/follow-up (P11/P12), report (P13).
- The clinical main thread is coherent and visible: `Register → Referral decision? → Book visit → Visit outcome? → Clinical care → Clinical plan? → Funding → Funding status? → Book treatment → Resources ready? → Care episode ended`.
- Urgent care has its own branch: `Urgent authorisation` (P8) → `Urgent care authorised?` → `Urgent finance follow-up` (P8), so urgent cases are not blocked by the normal queue.
- Finance/payment sub-thread: `Funding → Funding status? → Send payment request` (send task to the external payer) → `Payment result received` (intermediate catch event) → `Payment result?`.
- Letter sub-thread: `Dispatch clinic letter` (P9) → `Letter status?` → `Monitor letters` (overdue reminder / escalation).
- The choice of "single process" over "multiple independent processes" is because this course's operational model requires showing, in one diagram, the nine elements: Participants / Responsibilities / Activities / Decisions / Messages / Business rules / Exceptions / System boundaries / External services. A single process makes the cross-participant message flows and end-to-end paths clear at a glance, and also satisfies the precondition that the merged model must be deployable (see Assumptions and Trade-offs).

---

## 2. Participant boundaries

**Decision**: Model **4 pools (Participants)**, of which only `HOSPITAL` is a white-box executable process; the other 3 are **black-box external participants** that interact only via message flows.

**Justification**:
- `HOSPITAL | Patient pathway and supporting services` — inside the system boundary, carries all executable logic.
- `Referring organisation | GP / Other hospital` — referral source, sends `Msg_Referral` (referral documents) into Register.
- `Patient / authorised representative` — receives `Msg_Contact` (appointment / contact), `Msg_Treatment` (treatment arrangement).
- `External Payment Service Provider` — receives `Msg_PaymentRequest` (payment request), returns `Msg_Payment` (verified transaction result).
- This division clearly marks the **system boundary**: what enters the HOSPITAL pool and is orchestrated and executed by Camunda 8 is the process owned by this group; the referrer, patient, and payment provider are invoked/notified external entities whose internal processes are not modelled. This satisfies AISD-1's requirements for *System boundaries* and *External services*, and avoids forcing external organisations' internal business into this system.

---

## 3. Task allocation

**Decision**: Manual steps are assigned responsibility by **functional lane**; automatable steps are handed to **external Java workers (External Worker)**, each worker class owned and understood by a fixed group member.

**Justification (lane → responsibility)**:
- **Administration**: `Register request` (P1/P10/P13), `Admin enquiry` (P10), `Audit reports` (P13).
- **Clinical team**: `Review referral` / `Redirect` (P2), `Book visit` (P3/P4/P12), `Clinical care` (P5/P9/P12), `Dispatch clinic letter` / `Monitor letters` (P9), `Urgent authorisation` (P8), `Clinical enquiry` (P10), `Book treatment` (P6), `Clinical change` (P11/P12).
- **Finance**: `Funding assessment` (P7), `Funding issue` (P7), `Send payment request` (P7 send task), `Finance adjustment` (P7/P11/P12), `Urgent finance follow-up` (P8), `Finance enquiry` (P10).

**External worker ownership (10 `zeebe:taskDefinition` task types)**:

| Job type (matches `@JobWorker(type=…)`) | Process step | Owning member (worker class) |
|---|---|---|
| `dispatch-clinic-letter` | P9 Dispatch clinic letter | **Member C / Ender — LetterWorkers** |
| `notify-referrer` | P2 Notify referrer | **Member C / Ender — LetterWorkers** |
| `notify-care-change` | P11/P12 Notify care change | **Member D / Ryan — CareChangeWorkers** |
| `request-refund` | P7/P11/P12 Request refund / record adjustment | **Member A / Ruby — RefundWorkers** |
| `check-slot` | P3 Check / reserve outpatient slot | **Member B / Est — BookingWorkers** |
| `reserve-appointment` | P6 Reserve treatment slot / resources | **Member B / Est — BookingWorkers** |
| `send-booking-confirmation` | P6 Send booking confirmation | **Member B / Est — BookingWorkers** |
| `flag-resource-unavailable` | P6 Flag resource unavailable | **Member B / Est — BookingWorkers** |
| `request-payment` | P7 Send payment request (send task) | Finance / P7 payment-cluster worker |
| `mark-payment-investigate` | P7 Mark payment investigate | Finance / P7 payment-cluster worker |

- User tasks are bound via 19 `formId`s to Camunda Forms (11 `.form` files under `Coursework/hospital-pathway/forms/`), closing the loop "user fills form → variables enter process → worker reads variables".

---

## 4. Gateways

**Decision**: Use **exclusive gateways** throughout for branching/merging, and **every gateway is configured with a `default` branch**. The model has 28 exclusive gateways in total.

**Justification**:
- Key decision points: `Request type?`, `Referral decision?`, `Visit outcome?`, `Clinical plan?`, `Funding status?`, `Payment result?`, `Resources ready?`, `Formal request authorised?`, `Financial impact?`, `Letter status?`, `Urgent care authorised?`, etc.
- Every gateway has a default flow (e.g. `Request type?` defaults to `Select type`, `Referral decision?` defaults to `Select decision`), ensuring **any condition not explicitly hit has a fallback path**, so the process never gets stuck in Zeebe for lack of a matching sequence flow (incident / dead-end).
- This is deterministic routing, not inference by an LLM/rule engine, matching this course's "clear contract, deployable, testable" operational-model positioning.

---

## 5. External interactions

**Decision**: Cross-system / cross-organisation interaction is always expressed via **message flow + external worker / send task**, never simulating the other party's internal logic inside this process.

**Justification (5 message flows)**:
- `Msg_Referral`: Referrer → `Register` (referral documents enter).
- `Msg_Contact`: `BookVisit` → Patient (appointment / contact).
- `Msg_Treatment`: `SendBookingConfirmation` → Patient (treatment arrangement).
- `Msg_PaymentRequest`: `RequestPayment` → PaymentProvider (payment request, send task).
- `Msg_Payment`: PaymentProvider → `PaymentReceived` (verified transaction result, correlated by intermediate catch event).
- In addition, the 10 external workers are the "system–code boundary": e.g. `notify-referrer` simulates notifying the referrer, `dispatch-clinic-letter` simulates sending the Clinic Letter — both only write to the audit log and do not actually send, leaving "real external side effects" outside the system boundary (see Assumptions and Trade-offs).

---

## 6. Exception handling

**Decision**: Handle exceptions with a four-layer combination of "**gateway default branch + user-task re-entry + worker retry + idempotent audit**", without introducing a separate compensation / saga framework.

**Justification**:
- **Structural fallback**: all 28 gateways have a `default`; exceptions/unforeseen conditions take the default flow instead of terminating.
- **Business rejection / abnormal termination**: `Referral rejected` → `End rejected`; `Visit outcome? = Cancel/DNA` → `Clinical change` (reschedule / cancel); `Formal request authorised? = Missing/invalid` → `GetDocuments` (return for supplementary documents).
- **Payment exception**: `Payment result? = Unsuccessful` → `Mark payment investigate` (worker); `Funding status? = Pending/investigate` → same worker or `Funding issue` (manual review) → back to `Funding`.
- **Resource exception**: `Resources ready? = Pending/retry` → `Flag resource unavailable` (worker) → retry.
- **Letter overdue**: `Letter status? = Delay/follow-up` → `Monitor letters` (reminder / escalation) → back to `Clinical care`.
- **Worker resilience**: automated tasks set `retries="3"` (`notify-care-change`, `request-refund`, `mark-payment-investigate`, `notify-referrer`, `dispatch-clinic-letter`); audit writes use an **idempotency key** (`caseReference|workerType`) — check-then-insert — so retries do not create duplicate records.

---

## 7. Assumptions

1. **Merged model is deployable**: the announcement's contingency "if the merged model cannot deploy, each member splits into an independent BPMN" was **not triggered** — this merged model has `isExecutable="true"` and passes XML validation, verified by deployment on a local c8run cluster, so the single-process approach is adopted.
2. **External participants are black boxes**: Referrer / Patient / Payment Provider are represented only by pool + message flow, their internal processes not modelled.
3. **Workers are simulated**: all "send mail / notify / pay" only write to the H2 `audit_event` audit table, producing no real email, real letter, or real fund movement — consistent with the course demo positioning, and with no external-credential dependency.
4. **Storage**: audit uses H2 (file DB `data/hospital-domain.mv.db`), no extra domain tables created; the unique column provides basic de-duplication protection.
5. **Runtime**: Java 21 + Spring Boot workers, started with `mvn spring-boot:run`; c8run provides Zeebe / Operate / Tasklist.
6. **Forms**: 19 `formId`s bind to Camunda Forms under `forms/`, user tasks collect variables via forms.

---

## 8. Alternatives considered

1. **Per-member independent BPMN (announcement contingency) vs single merged process**: the contingency guarantees each person has a deployable model but loses the cross-participant end-to-end message flow and overall view; since the merged model deployed successfully, the single-process approach is adopted.
2. **Model external organisations' internal processes vs black-box pool + message flow**: the former is more complete but far exceeds this course's system boundary and workload; the latter has a clear boundary and controllable scope, so it is adopted.
3. **Real email/payment integration vs audit-simulated workers**: real integration needs external credentials and network, and is unsuitable for a demo; audit simulation is repeatable and observable, so it is adopted.
4. **Concurrency compensation framework (saga) for idempotency vs DB unique key + idempotency key**: saga is costly and error-prone; unique key + check-then-insert is enough to cover the course scenario's retry de-duplication, so it is adopted.
5. **LLM/agent dynamically decides branching vs deterministic gateway**: the agent path is uncontrollable, hard to test, and violates the "deployable operational model" positioning; the deterministic exclusive gateway is adopted.

---

## 9. Trade-offs

| Choice | Benefit | Cost / Risk | Mitigation |
|---|---|---|---|
| Single merged process | Complete end-to-end view, cross-pool messages clear, satisfies AISD-1 nine elements | Model is large, hard for one person to present | Each member deeply understands their own worker + can explain the whole flow (announcement requirement) |
| External participants black-boxed | Clear system boundary, controllable scope | Referrer/payer internals invisible | Course scope sufficient; message flows already express the interaction contract |
| Audit-simulated workers | Safe, repeatable demo, no external credentials | Not production-grade real side effects | Course positioning accepts it; code clearly marked "simulated" |
| Default flow on every gateway | No dead-ends, resilient | Unmodelled edge conditions silently take the default, may hide requirement gaps | Default flows clearly named, reviewed against the test plan |
| Unique-key idempotency (no saga) | Simple, sufficient | Weaker than full-compensation transactional guarantee | Course retry scenarios already covered by idempotency key |
| Functional-lane division of work | Clear responsibility | A single request spans multiple lanes (cross-functional) | Gateways and message flows connect cross-lane collaboration |
