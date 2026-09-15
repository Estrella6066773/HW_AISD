# Hospital Patient Referral, Treatment and Administration System

> Advanced Information Systems Development (AISD) — Group Project 2025-26

## 1. Project Overview

This project implements a **Hospital Patient Administration System** that supports the full patient pathway from GP/hospital referral through consultation, diagnosis, treatment, follow-up care, and ongoing communication.

The system is built on **Camunda 8** (Workflow Engine) and addresses the case study provided for both units:

- **BPM&EA**: Strategic BPMN, i\* (StarUML/Visual Paradigm) socio-technical modeling, requirements traceability, and acceptance criteria evaluation.
- **AISD**: Executable operational BPMN with External Workers, Camunda Forms, and an end-to-end demonstrated workflow.

### Case Study Summary

A specialist hospital service currently manages patient referrals, bookings, treatments, payments, clinic letters, and patient enquiries through a combination of disconnected systems, emails, telephone calls, and manual records. The proposed **Hospital Patient Administration System** will:

- Replace fragmented information transfer with a unified workflow engine.
- Maintain clear separation between clinical decisions, administrative responsibilities, and financial activities.
- Provide a full audit trail across all patient pathway stages.
- Integrate with external services (scheduling, correspondence, payment providers).

### Key Business Areas (Initial Release)

| # | Area | Description |
|---|------|-------------|
| 1 | **Referral Intake** | Medical Secretaries verify referral documents → Consultant accepts/rejects/redirects |
| 2 | **Outpatient Booking** | Book New Patient Appointment via external scheduler; notify patient by letter/phone |
| 3 | **Treatment Booking** | Consultant authorises Treatment Booking Request → Treatment Bookings Team coordinates |
| 4 | **Payment & Funding** | Determine funding source → Payment Service Provider integration → Refund handling |
| 5 | **Treatment Modification** | Clinical staff request schedule changes; Finance Team reviews financial impact |
| 6 | **Clinic Letters** | Consultant writes → Medical Secretaries process/distribute → Escalation if delayed |
| 7 | **Patient Enquiries** | Call Handling Team routes admin / financial / clinical enquiries |

---

## 2. Group Members

| Name | Student ID | Role | First Owner | Second Owner |
|------|------------|------|-------------|--------------|
| _(Placeholder)_ | - | - | - | - |

> **Note**: Every task/activity in the project must have both a First Owner and a Second Owner. The second owner ensures continuity when the first owner is unavailable.

---

## 3. Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Workflow Engine** | Camunda 8 Run | 8.10.0-alpha5 |
| **BPMN Editor** | Camunda Modeler | Latest stable |
| **External Workers** | _(TBD: Java / Python / Node.js)_ | - |
| **Forms** | Camunda Forms (JSON) | - |
| **i\* Modeling** | _(StarUML / Visual Paradigm / other)_ | - |
| **Version Control** | Git + GitHub | - |

---

## 4. Repository Structure

```
HW_AISD/
├── README.md                   ← You are here
├── .gitignore
│
├── docs/
│   ├── strategic-bpmn/         # High-level strategic BPMN models (.bpmn files)
│   ├── operational-bpmn/       # Detailed / executable operational BPMN models
│   ├── i-star/                 # i* SD (Strategic Dependency) + SR (Strategic Rationale)
│   ├── requirements/           # Requirements traceability matrix, acceptance criteria
│   └── architecture/           # System architecture diagrams, external service interactions
│
├── forms/                      # Camunda Forms (JSON) connected to BPMN user tasks
│
├── src/
│   └── workers/                # External Worker source code
│
├── agile/
│   ├── product-backlog.md      # Prioritised product backlog
│   ├── definition-of-done.md   # Definition of Done
│   ├── sprint-backlogs/        # Per-sprint backlog files
│   ├── standups/               # Standup notes & evidence
│   ├── sprint-reviews/         # Sprint review records & demo evidence
│   └── retrospective/          # Sprint retrospective notes
│
└── tests/
    ├── test-plans/             # Acceptance test plans
    └── test-results/           # Test execution evidence (screenshots, logs)
```

---

## 5. Setup & Run

### 5.1 Start Camunda 8

```powershell
# Navigate to your local Camunda 8 Run installation
cd path/to/camunda8-getting-started-bundle-*/c8run-*
.\c8run.exe start
```

Access endpoints (default credentials: `demo` / `demo`):

| Tool | URL |
|------|-----|
| Operate (process monitoring) | http://localhost:8080/operate |
| Tasklist (task completion) | http://localhost:8080/tasklist |
| Admin (user management) | http://localhost:8080/admin |

### 5.2 Deploy BPMN Models

1. Open [Camunda Modeler](https://camunda.com/download/modeler/)
2. Open a `.bpmn` file from `docs/operational-bpmn/`
3. Click the **Rocket icon** → deploy to `http://localhost:26500` (default gRPC port)
4. Verify in Operate or Tasklist

### 5.3 Run External Workers

```powershell
# Language TBD — placeholders below
# Python example:
python -m src.workers.referral_worker
python -m src.workers.booking_worker
python -m src.workers.payment_worker

# Java example:
mvn exec:java -Dexec.mainClass="com.hospital.workers.ReferralWorker"
```

### 5.4 Access Forms

Forms are automatically served by Camunda Tasklist once connected to user tasks.

---

## 6. Project Workflow

### Definition of Done

A user story / task is **done** when:

1. ✅ BPMN model is deployed and runs without errors in Camunda 8
2. ✅ All External Workers are implemented, tested, and handle error cases
3. ✅ Camunda Form is connected, validates inputs, and variables pass correctly
4. ✅ Code is committed to GitHub with a descriptive message
5. ✅ At least one team member (second owner) has reviewed the changes
6. ✅ Acceptance test evidence (screenshot/log) is saved in `tests/test-results/`
7. ✅ Documentation (if any) is updated

### Git Branching Strategy

```
main          ← production-grade, always deployable
  └── dev     ← integration branch
       ├── feature/referral-intake
       ├── feature/outpatient-booking
       └── feature/payment-module
```

---

## 7. Assessment Mapping

| Assessment | Where Evidence Lives |
|-----------|---------------------|
| **BPM&EA Task 1: Strategic BPMN** | `docs/strategic-bpmn/` |
| **BPM&EA Task 2: i\* SD & SR** | `docs/i-star/` |
| **BPM&EA Task 3: Alignment Evaluation** | `docs/requirements/` (traceability matrix) |
| **BPM&EA Task 4: Acceptance Criteria** | `tests/` (test plans + results) |
| **AISD Task 1: Executable BPMN** | `docs/operational-bpmn/` + deployed model |
| **AISD Task 2: External Workers** | `src/workers/` |
| **AISD Task 3: Camunda Forms** | `forms/` |
| **AISD Task 4: Demonstration** | Screenshots in `tests/test-results/` |
| **Agile Delivery** | `agile/` directory (backlogs, standups, reviews, retros) |

---

## 8. Case Study Assumptions

> Record any assumptions made where the case study does not provide complete information.

| # | Assumption | Rationale |
|---|-----------|-----------|
| 1 | _(To be documented)_ | - |

---

---

## Wednesday Workshop (Phase 1)

First workshop delivery plan: see [workshop-plan.md](./workshop-plan.md).

Part-aligned folders (in addition to the structure above):

| Part | Path |
|------|------|
| Case summary | docs/part1-case-summary/ |
| Deliverables list | docs/part2-deliverables/ |
| Product backlog | docs/part3-product-backlog/ |
| Task breakdown | docs/part4-task-breakdown/ |
| Assumptions | docs/part5-assumptions/ |
| Sprint backlog | gile/part6-sprint-backlog/ |
| Standup | gile/part7-standup/ |
| Sprint review | gile/part8-sprint-review/ |
| Contributions | gile/contributions/ |

## License

This project is created for academic purposes as part of the Advanced Information Systems Development module.
