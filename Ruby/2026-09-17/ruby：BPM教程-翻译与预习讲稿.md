# Introduction to Business Process Modelling · 翻译 + 预习讲稿

**文件**：`Introduction to Business Process Modelling - Completed.docx`  
**用法**：可以用自己的话。不要背 Word 长句。上场读「自己的话 · 上场稿」。中文先在心里过一遍。  
**时长**：约 2–3 分钟。老师只问一句，用「30 秒版」。  
**别搞混**：这不是 Part 6，也不是旁边那份 *Introduction to BPMN*。这份讲 **什么是流程 / 什么是 BPM / 医院里谁在、有哪些流程、谁卡住谁**。

---

## 你要干啥（上场前先读这一节）

这是 **BPM&EA 课的 tutorial 表格**，小组做，答案已经填进 Word。老师要听的不是代码、不是 Sprint 表，是三件事：

| 题号 | Word 里叫什么 | 你要证明你会 |
|------|----------------|--------------|
| Task 1.1 | Define a Business Process；What is BPM | 能用人话定义「业务流程」和「BPM」，并列出五个阶段 |
| Task 1.2 | Five phases of BPM lifecycle | 每个阶段：做什么、产出什么、和医院案例怎么对上 |
| Task 2.1 | Analyse the case study | 三块：**stakeholders**、**business processes**、**dependencies** |

现场打开这份 Word。顺序固定：

1. 先讲概念（1.1 + 1.2），**不要一上来念 13 条流程**。  
2. 再讲医院（2.1）：人 → 流程 → 依赖/门禁。  
3. 老师指表，再逐行补；不指表，就用下面的压缩句。

今天的增量仍是**文字理解**。不用画 `.bpmn`，不用跑 Camunda。图是 28 Sep 的 PB-12。

**可以自己讲。** Word 是交上去的答案，开口用短句就行。意思对即可，不必和表格一字不差。

---

## 自己的话 · 上场稿（主用）

每段：先看中文，再读英文。句子都很短。

### 开场

中文：这是 BPM 练习。先讲概念，再讲我们医院。今天没图、没代码。

*This is the BPM tutorial. First I explain the ideas. Then I talk about our hospital. No diagram today. No code.*

### 什么是 process，什么是 BPM

中文：流程就是活怎么一步步干完。有开始，有结束。比如转诊进来，最后要么约上号，要么医生拒绝。

*A business process is how work is done, step by step. It has a start and an end.*

*Example: a referral comes in. In the end, the patient gets a first appointment, or the doctor says no.*

中文：这件事重要，因为很多人一起干活。医生看病，秘书办事，财务管钱。如果步骤不清楚，就会乱、会慢、会越权。

*This is important because many people work together. Doctors, secretaries, and finance. If the steps are not clear, work becomes slow, or the wrong person decides.*

中文：BPM 就是管这些流程。不只是画图。我们先找到流程，看问题，再改进，再检查。

*BPM means we manage these processes. It is not only drawing a picture. We find the process, we look at problems, we improve it, and we check it later.*

*Five steps: find it, see how it works today, find problems, change it, then watch it.*

### 五个阶段（医院版）

中文：我们不管整个医院电脑系统，只管患者这条路。

*We do not look at the whole hospital IT. We only look at the patient path.*

中文：现在还是纸、邮件、电话。要先写清今天怎么走，不要先画理想系统。

*Today the hospital still uses paper, email and phone. We first write how it works now. Not the future system.*

中文：问题是：信息很散，查不到谁做了什么，秘书不能替医生做决定。

*The problems: information is in many places. Hard to see who did what. Admin cannot decide like a doctor.*

中文：以后用系统，但规则不能改。秘书还是不能接受转诊。

*Later we use a system. But the rules stay. A secretary still cannot accept a referral.*

中文：上线以后要盯延误。比如信超过七天没批准，流程自己要提醒。

*After that we watch delays. If a letter is not approved after seven days, the process should warn us.*

*So today we are only at the first two steps: which path, and how it works now.*

### 谁在里面（stakeholders）

中文：利益相关者就是谁被这件事影响到。

*Stakeholders means who is involved, and what they care about.*

*Patients and GPs. Doctors. Secretaries and booking staff. Finance. Outside services for calendar, letters and payment. Also insurers and hospital managers.*

中文：医生决定看病。财务决定钱。行政只做被允许的事，不能当医生。

*Simple rule: doctors decide care. Finance decides money. Admin only does the paperwork and booking. They cannot act like a doctor.*

中文：有一个冲突：医生不想记太多；领导要能查记录。

*There is a conflict. Doctors do not want too much recording. Managers want a clear record. We keep both in the model. We do not hide it.*

### 有哪些流程，谁先谁后

中文：不要把所有事画成一条糊的线。每段活有自己的开始和门。

*We split the work into smaller processes. Each one has a start, an owner, and a rule.*

*First four are enough for now.*

*One: secretaries check the papers. They cannot say yes or no.*

*Two: the doctor decides. Yes, no, ask for more papers, or send to another service.*

*Three: only after yes, we book the first visit. If there is no slot, we wait. We do not fake a booking.*

*Four: we send a letter. If the visit is in two weeks, we also call, and we write down each call.*

中文：看病以后才有治疗、付钱、写信、接电话。今天先不细讲。

*After the first visit, there is treatment, payment, letters and phone calls. Not today in detail.*

中文：依赖就是：前面没过，后面不能做。

*Dependency means: the next step cannot start if the last step is not finished.*

*If the doctor says no, we stop. No first appointment.*

*If the doctor wants more papers, we go back to the secretary.*

*If the doctor says yes, then we book, then we tell the patient.*

### 收尾

中文：答案在 Word 里，会传到小组仓库。以后再画 BPMN。人和规则不变。

*The answers are in this Word file. We upload it to the group repo. Later we draw BPMN. Same people. Same rules.*

---

## 这篇作业在问什么

老师要你们小组搞清四件事：

1. 什么叫 **business process**（业务流程），它对医院为什么重要  
2. 什么叫 **BPM**，五个阶段是什么  
3. 用医院案例指出 **stakeholders**（利益相关者）  
4. 有哪些 **processes**，它们之间怎么 **依赖**（谁先谁后、哪扇门打不开就不能往下走）

*This worksheet is Introduction to Business Process Modelling. First we define process and BPM. Then we apply that to our hospital case: who is involved, which processes exist, and how they depend on each other.*

中文：先定义，再套案例。案例三块 = 谁、干什么、谁卡住谁。

---

## 对照翻译（交的 Word 里写了什么）

### Aim

**EN** The aim of this tutorial is to establish a thorough understanding of business process, business process modelling, and to research new ways of representing business processes.  
**中** 搞清什么是业务流程、怎么给流程建模，并研究怎么把流程画出来。  
（Word 原文有拼写：*establish through understand*，开口时用正确句子。）

---

### Task 1.1 · 什么是 Business Process；什么是 BPM

**题目**：Define a Business Process and explain its significance in an organisation. What is BPM? List the main phases.

| 概念 | 中文 | 开口英文 |
|------|------|----------|
| Business process | 一组可重复的活动：有触发、有步骤、有决策、有角色、有结束状态。把输入变成对客户/利益相关者有价值的输出。 | *A business process is a structured, repeatable set of activities. It has a trigger, steps, decisions, roles, and an end state. It turns inputs into value for a customer or stakeholder.* |
| 医院例子 | 「转诊到第一次预约」就是一条流程。触发 = 转诊进来；结束 = 约上号，或记下拒绝。 | *In our hospital, referral to first appointment is a process. Trigger: a referral arrives. End: a booking, or a recorded rejection.* |
| 为什么重要 | 组织不是靠一个人单独干活创造价值，而是跨角色、按顺序、受控制地交接。流程不清就会延误、重复、越权。 | *Organisations create value when work crosses roles in a controlled order. If the process is unclear, you get delay, duplicate work, and unauthorised actions.* |
| 和案例的扣 | 看病、办事、管钱必须分开。流程就是挡住越权的那套机制。 | *In our case, clinical judgement, admin work and money must stay separate. The process is what enforces that.* |
| BPM | 识别、记录、分析、改进、执行、监控流程的管理方法。不只是画图。是一个循环。 | *BPM is a management discipline. Identify, document, analyse, improve, execute and monitor processes. It is a cycle, not only drawing diagrams.* |
| 五个阶段 | 识别 → 发现现状 → 分析问题 → 重新设计 → 监控 | *Five phases: Identification, Discovery, Analysis, Redesign, Monitoring.* |

**开口一句（定义不想展开时）**

*A process is how work creates value across roles. BPM is the cycle that finds that work, improves it, and checks it still works.*

中文：流程 = 跨角色怎么把活干完。BPM = 找到它、改它、再检查它还好不好。

---

### Task 1.2 · BPM 五个阶段

**题目**：Write a brief description of each phase.  
上场每阶段 **一句英文 + 一句医院对照**。不要把 Word 整段念完。

| 阶段 | 中文（心里过） | 开口英文 | 医院怎么对 |
|------|----------------|----------|------------|
| **Identification 识别** | 有哪些流程、现在先管哪一条。按部门列名单不算。 | *Identification: which processes exist, and which one matters now. Map a process landscape, not a department list.* | *We choose the patient administration path, not the whole hospital IT estate.* |
| **Discovery 发现** | 画出 **AS-IS 现状**：谁、按什么顺序、用什么文件/系统。要画纸、电话、表格，不要画理想未来。 | *Discovery: document the AS-IS path. Who does what, in what order, with which papers and systems. Record real work, including paper and phone.* | *Our case is still email, phone, letters and paper.* |
| **Analysis 分析** | 找浪费、延误、交接失败、越权。要有证据。 | *Analysis: find waste, delay, handoff failure and rule violations. Output is a list of issues with evidence.* | *Records are scattered. No audit trail. Admin must not make clinical decisions. External failures can duplicate bookings or charges.* |
| **Redesign 再设计** | 画 **TO-BE**：改介质（纸→系统），**不改门禁**。秘书仍不能接受转诊。 | *Redesign: design TO-BE without breaking mandatory rules. The gates stay. Email and paper become a controlled workflow.* | *A secretary still cannot accept a referral. Finance still cannot decide treatment.* |
| **Monitoring 监控** | 上线后看积压、等待、信件超时、支付卡住。超 7 天没批信，流程自己要报警。 | *Monitoring: measure backlog, waiting time, letter delay, failed payments. The process itself must raise delay, not a one-off report.* | *If a clinic letter is unapproved after seven days, that is a process signal.* |

**开口一句（五阶段不想逐条念时）**

*We identify the path, discover how it runs today, analyse the pain, redesign the workflow, then monitor delays. Today we are still in identification and discovery. We have not drawn the BPMN yet.*

中文：选哪条路 → 现状怎么走 → 哪里痛 → 怎么改 → 改完怎么盯。今天停在识别和发现。图还没画。

---

### Task 2.1 (1) · Stakeholders 利益相关者

**题目**：Identify different stakeholders of the business.  
这就是「利益相关者分析」：谁被卷进来、要什么、不能越权、有没有冲突。

材料来自 Part 1 第 2 问，不要另编一套人。

| Category | 中文 | 开口英文（Interest） |
|----------|------|----------------------|
| Patient side | 患者、授权代表 | *Patients want timely care, privacy, and a contact channel they can use.* |
| Referrers | GP、其他医院 | *GPs want a complete referral and feedback on accept or reject.* |
| Clinical | Consultant、CNS | *Doctors control clinical decisions: accept, authorise treatment, approve letters.* |
| Administrative | 秘书、预约、接线、路径协调、行政管理 | *Admin check papers, book slots, send letters and route calls. They cannot replace the doctor.* |
| Finance | 财务 | *Finance decides funding, payment and refund. They cannot decide whether to treat.* |
| External | 排班、发信、支付、化验/影像 | *Outside services provide slots, letters and charges.* |
| Funders | 保险/资助方 | *Insurers care about approval number, amount and restrictions.* |
| Governance | 医院管理层 | *Management wants progress, delay and audit, without extra clinical data entry.* |

**必须说出口的冲突**

*One conflict: clinicians want less recording during clinics; management wants an audit trail. Patients also disagree on paper versus electronic letters. The model must show the rule. We do not pick a side silently.*

中文：医生嫌记太多；管理要审计；患者有的要纸、有的要电子。图画规则，不偷偷站队。

**开口一句（表不想逐行念时）**

*Stakeholders: patients and GPs; doctors; admin; finance; outside services; insurers; management. Doctors decide care. Finance decides money. Admin only carries out authorised work.*

---

### Task 2.1 (2) · Business processes 有哪些流程

**题目**：Identify all the business processes.  
Word 里有 P1–P13。上场**不要从 P1 念到 P13**。先说原则，再念 Sprint 1 那四条，其余一句带过。

**原则**

*These are separate processes because each has its own trigger, owner and gate. Together they are one patient pathway, but not one undifferentiated flow.*

中文：每条流程自己有触发、负责人和门。串起来是一条患者路径，但不能画成糊成一团的一张图。

**主路径（优先念）**

| ID | 中文 | 开口英文 |
|----|------|----------|
| P1 | 收转诊、核材料。秘书不能接受。 | *P1: secretaries check papers. They do not accept the referral.* |
| P2 | 医生审核：接受 / 拒绝 / 再要材料 / 转走。 | *P2: the consultant accepts, rejects, asks for more papers, or redirects.* |
| P3 | 只有接受后才能约第一次门诊。没号就 pending。 | *P3: book the first visit only after accept. No slot stays pending.* |
| P4 | 常规写信；两周内再电话并记结果。 | *P4: send a letter. If the visit is within two weeks, also phone and log each call.* |

**第一次门诊之后（老师追问再念）**

- P5 治疗授权　*Treatment only after the doctor authorises it.*  
- P6 约治疗　*Book treatment, or pending, no duplicate booking.*  
- P7 资金/支付　*Know who pays before the treatment slot is confirmed.*  
- P8 紧急先治　*Treat first only if delay risks the patient; record the reason.*  
- P9 诊后信　*Letter cannot go out until the consultant approves it.*  
- P10 接电话　*Call handlers must not diagnose.*  
- P11 改治疗　*Verbal or email change is invalid. Need a formal request.*  
- P12 随访/取消/没来  
- P13 审计（横切，不替代上面那些）　*Audit sits on the key actions. It does not replace them.*

**开口一句**

*The first slice is P1 to P4: check papers, doctor decision, first booking, then notify the patient. Treatment, payment and letters come after the first visit.*

---

### Task 2.1 (3) · Dependencies 依赖和门禁

**题目**：Identify the dependencies among the business processes.  
依赖来自**案例规则**，不是图好看就连。门没开，后面的流程不准开始。

**主链（开口）**

*P1 goes to P2. The secretary cannot accept. If the doctor rejects, we stop. No first appointment. If the doctor wants more papers, we go back to P1. If the doctor accepts, then P3 booking, then P4 notification, then the first visit. Only after that: treatment, payment, letters and phone.*

中文：P1→P2。秘书不能代接受。拒绝就停，不准约新患。要补件就回到 P1。接受才 P3、P4，再看病。治疗和付钱在第一次门诊之后。

**硬门禁（老师最爱追，背这 4 句；其余被问再补）**

1. *Secretaries check papers. They cannot accept or reject.*  
2. *Book the first visit only after an authorised consultant accepts.*  
3. *Admin cannot book treatment without a doctor’s authorisation.*  
4. *Funding must be known before a treatment appointment is confirmed.*

补句（有空再说）：

- *If money was taken but we got no confirmation, mark it for check. Do not charge again.*  
- *A clinic letter cannot be sent until the consultant approves it.*  
- *Call handlers must not diagnose.*  
- *Verbal or email changes to treatment are invalid.*

**外部依赖（一句）**

*If the outside calendar is down, the booking stays pending. No duplicate appointment. Same idea for payment: retry is OK, automatic second charge is not.*

---

## 30 秒版（老师只让讲一句）

*A process is how work is done, step by step. BPM is how we manage it. In the hospital: patients, doctors, admin, finance. Secretaries check papers. Only a doctor can say yes. Then we book the first visit. Today we only explain this. No diagram yet.*

中文：流程就是活怎么一步步干。BPM 就是管它。医院里有患者、医生、行政、财务。秘书核材料，医生才说收，然后才能约号。今天只讲清楚，还没画图。

---

## 被追问（也用短句）

**这和 Part 6 / Sprint 有什么关系？**  
*Part 6 is our sprint to-do list. This is a BPM class exercise. Same hospital. Different paper.*

**Stakeholders 是什么？从哪来的？**  
*Stakeholders are the people involved. We took them from Part 1. We did not make new names.*

**为什么要拆成 13 条？**  
*Because each part has its own start and its own rule. If we put everything in one line, the rules disappear.*

**AS-IS 和 TO-BE？**  
*AS-IS is today: paper and phone. TO-BE is later: same rules, but in a system. We have not drawn TO-BE yet.*

**什么叫依赖？**  
*It means the next step cannot start too early. If the doctor says no, we cannot book.*

**外部系统挂了怎么办？**  
*We wait. We tell the team. We do not make a second booking. We do not charge twice.*

**i* 呢？**  
*That is later. i-star is about why people need each other. Today we only list who they are.*

---

## 现场别说的

- 不要说已经画好 BPMN、已经跑过 Camunda。这份 Word 没有图。  
- 不要把 13 条流程从头念到尾，除非老师指着表。  
- 不要和旁边那份 *Introduction to BPMN* 混讲（那份才是 UML vs BPMN、好模型）。  
- 不要把 Part 6 的 T01–T07 当成这张表的答案。编号不同：这里是 P1–P13。  
- 不要编「怎样算紧急」。P8 只说 delay would risk the patient；紧急咨询规则案例没写死。  
- 指人时说 *stakeholders*，指冲突时说 *clinicians versus management*。

---

## 和已有文档的对应

| 这份 Word | 仓库里已有 |
|-----------|------------|
| Stakeholders | Part 1 Q2；`ruby：part1回答.md` |
| P1–P13 | Part 1 Q3；案例第 3–27 段 |
| 依赖 / 门禁 | Part 5；`Ryan：part5依赖映射.md` |
| 旁边那份 BPMN Word | 另一场 pre：`ruby：BPMN教程-翻译与预习讲稿.md` |
| Sprint 表 | 另一场 pre：`ruby：Part6 Sprint Backlog-上场讲稿.md` |

上场打开：`Introduction to Business Process Modelling - Completed.docx`。  
人从 Task 2.1 第一张表指；门禁从 Word 最后 Hard gates 指。
