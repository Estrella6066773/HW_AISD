# A 同学答辩讲稿 / Student A Presentation Script（中英双语）

> 用途：汇报 + 现场演示。先看中文，下面英文可直接念（用词简单）。  
> Use: report + live demo. Read Chinese first; English below is ready to speak (simple words).  
> **演示时主要看本文 §4 / §5 / §6 的「▶ 演示时照着点」完整路线块**（★ = 你要重点讲或仔细填的步）。  
> **During demo, follow the full route blocks under ▶ in §4 / §5 / §6** (★ = your key step).  
> 正式演示建议用 `Coursework/hospital-pathway`（英文界面）。

---

## 演示速查 / Demo cheat sheet

| 命名 Name | 章节 | 病例号 Case ID |
|-----------|------|----------------|
| **Audit Line** 审计线 | 下面 §4 | `DEMO-001` |
| **Pay & Treat Line** 付费治疗线 ★主戏 | 下面 §5 | `DEMO-JAVA-01` |
| **Refund Line** 退款变更线 | 下面 §6 | `DEMO-001` |

★ = 你的重点（P5 / P7 / P13 / Java①）。其它步快速点过即可。  
★ = your key steps. Click through the other steps quickly.

---

## 记忆法：先记故事，再记选项 / How to remember: story first, then clicks

选项不是要背清单。**每一条线 = 一个病人故事。**  
选错选项 = 故事走岔路（驳回、随访、医院经费、不付钱……）。  
你只要记住：**这条线想演完哪一个故事**，选项就会自然对上。

*Do not memorise a long list. Each route is one patient story. A wrong click means you leave that story.*

### 三条线各一句话 / One sentence per route

| 线 | 故事（记这个就够） | English |
|----|--------------------|---------|
| **线 4 Audit** | 领导来看报告，看完就结束。 | A manager reads a report, then stop. |
| **线 10 Pay & Treat ★** | 收病人 → 看病 → **决定要治** → 写信 → **病人自己付钱** → Java 扣款 → 约治疗 → 再看病 → **出院**。 | Accept → visit → **treat** → letter → **patient pays** → Java → book treatment → visit again → **discharge**. |
| **线 13 Refund** | 病人要停/出院，**而且涉及退钱**，财务记一笔才能结束。 | Stop care **and money must change**; Finance records it, then end. |

### 线 10 为什么很长？因为它其实只有 4 幕

把 10 多步压成四幕，演示时心里只数 1-2-3-4：

```
第 1 幕  进得去医院     登记转诊 → 医生接受 → 约上号且人来了
第 2 幕  医生说要治     P5 选「治疗」→ 寄信     ★你的
第 3 幕  病人付钱       P7 选「患者付费」+ 10.01 → Java 自动扣款     ★你的
第 4 幕  约上治疗再走   治疗预约 ready → Java 确认（B 的点）→ P5 选「出院」→ 寄信结束     ★你的出院
```

**English (4 acts)**  
1) Get in (referral accepted, patient attends).  
2) Doctor says treat (then send letter).  
3) Patient pays 10.01 (Java payment).  
4) Book treatment, then discharge (send letter, end).

### 口诀（中文 16 字 / English 8 words）

**收、到、治、信、付 10.01、约、出、信**

*In, attend, treat, letter, pay 10.01, book, discharge, letter.*

### 选项记忆：只记「会把故事带偏」的那几个

同一张表常有 3～8 个选项。线 10 **永远选「让故事继续往下治、往下付」的那一项。**  
其它选项不是错，只是**另一条线**。

| 你看到的表 | 线 10 要选 | 别选（会去哪） |
|------------|------------|----------------|
| 登记 Request type | **新转诊 - 材料已核验** / New referral - documents checked | 问询/报告/变更 = 短线；材料缺失 = 补材料环 |
| P2 转诊决定 | **接受** / Accept | 驳回=结束；转科=关闭；要补充=回去补材料 |
| 预约到诊 | **已预约、通知且已到诊** / Booked, notified and attended | 未到诊/取消 = 进变更线 14；待定 = 卡住再约 |
| ★ P5 第一次 | **授权治疗** / Authorise treatment / next cycle | 随访=又去预约；**出院**=最短线 9，**走不到付钱** |
| 寄信 | **已批准信件已寄出** / Approved letter sent and recorded | 退回医生 / 延误 = 不进经费 |
| ★ P7 经费 | **需要患者付费 - 调用支付方** + 金额 **10.01** | **医院经费**=变成 B 的线 11（没有支付 Java）；10.00=支付失败 |
| P6 治疗预约 | **资源可用；预约已确认** | 资源没有 = 约不上，Java② 不跑 |
| ★ P5 第二次 | **授权出院** / Authorise discharge | 再选治疗=又绕一圈；随访=又去预约 |

**最容易错的两步（背下来）**

1. **第一次 P5 必须选「治疗」**，不能选「出院」。选出院就变成短线，**付不了钱、看不到 Java**。  
   *First P5 = treat, not discharge. Discharge skips payment.*  
2. **P7 必须选「患者付费」且金额 10.01**。选医院经费就变成线 11。  
   *P7 = patient payment + 10.01. Hospital funding = Route 11 (B).*

### 填表时其它格子怎么记

每张表几乎都要：病例号 + 人名角色 + 备注。  
**病例号全程同一个；人名和备注瞎填一句即可。真正决定下一条路的，永远是中间那个「结果 / Outcome」下拉框。**

*Same case ID all the way. Names and notes: type anything. Only the Outcome dropdown chooses the next path.*

---

## 0. 一分钟开场 / 1-minute opening

**中文**  
大家好。我负责医院路径里偏**临床授权、经费支付、紧急救治、审计报告**的部分，也就是表格里的 **P5、P7、P8、P13**。  
我会演示三条命名路线：**Audit Line（审计线）**、**Pay & Treat Line（付费治疗线，线 10）**、**Refund Line（退款变更线，线 13）**。  
和 B 同学的分工：我主讲**线 10（付费 + Java 支付）**，B 主讲**线 11（医院经费 + Java 预约确认）**。

**English (simple)**  
Hello. I cover **clinical authorisation, funding and payment, urgent care, and audit reports**. That is **P5, P7, P8, and P13**.  
I will show three named routes: **Audit Line**, **Pay & Treat Line (Route 10)**, and **Refund Line (Route 13)**.  
Split with B: I present **Route 10** (patient payment + Java payment). B presents **Route 11** (hospital funding + Java booking confirm).

---

## 1. 我负责什么 / What I own

| ID | 中文名 | English name | 一句话 |
|----|--------|--------------|--------|
| **P5** | 治疗授权 | Treatment authorisation | 医生决定：继续治疗、随访、还是出院 / Doctor decides: treat, follow-up, or discharge |
| **P7** | 经费与支付 | Funding and payment | 谁出钱；需要时调用外部支付 / Who pays; call outside payment if needed |
| **P8** | 紧急救治 | Urgent care without confirmed payment | 来不及等付款时先治，事后财务跟进 / Treat first if delay is risky; Finance follows later |
| **P13** | 审计与报告 | Audit and management reporting | 谁、何时、做了什么，要可查 / Who did what, and when — must be recorded |

**业务规则（口头金句）**  
医生定医疗，财务定钱，行政不能替医生做决定。  
*Doctors decide care. Finance decides money. Admin cannot take medical decisions.*

---

## 2. 我的三条线（命名）/ My three named routes

| 命名 Name | 对应线 Route | 终点 End | 演示重点 Focus |
|-----------|--------------|----------|----------------|
| **Audit Line** 审计线 | 线 4 / Route 4 | Report reviewed | P13 + 表单 `simple_record` |
| **Pay & Treat Line** 付费治疗线 ★ | 线 10 / Route 10 | Care episode ended | P5 + P7 + **Java① payment** |
| **Refund Line** 退款变更线 | 线 13 / Route 13 | Care episode ended | P7 财务调整 `finance_adjustment` |

另：**Urgent Rule** 紧急规则（P8）——主要指图讲解，线 10 默认不走进去。  
Also: **Urgent Rule (P8)** — explain on the diagram; Route 10 usually skips it.

和 B：  
- 我 = **Pay & Treat Line（线 10）**  
- B = **Hospital Fund Line（线 11）** — 医院经费，无支付 Java，有预约确认 Java  

---

## 3. 我用到的表单 / Forms I explain

### 3.1 `clinical_care` — 临床护理表（P5）

**中文讲**  
这张表问医生「下一步干什么」。三个关键选项：

| 选项（中） | 选项（英） | 接下来 |
|------------|------------|--------|
| 授权治疗 / 下一疗程 | Authorise treatment / next cycle | 寄信后进 **经费 P7** |
| 申请随访复诊 | Request follow-up visit | 回到预约就诊 |
| 授权出院 / 无需继续护理 | Authorise discharge / no further care | 寄信后结束本段诊疗 |

演示线 10 时：第一次选 **治疗**，第二次选 **出院**。

**English (simple)**  
This form asks the doctor: what next?  
- **Treatment** → later we go to funding (P7).  
- **Follow-up** → book another visit.  
- **Discharge** → send letter, then end this care episode.  
On Route 10: first choose **treatment**, later choose **discharge**.

其它字段：病例号、医生姓名角色、备注 —— 填满必填即可。  
Other fields: case ID, clinician name/role, notes — fill required fields.

---

### 3.2 `funding_assessment` — 经费评估表（P7）★ 最重要

**中文讲**  
这是我的核心表。关键字段：

| 字段 | 中文界面 | English UI | 演示怎么填 |
|------|----------|------------|------------|
| 病例号 | 患者 / 病例编号 | Patient / case ID | `DEMO-JAVA-01` |
| **经费结果** | 经费结果 | **Funding outcome** | 见下表 |
| 金额 | 收费金额 | Charge amount | **`10.01`**（成功） |
| 保险号 | 保险 / 经费参考号 | Insurer / funding reference | 可空或随便填 |
| 备注 | 财务备注 | Finance notes | 必填，写一句即可 |

**经费结果（常用）**

| 选这个（中） | English | 会怎样 |
|--------------|---------|--------|
| **需要患者付费 - 调用支付方** | **Patient payment required - call provider** | 触发 **Java①** `request-payment`（我的重点） |
| 医院经费已确认 | Hospital funding confirmed | 不调支付 Java（B 的线 11） |
| 保险批准已记录 | Insurer approval recorded | 不调支付 Java |
| 支付已核验 | Payment already verified | 不调支付 Java |
| 拒绝 / 不完整 / 经费待定 | Declined / incomplete / funding pending | 卡在经费问题处理 |

**金额口诀**  
- `10.01` → 支付成功 → 继续预约  
- `10.00` → 支付失败 → 进「处理经费问题」  

不要输入真实银行卡号（演示禁止）。  
*Never enter a real card number.*

**English (simple)**  
This is my main form.  
Choose **Patient payment required**. Type amount **`10.01`**.  
Then Java worker **`request-payment`** runs by itself — no form.  
`10.01` = success. `10.00` = fail.  
If I choose **Hospital funding confirmed**, we skip payment Java. That is B’s Route 11.

---

### 3.3 `simple_record` — 通用记录表（P13 / 补材料 / 经费问题等）

**中文讲**  
很多「记一笔就过」的步骤用这张表。关键是：

| 字段 | 填什么 |
|------|--------|
| 结果 / Outcome | **已完成并记录 / Completed and recorded** |
| 备注 | 写一句做了什么 |

审计线、转科记录、经费失败后的处理，都会用到它。

**English (simple)**  
This is a simple “record the step” form.  
Choose **Completed and recorded**, write a short note, finish.

---

### 3.4 `finance_adjustment` — 财务调整表（P7，退款线用）

**中文讲**  
病人变更或出院涉及退款、转账、留存时用。关键选项：

| 中 | Eng | 作用 |
|----|-----|------|
| 财务决定已授权且结果已记录 | Financial decision authorised and outcome recorded | 通过 → 可结束 |
| 提供方 / 批准结果待定 | Provider / approval result pending | 还没搞定，会再卡 |

**English (simple)**  
Use this when money must change after a clinical change — refund, transfer, or keep the money.  
For the demo, choose **Financial decision authorised and outcome recorded**.

---

### 3.5 `urgent_authorisation` — 紧急授权表（P8）

**中文讲**  
付款还没确认，但再等会伤害病人时用。医生必须写**理由**。选项：

| 中 | Eng |
|----|-----|
| 授权紧急救治并记录理由 | Authorise urgent care and record reason |
| 不授权 - 继续财务解决 | Not authorised - continue finance resolution |

线 10 正常路径默认 **不进 P8**；汇报时指着图说规则即可。

**English (simple)**  
If waiting for payment is dangerous, the doctor can authorise urgent care and must write a reason.  
Finance follows up later. Our normal Route 10 does not enter P8.

---

## 4. Audit Line（审计线 / 线 4）— 完整路线

**命名**：Audit Line / 审计线  
**时间**：约 1–2 分钟  
**病例号**：`DEMO-001`  
**表单**：`register_request` → `simple_record`

### ▶ 演示时照着点 / Click this during demo

```
开始申请 / Start request
  → P1 / P10 / P13　登记申请；核验材料与身份
     Register request; check documents and ID
     表单 form = register_request
       【选】申请类型 = 管理审计 / 报告
                / Management audit / report
       【填】病例号 = DEMO-001；其它必填随便填

  → ★ P13　授权管理者审阅审计轨迹与路径报告
     Authorised manager reviews audit trail and pathway reports
     表单 form = simple_record
       【选】结果 = 已完成并记录 / Completed and recorded
       【填】备注写一句，例如：Reviewed pathway report for demo.

  → 【终点】报告已审阅 / Report reviewed
```

### 口头稿 / Speak

**中文**  
P13 是横切能力：重要动作要留下审计轨迹。管理者可以审阅报告，但普通用户不能改审计记录。这条线最短，用来说明「系统可追溯」。

**English (simple)**  
P13 means we keep an audit trail — who did what, and when.  
Managers can review reports. Normal users cannot edit the audit.  
This short route shows the process is traceable.

---

## 5. Pay & Treat Line（付费治疗线 / 线 10）— 完整路线 ★主戏

**这条线要干什么？**  
演一遍「自费病人从进院到治完出院」，并**强制走到外部支付 Java**。  
中间那些登记、接受、到诊、寄信，只是为了**合法地走到「付钱」**；不是要你把每张表都讲透。

*What is this route for?*  
Show a **self-pay patient** from arrival to discharge, and **force the payment Java**.  
Register / accept / attend / letter are only the road to payment — click through them.

口诀：**收、到、治、信、付 10.01、约、出、信**

**命名**：Pay & Treat Line / 付费治疗线  
**时间**：约 5–8 分钟  
**病例号**：`DEMO-JAVA-01`（全程同一号）  
**前提**：Camunda 已开；**Java Worker 必须开着**  
**表单顺序**：`register_request` → `review_referral` → `book_visit` → **`clinical_care`** → `dispatch_letter` → **`funding_assessment`** → (Java①) → `book_treatment` → (Java②) → **`clinical_care`** → `dispatch_letter`

### ▶ 演示时照着点 / Click this during demo

```
开始申请 / Start request
  病例号 Case ID 全程 = DEMO-JAVA-01

  → P1 / P10 / P13　登记申请；核验材料与身份
     Register request; check documents and ID
     表单 form = register_request
       【选】申请类型 = 新转诊 - 材料已核验
                / New referral - documents checked
       （快速点 / click through — C 的入口）

  → P2　顾问医生审阅转诊；记录决定与理由
     Consultant reviews referral; records decision and reason
     表单 form = review_referral
       【选】转诊决定 = 接受 / Accept
       （快速点 / click through — C）

  → P3 / P4 / P12　预约就诊；通知患者；记录到诊 / 联系
     Book visit; notify patient; record attendance / contact
     表单 form = book_visit
       【选】结果 = 已预约、通知且已到诊
                / Booked, notified and attended
       （快速点 / click through — B）

  → ★ P5 / P9 / P12　会诊 / 治疗 / 复查；授权护理与门诊信件
     Consult / treat / review; authorise care and clinic letter
     表单 form = clinical_care
       【选】结果 = 授权治疗 / 下一疗程
                / Authorise treatment / next cycle
       【填】医生姓名角色 + 备注必填
       ← 停一下讲：只有医生能授权治疗 / Only a doctor authorises treatment

  → P9　核对并寄送已批准门诊信件
     Check and dispatch approved clinic letter
     表单 form = dispatch_letter
       【选】结果 = 已批准信件已寄出并记录
                / Approved letter sent and recorded
       （快速点 / click through — C）

  → ★ P7　评估经费；记录支付 / 批准状态
     Assess funding; record payment / approval status
     表单 form = funding_assessment
       【选】经费结果 = 需要患者付费 - 调用支付方
                / Patient payment required - call provider
       【填】收费金额 = 10.01 / Charge amount = 10.01
       【填】财务备注随便写一句
       ← 停一下讲：谁出钱；马上调外部支付 / Who pays; call outside payment

  → ★ P7　发出支付请求（Send Task）
     Send payment request to external provider
       ← Java ① request-payment：发布消息 payment-result
  → ★ P7　收到支付结果（Message Catch）
     Payment result received
       ← 关联键 case_reference = 病例号（表单里的 Patient / case ID）
       ← 看控制台 / watch console:
          request-payment SUCCESS ... publishing payment-result
       ← 若卡住：Java 是否开着？病例号是否填了？
          If stuck: Java running? case ID filled?

  → P6　确认已授权治疗与检查预约
     Confirm authorised treatment and investigation appointments
     表单 form = book_treatment
       【选】结果 = 资源可用；预约已确认
                / Resources available; booking confirmed
       （快速点 — B；会触发 Java② / click through — B; triggers Java②）

  → P6　发送预约确认
     Send booking confirmation
       ← Java ② send-booking-confirmation（自动 / automatic）
       ← 一句话：预约确认 Java 由 B 在线 11 细讲
          Booking-confirm Java is B’s focus on Route 11

  → ★ P5 / P9 / P12　会诊 / 治疗 / 复查……（第二次 / second pass）
     表单 form = clinical_care
       【选】结果 = 授权出院 / 无需继续护理
                / Authorise discharge / no further care
       ← 停一下讲：疗程结束后出院 / After treatment, discharge

  → P9　核对并寄送已批准门诊信件
     Check and dispatch approved clinic letter
     表单 form = dispatch_letter
       【选】结果 = 已批准信件已寄出并记录
                / Approved letter sent and recorded

  → 【终点】本段诊疗结束 / Care episode ended
```

### 日志应出现 / Expected logs

```text
request-payment SUCCESS ... publishing payment-result
send-booking-confirmation SENT ...
```

### 口头稿（主戏）/ Main speak

**中文**  
这条线叫 **Pay & Treat Line**。病人已被接受并到诊。  
在 **P5**，医生必须正式**授权治疗**——秘书不能替医生点这一步。  
寄信后进入 **P7**：财务判断谁出钱。我选择**患者付费**，金额 **10.01**，系统调用外部支付服务。  
这一步是 **Java Worker**：没有表单，后台自动完成。日志出现 SUCCESS，说明支付打通。  
然后进入治疗预约；预约确认的 Java 由 B 同学在 **Hospital Fund Line（线 11）** 详细讲。  
治疗后再回到 P5，我选择**出院**，寄信后本段诊疗结束。  
整条线说明：临床门、经费门、外部支付，是串在一起的。

**English (simple)**  
This route is called **Pay & Treat Line**.  
At **P5**, only a doctor can **authorise treatment**. Admin cannot do this.  
At **P7**, Finance decides who pays. I choose **patient payment** and amount **10.01**.  
Then the **Java payment worker** runs by itself. We look for SUCCESS in the log.  
Next is treatment booking. The booking-confirm Java is B’s topic on Route 11.  
Then I come back to P5 and choose **discharge**. After the letter, this care episode ends.  
So clinical rules, money rules, and outside payment work together in one path.

### 若被问：和线 11 有什么不同？

**中文**  
线 10：患者付费 → 有支付 Java①。  
线 11：医院经费 → 没有支付 Java，但仍有预约确认 Java②。  
所以我和 B 一人一条线，都能展示 Java，又不重复讲同一条。

**English (simple)**  
Route 10: patient pays → payment Java runs.  
Route 11: hospital pays → no payment Java, but booking Java still runs.  
A and B each take one route.

---

## 6. Refund Line（退款变更线 / 线 13）— 完整路线

**命名**：Refund Line / 退款变更线  
**时间**：约 2–3 分钟  
**病例号**：`DEMO-001`  
**表单**：`register_request` → `clinical_change` → **`finance_adjustment`**

### ▶ 演示时照着点 / Click this during demo

```
开始申请 / Start request
  病例号 Case ID = DEMO-001

  → P1 / P10 / P13　登记申请；核验材料与身份
     Register request; check documents and ID
     表单 form = register_request
       【选】申请类型 = 授权变更 / 随访 / 取消
                / Authorised change / follow-up / cancellation
       （快速点 / click through）

  → P11 / P12　授权变更、随访或取消
     Authorise modification, follow-up or cancellation
     表单 form = clinical_change
       【选】结果 = 授权停止 / 出院 - 需财务复核
                / Authorise stop / discharge - Finance review required
       （快速点 — D / click through — D）
       ← 可补一句：动到钱必须进财务 / Money affected → Finance must act

  → ★ P7 / P11 / P12　批准并记录退款、转账或留存
     Approve and record refund, payment transfer or retention
     表单 form = finance_adjustment
       【选】结果 = 财务决定已授权且结果已记录
                / Financial decision authorised and outcome recorded
       【填】财务人员姓名角色 + 退款备注必填
       ← 停一下讲：退款/转账要正式记录，不能口头了事
          Refund or transfer must be recorded — not only verbal

  → 【终点】本段诊疗结束 / Care episode ended
```

### 口头稿 / Speak

**中文**  
这条线叫 **Refund Line**。临床变更如果**动到钱**，不能口头改，必须走财务调整。  
财务记录退款、转账或留存后，流程才能干净结束。这体现「钱和医疗决定分开，但变更时要衔接」。

**English (simple)**  
This route is **Refund Line**.  
If a clinical change affects money, Finance must record the refund or transfer.  
We cannot finish with only a verbal change. Care and money stay separate, but they must connect.

---

## 7. P8 Urgent Rule（紧急规则）— 指图讲解

**命名**：Urgent Rule / 紧急规则（一般不单独跑长线）

**中文**  
如果等经费确认会耽误病人，**P8** 允许医生先授权紧急救治，并写清理由；之后财务跟进。  
表单是 `urgent_authorisation`。  
正常 **Pay & Treat Line** 为了演示清晰，默认不插这一步。

**English (simple)**  
If waiting for payment is dangerous, **P8** lets the doctor authorise urgent care and write a reason.  
Finance follows up later. Our normal Route 10 skips this, so the demo stays clear.

---

## 8. 建议汇报结构（总时长约 8–12 分钟）

| 段 | 内容 | 约 |
|----|------|----|
| 1 | 开场：我负责 P5/P7/P8/P13；A 线 10 / B 线 11 | 1 min |
| 2 | 指图：财务泳道 + 支付外部参与者 | 1 min |
| 3 | **Audit Line** 快演示（照 §4） | 1–2 min |
| 4 | **Pay & Treat Line** 主演示（照 §5）+ Java① | 5–7 min |
| 5 | **Refund Line**（照 §6）或口头讲 P8 | 2 min |
| 6 | 小结 | 30 sec |

### 结尾金句 / Closing

**中文**  
总结：我负责把「能不能治（P5）」「谁出钱、怎么付（P7）」「紧急例外（P8）」和「能不能查（P13）」说清楚，并用 **Pay & Treat Line** 证明外部支付 Java 已接上。

**English (simple)**  
To sum up: I explain **treat or not (P5)**, **who pays (P7)**, **urgent exception (P8)**, and **audit (P13)**.  
**Pay & Treat Line** shows the payment Java worker is connected.

---

## 9. 可能被问到 / Likely questions

**Q1：为什么金额要用 10.01？**  
演示约定：`10.01` 成功，`10.00` 失败，方便看两条分支。  
*Demo rule: 10.01 success, 10.00 fail.*

**Q2：不开 Java 会怎样？**  
流程会停在 Send Task「发出支付请求」，或卡在 Message Catch「收到支付结果」（没发到消息 / 病例号对不上）。  
*It stops on the send-task job, or waits forever on the payment-result catch if the message was not published or the case ID does not match.*

**Q3：秘书能选「授权治疗」吗？**  
业务上不能。图上用临床泳道 + 表单表达「必须临床授权」。  
*In real rules, only clinicians authorise treatment.*

**Q4：P7 和 P8 谁先？**  
正常先经费；紧急时 P8 可先救治，财务后补。  
*Normal path: funding first. Urgent path: care first, money later.*

---

## 10. 演示前检查清单 / Checklist

- [ ] Camunda Operate / Tasklist 已开（demo / demo）  
- [ ] `mvn spring-boot:run` 已启动，窗口未关  
- [ ] 未同时开中文版和英文版两套工程  
- [ ] 病例号准备：`DEMO-JAVA-01`（线 10）、`DEMO-001`（线 4 / 13）  
- [ ] 记住主选项：治疗 → 患者付费 → **10.01** → 出院  
- [ ] 演示时打开本文 §4 / §5 / §6 的「▶ 演示时照着点」对照点  

---

## 附录：三条线命名速查 / Name cheat sheet

| 命名 | 线号 | 一句话 |
|------|------|--------|
| **Audit Line** 审计线 | 4 | 管理者审报告 |
| **Pay & Treat Line** 付费治疗线 | 10 | 患者付费 + Java 支付（A 主演示） |
| **Refund Line** 退款变更线 | 13 | 变更后退款/财务调整 |
| **Urgent Rule** 紧急规则 | P8 | 先救治，后财务（指图） |
| （B）**Hospital Fund Line** 医院经费线 | 11 | 医院出钱 + Java 预约确认 |
