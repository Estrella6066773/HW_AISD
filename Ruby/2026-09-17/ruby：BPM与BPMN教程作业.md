# Introduction to Business Process Modelling & BPMN

**课程**：Business Process Modelling and Enterprise Architecture & Advanced Information System Development  
**Tutorial**：Introduction to Business Process Modelling；Introduction to BPMN  
**案例**：Hospital Patient Referral, Treatment and Administration System  
**小组**：Ruby / Estrella / Dluffy / Ryan  
**日期**：2026-09-17  
**依据**：两份 tutorial 表格；案例第 1–30 段；Part 1 摘要；Part 5 依赖映射

> 用法：第一节是「要干啥」。后面从 Task 1 起到 Task D 是填好的答案。交仓库时交英文正文即可；中文是给组内讲和答辩用的。

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

目标：搞清 BPMN 怎么建模、什么叫好模型、AS-IS 该用什么记号。

| 题号 | 要交什么 | 怎么做 |
|------|----------|--------|
| Task A | 填 UML vs BPMN 对比表 | 按 Capability / Audience / Adaptability / Scalability / Ability to automation 逐行对比，最后补一行 Purpose |
| Task B | AS-IS 系统该用哪种建模工具，并说明理由 | 结论：**BPMN**（可用 UML Activity 作补充）。要结合医院案例，不要空谈 |
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
- [ ] Task A 表格 6 行都填了
- [ ] Task B 明确写出工具名 + 针对 AS-IS 的理由
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

**Process Identification**  
Decide which processes exist and which ones matter now. The organisation is mapped as a process landscape, not as a list of departments. Criteria such as strategic importance, pain, volume and risk are used to choose a candidate. Output: a process architecture and a shortlist. In our project this is “patient administration path”, not “the whole hospital IT estate”.

**Process Discovery**  
Document the **AS-IS** process: who does what, in what order, with which documents and systems. Sources include interviews, observation, existing forms, emails and the case study. Output: an AS-IS model at an agreed abstraction level. Discovery must record real work, including paper, phone and spreadsheets, not the ideal future path.

**Process Analysis**  
Examine the AS-IS model for waste, delay, risk, handoff failure and rule violations. Qualitative analysis finds bottlenecks and unclear responsibilities; quantitative analysis uses waiting time, backlog and failure rates if data exist. Output: a list of issues with evidence. In the case: fragmented records, no audit trail, unauthorised clinical decisions by admin staff, and external-service failures that create duplicate bookings or duplicate charges.

**Process Redesign**  
Design the **TO-BE** process that removes the issues without breaking mandatory rules. Options include removing waste, tightening gates, automating handoffs, and adding exception paths. Output: a TO-BE model plus change rationale. In our case the redesign cannot let a secretary accept a referral or let finance decide treatment. The gates stay; the medium (email/paper) is replaced by a controlled workflow.

**Process Monitoring**  
After the new process is in use, measure whether it behaves as designed. KPIs include backlog, waiting time, letter delay, unpaid funding, failed payments and unfinished enquiries. Monitoring feeds the next Identification/Analysis cycle. If a letter is unapproved after seven days, the process itself must raise delay and escalation — that is monitoring, not a one-off report.

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

**Aim:** The aim of this tutorial is to explore BPMN and modelling aspects and good practices.  
**Constraint:** For this tutorial, we MUST work in our groups.

---

### Task A · Compare and contrast UML and BPMN

| Criteria | BPMN | UML |
|----------|------|-----|
| **Capability** | Built for end-to-end **business processes**: events, gateways, pools/lanes, message flows, interrupting vs non-interrupting events, compensation. Strong at showing *when work starts, who waits, and how exceptions branch*. | A **family of diagrams** for software structure and behaviour (class, sequence, state, component, deployment, activity). Activity diagrams can show flow, but UML’s centre of gravity is system design, not organisational process. |
| **Audience** | Business analysts, process owners, operations staff, and developers. The same diagram can be discussed with a secretary and later executed in an engine. | Primarily software engineers and architects. Class/sequence diagrams are not intended for a finance clerk or a pathway coordinator. |
| **Adaptability** | One notation scales from a strategic (level-1) map to an operational (level-3) executable model by adding events and data, without changing language. Easy to mark AS-IS (phone, letter, paper) versus TO-BE (workflow tasks). | Highly adaptable **across concerns** (data, interaction, deployment), but switching concern means switching diagram type. Adapting an activity diagram into an implementation usually requires other UML views. |
| **Scalability** | Pools and lanes scale to many roles and organisations (hospital vs payment provider vs GP). Sub-processes hide detail. Collaboration diagrams scale across enterprise boundaries. | Scales well **inside a software system** (packages, components). Cross-organisation work is possible but less natural; there is no first-class “external participant pool”. |
| **Ability to automation** | High. BPMN 2.0 is an **executable** standard. Engines (e.g. Camunda) can run the model, bind user forms, and call external workers. This matches our later AISD work. | Indirect. UML can generate or guide code, especially class/state models, but UML activity diagrams are not the native language of process engines. Automation needs a separate implementation step. |
| **Purpose / focus** *(extra row)* | **What work happens, in what order, under which business rules**, including human tasks and external messages. | **What the software is**: structure, object interaction, and technical behaviour. Process is only one of several views. |

**Short contrast:**  
UML answers “how do we build the system?” BPMN answers “how does the hospital actually move a patient from referral to treatment?” For this unit we need both later (BPMN for process, UML or class/API notes for software), but they are not interchangeable.

---

### Task B · Most appropriate modelling tool for the AS-IS system

**Choice: BPMN 2.0, at a strategic / descriptive level, as the primary AS-IS tool.**  
UML Activity Diagrams may be used as a secondary view if we need to zoom into one software interaction. They are not the best primary choice for this AS-IS.

**Why BPMN fits this AS-IS**

1. **The AS-IS is a cross-role pathway, not a single application.**  
   Today the work already exists: secretaries, consultants, booking teams, finance, call handling, plus letters, phone and paper. BPMN pools/lanes show those roles without pretending there is already one system.

2. **AS-IS includes messages and waiting, not only sequential actions.**  
   Referral packs, appointment letters, two-week phone chases, payment receipts and clinic letters are *message flows* and *wait states*. BPMN events and message flows represent this directly. A UML class diagram cannot.

3. **Exception paths are first-class in the case.**  
   Missing documents, reject/redirect, no slot, unpaid treatment, payment with no hospital receipt, letter delay, DNA. BPMN gateways and boundary events keep these on the same diagram as the happy path. That is what “AS-IS honestly” requires.

4. **External organisations are participants, not just APIs.**  
   GP, insurer, scheduling service, payment provider, lab/imaging sit outside the hospital. BPMN black-box pools show them as independent actors. That matches Task 2.1 dependencies.

5. **The course stack expects BPMN later.**  
   Deliverables already include a strategic BPMN and later an operational BPMN with Camunda forms and workers. Starting AS-IS in BPMN avoids a notation change between discovery and redesign.

**Why not the other common options as the main AS-IS tool**

| Tool | Why not primary for AS-IS |
|------|---------------------------|
| UML Class / Sequence | Good for TO-BE software structure and API calls. They hide the current paper/phone work and the role gates. |
| UML Activity only | Can sketch flow, but weaker on organisational pools, message events, and later execution in a process engine. |
| i* (SD/SR) | Needed for *why* actors depend on each other (goals, soft goals). It does not show sequence, gates or time. Use it alongside BPMN, not instead of it. |
| EPC / flowcharts | Readable, but not the unit standard and not executable. |
| Data-flow diagram | Shows information movement, not responsibility or clinical/finance gates. |

**Abstraction rule for the AS-IS model:**  
Show processes P1–P10, the three internal lanes (Clinical / Admin / Finance), external pools, and the hard gates listed in Task 2.1. Do **not** put form field lists or Camunda worker names on the AS-IS diagram. Those belong to TO-BE operational BPMN.

**Justification in one sentence:**  
The AS-IS system is a human-and-paper specialist-hospital pathway with strict role gates and external messages; BPMN is the notation designed to make that visible, discussable with non-developers, and later refinable into an executable TO-BE model.

---

### Task C · What constitutes a good model?

A good model is **fit for a stated purpose at a stated abstraction level**. Pretty notation is not enough.

Our group checklist:

1. **Purpose is explicit.**  
   AS-IS discovery, TO-BE redesign, execution, or stakeholder goals are different jobs. Mixing them produces a diagram nobody can use. For this tutorial the purpose of the process model is: *show how referral-to-treatment actually runs, including gates and exceptions*.

2. **Right abstraction.**  
   Strategic model: processes, roles, gates, external parties. Operational model: user tasks, forms, workers. A good model omits detail that does not serve the purpose, and says so (our PB-12 acceptance condition).

3. **Correct against the domain.**  
   Every gate in the case must be true in the model: no booking before accept; no treatment booking before clinical authorisation; no letter before approval. If the model allows a secretary to accept a referral, it is a bad model even if it looks neat.

4. **Complete at that level.**  
   Happy path plus the exceptions the case actually names (missing pack, reject, no slot, payment failure, no receipt, letter delay). Invented clinical policy (e.g. how to grade “urgent” calls) must be marked as unresolved, not drawn as fact.

5. **Consistent.**  
   Names of roles, processes and states match Part 1, the backlog IDs, and later BPMN files. One concept, one name.

6. **Understandable to its audience.**  
   A secretary and a developer should both recognise their work. BPMN lanes and plain task names matter more than rare symbols.

7. **Traceable and testable.**  
   A reader can point from a model element to a case paragraph and to a backlog item. If the model claims a gate, a test can fail when that gate is missing.

8. **Honest about AS-IS vs TO-BE.**  
   A good AS-IS model shows email, phone and paper. Hiding them to make the hospital look digital is not modelling; it is wishful TO-BE.

**Group conclusion:**  
A good model is a shared, checkable statement about work. It is good when it is purposeful, correctly abstracted, faithful to the case, consistent with our other artefacts, and usable in the next BPM phase (analysis or redesign).

---

### Task D · Upload to the group repository

Upload this file to the group repository created in the previous tutorial.

**Suggested path:** `Ruby/2026-09-17/ruby：BPM与BPMN教程作业.md`  
After merge to the shared repo, record the commit hash in the contribution log.

| Item | Status |
|------|--------|
| Tutorial 1 Task 1.1–1.2 | Filled |
| Tutorial 1 Task 2.1 stakeholders / processes / dependencies | Filled |
| Tutorial 2 Task A comparison table | Filled |
| Tutorial 2 Task B AS-IS tool + justification | Filled |
| Tutorial 2 Task C good model | Filled |
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
