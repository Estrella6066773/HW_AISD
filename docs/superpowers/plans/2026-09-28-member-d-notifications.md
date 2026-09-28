# Member D notifications implementation plan

**Goal:** Deliver D's `notify-care-change` and optional `ack-enquiry-routed` in the formal hospital-pathway package, with BPMN wiring, shared H2 audit evidence, retry tests and presentation guidance.

**Authority:** User requested latest repository sync and implementation of D's allocation in Est's worker/database guide. Baseline: 98fad83. Work branch: codex/member-d-notifications. Formal package only; the optional learning package will be explicitly marked stale until merged.

**Architecture:** Preserve human decisions and existing A/B workers. Insert care-change notification immediately after ClinicalChange, before ChangeValid; insert enquiry acknowledgements after the three enquiry tasks. Reject inconsistent input; skip unapproved changes. Mock notifications become append-only audit facts, committed before automatic Camunda completion. An optional unique idempotency key on audit_event and a backward-compatible AuditEventWriter overload provide retry/concurrency deduplication. Existing four-argument append remains unchanged. No real email, no new BPMN message subscription, no payment writes.

**Contract:** care change reads patientId/case_reference, clinicianId, modificationDecision, changeTarget, moneyAffected. Output: careChangeNotificationSent, careChangeNotificationStatus, careChangeNotificationReference. Enquiries read patientId/case_reference, staffRole, requestKind and the corresponding enquiry note; output enquiryAcknowledgementSent, enquiryAcknowledgementReference. Keys use task type + process-instance key + element-instance key, so retries reuse records and later legitimate changes get distinct records. memberDNotificationFailure is a local-demo injection switch; it fails once per job while the process stays running.

**Data boundary:** Save brief structured metadata, not clinical text. Paid changes read payment_ledger and label Finance review required; empty ledger is a valid result. Notifications are mocked and audit-deduplicated, not a claim of exactly-once real email delivery.

## Tasks

- [x] Claim D in the team guide and document the variable contract.
- [x] Add JUnit/Spring test support; first run assertions against nonfunctional Worker scaffolding and the missing unique-key contract.
- [x] Extend audit append compatibly, add D workers, pass input/skip/paid/read-only/retry/concurrency tests.
- [x] Patch BPMN node references, lane membership, flow endpoints, meaningful DI coordinates and documentation. Verify all job types have workers and D's four task instances are connected.
- [x] Build the full project. Start the existing local Camunda installation if available and only one formal Worker process. Deploy BPMN and all forms.
- [x] Run actual process instances for three enquiry branches, authorised change, unapproved change and a controlled failure/retry. Capture engine state plus H2 audit rows.
- [x] Add reproducible verification commands, exact code-reading pointers and D demo instructions. Record limits and human second-owner review pending; do not mark the whole backlog or team acceptance Done.

## Verification design

Use a Spring test application that scans only domain persistence and D workers, with Camunda client disabled and a distinct in-memory H2 database. Mock only the Camunda ActivatedJob boundary; use the real repository and transactions. Assert database rows, unique-key enforcement, unchanged payment rows, error handling and repeat-call behavior. Separately test BPMN XML topology and bindings. The runtime smoke script must create only uniquely named demo cases and retain their process keys for verification.

## Outcome

20 Java tests, 4 BPMN checks and 8 real Camunda instances passed. Evidence: `evidence/PB-10_PB-21_member-D_workers_2026-09-28/`. Shared file-H2 inspection found 9 D receipts plus 1 B audit row, no duplicate receipt keys; rows persisted after Java restart. Operate completed-state and Worker details were checked visually. Second-owner review by A/B and team merge remain pending.
