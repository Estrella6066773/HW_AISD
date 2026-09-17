# Introduction to Business Process Modelling · 文档对照批注

对照：`Introduction to Business Process Modelling - Completed.docx`  
用法：左边 / 上边是 Word 里交的英文；下面是中文意思 + 简单开口。  
讲的时候用「简单讲」斜体英文，不要把 Word 长句背下来。

**今天只讲这份表格。不画图，不写代码，不是 Sprint。**  
*This worksheet is about BPM ideas and our hospital. No diagram. No code.*

---

## 0. 封面 / Aim

**Word**  
Introduction to Business Process Modelling  
Aim: establish a thorough understanding of business process, business process modelling, and new ways of representing business processes.

**中文**  
搞清什么是业务流程、怎么给流程建模。

**批注**  
标题有点绕。开口说：这是 BPM 练习，先定义，再套医院。

> *This is the BPM tutorial. We explain process and BPM, then we use our hospital case.*

---

## Task 1.1 · 什么是 Business Process；什么是 BPM

### Define a Business Process

**Word（交上去的）**  
A business process is a structured, repeatable set of activities that transforms inputs into outputs of value for a customer or stakeholder. It has a clear trigger, a sequence of tasks, decision points, roles, and an end state. In a hospital, “referral to first appointment” is a process: the trigger is an incoming referral; the output is either an accepted booking or a recorded rejection. A process is significant because organisations create value when work crosses roles in a controlled order. If the process is unclear, delays, duplicated work and unauthorised actions appear. In our case, clinical judgement, administrative execution and financial approval must stay separate; the process is the mechanism that enforces that separation.

**中文**  
业务流程 = 一组能重复做的步骤。有开始、有步骤、有决定、有谁来做、有结束。把输入变成对别人有用的结果。  
医院例子：转诊进来 → 最后要么约上第一次门诊，要么记下医生拒绝。  
为什么重要：很多人一起干活。步骤不清就会慢、会重复、会越权。  
我们的案例：医生看病、行政办事、财务管钱，必须分开。流程就是用来挡住越权的。

**简单讲**

> *A business process is how work is done, step by step. It has a start and an end.*  
> *Example: a referral comes in. Then the patient gets a first booking, or the doctor says no.*  
> *If the steps are not clear, work is slow, or the wrong person decides.*  
> *Doctors decide care. Finance decides money. Admin only does the paperwork.*

---

### What is BPM? List the main phases

**Word（交上去的）**  
Business Process Management (BPM) is a management discipline for identifying, documenting, analysing, improving, executing and monitoring processes so that they remain aligned with organisational goals. BPM is not only drawing diagrams. It is a cycle: understand the current work, find problems, redesign, put the new design into operation, and check whether it actually improved. Main phases: Process Identification; Process Discovery; Process Analysis; Process Redesign; Process Monitoring.

**中文**  
BPM = 管流程的方法。找到流程、写下来、找问题、改、再检查。不只是画图。是一个循环。  
五个阶段：识别 → 发现现状 → 分析 → 再设计 → 监控。  
（教材里 Redesign 和 Monitoring 之间还有 Implementation。作业只列五个，我们按作业说。）

**简单讲**

> *BPM is how we manage processes. It is not only a picture.*  
> *We find the process, see problems, improve it, then check it later.*  
> *Five steps: Identification, Discovery, Analysis, Redesign, Monitoring.*

---

## Task 1.2 · 五个阶段

**Word 题目**  
Write a brief description of each phase.

每阶段：Word 原句 → 中文 → 简单讲。

### Process Identification

**Word**  
Decide which processes exist and which ones matter now. The organisation is mapped as a process landscape, not as a list of departments. Output: a process architecture and a shortlist. In our project this is the patient administration path, not the whole hospital IT estate.

**中文**  
先问：有哪些流程？现在先做哪一条？不要按部门点名。我们选的是患者这条路，不是整个医院 IT。

**简单讲**  
> *First we choose which process matters. We look at the patient path, not the whole hospital computer system.*

---

### Process Discovery

**Word**  
Document the AS-IS process: who does what, in what order, with which documents and systems. Discovery must record real work, including paper, phone and spreadsheets, not the ideal future path.

**中文**  
写清**今天怎么走（AS-IS）**：谁、按什么顺序、用什么文件。要写纸、电话、表格。不要先画理想系统。

**简单讲**  
> *Discovery means: how does it work today? Paper, phone and email. Not the future system.*

---

### Process Analysis

**Word**  
Examine the AS-IS model for waste, delay, risk, handoff failure and rule violations. In the case: fragmented records, no audit trail, unauthorised clinical decisions by admin staff, and external-service failures that create duplicate bookings or duplicate charges.

**中文**  
找问题：浪费、延误、交接失败、越权。  
这个案例：信息很散；查不到谁做了什么；行政不能替医生决定；外面系统挂了可能重复预约、重复扣款。

**简单讲**  
> *Analysis means: what is wrong today? Information is in many places. Hard to see who did what. Admin cannot decide like a doctor.*

---

### Process Redesign

**Word**  
Design the TO-BE process that removes the issues without breaking mandatory rules. In our case the redesign cannot let a secretary accept a referral or let finance decide treatment. The gates stay; the medium (email/paper) is replaced by a controlled workflow.

**中文**  
设计以后怎么走（TO-BE）。可以换工具（纸 → 系统），**规则不能改**。秘书还是不能接受转诊。财务还是不能决定治不治。

**简单讲**  
> *Redesign means: later we use a system. But the rules stay. A secretary still cannot accept a referral.*

---

### Process Monitoring

**Word**  
After the new process is in use, measure whether it behaves as designed. KPIs include backlog, waiting time, letter delay, unpaid funding, failed payments and unfinished enquiries. If a letter is unapproved after seven days, the process itself must raise delay and escalation.

**中文**  
上线以后盯着看：积压、等待、信晚了、钱没付。信超过 7 天没批准，流程自己要提醒，不是等人写报告。

**简单讲**  
> *Monitoring means: after we change it, we watch delays. If a letter is not approved after seven days, the process should warn us.*

**五阶段收一句**  
> *Today we are only at the first two steps: which path, and how it works now. We have not drawn BPMN yet.*

---

## Task 2.1 · 用医院案例

**Word**  
Case: Hospital Patient Referral, Treatment and Administration System.

**中文**  
专科医院。病人从 GP 或别的医院转来。看病、治疗、付钱、写信、打电话。现在信息很散。新系统要把这条路串起来，并且看病 / 办事 / 管钱分开。

**简单讲**  
> *Our case is a specialist hospital. Patients come by referral. Today information is messy. Medical work, admin work and money must stay separate.*

---

### (1) Stakeholders 利益相关者

**这就是「利益相关者分析」。** Word 问：Identify different stakeholders of the business.

**Word 先写的冲突**  
Clinicians want less recording during clinics; management wants an audit trail. Patients disagree on paper versus electronic contact.

**中文**  
医生嫌看病时记太多；领导要能查记录。患者有的要纸质信，有的要电子。图画规则，不偷偷站队。

**简单讲**  
> *Stakeholders means who is involved, and what they care about.*  
> *Doctors do not want too much recording. Managers want a clear record. We keep both. We do not hide it.*

| Word Category | Word Stakeholder | Word Interest | 中文 | 简单讲 |
|---------------|------------------|---------------|------|--------|
| Patient side | Patient; authorised representative | Timely care, privacy, preferred contact channel | 患者要及时看病、隐私、通知方式可选 | *Patients want care on time, and privacy.* |
| Referrers | GP; other hospitals | Complete referral, feedback on accept/reject | GP 要转诊材料齐，并知道收没收 | *GPs send the patient. They want to know yes or no.* |
| Clinical | Consultant; CNS | Control clinical decisions | 医生决定：收不收、治不治、信能不能发 | *Doctors decide medical things.* |
| Administrative | Secretaries; Bookings; Call Handling; Pathway; Admin Management | Check papers, book, letters, calls — cannot replace the doctor | 行政核材料、约号、发信、接电话；不能当医生 | *Admin does paperwork and booking. Not a doctor.* |
| Finance | Finance Team | Funding, payment, refund — cannot decide whether to treat | 财务管钱、退款；不能决定治不治 | *Finance decides money. Not treatment.* |
| External providers | Scheduling; correspondence; payment; lab/imaging | Slots, letters, charges | 外面帮排班、发信、扣款、化验 | *Outside services: calendar, letters, payment.* |
| Funders | Insurer | Approval number, amount, restrictions | 保险要批复号、金额、限制 | *Insurers care about funding approval.* |
| Governance | Hospital management | Progress, delay, audit | 领导要进度、延误、审计 | *Managers want progress and audit.* |

**表不想逐行念时**  
> *Patients and GPs. Doctors. Secretaries. Finance. Outside services. Managers.*  
> *Doctors decide care. Finance decides money. Admin only does what they are allowed to do.*

---

### (2) Business processes 有哪些流程

**Word**  
The processes below each have a trigger, owner and end state.

**中文**  
每条流程有自己的开始、负责人和结束。不要画成一条糊的线。上场先讲 P1–P4，后面老师问再补。

**简单讲**  
> *We split the work into smaller processes. Each one has a start, an owner, and a rule.*

| ID | Word 流程名 | 中文 | 简单讲 |
|----|-------------|------|--------|
| P1 | Referral receipt and document check | 收转诊、核材料。秘书不能接受。 | *Secretaries check papers. They cannot say yes or no.* |
| P2 | Clinical review of referral | 医生：接受 / 拒绝 / 再要材料 / 转走 | *The doctor decides: yes, no, more papers, or another service.* |
| P3 | New Patient Appointment booking | 只有接受后才能约第一次门诊。没号就等。 | *Only after yes, we book the first visit. No slot, we wait.* |
| P4 | Patient notification and contact log | 写信；两周内再电话并记下 | *We send a letter. If the visit is in two weeks, we also call.* |
| P5 | Treatment authorisation | 看病后医生授权才能约治疗 | *Treatment only after the doctor says yes.* |
| P6 | Treatment / investigation booking | 约治疗；失败就挂起，不重复约 | *Book treatment, or wait. No second booking.* |
| P7 | Funding assessment and payment | 确认治疗前先分清谁出钱 | *We must know who pays, before we confirm treatment.* |
| P8 | Urgent treatment without confirmed payment | 再等会害病人，可以先治，但要记原因 | *If waiting is dangerous, treat first, and write the reason.* |
| P9 | Clinic letter authoring and distribution | 诊后信：医生批准才能发；超 7 天要催 | *The doctor must approve the letter before we send it.* |
| P10 | Enquiry handling | 接电话分流；接线员不能诊断 | *Phone staff must not diagnose.* |
| P11 | Treatment modification | 改治疗必须正式申请；口头/邮件不算 | *Email or verbal change is not enough. Need a formal request.* |
| P12 | Follow-up booking and DNA / cancellation | 随访、取消、没来 | *Follow-up, cancel, or the patient does not come.* |
| P13 | Audit, identity check and management reporting | 审计横切；不替代上面那些流程 | *We record who did what. This does not replace the other steps.* |

**先讲这一句就够**  
> *First: check papers. Then the doctor decides. Then we book the first visit. Then we tell the patient. Treatment and payment come after the first visit.*

---

### (3) Dependencies 依赖

**Word**  
P1 → P2. If P2 = reject/redirect, stop (no New Patient Appointment). If P2 = request more information, return to P1. If P2 = accept → P3 → P4, then first visit → P5 → P6, P7 (P8 only if delay risks the patient), P9, P11. P10 after first visit. P12 follow-up. P13 audit sits on P2, P5, P7, P8, P9, P11.

**中文**  
依赖 = 前面没过，后面不能做。不是图好看就连线。  
秘书核完 → 医生看。医生拒绝 = 停，不准约新患。医生要补件 = 回到秘书。医生接受 = 才能约号、再通知。看病以后才有治疗、付钱、写信。

**简单讲**  
> *Dependency means the next step cannot start too early.*  
> *If the doctor says no, we stop. We cannot book.*  
> *If the doctor wants more papers, we go back to the secretary.*  
> *If the doctor says yes, then we book, then we tell the patient.*

---

### Hard gates 硬规则（Word 最后这段，老师爱问）

| Word | 中文 | 简单讲 |
|------|------|--------|
| Secretaries check papers only and do not decide acceptance | 秘书只核材料，不能决定收不收 | *Secretaries check papers. They cannot say yes or no.* |
| New Patient Appointment only after an authorised Consultant accepts | 只有授权医生接受后才能约第一次门诊 | *We book the first visit only after the doctor says yes.* |
| Admin must not process an unauthorised treatment request | 没医生授权，行政不能办治疗 | *No doctor OK, no treatment booking.* |
| Funding source known before a treatment appointment is confirmed | 确认治疗前先知道谁出钱 | *We must know who pays before we confirm treatment.* |
| Payment succeeds but hospital has no receipt → investigate, do not auto-charge again | 外面扣了钱、本院没回执：标出来查，禁止自动再扣 | *If we are not sure about payment, we check. We do not charge twice.* |
| Clinic letter cannot be sent until the Consultant approves | 信没批准不能发 | *No doctor approval, no letter.* |
| Call handlers must not diagnose | 接线员不能当医生 | *Phone staff must not diagnose.* |
| Verbal or email changes to treatment are invalid | 口头/邮件改治疗不算 | *A phone call cannot change treatment. Need a formal request.* |

**开口只背 4 句**  
> *Secretaries check papers. They cannot say yes or no.*  
> *We book only after the doctor says yes.*  
> *Admin cannot book treatment without the doctor.*  
> *If the outside calendar is down, we wait. We do not make a second booking.*

---

### External dependencies 外部挂了怎么办

| Word 外部 | 用在哪 | Word 失败时 | 简单讲 |
|-----------|--------|-------------|--------|
| Scheduling | P3 / P6 / P12 | pending，不重复约 | *No calendar, we wait. No second booking.* |
| Correspondence | P4 / P9 | 重试，记下发送状态 | *If letters fail, we try again and keep the status.* |
| Payment provider | P7 / P8 | 失败可再付；没回执不自动再扣 | *Retry is OK. Automatic second charge is not.* |
| Lab / imaging / external treatment | P6 | pending + 通知 | *If the lab is down, we wait and tell the team.* |
| Referrer / insurer | P1 / P2 / P7 | 缺材料或缺批复，下一扇门打不开 | *No papers or no funding, the next step cannot start.*

---

## 对着 Word 怎么翻页讲（约 2 分钟）

打开这份 docx，按页说，用自己的话。

1. **Aim**  
   *This is BPM. Ideas first, then the hospital.*

2. **1.1 那两段定义**  
   *A process is work step by step. BPM is how we manage it. Not only a picture. Five steps.*

3. **1.2 五个标题**  
   *We choose the patient path. We write how it works today: paper and phone. Later we change the tool, not the rules.*

4. **2.1 第一张表**  
   *These are stakeholders. Doctors decide care. Finance decides money. Admin cannot act like a doctor.*

5. **2.1 第二张表**  
   *These are processes. I only talk about the first four: papers, doctor yes or no, first booking, then tell the patient.*

6. **最后依赖那段**  
   *If the doctor says no, we stop. We cannot book. That is a dependency.*

---

## 30 秒

*A process is how work is done, step by step. BPM is how we manage it. In this hospital: patients, doctors, admin, finance. Secretaries check papers. Only a doctor can say yes. Then we book the first visit. Today we only explain the Word. No diagram yet.*

---

## 别说的

- 不要背 Word 第一段那句 *structured, repeatable set of activities*。用人话说。  
- 不要从 P1 念到 P13，除非老师指着表。  
- 不要说已经画好 BPMN、已经跑过系统。  
- 不要和旁边 *Introduction to BPMN* 那份混在一起讲。  
- 不要把这里的 P1 说成 Part 6 的 T01。编号不是一套。
