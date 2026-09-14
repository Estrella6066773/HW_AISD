# Sprint Review — Template

> Copy this file and rename to `sprint-review-N.md` (e.g., `sprint-review-1.md`). **Sprint Reviews are graded.** The whole team must present.

---

## Sprint Review N

**Date**: YYYY-MM-DD
**Sprint Being Reviewed**: Sprint N
**Audience**: Tutor(s), team members

---

## 1. Sprint Goal (Slide 1)

> _Restate the sprint goal verbatim. Then show whether it was achieved._

**Goal**: _(e.g., "Deploy a working referral intake BPMN model with Medical Secretary verification, Consultant review, and basic external payment worker")_

**Achieved?**: ✅ Yes / ⚠️ Partially / ❌ No

---

## 2. Demo of Completed Work (Slides 2–5)

> **Walk through each completed increment live.** Screenshots in this document serve as backup evidence.

### Increment A: _(e.g., Referral Verification User Task)_

- **File(s)**: `docs/operational-bpmn/referral-process.bpmn`, `forms/referral-verification.form.json`
- **Demo**: _(Step-by-step walkthrough — who does what, what they see)_
- **Evidence**: _(Screenshot of the running process in Operate / Tasklist)_

![Evidence](test-results/screenshot-referral-verification.png)

### Increment B: _(e.g., Consultant Review Decision)_

- **File(s)**: `docs/operational-bpmn/referral-process.bpmn`, `forms/consultant-review.form.json`
- **Demo**:
- **Evidence**:

![Evidence](test-results/screenshot-consultant-review.png)

### Increment C: _(e.g., External Payment Worker)_

- **File(s)**: `src/workers/payment_worker.py`
- **Demo**: _(Show worker logs in terminal; show Operate that task completed)_
- **Evidence**:

![Evidence](test-results/screenshot-payment-worker.png)

---

## 3. Unfinished Work (Slide 6)

> **Be clear about what didn't get done.** Don't hide it.

| Backlog Item | Original Commitment | Not Completed Because | New Plan |
|-------------|---------------------|----------------------|----------|
| PB-XX | Full implementation | External service mockup not ready | Move to Sprint N+1 with mockup pre-built |

---

## 4. Key Decisions Made During This Sprint (Slide 7)

> Show that your team made informed choices, not just guesses.

| Decision | Alternatives Considered | Choice Rationale |
|----------|------------------------|------------------|
| _(e.g., Use Python for workers)_ | Java (more verbose), Node.js (async complexity) | Team already knows Python; Zeebe Python client mature enough |

---

## 5. Limitations Known (Slide 8)

> What isn't perfect yet?

| Limitation | Impact | When It Will Be Addresssed |
|-----------|--------|---------------------------|
| _(e.g., Payment worker doesn't handle network timeout yet)_ | Payment requests may fail silently | Sprint N+1 |

---

## 6. Feedback Received (Slide 9)

> Record what the tutor / stakeholders told you. You will need to act on this in the next sprint.

| # | Feedback Source | Feedback | Action Taken / Planned |
|---|----------------|----------|------------------------|
| 1 | Tutor | | |
| 2 | Stakeholder (peer group) | | |

---

## 7. Individual Contributions (Slide 10)

> Each team member must be able to explain their own contribution.

| Member | Backlog Items | Key Deliverables | Evidence |
|--------|--------------|------------------|----------|
| _(Name)_ | PB-01, PB-03 | ReferralVerification user task + Form | `docs/operational-bpmn/...`, `forms/...` |
| | | | |

---

## 8. Planning for Next Sprint (Slide 11)

> Show you're thinking ahead.

- **Proposed Sprint N+1 Goal**:
- **High-priority backlog items pulled forward**:
- **Changes from previous sprint plan** (with reasons):
