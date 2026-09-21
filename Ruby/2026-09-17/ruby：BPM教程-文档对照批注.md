# Introduction to Business Process Modelling · 文档对照批注

对照：`Introduction to Business Process Modelling - Completed.docx`  
用法：每道题先看 **题目 EN / 题目中文**，再看我们交的答案。上场用「简单讲」，不要背 Word 长句。

**今天只讲这份表格。不画图，不写代码，不是 Sprint。**  
*This worksheet is about BPM ideas and our hospital. No diagram. No code.*

---

## 整张表的题目（先看这个）

Word 上的标题和题目，原句 + 中文。

| Word 原句 | 中文 |
|-----------|------|
| TUTORIAL — Business Process Modelling and Enterprise Architecture & Advanced Information System Development | 教程：业务流程建模与企业架构，以及高级信息系统开发 |
| Introduction to Business Process Modelling | 业务流程建模入门 |
| Aim: The aim of this tutorial is to establish a thorough understanding of business process, business process modelling and to research new ways of representing business processes. | 目的：搞清什么是业务流程、什么是业务流程建模，并研究怎么把流程画出来。（Word 原文有拼写 *through understand*，意思按这句。） |
| Task 1: Understanding Key Concepts | 任务 1：理解关键概念 |
| 1.1: Define Business Process and BPM | 1.1：定义业务流程和 BPM |
| Define a Business Process and explain its significance in an organization. | 什么是业务流程？说明它对一个组织为什么重要。 |
| What is Business Process Management (BPM)? List the main phases involved in BPM. | 什么是业务流程管理（BPM）？列出 BPM 的主要阶段。 |
| 1.2: Research and Review | 1.2：查阅与综述 |
| Use lecture materials or online resources to learn about the five phases of BPM lifecycle | 用讲义或网上资料，了解 BPM 生命周期的五个阶段 |
| Task: Write a brief description of each phase. | 题目：给每个阶段写一段简短说明。 |
| Task 2: Application of Key Concepts | 任务 2：把概念用到案例上 |
| 2.1: Analyse the case study provided | 2.1：分析所给案例 |
| Identify different stakeholders of the business | 找出这项业务里不同的利益相关者（Word 写成 *stake holders*） |
| Identify all the business processes | 找出全部业务流程 |
| Identify the dependencies among the business processes. | 找出这些业务流程之间的依赖关系 |

---

## 0. 封面 / Aim

**题目 EN**  
Introduction to Business Process Modelling  
Aim: The aim of this tutorial is to establish a thorough understanding of business process, business process modelling and to research new ways of representing business processes.

**题目中文**  
业务流程建模入门。  
目的：搞清什么是业务流程、什么是业务流程建模，并研究怎么把流程画出来。

**批注**  
标题有点绕。开口说：这是 BPM 练习，先定义，再套医院。

> *This is the BPM tutorial. We explain process and BPM, then we use our hospital case.*

---

## Task 1 · Understanding Key Concepts

**题目 EN** Task 1: Understanding Key Concepts  
**题目中文** 任务 1：理解关键概念  
（先讲定义，先不要翻到医院那张表。）

---

## Task 1.1 · Define Business Process and BPM

**题目 EN** 1.1: Define Business Process and BPM  
**题目中文** 1.1：定义业务流程和 BPM

### Define a Business Process

**题目 EN** Define a Business Process and explain its significance in an organization.  
**题目中文** 什么是业务流程？说明它对一个组织为什么重要。

**Word（交上去的答案）**  
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

**题目 EN** What is Business Process Management (BPM)? List the main phases involved in BPM.  
**题目中文** 什么是业务流程管理（BPM）？列出 BPM 的主要阶段。

**Word（交上去的答案）**  
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

## Task 1.2 · Research and Review

**题目 EN** 1.2: Research and Review. Use lecture materials or online resources to learn about the five phases of BPM lifecycle: Process Identification; Process Discovery; Process Analysis; Process Redesign; Process Monitoring.  
**题目 EN** Task: Write a brief description of each phase.  
**题目中文** 1.2：查阅与综述。用讲义或网上资料，了解 BPM 生命周期的五个阶段（识别、发现、分析、再设计、监控）。  
**题目中文** 给每个阶段写一段简短说明。

**Word 答案（一张表，不要五段）**  
表头：Phase 阶段 ／ What we do 做什么 ／ Output 产出什么 ／ In our case 我们医院怎么对上

| Phase 阶段 | What we do 做什么 | Output 产出 | In our case 医院 |
|------------|-------------------|-------------|------------------|
| Process Identification 识别 | Decide which processes exist and which one matters now. Map a process landscape, not a department list. 有哪些流程、现在先做哪条。画流程全景，不要按部门点名。 | A shortlist 短名单 | Patient administration path, not the whole hospital IT. 患者这条路，不是整个医院电脑系统。 |
| Process Discovery 发现 | Document AS-IS: who, order, papers and systems. Include paper, phone and spreadsheets. Not the future path. 写清今天怎么走。要写纸、电话、表格。不要先画理想系统。 | AS-IS model 现状模型 | Email, phone, letters and paper. 现在还是邮件、电话、信和纸。 |
| Process Analysis 分析 | Find waste, delay, handoff failure and rule violations. 找浪费、延误、交接失败、越权。 | Issues with evidence 有证据的问题清单 | Scattered records; no audit trail; admin must not decide like a doctor; external failure can duplicate bookings or charges. 信息很散；查不到谁做了什么；行政不能当医生；外面挂了可能重复约号或重复扣款。 |
| Process Redesign 再设计 | Design TO-BE without breaking mandatory rules. Keep the gates; change paper/email into a controlled workflow. 设计以后怎么走。规则不能改，只换工具。 | TO-BE model + why 未来模型 + 理由 | A secretary still cannot accept a referral. Finance still cannot decide treatment. 秘书还是不能接受转诊。财务还是不能决定治不治。 |
| Process Monitoring 监控 | After the new process is in use, measure delays. The process itself must raise warnings. 上线以后盯延误。流程自己要报警，不是写一次报告。 | KPIs and alerts 指标和提醒 | Letter unapproved after 7 days: delay and escalation. 信超过 7 天没批准，就算延迟并升级。 |

**简单讲（指着表，一行一句）**

> *Five phases in one table.*  
> *Identification: we choose the patient path, not the whole hospital IT.*  
> *Discovery: how it works today. Paper, phone and email.*  
> *Analysis: what is wrong. Information is scattered. Admin cannot decide like a doctor.*  
> *Redesign: later we use a system, but the rules stay.*  
> *Monitoring: if a letter is not approved after seven days, the process should warn us.*  
> *Today we are only at the first two steps. No BPMN yet.*

---

## Task 2 · Application of Key Concepts

**题目 EN** Task 2: Application of Key Concepts  
**题目中文** 任务 2：把概念用到案例上

---

## Task 2.1 · Analyse the case study provided

**题目 EN** 2.1: Analyse the case study provided  
**题目中文** 2.1：分析所给案例

案例名 EN：Hospital Patient Referral, Treatment and Administration System  
案例名中文：医院患者转诊、治疗与行政系统

**中文（案例在讲什么）**  
专科医院。病人从 GP 或别的医院转来。看病、治疗、付钱、写信、打电话。现在信息很散。新系统要把这条路串起来，并且看病 / 办事 / 管钱分开。

**简单讲**  
> *Our case is a specialist hospital. Patients come by referral. Today information is messy. Medical work, admin work and money must stay separate.*

---

### (1) Identify different stakeholders of the business

**题目 EN** Identify different stakeholders of the business  
**题目中文** 找出这项业务里不同的利益相关者  
（Word 写成 *stake holders*，开口说 *stakeholders*。）

**这就是「利益相关者分析」。** 问的是：谁被卷进来、各自要什么。

**Word 先写的冲突**  
Clinicians want less recording during clinics; management wants an audit trail. Patients disagree on paper versus electronic contact.

**中文**  
医生嫌看病时记太多；领导要能查记录。患者有的要纸质信，有的要电子。图画规则，不偷偷站队。

**简单讲**  
> *Stakeholders means who is involved, and what they care about.*  
> *Doctors do not want too much recording. Managers want a clear record. We keep both. We do not hide it.*

表头：Category 类别 ／ Stakeholder 谁 ／ Interest 要什么。

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

### (2) Identify all the business processes

**题目 EN** Identify all the business processes  
**题目中文** 找出全部业务流程

**Word 答案开头**  
The processes below each have a trigger, owner and end state.

**中文**  
每条流程有自己的开始、负责人和结束。不要画成一条糊的线。上场先讲 P1–P4，后面老师问再补。

**简单讲**  
> *We split the work into smaller processes. Each one has a start, an owner, and a rule.*

表头：ID 编号 ／ Business process 流程名 ／ Trigger 什么时候开始 ／ Main owner 谁负责 ／ End state 做到什么算结束。

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

### (3) Identify the dependencies among the business processes

**题目 EN** Identify the dependencies among the business processes.  
**题目中文** 找出这些业务流程之间的依赖关系。  
（谁必须先做完，后面才能开始。）

**Word 答案**  
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
