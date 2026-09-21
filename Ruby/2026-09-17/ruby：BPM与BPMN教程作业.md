# Introduction to Business Process Modelling & BPMN

**课程**：Business Process Modelling and Enterprise Architecture & Advanced Information System Development  
**Tutorial**：Introduction to Business Process Modelling；Introduction to BPMN  
**案例**：Hospital Patient Referral, Treatment and Administration System  
**小组**：Ruby / Estrella / Dluffy / Ryan  
**日期**：2026-09-17  
**依据**：两份 tutorial 表格；案例第 1–30 段；Part 1 摘要；Part 5 依赖映射

> 用法：第一节是「要干啥」。后面从 Task 1 起到 Task D 是填好的答案。交仓库时交英文正文即可；中文是给组内讲和答辩用的。  
> BPMN 的 Task A 已按 `Introduction to BPMN - Completed(1).docx` 收录；**Task B / C / D 是接着写的提交稿**。

---

## 0. 你要干啥

这两份 Word 不是 Agile Workshop 的 Part 1–8，而是 **BPM&EA 课的 tutorial 表格**。老师要你们先搞懂业务流程和 BPMN，再把医院案例套进去，最后把答案上传到上次 tutorial 建的小组仓库。

必须**小组一起做**（第二份表格写了 *MUST work in your groups*）。

### 第一份：Introduction to Business Process Modelling

目标：搞懂什么是业务流程、什么是 BPM，并研究怎么把流程画出来。

| 题号 | 要交什么 | 怎么做 |
|------|----------|--------|
| Task 1.1 | 定义 Business Process；解释它对组织的意义；定义 BPM；列出 BPM 主要阶段 | 概念题，用讲义/教材语言答，不要抄案例 |
| Task 1.2 | 五阶段各写一段：Identification / Discovery / Analysis / Redesign / Monitoring | 每阶段 3–5 句：做什么、产出什么、和后一阶段怎么接 |
| Task 2.1 | 用**本组医院案例**填三块：stakeholders、business processes、dependencies | 从 Part 1 和 Part 5 抽，不要另编一套流程 |

### 第二份：Introduction to BPMN

目标：搞清 BPMN 怎么建模、什么叫好模型、AS-IS 该用什么记号。Completed 稿里 **Task A 已填完**，后面从 Task B 起要自己写。

| 题号 | 要交什么 | 怎么做 |
|------|----------|--------|
| Task A | 填 UML vs BPMN 对比表 | **已完成**（Completed 文档：Capability / Audience / Adaptability / Scalability / Ability to automation / Notation） |
| Task B | AS-IS 系统该用哪种建模工具，并说明理由 | 结论：**BPMN**。必须扣医院案例，不要空谈 |
| Task C | 什么叫好模型 | 小组讨论口径：目的对、抽象层对、完整、一致、可验证 |
| Task D | 把答案传到小组仓库 | 本文件上传后勾掉 |

### 和 Agile Workshop 的关系

- 这份表格 **不替代** Part 1–8。Part 1 是案例理解，Part 3/6 是 backlog。这里是 BPM 课的概念 + 建模选择题。
- Task 2.1 的流程和依赖必须和 Part 1、Part 5 一致，否则老师两边对不上。
- 现在还不用画 `.bpmn` 图。PB-12 战略 BPMN 仍按原计划后补。本文件只交文字答案。

### 交之前检查

- [ ] 五阶段每段都写了，没有只列标题
- [ ] stakeholders 覆盖临床 / 行政 / 财务 / 患者转诊方 / 外部服务
- [ ] 流程依赖服从案例门禁：未接受不能约号，未授权不能约治疗
- [x] Task A 表格 6 行都填了（Completed 稿）
- [x] Task B 明确写出工具名 + 针对 AS-IS 的理由
- [x] Task C 什么叫好模型已写
- [ ] 已上传小组仓库（Task D）

---

## Tutorial 1 · Introduction to Business Process Modelling

**Aim:** The aim of this tutorial is to establish a thorough understanding of business process, business process modelling, and to research new ways of representing business processes.

---

### Task 1: Understanding Key Concepts

#### 1.1 Define Business Process and BPM

**Define a Business Process and explain its significance in an organisation.**

A **business process** is a structured, repeatable set of activities that transforms inputs into outputs of value for a customer or stakeholder. It has a clear trigger, a sequence of tasks, decision points, roles, and an end state. In a hospital, “referral to first appointment” is a process: the trigger is an incoming referral; the output is either an accepted booking or a recorded rejection.

A process is significant because organisations do not create value through isolated tasks. They create value when work crosses roles in a controlled order. If the process is unclear, delays, duplicated work, and unauthorised actions appear. In our case, clinical judgement, administrative execution and financial approval must stay separate; the process is the mechanism that enforces that separation.

**What is Business Process Management (BPM)? List the main phases involved in BPM.**

**Business Process Management (BPM)** is a management discipline for identifying, documenting, analysing, improving, executing and monitoring processes so that they remain aligned with organisational goals. BPM is not only drawing diagrams. It is a cycle: understand the current work, find problems, redesign, put the new design into operation, and check whether it actually improved.

Main phases (as required by this tutorial):

1. Process Identification  
2. Process Discovery  
3. Process Analysis  
4. Process Redesign  
5. Process Monitoring  

*(The full academic lifecycle also includes Implementation between Redesign and Monitoring. The worksheet lists five phases; we follow that list below.)*

---

#### 1.2 Research and Review — Five phases of the BPM lifecycle

| Phase | What we do | Output | In our case |
|-------|------------|--------|-------------|
| Process Identification | Decide which processes exist and which one matters now. Map a process landscape, not a department list. | A shortlist of processes | Patient administration path, not the whole hospital IT estate |
| Process Discovery | Document AS-IS: who does what, in what order, with which papers and systems. Include paper, phone and spreadsheets. Not the future path. | AS-IS model | Work still sits in email, phone, letters and paper |
| Process Analysis | Find waste, delay, handoff failure and rule violations. | Issues with evidence | Scattered records; no audit trail; admin must not decide like a doctor; external failure can duplicate bookings or charges |
| Process Redesign | Design TO-BE without breaking mandatory rules. Keep the gates; change paper/email into a controlled workflow. | TO-BE model + why | A secretary still cannot accept a referral. Finance still cannot decide treatment |
| Process Monitoring | After the new process is in use, measure delays. The process itself must raise warnings, not a one-off report. | KPIs and alerts | Letter unapproved after 7 days: delay and escalation |

---

### Task 2: Application of Key Concepts

#### 2.1 Analyse the case study provided

Case: **Hospital Patient Referral, Treatment and Administration System**.  
The hospital runs a specialist service. Patients arrive by referral from a GP or another hospital, then move through visit, treatment, payment, letters and phone enquiries. Information currently sits in legacy systems, spreadsheets, email, phone, letters and paper. The proposed system must connect this path and keep medical work, admin work and money work separate.

##### (1) Identify different stakeholders of the business

| Category | Stakeholder | Interest |
|----------|-------------|----------|
| Patient side | Patient; authorised representative | Timely care, privacy, preferred contact channel (letter / electronic / accessible format) |
| Referrers | GP; other hospitals | Complete referral, feedback on accept/reject, later outcome letters |
| Clinical | Consultant; Clinical Nurse Specialist (CNS) and related clinicians | Control clinical decisions: accept referral, authorise treatment, approve letters, change treatment |
| Administrative | Medical Secretaries; Outpatient Bookings; Treatment / Chemo Bookings; Call Handling; Pathway Coordinators; Administrative Management | Check papers, book slots, send letters, route calls, watch delays — **cannot** replace the doctor |
| Finance | Finance Team | Funding decision, payment, refund — **cannot** decide whether to treat |
| External providers | External scheduling service; correspondence service; payment service provider; lab / imaging / external treatment | Slots, letters, charges/refunds, resource availability |
| Funders | Insurer or funding organisation | Approval number, amount, restrictions |
| Governance | Hospital management | Progress, delay, audit, reports — without extra clinical data entry |

**Conflict to keep visible:** clinicians want less recording during clinics; management wants an audit trail. Patients disagree on paper versus electronic contact. The model must show the rule, not pick a side silently.

##### (2) Identify all the business processes

We treat these as distinct processes because each has its own trigger, owner and gate. They form one patient pathway, but they are not one undifferentiated flow.

| ID | Business process | Trigger | Main owner | End state |
|----|------------------|---------|------------|-----------|
| P1 | Referral receipt and document check | New referral arrives | Medical Secretaries | Complete / incomplete pack; **no clinical accept** |
| P2 | Clinical review of referral | Pack sent to Consultant | Consultant | Accept / reject / request more information / redirect |
| P3 | New Patient Appointment booking | Referral accepted by authorised Consultant | Outpatient Bookings + external scheduling | Confirmed appointment, or pending if no slot / service down |
| P4 | Patient notification and contact log | Booking confirmed | Admin + correspondence service | Letter sent; if appointment is within two weeks, phone attempts and outcomes recorded |
| P5 | Treatment authorisation | Patient agrees to treatment after first visit | Consultant | Authorised Treatment Booking Request |
| P6 | Treatment / investigation booking | Authorised request exists | Treatment Bookings + lab/imaging/external treatment | Booked, or pending without duplicate bookings |
| P7 | Funding assessment and payment | Treatment about to be confirmed | Finance + payment provider | Hospital-funded / insurer-funded / patient-paid; paid, failed, or marked for investigation |
| P8 | Urgent treatment without confirmed payment | Delay would risk the patient | Consultant, then Finance | Treatment proceeds; reason recorded; Finance follows up |
| P9 | Clinic letter authoring and distribution | After appointment | Consultant (content) + Secretaries (dispatch) | Approved letter sent; delay/escalation if >7 days / ~1 month / ~3 months |
| P10 | Enquiry handling | Patient or referrer calls | Call Handling, then Admin / Finance / CNS | Logged, routed; handler must not diagnose |
| P11 | Treatment modification | Clinical need to change plan | Consultant; Finance if money is affected | Formal Modification Request; verbal/email change rejected |
| P12 | Follow-up booking and DNA / cancellation | Review due, or patient cancels / does not attend | Bookings + clinical + Finance if paid | Slot booked or pending; DNA outcome recorded |
| P13 | Audit, identity check and management reporting | Cross-cutting; runs with every significant action | System + Admin Management | Who / when / what is recorded; ordinary users cannot edit audit |

##### (3) Identify the dependencies among the business processes

Dependencies come from the case rules, not from convenience. A later process must not start if the gate is closed.

```text
P1 Referral check
   └─ P2 Clinical review (secretary cannot accept)
         ├─ P2 = reject / redirect  →  stop; no New Patient Appointment
         ├─ P2 = request more info  →  back to P1
         └─ P2 = accept
               └─ P3 New Patient Appointment
                     ├─ P4 Notification (letter; phone if within two weeks)
                     └─ first visit happens
                           ├─ P5 Treatment authorisation
                           │     ├─ P6 Treatment booking
                           │     ├─ P7 Funding / payment  (must be known before treatment is confirmed)
                           │     │     └─ P8 Urgent treat-first only if delay risks the patient
                           │     ├─ P9 Clinic letter
                           │     └─ P11 Formal modification (if plan changes)
                           ├─ P10 Call handling (after first visit in the case)
                           └─ P12 Follow-up / DNA
P13 Audit sits on P2, P5, P7, P8, P9, P11 — not a substitute for them.
```

**Hard gates (must appear in the model):**

1. Secretaries check papers only. They do not decide acceptance.  
2. A New Patient Appointment is allowed **only after** an authorised Consultant accepts.  
3. Administrative staff must not process a treatment request that is not clinically authorised.  
4. Funding source must be known before a treatment appointment is confirmed.  
5. If the payment provider succeeds but the hospital has no receipt: mark for investigation; **do not** auto-charge again.  
6. A clinic letter cannot be sent until the Consultant approves it.  
7. Call handlers must not diagnose, interpret results, or suggest treatment.  
8. Verbal or email changes to treatment are invalid; a formal Modification Request is required.

**External dependencies (failure behaviour is part of the process):**

| External service | Used by | If unavailable |
|------------------|---------|----------------|
| Scheduling | P3, P6, P12 | Remain pending; notify responsible team; record retries; no duplicate appointment |
| Correspondence | P4, P9 | Retry; keep send status |
| Payment provider | P7, P8 | Failed: notify and allow retry without duplicate charge. No receipt: investigate, no auto-retry |
| Lab / imaging / external treatment | P6 | Pending + notify; no duplicate booking |
| Referrer / insurer | P1, P2, P7 | Missing pack or missing approval blocks the next gate |

---

## Tutorial 2 · Introduction to BPMN

**Aim:** The aim of this tutorial is to explore the BPMN and modelling aspects and good practices.  
**Constraint:** For this tutorial, you MUST work in your groups.

> Task A 原文照抄 `Introduction to BPMN - Completed(1).docx`。  
> **Task B / C / D 是接着空表写的提交稿**，可直接贴回 Word。

### Task A · Compare and contrast UML and BPMN modelling notations.

| Criteria | BPMN | UML |
|----------|------|-----|
| Capability | Models end-to-end business processes, including tasks, decisions, events and communication between participants. | Models system structure and behaviour using diagrams such as class, use case, sequence and activity diagrams. |
| Audience | Business analysts, process owners and managers, as well as developers implementing workflows. | Mainly software developers, architects and systems analysts; use case and activity diagrams also support business discussions. |
| Adaptability | Applies across industries and supports both AS-IS and TO-BE processes, while remaining focused on process modelling. | Supports many modelling purposes and domains; profiles and stereotypes allow domain-specific extensions. |
| Scalability | Uses subprocesses and reusable processes to manage complexity. Large diagrams still need decomposition to remain readable. | Uses packages, components and multiple diagram views to organise large systems. Views must be kept consistent. |
| Ability to automation | Executable BPMN 2.0 models can run on compatible process engines after adding execution details and integrations; not every diagram is executable. | Can support code generation and simulation with suitable tools. Executable subsets such as fUML exist, but ordinary UML diagrams are not directly executable. |
| Notation | Uses events, activities, gateways, pools, lanes, sequence flows and message flows to describe processes and collaboration. | Uses different symbols for each diagram type, such as classes and associations, actors and use cases, or lifelines and messages. |

---

### Task B · Based on the case study provided, what would be the most appropriate modelling tool for modelling the AS-IS system. Justify your answer.

**Most appropriate tool: BPMN** (descriptive / strategic level).  
UML activity diagrams may be used later as a secondary view of one software interaction. They are not the primary AS-IS tool.

The case describes a specialist hospital **patient pathway**, not a single software application. Referrals currently move through Medical Secretaries, Consultants, Outpatient Bookings, Finance, Call Handling, letters, telephone and paper, plus external scheduling, correspondence and payment services. The AS-IS model must show **who does the work, in what order, and where the work waits or fails**. BPMN is designed for that: pools and lanes show clinical, administrative and finance responsibilities; message flows show letters, phone contact and external replies; gateways show accept / reject / request further information / redirect.

The case also contains **hard gates** that an AS-IS model must not hide. A New Patient Appointment may be arranged only after an authorised Consultant has accepted the referral. Administrative staff must not process an unauthorised treatment request. A clinic letter cannot be sent until the Consultant approves it. If an external service is unavailable, the booking remains pending and duplicate appointments must not be created. BPMN can put these gates and exception paths on the same diagram as the happy path. A UML class or sequence diagram would start from system objects and method calls, which pretends the current work is already one application.

UML remains useful later for software structure. i* is useful for *why* actors depend on each other. Neither replaces BPMN for documenting how the hospital actually runs today. Starting AS-IS in BPMN also matches the later course deliverable: a strategic BPMN that can be refined into an operational, engine-ready model without changing notation.

**One-sentence justification:**  
The AS-IS system is a cross-role, paper-and-phone hospital pathway with external participants and strict clinical/finance gates; BPMN is the notation that makes that pathway visible to business and technical readers.

---

### Task C · What constitutes a good model? Discuss in your groups.

A good model is a shared, checkable statement about work. It is **fit for a stated purpose at a stated abstraction level**. A diagram that looks complete but serves no purpose, or mixes AS-IS paper work with TO-BE system tasks, is not a good model.

Our group agreed on the following tests.

| Test | What it means on this case |
|------|----------------------------|
| Purpose | The AS-IS model exists to show how referral-to-treatment currently runs, including gates and exceptions. It is not yet an executable Camunda diagram. |
| Right abstraction | Strategic BPMN shows processes, roles, gates and external parties. Form fields and worker names belong to the later operational model and should be omitted here, with that choice stated. |
| Correctness | The model must not allow a secretary to accept a referral, or allow treatment booking before clinical authorisation. If it does, it is wrong even if the notation is tidy. |
| Completeness at that level | Happy path plus the exceptions the case actually names: missing documents, reject/redirect, no slot, payment failure, payment with no hospital receipt, letter delay. Rules the case leaves open (how to grade an “urgent” call) must be marked unresolved, not invented. |
| Consistency | Role names, process names and states match Part 1 and the backlog. One concept, one name. |
| Understandability | A secretary and a developer should both recognise their work. Common BPMN symbols and plain task names matter more than rare notation. |
| Traceability | A reader can point from a model element to a case paragraph. If the model claims a gate, a later test can fail when that gate is missing. |
| Honesty (AS-IS vs TO-BE) | A good AS-IS model shows email, phone and paper. Hiding them to make the hospital look digital is wishful TO-BE, not discovery. |

**Group conclusion:**  
A good model is purposeful, correctly abstracted, faithful to the case, consistent with our other artefacts, understandable to its audience, and usable in the next BPM phase (analysis or redesign). Pretty notation is not enough.

---

### Task D · Upload your answers to the group repository you created during the last tutorial.

Upload this file (or the completed Word) to the group repository created in the previous tutorial.

**Suggested path:** `Ruby/2026-09-17/Introduction to BPMN - Completed.docx`  
After merge, record the commit hash in the contribution log.

| Item | Status |
|------|--------|
| Tutorial 1 Task 1.1–1.2 | Filled |
| Tutorial 1 Task 2.1 stakeholders / processes / dependencies | Filled |
| Tutorial 2 Task A comparison table | Copied from Completed worksheet |
| Tutorial 2 Task B AS-IS tool + justification | Filled in this file |
| Tutorial 2 Task C good model | Filled in this file |
| Tutorial 2 Task D repository upload | Pending — do after this file is committed |

---

## Appendix · Mapping to existing group work

| This tutorial | Already in our repo |
|---------------|---------------------|
| Stakeholders | Part 1 Q2；`ruby：part1回答.md` |
| Business processes P1–P13 | Part 1 Q3；`ruby：案例段落精华.md` |
| Dependencies / gates | Part 5；`Ryan：part5依赖映射.md` |
| External services | Part 1 Q7；`Ryan：part1外部系统.md` |
| Exceptions | Part 1 Q6；`Ryan：part1异常路径.md` |
| Later BPMN deliverable | PB-12 战略 BPMN；Part 2 交付物清单 |

If any name in this file drifts from Part 1, Part 1 wins. This tutorial must not invent a second hospital.
