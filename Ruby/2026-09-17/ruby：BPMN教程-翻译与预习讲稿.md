# Introduction to BPMN · 翻译 + 预习讲稿

**文件**：`Introduction to BPMN - Completed.docx`  
**用法**：先扫「对照翻译」，上场只说斜体英文。中文是心里过一遍的。  
**时长**：约 3–4 分钟。老师只问一句，用文末「30 秒版」。

---

## 这篇作业在问什么

老师要你们小组搞清三件事：

1. UML 和 BPMN 有什么不一样  
2. 医院**现状（AS-IS）**该用哪种记号画  
3. 什么叫一张好模型  

最后把答案传到小组仓库。

*This tutorial is about modelling, not code. We compare UML and BPMN, choose a tool for the AS-IS hospital path, and say what a good model is.*

---

## 对照翻译（交的 Word 里写了什么）

### Aim

**EN** The aim of this tutorial is to explore the BPMN and modelling aspects and good practices.  
**中** 搞清 BPMN、怎么建模、什么是好做法。必须小组做。

---

### Task A · UML vs BPMN

**题目**：Compare and contrast UML and BPMN modelling notations.  
**中**：对比 UML 和 BPMN 两种建模记号。

老师如果指着表问，按行读斜体英文。每格一句人话。

| 标准 | 中文 | 开口英文 |
|------|------|----------|
| **Capability 能力** | BPMN 画整条业务怎么走。UML 画软件长什么样、怎么跑。 | *BPMN shows the whole business path: tasks, decisions, events, and how people talk. UML shows the software: class, use case, sequence, and activity diagrams.* |
| **Audience 谁看** | BPMN 给业务和开发一起看。UML 主要给工程师看。 | *BPMN is for business people and developers. UML is mainly for software people.* |
| **Adaptability 适用** | BPMN 各行都能用，现状和未来都能画，但只画流程。UML 什么都能画，不限于流程。 | *BPMN can draw today and later, but only processes. UML can model many things, not only process.* |
| **Scalability 变大** | BPMN 用子流程把大图拆小。UML 用包和多张图管大系统，视图必须对得上。 | *BPMN splits a big path into smaller processes. UML splits a big system into packages and many views. Those views must match.* |
| **Automation 能不能跑** | BPMN 补细节后能上引擎；不是每张图都能跑。普通 UML 不能直接跑。 | *BPMN can run on an engine after we add extra detail. Not every BPMN drawing can run. Normal UML cannot run by itself.* |
| **Notation 符号** | BPMN：事件、活动、网关、泳池、泳道、箭头、消息。UML：每种图一套符号。 | *BPMN uses events, tasks, gateways, pools, lanes, and arrows. UML uses different symbols for each diagram type.* |

**开口一句（表不想逐行念时）**

*BPMN models the work. UML models the software. Same project, different job.*

中文：BPMN 画「活怎么干」；UML 画「系统长什么样」。一个项目两种图，不互相替代。

---

### Task B · AS-IS 用什么工具

**题目**：Based on the case study, what is the most appropriate modelling tool for the AS-IS system? Justify.  
**中**：按医院案例，现状系统最该用什么建模工具？说明理由。

**答案**：BPMN（描述层 / 战略层）。  
UML 活动图以后可以补一张软件交互，但不是现状的主工具。

**理由（压缩成四句）**

1. 案例是专科医院**患者路径**，不是一个软件。秘书、医生、预约、财务、接线、信件、电话、纸，再加上外部排班、发信、支付。  
2. 现状图必须画出：**谁做、按什么顺序、卡在哪、失败怎么办**。BPMN 的池/道、消息流、网关就是干这个的。  
3. 案例有硬门禁：医生没接受不能约号；没临床授权行政不能约治疗；信没批准不能发；外部挂了要 pending、不能重复建号。这些和主路径要画在同一张图上。  
4. UML 类图/时序图会从对象和调用画起，等于假装现在已经有一套系统。i* 只回答「谁依赖谁、要什么」，不画顺序。所以现状主工具仍是 BPMN。

**Justification 原句**  
The AS-IS system is a cross-role, paper-and-phone hospital pathway with external participants and strict clinical/finance gates; BPMN is the notation that makes that pathway visible to business and technical readers.

**中** 现状是跨角色、靠纸和电话、有外部参与方、有临床/财务硬门禁的医院路径；BPMN 能让业务和开发都看见这条路径。

**开口**

*For AS-IS we choose BPMN. The case is a hospital path with secretaries, doctors, finance, letters and phone. It is not one application yet. BPMN can show who works, the order, and the gates: no booking before the consultant accepts. UML class diagrams would pretend the system already exists.*

---

### Task C · 什么叫好模型

**题目**：What constitutes a good model?  
**中**：什么算一张好模型？

**定义**  
A good model is a shared, checkable statement about work. It is fit for a stated purpose at a stated abstraction level.  
好模型是对工作的**共享、可核对**的陈述。目的要说清，抽象层也要对。图画得很满但没目的，或把现状纸质工作和未来系统任务混在一张图上，都不是好模型。

| 检验 | 中文 | 开口英文 |
|------|------|----------|
| Purpose 目的 | 这张图只说明今天转诊到治疗怎么走。还不是能跑的系统图。 | *Purpose: this picture shows today’s path. It is not a running Camunda model yet.* |
| Right abstraction 画到哪一层 | 只画流程、角色、门禁、外部方。表单和 worker 先不画。 | *Right level: we draw roles and gates. We do not draw form fields yet.* |
| Correctness 对不对 | 秘书不能接受转诊。没授权不能约治疗。图画漂亮但规则错了，仍是错的。 | *If a secretary can accept a referral, the model is wrong. Pretty is not enough.* |
| Completeness 够不够 | 主路径要有，案例写过的异常也要有。没写死的规则标未定，不自己编。 | *We include the happy path and the exceptions in the case. We do not invent missing rules.* |
| Consistency 名字一致 | 角色名、流程名和 Part 1、backlog 一样。一个意思一个名字。 | *One idea, one name. Same names as Part 1.* |
| Understandability 谁都看得懂 | 秘书和开发都要认得自己的活。用常见符号，任务名说人话。 | *A secretary and a developer should both understand the picture.* |
| Traceability 对得上案例 | 图上每一条门禁都能指回案例。门禁没了，测试就该失败。 | *Each gate must point back to the case. If the gate is missing, a test should fail.* |
| Honesty 别装已经电子化 | 现状要画出邮件、电话、纸。藏起来就是在画未来，不是现状。 | *AS-IS must show email, phone and paper. Do not hide them to look modern.* |

**小组结论**

*A good model is purposeful, correctly abstracted, faithful to the case, consistent, understandable, and usable in the next BPM phase. Pretty notation is not enough.*

中文：目的对、层对、忠于案例、名字一致、双方看得懂、能进入下一阶段。图画得好看不够。

---

### Task D · 上传仓库

**题目**：把答案传到上次 tutorial 建的小组仓库。  
**我们写的**：会把这份完成的 Word，连同 `Ruby/2026-09-17/` 里的笔记一起上传。

*We will upload this worksheet to the group repository.*

---

## 上场讲稿（约 3 分钟）

斜体英文直接说。每段先看中文。

### 开场（20 秒）

中文：这是 BPMN tutorial。小组做。三题：对比、选工具、好模型。

*This is the BPMN tutorial. We worked as a group. Three questions: UML versus BPMN, the AS-IS tool, and what a good model is. Our case is the specialist hospital patient path.*

### Task A（若老师要你念表：约 70 秒）

中文：六行，一行一句。不想念表就只说最后那句。

*Task A. Six points.*

*Capability: BPMN shows the whole business path. UML shows the software.*

*Audience: BPMN is for business people and developers. UML is mainly for software people.*

*Adaptability: BPMN can draw today and later, but only processes. UML can model many things.*

*Scalability: BPMN splits a big path into smaller processes. UML splits a big system into many views.*

*Automation: BPMN can run on an engine after we add extra detail. Normal UML cannot run by itself.*

*Notation: BPMN uses events, tasks, gateways, pools and lanes. UML uses different symbols for each diagram.*

*One line: BPMN is for the hospital path. UML is for the system we will build later.*

### Task B（70 秒）

中文：现状选 BPMN。现在还是纸、电话、跨角色，不是一套系统。

*Task B. For AS-IS we choose BPMN at a descriptive level.*

*The case is not one application. Secretaries check papers. Only a consultant can accept. Then booking, letters, phone, finance, and external scheduling and payment. The model must show who works, in what order, and where work waits or fails.*

*Hard gates must stay visible. No new-patient appointment before accept. No treatment booking without clinical authorisation. No letter before approval. If an external service is down, pending, no duplicate booking.*

*UML class or sequence diagrams start from objects. That pretends the system already exists. i-star is useful for why actors depend on each other, but not for sequence. So BPMN is the primary AS-IS tool.*

### Task C（若老师要你念表：约 60 秒）

中文：八条里优先说目的、对不对、别装电子化。其余被问再补。

*Task C. A good model has a clear purpose and the right level of detail.*

*Purpose: this picture shows today’s path, not a running system.*

*Right level: roles and gates, not form fields.*

*Correctness: if a secretary can accept a referral, the model is wrong.*

*Completeness: we include the exceptions in the case. We do not invent missing rules.*

*Consistency: one idea, one name.*

*Understandability: a secretary and a developer should both understand it.*

*Traceability: each gate must point back to the case.*

*Honesty: AS-IS must show paper and phone. Do not hide them.*

*Pretty notation is not enough.*

### 收尾（15 秒）

*Task D: we upload this worksheet to the group repository. Later we refine the same BPMN into an operational model. We do not change notation.*

---

## 30 秒版（老师只让讲一句）

*We compared UML and BPMN. For the hospital AS-IS we choose BPMN, because the work is still paper, phone and role gates, not one system. A good model is faithful to the case at the right level. Pretty diagrams are not enough.*

中文：对比过了。现状用 BPMN，因为现在还是纸、电话和岗位门禁。好模型要忠于案例、层要选对。好看不够。

---

## 被追问

**为什么不用 UML 活动图当主工具？**  
*Activity diagrams can sketch flow, but they are weaker on pools, messages and later execution. We may use one later as a zoom-in, not as the AS-IS master.*

**i* 呢？**  
*i-star shows why actors depend on each other. BPMN shows the order. We need both later. For AS-IS process, BPMN first.*

**AS-IS 要画到多细？**  
*Strategic level: processes, three lanes — clinical, admin, finance — external pools, and the gates. No form fields. No worker names. That is TO-BE operational BPMN.*

**什么叫画错？**  
*If the model lets a secretary accept a referral, or lets admin book treatment with no authorisation, it is wrong even if it looks neat.*
