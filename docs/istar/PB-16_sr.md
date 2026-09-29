# PB-16 · i\* SR (Strategic Rationale) diagrams

Companion notes: [`PB-16_istar-sd-sr.md`](PB-16_istar-sd-sr.md) · SD diagram: [`PB-16_sd.md`](PB-16_sd.md)

## Legend (Mermaid substitution for i\* notation)

| Visual | Meaning |
|--------|---------|
| Rounded rectangle `([Name])` | Actor boundary |
| Stadium / rounded node inside an actor | Goal, softgoal, task or resource (label states the kind) |
| Solid arrow inside an actor | Means-ends / decomposition link (element supports or provides another) |
| Dashed arrow leaving an actor | Strategic dependency, labelled with the SD identifier `Dn` |

Diagrams are split by actor so each graph stays readable. Every dashed edge cites an SD dependency from [`PB-16_sd.md`](PB-16_sd.md). Softgoals that are **not** committed initial-release product features are listed in the notes file Section 8 and are omitted from these graphs except where a softgoal is required to justify an in-scope dependency (for example D22–D24).

---

## SR-1 · ReferringOrganisation

SD links: **D1** (provides), **D2**, **D3**.

```mermaid
flowchart TB
  RO([ReferringOrganisation])
  subgraph RO_boundary[ReferringOrganisation rationale]
    RO_G1[goal: Patient accepted onto appropriate specialist pathway]
    RO_T1[task: Submit referral with supporting documents]
    RO_SG1[softgoal: Timely feedback on rejection redirect or DNA]
    RO_T1 --> RO_G1
    RO_SG1 --> RO_G1
  end
  RO --- RO_boundary
  CL([ClinicalTeam])
  AD([AdministrativeTeam])
  RO_T1 -.->|D1 resource to AdministrativeTeam| AD
  RO_G1 -.->|D2 goal on ClinicalTeam| CL
  RO_SG1 -.->|D3 task on AdministrativeTeam| AD
```

---

## SR-2 · Patient

SD links: **D12**, **D13** (provides), **D17**, **D20**.

```mermaid
flowchart TB
  PT([Patient])
  subgraph PT_boundary[Patient rationale]
    PT_G1[goal: Receive appropriate specialist care]
    PT_G2[goal: Fair and clear charging]
    PT_G3[goal: Give or withhold informed consent]
    PT_T1[task: Attend or respond to appointment contacts]
    PT_SG1[softgoal: Timely understandable communication]
    PT_T1 --> PT_G1
    PT_SG1 --> PT_G1
    PT_G3 --> PT_G1
  end
  PT --- PT_boundary
  CL([ClinicalTeam])
  FI([FinanceTeam])
  AD([AdministrativeTeam])
  PT_G1 -.->|D12 goal on ClinicalTeam| CL
  PT_G3 -.->|D13 goal provided to ClinicalTeam| CL
  PT_G2 -.->|D17 goal on FinanceTeam| FI
  PT_SG1 -.->|D20 task on AdministrativeTeam| AD
```

---

## SR-3 · ClinicalTeam

SD links: **D2** (provides), **D4**, **D5**–**D7** (provides), **D8**, **D12** (provides), **D13**, **D18**, **D19** (provides), **D21** (provides), **D24**.

```mermaid
flowchart TB
  CL([ClinicalTeam])
  subgraph CL_boundary[ClinicalTeam rationale]
    CL_G1[goal: Make safe referral and treatment decisions]
    CL_G2[goal: Obtain informed consent before treatment]
    CL_T1[task: Review referral and record decision]
    CL_T2[task: Authorise treatment booking request]
    CL_T3[task: Approve clinic letter content]
    CL_T4[task: Respond to escalated clinical enquiries]
    CL_T5[task: Authorise treatment modification]
    CL_R1[resource: Checked referral package]
    CL_SG1[softgoal: Clinical work not delayed solely by payment gaps]
    CL_SG2[softgoal: Clinical authorisations recorded and protected]
    CL_R1 --> CL_T1
    CL_T1 --> CL_G1
    CL_T2 --> CL_G1
    CL_T3 --> CL_G1
    CL_T4 --> CL_G1
    CL_T5 --> CL_G1
    CL_G2 --> CL_G1
    CL_SG1 --> CL_G1
    CL_SG2 --> CL_G1
  end
  CL --- CL_boundary
  AD([AdministrativeTeam])
  PT([Patient])
  FI([FinanceTeam])
  HPAS([HospitalPatientAdministrationSystem])
  RO([ReferringOrganisation])
  CL_T1 -.->|D2 goal to ReferringOrganisation| RO
  CL_R1 -.->|D4 resource from AdministrativeTeam| AD
  CL_T1 -.->|D5 goal to AdministrativeTeam| AD
  CL_T2 -.->|D6 resource to AdministrativeTeam| AD
  CL_T3 -.->|D7 goal to AdministrativeTeam| AD
  CL_G1 -.->|D8 task on AdministrativeTeam| AD
  CL_G1 -.->|D12 goal to Patient| PT
  CL_G2 -.->|D13 goal on Patient| PT
  CL_SG1 -.->|D18 softgoal on FinanceTeam| FI
  CL_T5 -.->|D19 resource to FinanceTeam| FI
  CL_T4 -.->|D21 task to AdministrativeTeam| AD
  CL_SG2 -.->|D24 softgoal on HospitalPatientAdministrationSystem| HPAS
```

---

## SR-4 · AdministrativeTeam

SD links: **D1**, **D3** (provides), **D4** (provides), **D5**–**D7**, **D8** (provides), **D9**–**D11**, **D14**, **D20** (provides), **D21**, **D22**.

```mermaid
flowchart TB
  AD([AdministrativeTeam])
  subgraph AD_boundary[AdministrativeTeam rationale]
    AD_G1[goal: Keep pathway moving within clinical authorisations]
    AD_T1[task: Check referral documents and request missing items]
    AD_T2[task: Book clinic and treatment appointments]
    AD_T3[task: Notify patient and record contact attempts]
    AD_T4[task: Distribute approved clinic letters]
    AD_T5[task: Route enquiries and escalate clinical matters]
    AD_T6[task: Communicate pathway outcome to referrer when required]
    AD_R1[resource: Authorised referral acceptance]
    AD_R2[resource: Authorised treatment booking request]
    AD_R3[resource: Available appointment slot]
    AD_R4[resource: External clinical service availability]
    AD_SG1[softgoal: No duplicate bookings when external services fail]
    AD_T1 --> AD_G1
    AD_R1 --> AD_T2
    AD_R2 --> AD_T2
    AD_R3 --> AD_T2
    AD_R4 --> AD_T2
    AD_T2 --> AD_G1
    AD_T3 --> AD_G1
    AD_T4 --> AD_G1
    AD_T5 --> AD_G1
    AD_T6 --> AD_G1
    AD_SG1 --> AD_G1
  end
  AD --- AD_boundary
  RO([ReferringOrganisation])
  CL([ClinicalTeam])
  ESS([ExternalSchedulingService])
  ECS([ExternalClinicalServices])
  ECSND([ExternalCorrespondenceService])
  FI([FinanceTeam])
  PT([Patient])
  HPAS([HospitalPatientAdministrationSystem])
  AD_T1 -.->|D1 resource on ReferringOrganisation| RO
  AD_T6 -.->|D3 task to ReferringOrganisation| RO
  AD_T1 -.->|D4 resource to ClinicalTeam| CL
  AD_R1 -.->|D5 goal on ClinicalTeam| CL
  AD_R2 -.->|D6 resource on ClinicalTeam| CL
  AD_T4 -.->|D7 goal on ClinicalTeam| CL
  AD_T2 -.->|D8 task to ClinicalTeam| CL
  AD_R3 -.->|D9 resource on ExternalSchedulingService| ESS
  AD_R4 -.->|D10 resource on ExternalClinicalServices| ECS
  AD_T3 -.->|D11 task on ExternalCorrespondenceService| ECSND
  AD_T4 -.->|D11 task on ExternalCorrespondenceService| ECSND
  AD_G1 -.->|D14 goal on FinanceTeam| FI
  AD_T3 -.->|D20 task to Patient| PT
  AD_T5 -.->|D21 task on ClinicalTeam| CL
  AD_SG1 -.->|D22 softgoal on HospitalPatientAdministrationSystem| HPAS
```

---

## SR-5 · FinanceTeam

SD links: **D14** (provides), **D15**, **D16**, **D17** (provides), **D18** (supports), **D19**, **D23**.

```mermaid
flowchart TB
  FI([FinanceTeam])
  subgraph FI_boundary[FinanceTeam rationale]
    FI_G1[goal: Determine funding before treatment confirmation]
    FI_G2[goal: Collect or refund money correctly]
    FI_T1[task: Record funding approval details]
    FI_T2[task: Request payment or refund via provider]
    FI_T3[task: Investigate missing confirmation without automatic re-charge]
    FI_R1[resource: Treatment and modification context for charges]
    FI_R2[resource: Funding approval record]
    FI_R3[resource: Verified payment or refund result]
    FI_SG1[softgoal: Separate financial authority from clinical necessity]
    FI_SG2[softgoal: Auditable payments without full card storage]
    FI_R1 --> FI_G1
    FI_R2 --> FI_T1
    FI_T1 --> FI_G1
    FI_R3 --> FI_G2
    FI_T2 --> FI_G2
    FI_T3 --> FI_G2
    FI_SG1 --> FI_G1
    FI_SG2 --> FI_G2
  end
  FI --- FI_boundary
  AD([AdministrativeTeam])
  FO([FundingOrganisation])
  PSP([PaymentServiceProvider])
  PT([Patient])
  CL([ClinicalTeam])
  HPAS([HospitalPatientAdministrationSystem])
  FI_G1 -.->|D14 goal to AdministrativeTeam| AD
  FI_R2 -.->|D15 resource on FundingOrganisation| FO
  FI_R3 -.->|D16 resource on PaymentServiceProvider| PSP
  FI_G2 -.->|D17 goal to Patient| PT
  FI_SG1 -.->|D18 softgoal support to ClinicalTeam| CL
  FI_R1 -.->|D19 resource on ClinicalTeam| CL
  FI_SG2 -.->|D23 softgoal on HospitalPatientAdministrationSystem| HPAS
```

---

## SR-6 · ExternalSchedulingService

SD links: **D9** (provides).

```mermaid
flowchart TB
  ESS([ExternalSchedulingService])
  subgraph ESS_boundary[ExternalSchedulingService rationale]
    ESS_R1[resource: Available appointment slot]
    ESS_SG1[softgoal: Availability reliable enough for pending and retry]
    ESS_SG1 --> ESS_R1
  end
  ESS --- ESS_boundary
  AD([AdministrativeTeam])
  ESS_R1 -.->|D9 resource to AdministrativeTeam| AD
```

---

## SR-7 · ExternalClinicalServices

SD links: **D10** (provides).

```mermaid
flowchart TB
  ECS([ExternalClinicalServices])
  subgraph ECS_boundary[ExternalClinicalServices rationale]
    ECS_R1[resource: External treatment laboratory or imaging availability]
    ECS_SG1[softgoal: Signal unavailability without forcing duplicate bookings]
    ECS_SG1 --> ECS_R1
  end
  ECS --- ECS_boundary
  AD([AdministrativeTeam])
  ECS_R1 -.->|D10 resource to AdministrativeTeam| AD
```

---

## SR-8 · ExternalCorrespondenceService

SD links: **D11** (provides).

```mermaid
flowchart TB
  ECSND([ExternalCorrespondenceService])
  subgraph ECSND_boundary[ExternalCorrespondenceService rationale]
    ECSND_T1[task: Deliver outbound correspondence]
  end
  ECSND --- ECSND_boundary
  AD([AdministrativeTeam])
  ECSND_T1 -.->|D11 task to AdministrativeTeam| AD
```

---

## SR-9 · PaymentServiceProvider

SD links: **D16** (provides).

```mermaid
flowchart TB
  PSP([PaymentServiceProvider])
  subgraph PSP_boundary[PaymentServiceProvider rationale]
    PSP_T1[task: Process payment or refund]
    PSP_R1[resource: Verified transaction result]
    PSP_T1 --> PSP_R1
  end
  PSP --- PSP_boundary
  FI([FinanceTeam])
  PSP_R1 -.->|D16 resource to FinanceTeam| FI
```

---

## SR-10 · FundingOrganisation

SD links: **D15** (provides).

```mermaid
flowchart TB
  FO([FundingOrganisation])
  subgraph FO_boundary[FundingOrganisation rationale]
    FO_R1[resource: Funding approval record]
  end
  FO --- FO_boundary
  FI([FinanceTeam])
  FO_R1 -.->|D15 resource to FinanceTeam| FI
```

---

## SR-11 · HospitalPatientAdministrationSystem

SD links: **D22**, **D23**, **D24** (provides softgoal satisfaction to depender actors).

```mermaid
flowchart TB
  HPAS([HospitalPatientAdministrationSystem])
  subgraph HPAS_boundary[HospitalPatientAdministrationSystem rationale]
    HPAS_G1[goal: Coordinate referral booking funding payment and letter stages]
    HPAS_SG1[softgoal: Traceable pathway without duplicate bookings]
    HPAS_SG2[softgoal: Auditable payment trail without full card storage]
    HPAS_SG3[softgoal: Recorded clinical authorisations ordinary-user immutable]
    HPAS_SG1 --> HPAS_G1
    HPAS_SG2 --> HPAS_G1
    HPAS_SG3 --> HPAS_G1
  end
  HPAS --- HPAS_boundary
  AD([AdministrativeTeam])
  FI([FinanceTeam])
  CL([ClinicalTeam])
  HPAS_SG1 -.->|D22 softgoal to AdministrativeTeam| AD
  HPAS_SG2 -.->|D23 softgoal to FinanceTeam| FI
  HPAS_SG3 -.->|D24 softgoal to ClinicalTeam| CL
```

---

## Cross-check checklist (automatable by search)

Search this file for `D1` through `D24`. Each identifier must appear at least once in a dashed dependency edge label. The authoritative direction and dependum text remain those in [`PB-16_sd.md`](PB-16_sd.md) and the catalogue in [`PB-16_istar-sd-sr.md`](PB-16_istar-sd-sr.md).
)
