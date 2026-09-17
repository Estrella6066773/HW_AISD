# Part 1 / 3 / 6 / 8 演讲稿（16 Sep）

---

## 先讲这个：我做了什么 + 我怎么理解（约 1.5 分钟）

老师如果只问贡献和理解，就停在这一节。后面全文是展开用的。斜体英文直接说。

### 开场一句

中文：我是 Hao Zheng。今天只交计划。我主笔 Part 1、Part 6、Part 8，Part 3 我能讲清单怎么从案例来、怎么接到这一期。

*Hi, I am Hao Zheng. Today we only show the plan, not a running system. I led Part 1, Part 6 and Part 8. For Part 3 I can explain the product backlog: where each item comes from, and what we pulled into this sprint.*

### 我做了什么

*What I did.*

*Part 1: I read the case with the group. I wrote the short summary. We answered the eight questions: who is involved, the main path, the rules, the exceptions, and the outside systems. Evidence is the Part 1 table. 〔第1–30段整篇；摘要刀口第3–5段〕*

*Part 3: the product backlog is the full list, 29 items, twelve fields each. I helped check that each item maps to the case, and that Sprint 1 only takes the first slice. 〔作业 Part 3；条目对案例见后文证据表〕*

*Part 6: I made the Sprint 1 backlog and the sprint goal. We picked T01 to T07 and T20. First slice: check papers, doctor decision, first clinic booking. 〔第3–5段；作业 Part 6〕*

*Part 8: I prepared the sprint review. Completed, unfinished, key decisions, and where the IDs match. T01 is done. T03 to T07 are planned, not built. 〔作业 Part 8；T01 第3段〕*

*Next: I finish T02 path notes, then T03 decision fields after this review. 〔第3–4段〕*

### 我对这些部分的理解

*How I understand these parts.*

*Part 1 is “do we get the hospital story?” Not code. Secretaries check papers. Only a doctor can accept. Finance handles money. 〔第3、4、13段〕*

*Part 3 is the full wish list. Everything in the case goes here, even work we will not do this week. 〔作业：Product Backlog = 全部工作〕*

*Part 6 is what we promise now. We pull from Part 3. We do not put treatment, payment or letters in this sprint, because in the case they come after the first visit. 〔第7段以后〕*

*Part 8 is: show the increment, say what is done, say what is not done, and do not hide it. Today the increment is one plan: same IDs, same slice, same GitHub. 〔作业 Part 8〕*

### 被追问时再补这三句

*I am first owner for Part 1, 6 and 8. Second owner can take over if I am stuck.*  
*Done needs evidence. I do not mark T03 done, because there is no form yet.*  
*If the case is unclear, like “urgent” calls, we ask you. We do not invent a rule. 〔第18、30段〕*

---

用法：每段先看中文，再读斜体英文。英文就是你要开口说的。  
**〔第 n 段〕** = 案例原文段落（`Case Study-批注.docx`）。老师追问时指这一段。  
**作业** = Agile Workshop 要求，不是案例正文。  
今天只交计划。现场边讲边打开对应表格。总时长约 8–10 分钟。


---

## 开场（约 30 秒）

中文心里过一遍：专科医院病人路径。今天交计划，不是软件。你讲 Part 1、3、6、8。

*Hi. Our case is a specialist hospital patient path. A patient comes in by referral, then visit, treatment, payment, letters and phone calls. 〔第1段〕 Information is messy now. 〔第2段〕 Today we show the plan only: product backlog and sprint backlog. No diagrams. No code yet. 〔作业 Part 6 / 16 Sep〕 I will cover Part 1, Part 3, Part 6 and Part 8.*

---

## Part 1：案例理解（约 2 分钟）

打开作业 **Part 1 小组摘要表**。八问的出处见文末「Part 1 证据表」。

### 这是什么业务　〔第1段〕

中文：专科医院，不是普通挂号网站。病人从 GP 或别的医院转过来。看病、办事、管钱必须分开。

*This is a specialist hospital, not a normal booking website. Patients come from a GP or another hospital. Medical work, admin work and money work must stay separate. 〔第1段〕*

### 系统要解决什么问题　〔第2段〕

中文：现在信息散在旧系统、邮件、电话、信和本子里。看不清走到哪、延误在哪、谁做的。新系统要把路径串起来，还要挡住越权。

*Today info is in old systems, email, phone, letters and paper. Hard to see progress, delays, or who did what. 〔第2段〕 The new system should connect the path, and stop people doing work they should not do. 〔第1段：三权分开；第8、11、12段：失败时不乱约、不乱扣〕*

### 主流程（本期只走到第 5 段）

中文：秘书收材料 → 医生决定收不收 → 才能约第一次门诊。后面才是治疗、付钱、写信、打电话。全程要留痕。

*Main path: secretary checks papers 〔第3段〕 → doctor accepts or not 〔第4段〕 → only then book the first visit 〔第4–5段〕. After that comes treatment 〔第7段〕, payment 〔第9–13段〕, letters 〔第19–23段〕 and phone 〔第16–18段〕. Keep a full record 〔第26–27段〕. Sprint 1 stops at the first clinic booking. 〔第4段门禁 + 作业 Sprint Goal〕*

### 谁在里面　〔第1段为主；冲突第28段；偏好第29段〕

中文：患者和转诊方；医生和专科护士；秘书、预约组、接线、路径协调；财务；外面的排班、发信、支付、化验影像。

*Main people: patients and the referring doctor; specialist doctors and nurses; secretaries, booking staff, phone staff and the pathway team; finance; and outside services for calendar, letters, payment, labs and scans. 〔第1段列团队；财务细节第9、13段；外部系统第5、8、10段〕*

冲突一句：

*Doctors worry that too much recording steals time. Managers want reports. These two goals conflict. 〔第28段〕*

### 硬规则（老师最爱追，背这 4 句）

1. *Secretaries check papers. They cannot accept or reject the patient.*　〔第3段〕
2. *Book the first visit only after the doctor accepts. Record the reason and who decided.*　〔第4段〕
3. *Admin cannot book treatment without a doctor’s authorisation.*　〔第7段〕 *Finance decides money. Doctors do not approve refunds.*　〔第13段〕
4. *Phone staff must not diagnose, read test results, or suggest treatment.*　〔第17段〕

### 异常、外部系统、要记什么

中文：异常很多。紧急咨询怎么判定，案例没写死，我们问老师，不自己编。

*Exceptions include missing papers 〔第3段〕, reject 〔第4段〕, no slot 〔第6段〕, outside service down 〔第8段〕, payment fail 〔第11段〕, treat first in an emergency 〔第12段〕, and late letters 〔第22段〕. The hospital has not fully defined “urgent”. We ask the tutor. We do not invent policy. 〔第18段 + 第30段〕*

*Outside systems: calendar 〔第5段〕, letters 〔第5段〕, payment company 〔第10段〕, labs and scans 〔第8段〕, the GP 〔第1、19段〕, and the insurer 〔第9段〕.*

*We must record: papers complete or not 〔第3段〕; the doctor’s decision 〔第4段〕; booking window 〔第5段〕; each call result 〔第6段〕; who pays 〔第9段〕; payment status, but never full card numbers 〔第10段〕; letter dates 〔第21段〕; and who did what, when. Normal users cannot edit the audit log. 〔第26–27段〕*

### 小组假设　〔第30段授权我们标缺口、问老师、写假设〕

*Three assumptions. One: we may mock the outside calendar and payment, but we still keep the failure rules. 〔第8、11、12段规则保留；第30段允许假设〕 Two: we do not invent urgency rules. 〔第18段〕 Three: this sprint only covers check papers → doctor decision → first booking. 〔第3–5段；治疗从第7段才开始〕*

---

## Part 3：Product Backlog（约 2 分钟）

打开作业 **Part 3 产品待办表**（29 行、12 字段）。完整段落对照见文末「Part 3 证据表」。

中文：Part 3 是全部工作清单，不是这一周要干完的。

*Part 3 is the full product backlog. It is the whole wish list, not this week’s work. 〔作业 Part 3〕 Each item has twelve fields. It covers modelling, build, testing, review and evidence. We have 29 items, taken from the case plus workshop tasks.*

### 怎么排优先级

*P0 is for the first release. P1 is in the case, but not the first slice. P2 can wait. Most items are still “not started”. That is OK today, because this increment is the plan. 〔作业：16 Sep 交计划〕*

### 指着表讲第一刀（PB-01 到 PB-04）

*Sprint 1 only pulls the first-booking slice.*

- *PB-01: secretaries check papers. They cannot accept.*　〔第3段〕
- *PB-02: the doctor reviews. Accept, reject, ask for more papers, or send to another service. Must record why and who.*　〔第4段〕
- *PB-03: book the first visit only after accept. If no slot, keep pending and tell the pathway team.*　〔第4–6段〕
- *PB-04: normally send a letter. If the visit is within two weeks, also phone, and log every call.*　〔第5–6段〕
- *PB-15 is the review prep. That is why I am speaking now.*　〔作业 Part 8〕

### 明确说本期不做（老师一问就能指段）

*Treatment, payment, clinic letters and phone routing stay on the product backlog. We did not forget them.*

- 治疗授权　PB-05　〔第7段〕
- 外部服务挂了　PB-06　〔第8段〕
- 付钱　PB-07　〔第9–12段〕
- 诊后信　PB-09　〔第19–23段〕
- 接电话分流　PB-10　〔第16–18段〕

*The case puts treatment after the first visit. 〔第7段〕 We keep the sprint goal small.*

老师如果问「为什么 29 条不全做」：

*A product backlog holds all the work. A sprint backlog holds only what we promise now. 〔作业 Part 3 vs Part 6〕*

---

## Part 6：Sprint Backlog（约 2 分钟）

打开作业 **Part 6 Sprint 1 表**。每张卡出处见文末「Part 6 证据表」。

中文：Part 6 是从总清单里挑出来的 Sprint 1 待办。不是再写一份总表。

*Part 6 is the Sprint 1 to-do list. We pick tasks from the product backlog. Not everything goes in. 〔作业 Part 6〕*

### Sprint Goal

*Sprint 1 goal: finish and upload the product backlog and this sprint backlog by 16 September. 〔作业硬检查〕 First slice: referral check → consultant decision → first clinic booking. 〔第3–5段〕 We may mock the outside calendar. 〔第5段外部排班 + 第30段假设〕 Payment, letters and phone routing are out of this sprint. 〔第9–13、19–23、16–18段仍在总清单〕*

### 八张卡，按状态讲

*Each task has two owners, a time estimate, a done-check, and evidence. 〔作业表头〕*

**已经完成**

*T01 is done. Secretaries may request missing papers. They must not accept a referral. 〔第3段〕 Evidence is the permission rule in Part 1.*

**进行中**

*T02 is in progress. Write the main path in words: receive → check papers → send to the doctor. 〔第3–4段〕 No diagram yet. 〔作业：16 Sep 不画图〕*

*T20 is in progress. Upload both tables. All members are on GitHub. Plan only. 〔作业硬检查；不是案例段落〕*

**还没开始，但已经写进这一期**

*T03: four doctor outcomes. Cannot continue without reason and who decided.*　〔第4段〕  
*T04: if rejected, do not book the first visit.*　〔第4段〕  
*T05: admin cannot book before accept.*　〔第4段门禁〕  
*T06: confirm a slot, or keep pending if no slot. Mock is OK. Do not book outside the doctor’s time.*　〔第5–6段；「不约窗外」第6段，随访同款措辞第24段是组内假设〕  
*T07: letter as normal; phone if within two weeks; log every call.*　〔第5–6段〕

### 一句收住

*So this sprint is only T01 to T07, plus T20. Diagrams and code come later, on 28 September. 〔作业时间盒〕*

---

## Part 8：Sprint Review（约 3 分钟）

打开作业 **Part 8 七条**。决策出处见文末「Part 8 证据表」。

中文：今天的增量是计划：同一套编号、同一刀范围、同一个仓库。不是已经跑起来的 Camunda。

*Part 8 is the sprint review. We must show the current integrated increment. 〔作业 Part 8〕 Today that increment is the plan: one ID scheme, one sprint slice, one GitHub repo. Not a running process yet.*

### 1. 已完成

*Completed: case summary, deliverable list, product backlog, task breakdown, dependency map, sprint backlog, and T01 permission rules. 〔T01 = 第3段；其余是作业表〕*

### 2. 未完成（带原因，别装完）

*Unfinished on purpose. T03 to T07 are planned, not built. 〔规则来自第4–6段，今天不实现〕 No form, no worker today. Treatment, payment, letters and phone are outside the sprint goal. 〔第7段以后〕 BPMN, i-star, Camunda and real tests are for 28 September. We will not mark them done.*

### 3. 关键决策

*Key decisions all come from the case. We do not invent rules. 〔第30段〕*

1. *Doctors decide care. Finance decides money. Admin only carries out authorised work.*　〔第1段；钱的边界第13段〕
2. *Sprint 1 stops at the first clinic booking.*　〔第4段：接受后才能约新患〕
3. *We may mock outside services, but failed slots stay pending. No duplicate bookings.*　〔第8段；排班侧第6段〕
4. *If the case is unclear, we ask the tutor. We do not write unofficial policy.*　〔第18段紧急未定 + 第30段〕
5. *Every task has a first owner and a second owner. Done needs evidence.*　〔作业双负责人〕

### 4. 集成证据

边说边指编号：

*Integration today means the IDs match. PB-01 maps to T01 and T02 〔第3–4段〕. PB-02 maps to T03 and T04 〔第4段〕. PB-03 maps to T05 and T06 〔第4–6段〕. PB-04 maps to T07 〔第5–6段〕. PB-15 maps to T20 〔作业〕. Same IDs in Part 3, Part 4 and Part 6. Four members are on GitHub.*

### 5. 测试 / 校验

*Validation today is against the case study text, not a running system. T01 matches paragraph 3: secretaries cannot accept. 〔第3段〕 Executable tests come on 28 September. We will not tick tests as passed in advance.*

28 Sep 打算测什么：

*Later we will test: wrong role cannot accept 〔第3段〕; happy path to first booking 〔第3–5段〕; reject does not create a booking 〔第4段〕; no slot stays pending 〔第6段〕.*

### 6. 已收到的反馈

*Tutor feedback is not in yet. We will record it in the session, with a decision, an owner and a backlog change. Group feedback we already used: do not plan the happy path only 〔第4、6、8、11、12段都有异常〕; mock outside services but keep failure rules 〔第8段〕; done needs evidence 〔作业〕; do not invent urgency policy 〔第18段〕.*

### 7. Backlog 更新

*The product backlog still holds the full case. This sprint only pulled the first booking slice 〔第3–5段〕. Unfinished work stays visible. We do not delete items. 〔作业：条目不删，只移出 sprint〕*

### 收尾

*That is our plan increment for 16 September. Next, 28 September, we implement referral form → doctor decision → mocked booking on one model. 〔第3–5段那一刀的实现〕*

---

## 压缩版（时间不够就只说这些）

1. *This is a hospital patient path: referral, first visit, treatment, payment, letters, phone.*　〔第1段〕
2. *The problem: info is scattered, so delays and actions are hard to track.*　〔第2段〕
3. *Key rule: secretaries check papers; only a doctor can accept and authorise treatment; finance handles money.*　〔第3、4、7、13段〕
4. *Part 3 is the full backlog, 29 items, twelve fields each.*　〔作业 Part 3；条目来自全篇案例〕
5. *Part 6 is Sprint 1 only: check papers → doctor yes or no → first clinic booking.*　〔第3–5段〕
6. *Completed: tables and T01. Unfinished: diagrams, code, payment, letters.*　〔T01=第3段；支付/信=第9–13、19–23段〕
7. *Today we present the plan only. No diagrams, no code yet.*　〔作业〕

---

## 老师追问时怎么接（英文短答 + 指哪一段）

**为什么今天没有图 / 没有系统？**  
*Workshop says 16 Sep is the plan: backlog and sprint backlog. Implementation is 28 Sep.*　〔作业〕

**秘书能不能接受转诊？**  
*No. They only check if papers are complete. Only a doctor can accept.*　〔第3段；医生决策第4段〕

**拒绝以后能不能约门诊？**  
*No. Book the first visit only after the doctor accepts.*　〔第4段〕

**没号怎么办？**  
*Keep it pending. Flag the pathway team. Do not book outside the window.*　〔第6段；随访同款第24段〕

**为什么治疗不进 Sprint 1？**  
*In the case, treatment comes after the first visit.*　〔第7段〕 *We keep the sprint goal small.*

**外部系统怎么办？**  
*We may mock calendar and payment. 〔第5、10段有外部系统；第30段允许假设〕 If the service is down, keep it pending, tell the team, and do not make two bookings.*　〔第8段〕

**付钱失败怎么办？**  
*Not in this sprint. Later: retry is OK, but no double booking and no double charge. 〔第11段〕 If money was taken but we got no confirmation, mark it for check. Do not charge again. 〔第12段〕*

**财务能不能决定要不要治？**  
*No. Doctors do not approve money. Finance does not decide if treatment is needed.*　〔第13段〕

**电话改治疗行不行？**  
*No. Submit a formal request in the system. Email or phone is not enough.*　〔第15段〕

**紧急咨询怎么分级？**  
*The hospital has not fully defined “urgent”. We ask you. We do not invent policy.*　〔第18段；第30段要求问 tutor〕

**接线员能不能给医疗建议？**  
*No. Phone staff must not diagnose, read test results, or suggest treatment.*　〔第17段〕

**Done 凭什么算完成？**  
*Done needs evidence in the repo. A status with no evidence is not done.*　〔作业完成定义〕

**集成在哪？**  
*Same IDs across Part 3, 4 and 6. Same sprint slice 〔第3–5段〕. Same GitHub. Running Camunda comes on 28 Sep.*

**你个人做了什么？**  
*I led the case summary, the sprint backlog, and this review prep. I also covered the product backlog for this talk. Next I close T02 path notes 〔第3–4段〕, then T03 decision fields after the review 〔第4段〕.*

---

## Part 1 证据表（作业 8 问 → 案例哪一段）

打开作业 Part 1 那张摘要时用。

| 作业问的 | 你表里写的 | 原文段落 |
|----------|------------|----------|
| 1. 什么组织 / 业务 | 专科医院；转诊进来；临床/行政/财务分开 | **第1段** |
| 2. 主要利益相关者 | 第1段那些团队 + 患者/转诊方 + 财务 + 外部服务 | **第1段** 列角色；财务细节 **第9、13段**；冲突 **第28段**；患者偏好 **第29段** |
| 3. 主业务流程 | 秘书核材料 → 医生决定 → 约第一次门诊 → 治疗 → 付钱 → 写信/电话 | **第3→4→5→7→9→19/16段**；留痕 **第26–27段**。本期只演示到 **第5段** |
| 4. 系统要解决什么问题 | 信息散、看不清进度/延误/谁做的 | **第2段**；失败时不乱约不乱扣 **第8、11、12段** |
| 5. 关键业务规则 | 见硬规则 4 句 + 表里其余规则 | 秘书 **第3段**；接受后才约、记原因 **第4段**；治疗授权 **第7段**；不存卡号 **第10段**；先付后确认 **第11段**；无回执不自动再扣 **第12段**；退款权限 **第13段**；接线不能诊断 **第17段**；信须批准、超7天延迟 **第20–22段** |
| 6. 异常 / 替代路径 | 缺件、拒绝、没号、外面挂、支付失败、紧急先治、信件超时、紧急未定义 | 缺件 **第3段**；拒绝/转专科 **第4段**；电话失败/没号 **第6段**；外部挂 **第8段**；支付失败 **第11段**；无回执/紧急先治 **第12段**；口头改期无效 **第15段**；紧急咨询未定 **第18段**；信件超时 **第22段** |
| 7. 外部系统 / 组织 | 排班、发信、支付、化验/影像、转诊方、保险 | 排班+发信 **第5段**；化验/影像/外部治疗 **第8段**；支付公司 **第10段**；GP/别的医院 **第1、19段**；保险/资助方 **第9段** |
| 8. 要捕获 / 存储 / 传递 / 验证的信息 | 材料、决定、预约窗、联系结果、授权、资金、支付、信件时间、咨询分类、审计 | 材料 **第3段**；决定 **第4段**；预约请求字段 **第5段**；每次电话结果 **第6段**；治疗授权内容 **第7段**；资金批复 **第9段**；支付回传、禁存卡号 **第10段**；信件时间戳 **第21段**；咨询登记 **第18段**；审计谁/何时/做了啥、不可改 **第26–27段** |
| 小组假设 | mock 排班/支付；紧急规则问老师；第一刀只到第一次门诊 | **第30段** 授权标缺口、问 tutor、写假设；紧急未定 **第18段**；第一刀范围 **第3–5段** |

---

## Part 3 证据表（产品待办每一行 → 案例哪一段）

打开 29 行表时用。作业 12 字段本身来自 **作业 Part 3**，不是案例。

| ID | 表里这条在说什么 | 案例段落 | 这个 sprint |
|----|------------------|----------|-------------|
| PB-01 | 秘书核材料，不能接受/拒绝 | **第3段** | 本期（T01、T02） |
| PB-02 | 医生四态；原因和操作人必填 | **第4段** | 本期（T03、T04） |
| PB-03 | 接受后才约新患；无号标出转路径组 | **第4–6段** | 本期（T05、T06） |
| PB-04 | 常规信；两周内再电话；记下每次结果 | **第5–6段** | 本期（T07） |
| PB-05 | 没医生授权，行政不能办治疗 | **第7段** | 总清单，本期不做 |
| PB-06 | 外部服务挂了：挂起、通知、不重复建号 | **第8段** | 总清单 |
| PB-07 | 谁出钱、外部支付、失败可再付、无回执不自动再扣 | **第9–12段** | 总清单 |
| PB-08 | 紧急可先治，必须写原因，事后交财务 | **第12段** | 总清单 |
| PB-09 | 诊后信批准、7 天、1 月/3 月升级 | **第19–23段** | 总清单 |
| PB-10 | 咨询分流；接线员不能当医生；紧急规则未定 | **第16–18段** | 总清单 |
| PB-11 | 关键动作留痕，普通人改不了 | **第26–27段** | 总清单 |
| PB-12 | 战略 BPMN | 主流程 **第1、3–9、16、19段**；图本身是 **作业 BPM&EA** | 28 Sep |
| PB-13 | Camunda 表单（转诊核验、医生决策） | 采集字段来自 **第4–5段**；表单本身是 **作业 AISD** | 28 Sep |
| PB-14 | 主路径 + 拒绝路径验收测试 | 主路径 **第3–5段**；拒绝 **第4段**；测试格式是 **作业** | 28 Sep |
| PB-15 | Sprint Review 准备 | **作业 Part 8** | 本期（T20） |
| PB-16 | i* SD/SR | 利益相关者 **第1、28、29、30段**；模型是 **作业 BPM&EA** | 28 Sep |
| PB-17 | 举证与贡献记录 | **第30段**（需求组要留下调查/假设）+ **作业举证** | 过程项 |
| PB-18 | 补测：越权、无号、支付失败、无回执 | **第3、6、11、12段** | 后期 |
| PB-19 | 改治疗必须走系统正式申请 | **第15段** | 总清单 |
| PB-20 | 退款只有财务批；整条链可查 | **第13、25段** | 总清单 |
| PB-21 | 随访无号要标出；取消/没来要记录 | **第24–25段** | 总清单 |
| PB-22 | 登录与按岗位最小权限 | **第26段** | 总清单 |
| PB-23 | 化疗复查后只有临床能定继续 | **第14段** | 总清单 |
| PB-24 | 防止配错病人 | **第27段** | 总清单 |
| PB-25 | 系统挂了，事后能补录 | **第27段** | 总清单 |
| PB-26 | 管理报表 vs 医生嫌记太多 | **第28段** | 总清单 |
| PB-27 | 纸质/电子/翻译/代表，做法不统一 | **第29段** | 总清单 |
| PB-28 | 需求追溯矩阵 | **作业追溯要求**；需求来自全篇 | 过程项 |
| PB-29 | 完成定义与证据最低要求 | **作业 Definition of Done** | 过程项 |

---

## Part 6 证据表（Sprint 1 每一行 → 案例哪一段）

打开 Sprint Backlog 表时用。表头（Sprint / Owner / Estimate / Evidence / Status）来自 **作业 Part 6**。

| Task ID | 表里这条 | 案例段落 | 状态怎么报 |
|---------|----------|----------|------------|
| Goal | 第一刀：核材料 → 医生决定 → 第一次门诊；排班可 mock | 范围 **第3–5段**；mock 授权 **第30段**；付钱/信/电话不进本期 = **第7段以后** | 口述 Goal |
| T01 | 秘书可补件，不可接受 | **第3段** | Done |
| T02 | 收件 → 核材料 → 送医生 | **第3–4段** | In progress |
| T03 | 医生四态；原因和操作人必填 | **第4段** | Not started（规则有，表单无） |
| T04 | 拒绝后不约新患 | **第4段**（只有接受后才能约） | Not started |
| T05 | 接受后才能发第一次门诊预约请求 | **第4段门禁**；请求字段 **第5段** | Not started |
| T06 | 外部排班找号；无号 pending，不约窗外 | 找号/确认 **第5段**；无号/急症 **第6段**；「不约窗外」随访原文 **第24段**（组内借来用于第一次门诊，要说是假设） | Not started |
| T07 | 常规信；两周内电话；每次结果都记 | **第5–6段** | Not started |
| T20 | 上传 PB + Sprint 表；四人在 GitHub | **作业硬检查**，不是案例段落 | In progress |

---

## Part 8 证据表（评审 7 条 → 案例 / 作业）

打开 Part 8 准备表时用。

| 作业要出示的 | 你指什么 | 原文 |
|--------------|----------|------|
| 1. Completed tasks | Part 1–6 计划表；T01 Done | T01 = **第3段**；其余 = **作业表** |
| 2. Unfinished tasks | T03–T07 计划未实现；治疗/支付/信/电话不在 Goal | 规则 **第4–6段**；后段工作 **第7段起**；紧急未定 **第18段** |
| 3. Key decisions D01 | 临床 / 行政 / 财务分开 | **第1段** |
| 3. D02 | Sprint 1 只到第一次门诊 | **第4段** |
| 3. D03 | 外部可 mock，失败仍 pending、不重复建号 | **第8段**（排班失败同类 **第6段**） |
| 3. D04 | 案例没写清的不编政策 | **第18段 + 第30段** |
| 3. D05 | 双负责人；没证据不算 Done | **作业** |
| 3. D06 | 无回执不自动再扣；紧急先治要写原因 | **第12段**（本期不演示软件） |
| 4. Evidence of integration | PB↔T 同一套 ID；第一刀同一条路径 | ID 是作业编号；路径是 **第3–5段** |
| 5. Testing / validation | 今天对照案例文字；28 Sep 再跑 | 秘书不能接受 **第3段**；拒绝不约 **第4段**；无号 pending **第6段**；两周内电话 **第5–6段** |
| 6. Feedback received | 组内已改；老师意见现场记 | 异常不能只做 happy path ← **第4、6、8、11、12段**；紧急问 tutor ← **第18段** |
| 7. Backlog updates | 全案仍在 PB；本期只拉第一刀 | 第一刀 **第3–5段**；其余不删 |

---

## 现场别说的

- 不要说已经测过支付、已经跑过流程、已经画好 BPMN。
- 不要把 T03–T07 说成 Done。规则在 **第4–6段**，实现还没有。
- 不要编「怎样算紧急」的医院政策。原文 **第18段** 写明还没定。
- 证据说 GitHub 和作业表格，不要报自己电脑上的文件夹路径。
- 老师给新意见，记下来再改 backlog，不要当场把范围偷偷加大。
- 指段落时说 *paragraph 3 of the case study*，不要说 Word 批注文件名。
