# PB-16 · i\* SD (Strategic Dependency) diagram

Companion notes: [`PB-16_istar-sd-sr.md`](PB-16_istar-sd-sr.md) · SR diagrams: [`PB-16_sr.md`](PB-16_sr.md)

## Legend (Mermaid substitution for i\* notation)

| Visual | Meaning |
|--------|---------|
| Rounded rectangle `([Name])` | Actor |
| Arrow `Depender --> Dependee` | Depender depends on Dependee |
| Edge label `Dn type: dependum` | Dependency identifier, dependum type (`goal` / `softgoal` / `task` / `resource`), and the dependum name |

i\* has no native Mermaid shapes; this legend is the mapping used throughout.

## Strategic Dependency model (initial release)

```mermaid
flowchart LR
  RO([ReferringOrganisation])
  PT([Patient])
  CL([ClinicalTeam])
  AD([AdministrativeTeam])
  FI([FinanceTeam])
  ESS([ExternalSchedulingService])
  ECS([ExternalClinicalServices])
  ECSND([ExternalCorrespondenceService])
  PSP([PaymentServiceProvider])
  FO([FundingOrganisation])
  HPAS([HospitalPatientAdministrationSystem])

  AD -->|D1 resource: Supporting referral documents| RO
  RO -->|D2 goal: Referral decision recorded| CL
  RO -->|D3 task: Communicate pathway outcome to referrer| AD
  CL -->|D4 resource: Checked referral package| AD
  AD -->|D5 goal: Authorised referral acceptance| CL
  AD -->|D6 resource: Authorised treatment booking request| CL
  AD -->|D7 goal: Clinic letter clinically approved| CL
  CL -->|D8 task: Arrange clinic and treatment appointments| AD
  AD -->|D9 resource: Available appointment slot| ESS
  AD -->|D10 resource: External treatment lab or imaging availability| ECS
  AD -->|D11 task: Send outbound patient correspondence| ECSND
  PT -->|D12 goal: Appropriate clinical assessment and care| CL
  CL -->|D13 goal: Informed consent to treatment| PT
  AD -->|D14 goal: Funding or payment cleared before confirmation| FI
  FI -->|D15 resource: Funding approval record| FO
  FI -->|D16 resource: Verified payment or refund result| PSP
  PT -->|D17 goal: Fair charging and refund handling| FI
  CL -->|D18 softgoal: Urgent care not blocked solely by payment delay| FI
  FI -->|D19 resource: Treatment and modification context for charges| CL
  PT -->|D20 task: Recorded appointment notification and contact attempts| AD
  AD -->|D21 task: Handle escalated clinical enquiry| CL
  AD -->|D22 softgoal: Traceable pathway without duplicate bookings| HPAS
  FI -->|D23 softgoal: Auditable payment trail without full card storage| HPAS
  CL -->|D24 softgoal: Recorded clinical authorisations ordinary-user immutable| HPAS
```

## Reading notes

- Edges point from the **depender** to the **dependee**.
- Categories required by PB-16 are all present: referring organisation (`RO`), clinical (`CL`), administrative (`AD`), financial (`FI`), and external organisations (`ESS`, `ECS`, `ECSND`, `PSP`, `FO`).
- Classroom mocks of scheduling and payment do not remove D9 or D16; they remain strategic dependencies (see assumptions in the notes file).
)
