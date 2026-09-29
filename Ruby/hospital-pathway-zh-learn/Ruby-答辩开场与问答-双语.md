# Ruby 答辩开场稿（打头阵 · 约 8 分钟）+ 可能问答

**侧重点：Java + 领域库。** 线 4 / 10 / 13 顺序已从 `完整体验路线.md` 贴入第二节，现场指图即可。  
**演示工程：** `Coursework/hospital-pathway`  
**我是谁：** Ruby（成员 A）

计时建议：组员 **约 1 分钟** → 指线 **约 1 分钟** → **Java / 库约 5–6 分钟** → 收尾 **约 1 分钟**。

---

## 〇、开场

大家好，我是 Ruby。我先总起介绍分工，然后重点讲我做的 Java 工作器和数据库，大约八分钟。

Hello everyone. I am Ruby. I will open with our team split, then focus on my Java workers and database, about eight minutes.

---

## 一、项目 + 组员（约 1 分钟）

我们用 Camunda 8 跑医院护理路径：BPMN + 表单 + Spring Boot JobWorker + 领域 H2 库。

We run a hospital pathway on Camunda 8: BPMN, forms, Spring Boot job workers, and a domain H2 database.

| 同学 | 一句话 | 主要 Java |
|------|--------|-----------|
| **我 · Ruby · A** | 钱：付、查、退 | `request-payment`；`mark-payment-investigate`；`request-refund` → `payment_ledger` |
| **Estrella · B** | 号：占号 / 确认 | `check-slot`；`reserve-appointment`；`flag-resource-unavailable`；`send-booking-confirmation` → `booking_slot` |
| **Ender · C** | 信 / 转诊通知 | `dispatch-clinic-letter`；`notify-referrer`（方向）→ 审计 |
| **Ryan · D** | 变更通知 | `notify-care-change` → `audit_event` |

One-line map: **A = money**; **B = slots**; **C = letters**; **D = change notice**.

涉钱变更时，D 只写通知回执；**真正退款仍走我的 `request-refund`**。  
If money is affected, D only writes a notice receipt; **the real refund is still my `request-refund`**.

---

## 二、线 4 / 10 / 13（自 `完整体验路线.md` 复制 · 指图用）

讲的时候侧重点仍在 Java；下面顺序对照图指一下即可。  
口诀：**付 · 查 · 退**。 / Remember: **pay · investigate · refund**.

### 线 4｜P13 审计报告 → 报告已审阅  
### Route 4｜P13 Audit report → Report reviewed

```
开始申请 / Start request
  → P1 / P10 / P13　登记申请；核验材料与身份
     Register request; check documents and ID
       【选】申请类型 = 管理审计 / 报告 / Management audit / report
  → P13　授权管理者审阅审计轨迹与路径报告
     Authorised manager reviews audit trail and pathway reports
       【选】结果 = 已完成并记录 / Completed and recorded
  → 【终点】报告已审阅 / Report reviewed
```

### 线 10｜★ 完整体验 + Java → 本段诊疗结束  
### Route 10｜★ Full path + Java → Care episode ended

病例号 `DEMO-JAVA-01`。A 重点：`request-payment`；可选失败支 `mark-payment-investigate`。

```
开始申请 / Start request
  → P1 登记　【选】新转诊 - 材料已核验 / New referral - documents checked
  → P2 转诊　【选】接受 / Accept
  → P3/P4 预约　【选】已预约、通知且已到诊 / Booked, notified and attended
       ← B：check-slot（自动）
  → ★ P5 临床　【选】授权治疗 / Authorise treatment / next cycle
  → P9 寄信　【选】已批准信件已寄出 / Approved letter sent and recorded
  → ★ P7 经费　【选】需要患者付费 - 调用支付方 / Patient payment required
                【填】金额 = 10.01（成功）或 10.00（失败演示）
  → ★ Send Task「发出支付请求」← Java ① request-payment（发布 payment-result）
  → Message Catch「收到支付结果」
       · 10.01 成功 → 继续治疗预约
       · 10.00 失败 → ★ Mark payment investigate ← Java mark-payment-investigate
                      → P7 Funding issue（人工）→ 再评经费
  → P6 治疗预约　【选】资源可用；预约已确认
       ← B：reserve-appointment（自动）
  → Send Task「发送预约确认」← Java ② send-booking-confirmation（B）
  → ★ P5 第二次　【选】授权出院 / Authorise discharge
  → P9 寄信　【选】已批准信件已寄出
  → 【终点】本段诊疗结束 / Care episode ended
```

成功日志：

```text
request-payment SUCCESS ... publishing payment-result
send-booking-confirmation SENT ...
```

失败（10.00）额外日志：

```text
mark-payment-investigate case=... status=INVESTIGATE ...
```

### 线 13｜登记进变更 → 财务调整 → 退款 Java → 出院  
### Route 13｜Change → finance adjustment → request-refund Java → ended

A 重点：表单后自动跑 **`request-refund`**，写 `payment_ledger`。

```
开始申请 / Start request
  → P1 登记　【选】授权变更 / 随访 / 取消 / Authorised change / follow-up / cancellation
  → P11/P12 变更　【选】授权停止 / 出院 - 需财务复核
                / Authorise stop / discharge - Finance review required
       ← D：notify-care-change（自动）
  → ★ P7 财务调整　form = finance_adjustment
       【选】财务决定已授权且结果已记录 / Financial decision authorised and outcome recorded
  → ★ Service Task「Request refund」← Java request-refund（写 payment_ledger SUCCESSFUL）
       ← 控制台：request-refund case=... decision=resolved status=SUCCESSFUL
  → 【终点】本段诊疗结束 / Care episode ended
```

若选「提供方结果待定 / pending」→ `request-refund` 写 **INVESTIGATE**，网关回到财务调整重试。

---

## 三、我的 Java（核心 · 约 5–6 分钟）

### 3.1 两个类、三个类型

代码位置：

- `HospitalPathwayWorkers.java` → **`request-payment`**（既有；我主讲）
- `RefundWorkers.java` → **`request-refund`**、**`mark-payment-investigate`**（我一责新加）

审计 actor 写 **`ruby`**。类名是 `RefundWorkers`，按退款这个职责命名。  
Audit actor is **`ruby`**. The class is `RefundWorkers`, named for the refund work.

图上挂点（指 BPMN）：

- **付**：Send Task「发出支付请求」→ Message Catch「收到支付结果」  
- **查**：支付失败之后、Funding issue **之前**  
- **退**：FinanceAdjustment **之后**、结果网关之前  

Hang points: **pay** = send task + message catch; **investigate** = after fail, before Funding issue; **refund** = after FinanceAdjustment.

---

### 3.2 `request-payment` —— 付（主戏）

**干什么：** 模拟外部支付方；发布 BPMN 消息 `payment-result`；再完成 Send Task。

**What it does:** Mock the payment provider; publish BPMN message `payment-result`; then complete the send task.

**核心逻辑（就讲这四点）：**

1. 读病例号（`case_reference` / `patientId`）和金额（默认 `10.01`）。没有病例号就 fail。  
   Read case ID and amount (default `10.01`). No case ID → fail the job.
2. **演示规则：** 金额字符串**以 `0` 结尾** → 失败；否则成功，生成 `TX-xxxxxxxx`。  
   **Demo rule:** amount ending in `0` fails; else success and create `TX-…`.
3. **`publishMessage("payment-result")`**，correlationKey = 病例号 —— 流程里的 Catch 才能醒。  
   Publish `payment-result` with case ID as correlation key — otherwise the catch never continues.
4. 若已有 `payment_requested_once`，复用上次结果（防演示重复扣）。  
   If `payment_requested_once` is already set, reuse the last result (no double charge in demo).

成功日志：`request-payment SUCCESS ... publishing payment-result`  
失败日志：`request-payment UNSUCCESSFUL ...`

**为什么必须发消息？**  
Send Task 只是“我发出去了”；流程停在 Message Catch 等结果。不发 `payment-result`，流程卡住。这是 Est 的 Message Example 模式。

**Why publish?** The send task means “I sent it”; the process waits on the message catch. Without `payment-result`, the process sticks. This is Est’s message pattern.

**不想点全表时：** Modeler 选中 Send payment request → Test，贴：

```json
{
  "patientId": "DEMO-JAVA-01",
  "case_reference": "DEMO-JAVA-01",
  "charge_amount": "10.01",
  "fundingStatus": "patient_payment_required"
}
```

失败把金额改成 `"10.00"`。

---

### 3.3 `mark-payment-investigate` —— 查

**干什么：** 支付失败后、进人工 Funding issue **之前**，先在账本标 **INVESTIGATE**。

**What it does:** After payment fail, **before** the human Funding issue, mark the ledger **INVESTIGATE**.

**为什么要有：** 服务商可能已经扣过款；本院先核对，**禁止自动再扣**。

**Why:** The provider may already have charged; we check first and **must not auto-charge again**.

**核心：** 幂等键查 `payment_ledger` → 无则插入 INVESTIGATE → 写 `audit_event`（actor=`ruby`）→ 返回 `payment_investigate=true` 等变量。

**Core:** Find by idempotency key → insert INVESTIGATE if new → append audit (`ruby`) → return flags for the process.

日志：`mark-payment-investigate ... status=INVESTIGATE`

---

### 3.4 `request-refund` —— 退

**干什么：** 财务调整表填完后，把退款/划转结果写入 `payment_ledger`。

**What it does:** After the Finance form, write the refund / adjustment result into `payment_ledger`.

**核心：**

1. 读 `financeAdjustment`：`resolved` → **SUCCESSFUL**；否则 **INVESTIGATE**。  
   Read `financeAdjustment`: `resolved` → **SUCCESSFUL**; else **INVESTIGATE**.
2. 幂等键：`病例号|refund|决定|金额` —— 同一意图重试**不插第二行**。  
   Key: `case|refund|decision|amount` — retry **reuses** the row.
3. 写审计（actor=`ruby`），返回 `refund_status`、`refund_transaction_reference` 给后续网关。  
   Append audit; return variables for the next gateway.

成功日志：`request-refund ... decision=resolved status=SUCCESSFUL`

Modeler Test（选中齿轮 Request refund）：

```json
{
  "patientId": "DEMO-001",
  "case_reference": "DEMO-001",
  "financeAdjustment": "resolved",
  "charge_amount": "25.50"
}
```

`pending` 则变成 INVESTIGATE。

---

### 3.5 数据库（我这块）

两套库不要混：

Do not mix two databases:

1. **Camunda 引擎库** —— 流程实例、任务、作业、消息关联（流程状态）  
   **Engine DB** — instances, tasks, jobs, message correlation (process state)
2. **领域 H2 文件** —— `Coursework/hospital-pathway/data/hospital-domain`（业务事实）  
   **Domain H2 file** — business facts

| 表 | 谁写 | 我强调 |
|----|------|--------|
| **`payment_ledger`** | **我（退 / 查）** | 病例号、金额、状态 SUCCESSFUL / INVESTIGATE、交易号、幂等键 |
| `audit_event` | A/B/D | 我的 actor = **`ruby`** |
| `booking_slot` | B | 不是我的 |

答辩金句：退款和待调查的**可核对事实**在 `payment_ledger`，不是只活在 Tasklist 变量里。  
Key line: refund / investigate **facts** live in `payment_ledger`, not only in process variables.

查库前**先停 Java**，Database 连接：

```text
jdbc:h2:file:<模块绝对路径>/data/hospital-domain;IFEXISTS=TRUE
```

用户 `sa`，密码空。

```sql
SELECT * FROM payment_ledger ORDER BY id;
SELECT * FROM audit_event WHERE actor = 'ruby' ORDER BY id;
```

---

### 3.6 收尾交接

总结：我负责钱相关的三个 Worker——**付、查、退**；事实进 `payment_ledger`。线路上我指过 4 / 10 / 13。接下来请 Estrella 讲预约与占号 Java。

To close: I own three money workers — **pay, investigate, refund**; facts go to `payment_ledger`. I pointed at routes 4 / 10 / 13. Next, Estrella will cover booking workers.

谢谢。  
Thank you.

---

## 四、可能问答（偏 Java · 中英逐段）

---

### Q1. 你具体做了哪些 Java？

三个类型：`request-payment`（主讲既有）、`mark-payment-investigate` 和 `request-refund`（我新加，在 `RefundWorkers`）。写 `payment_ledger` 和 `audit_event`。

Three job types: `request-payment` (existing, I present it), plus `mark-payment-investigate` and `request-refund` (I added them in `RefundWorkers`). They write `payment_ledger` and `audit_event`.

---

### Q2. `request-payment` 核心逻辑是什么？

读病例号和金额；金额以 0 结尾则失败，否则成功；发布消息 `payment-result`（关联键=病例号）；再完成 Send Task。已请求过则复用结果。

Read case ID and amount; fail if amount ends with 0, else success; publish `payment-result` with that case ID; then complete the send task. If already requested once, reuse the result.

---

### Q3. 为什么一定要 `publishMessage`？直接 complete 不行吗？

BPMN 用的是「发出请求 + 中间捕获消息」。Catch 靠消息名和 correlationKey 唤醒。只 complete Send Task 而不发消息，流程仍停在 Catch。

The BPMN uses “send request + intermediate message catch”. The catch wakes on message name and correlation key. Completing the send task without publishing leaves the process stuck on the catch.

---

### Q4. 为什么 10.01 成功、10.00 失败？

课堂演示约定，不是真实银行：金额字符串以 `0` 结尾失败。方便现场切成功/失败。

Classroom demo rule, not a real bank: amount string ending in `0` fails. Easy to switch success and fail live.

---

### Q5. `mark-payment-investigate` 解决什么问题？

支付失败进人工前，先把意图标成 INVESTIGATE。表示可能已扣款，禁止自动再扣，避免重复收费。

Before the human funding task, mark the intent INVESTIGATE. It means a charge may already exist — do not auto-charge again.

---

### Q6. `request-refund` 如何决定 SUCCESSFUL 还是 INVESTIGATE？

读表单变量 `financeAdjustment`：`resolved` → SUCCESSFUL；`pending`（或其他非 resolved）→ INVESTIGATE。

It reads `financeAdjustment`: `resolved` → SUCCESSFUL; `pending` (or not resolved) → INVESTIGATE.

---

### Q7. 幂等怎么实现？

退款键 = `病例号|refund|决定|金额`。`findByIdempotencyKey`：有则返回原行，无则 `save` 新行。调查键类似。同一意图重试不插第二笔。

Refund key = `case|refund|decision|amount`. `findByIdempotencyKey`: reuse if found, else save. Investigate is similar. Retry of the same intent does not insert a second row.

---

### Q8. 为什么要领域库？引擎库不够吗？

引擎库存流程状态。领域库存业务事实——这笔退款记没记、是否待调查。要能直接 SQL 核对，不能只靠流程变量。

The engine stores process state. The domain DB stores business facts — was the refund recorded, is it under investigate. We need SQL we can check, not only process variables.

---

### Q9. 你写哪张表？存卡号吗？

主要写 `payment_ledger`，并 append `audit_event`（actor=`ruby`）。不写 `booking_slot`。不存卡号、CVV、病历正文。

Mainly `payment_ledger`, plus `audit_event` with actor `ruby`. Not `booking_slot`. No card numbers, no CVV, no clinical notes.

---

### Q10. 和 Est 的支付模式是什么关系？

支付发消息模式来自 Est 的 Message Example。我在此基础上补了调查和退款两个 Worker，并挂到全院图。

The publish-message payment pattern comes from Est’s message example. I added investigate and refund workers on top, and hung them on the hospital diagram.

---

### Q11. 和 D 的 `notify-care-change` 怎么分工？

D 只记通知是否发出的审计回执，不写 `payment_ledger`。涉钱退款由我的 `request-refund` 记账。

D only stores a notification audit receipt; it does not write `payment_ledger`. Money refunds are recorded by my `request-refund`.

---

### Q12. `autoComplete = false` 是什么意思？（若问到支付）

`request-payment` 要先发消息再自己 `complete`。若用默认 autoComplete，可能在消息发出前就结束作业，时序不安全。所以手动完成。

`request-payment` must publish first, then complete itself. Default autoComplete might finish the job before the message is published. So we complete manually.

---

### Q13. 演示 / 查库要注意什么？

先开 Camunda，再 `mvn spring-boot:run`。不要同时开学习镜像。查 H2 前停 Java（文件锁）。

Start Camunda, then `mvn spring-boot:run`. Do not run the learn mirror at the same time. Stop Java before opening the H2 file.

---

### Q14. 为什么类名 MemberA、actor 却是 ruby？

早期按 A/B/C/D 命名类。我是 Ruby，审计用可读名 `ruby`；类名大改会牵测试，先保持兼容。

Classes were named A/B/C/D early on. I am Ruby, so the audit actor is `ruby`. Renaming the class would break tests; we keep the class name for now.

---

### Q15. 如果老师问线怎么走？

我指图：线 10 是付；失败支是查；线 13 是退。细点选表我可以补一句「第一次临床要选治疗、经费选患者付费」，细节以 Java 为准。

I point on the diagram: Route 10 is pay; the fail branch is investigate; Route 13 is refund. For clicking I can add one line — first clinical = treat, funding = patient pay — but the focus is the Java.

---

## 五、上台小抄

1. Ruby，打头阵；重点 **Java**。  
2. 四人：A 钱 · B 号 · C 信 · D 变更通知。  
3. 指图：4 审计 / 10 **付·查** / 13 **退**。  
4. 三个 Worker：`request-payment` → 发 `payment-result`；investigate → INVESTIGATE；refund → 看 `financeAdjustment`。  
5. 表：`payment_ledger`；actor=`ruby`；不存卡号。  
6. 交接 Estrella。

1. Ruby opens; focus on **Java**.  
2. A money · B slots · C letters · D change notice.  
3. Point: 4 audit / 10 **pay·investigate** / 13 **refund**.  
4. Three workers: pay publishes `payment-result`; investigate marks INVESTIGATE; refund follows `financeAdjustment`.  
5. Table `payment_ledger`; actor `ruby`; no card data.  
6. Hand over to Estrella.

---

*细点选表仍见 `A同学-答辩讲稿-双语.md` / `完整体验路线.md`。本文 = 开场 + Java 主讲 + 问答。*
