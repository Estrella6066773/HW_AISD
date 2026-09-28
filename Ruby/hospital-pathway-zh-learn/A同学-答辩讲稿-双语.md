# A 同学答辩讲稿

正式演示用 `Coursework/hospital-pathway`。线路对照 `完整体验路线.md`。  
我负责 **P5 / P7 / P8 / P13**；主讲 **线 4、线 10、线 13**。  
*I own P5, P7, P8, P13. I present Routes 4, 10 and 13.*

病例号：审计 / 退款 `DEMO-001`；付费线 `DEMO-JAVA-01`。

---

## 一、我负责的线路讲明白

### 线 4｜审计报告 —— 干什么？

**故事**：管理者来看路径/审计报告，看完就结束。不看病、不付钱。

**English (simple):** A manager only reviews an audit report, then stop. No visit, no payment.

**为什么有这条线？**  
P13 要求「谁、何时、做了什么」可查。这条线最短，用来证明系统可追溯，不是跑完整护理。

**English:** This short route shows the process is traceable (P13).

**▶ 演示时照着点（线 4）**

病例号 `DEMO-001`。

```
开始申请 / Start request
  → P1 登记　【选】管理审计 / 报告 / Management audit / report
  → ★ P13　授权管理者审阅审计轨迹与路径报告
     Authorised manager reviews audit trail and pathway reports
       【选】结果 = 已完成并记录 / Completed and recorded
  → 【终点】报告已审阅 / Report reviewed
```

**怎么选、为什么：**

1. 登记 → **管理审计 / 报告** —— 别的类型会进问询、转诊、变更；只有这一项进审计。  
2. P13 → **已完成并记录** —— `simple_record` 只有这一项合法出口。  

口头 / **Speak:** 普通用户不能改审计；管理者只能审阅。  
*Normal users cannot edit the audit. Managers only review.*

---

### 线 10｜付费治疗（主戏）—— 干什么？

**故事**：自费病人从进院到治完出院，并且**必须走到外部支付 Java**。

**English (simple):** A self-pay patient goes from arrival to discharge, and we must hit the payment Java.

**为什么有这条线？**  
把「医生授权治疗（P5）」和「谁出钱、怎么付（P7）」串成一条可演示的 happy path，并证明 `request-payment` 已接上。

**English:** Links clinical authorisation (P5) with who pays (P7), and proves `request-payment` works.

口诀：**收 → 到 → 治 → 信 → 付 10.01 → 约 → 出 → 信**  
*In → attend → treat → letter → pay 10.01 → book → discharge → letter*

**▶ 演示时照着点（线 10 完整路径）**

病例号全程 `DEMO-JAVA-01`。Java 必须开着。

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

成功日志：`request-payment SUCCESS ... publishing payment-result`  
失败额外：`mark-payment-investigate ... status=INVESTIGATE`

**逐步怎么选、为什么：**

| 步 | 选什么 | 为什么这样选 |
|----|--------|--------------|
| 登记 | **新转诊 - 材料已核验** | 进主护理路径；问询/报告/变更都是短线或旁路 |
| 转诊 | **接受** | 驳回/转科/要补充都走不到治疗和支付 |
| 预约 | **已预约、通知且已到诊** | 人没来会进变更；待定会卡住。到诊后才能临床授权 |
| ★ P5 第一次 | **授权治疗 / 下一疗程** | **最容易错**：若选「出院」就变成最短线 9，**付不了钱、看不到支付 Java**。治疗才进经费 |
| 寄信 | **已批准信件已寄出** | 每诊后要有信；延误/退回医生不进经费 |
| ★ P7 经费 | **需要患者付费 - 调用支付方** + 金额 **10.01** | 只有「患者付费」才调 `request-payment`。选「医院经费」会变成线 11（B 的线，无支付 Java） |
| 金额 | **10.01** 成功；**10.00** 失败演示 | 演示约定：金额以 `0` 结尾失败，否则成功 |
| 支付后 | 自动 Send Task + Catch | 无表单；看 Java 日志 |
| 治疗预约 | **资源可用；预约已确认** | 资源没有则约不上，后面确认 Java 不跑（B） |
| ★ P5 第二次 | **授权出院** | 疗程结束；再选治疗会绕圈 |
| 寄信 | **已批准信件已寄出** | 出院后收尾 |

**失败支（可选）：** 金额 **10.00** → `mark-payment-investigate` → Funding issue → 再评经费。

**English speak (Route 10):**  
First P5 must be **treat**, not discharge — or we skip payment.  
P7 must be **patient payment** + **10.01**. Hospital funding is Route 11 (B).  
Then Java payment runs. Later P5 = **discharge**. Done.

**和线 11：** 线 10 = 患者付费 + 支付 Java（我）；线 11 = 医院经费 + 预约确认 Java（B）。

---

### 线 13｜变更 + 退款 —— 干什么？

**故事**：病人要停/出院，**而且动到钱**；财务记退款/划转后才能干净结束。

**English (simple):** Stop care **and money changes**. Finance must record the refund, then end.

**为什么有这条线？**  
临床变更若涉钱，不能口头了事。P7 财务调整之后挂 **`request-refund`**，写入 `payment_ledger`。

**English:** If money is affected, we cannot finish with only words. The refund worker writes the ledger.

**▶ 演示时照着点（线 13 完整路径）**

病例号 `DEMO-001`。Java 必须开着。

```
开始申请 / Start request
  → P1 登记　【选】授权变更 / 随访 / 取消
                / Authorised change / follow-up / cancellation
  → P11/P12 变更　【选】授权停止 / 出院 - 需财务复核
                / Authorise stop / discharge - Finance review required
       ← D：notify-care-change（自动）
  → ★ P7 财务调整　form = finance_adjustment
       【选】财务决定已授权且结果已记录
                / Financial decision authorised and outcome recorded
  → ★ Service Task「Request refund」← Java request-refund
       （写 payment_ledger SUCCESSFUL）
       ← 控制台：request-refund case=... decision=resolved status=SUCCESSFUL
  → 【终点】本段诊疗结束 / Care episode ended
```

若财务表选「提供方 / 批准结果待定 / pending」→ `request-refund` 写 **INVESTIGATE**，网关回到财务调整重试。

**怎么选、为什么：**

1. 登记 → **授权变更…** —— 直接进变更，不走完整转诊护理。  
2. 变更 → **需财务复核** —— 选「无财务影响」走线 12，**看不到退款 Java**。  
3. ★ 财务 → **财务决定已授权且结果已记录** —— 批准退款/划转；pending 则待调查重试。  
4. ★ 自动 `request-refund` → 写库 → 终点。

口头 / **Speak:** 医生定停不停，财务定退不退；Worker 只落账。  
*Doctor decides stop/discharge. Finance decides refund. The worker only records it.*

---

### P8 紧急规则（指图，线 10 默认不进）

等付款会伤害病人时，医生可先授权紧急救治并写理由，财务后补。  
**English:** If waiting for payment is dangerous, the doctor may authorise urgent care first; Finance follows later. Normal Route 10 skips this.

---

## 二、我负责的 Java（核心怎么讲）

**English (simple):** I own three workers: pay (`request-payment`), mark investigate, and refund (`request-refund`).

代码位置：

- 既有支付：`HospitalPathwayWorkers.java` → `request-payment`
- 新加退款/调查：`MemberAPathwayWorkers.java` → `request-refund`、`mark-payment-investigate`

图上挂点：

- 支付：Send Task「发出支付请求」→ Catch「收到支付结果」
- 调查：支付失败 / 经费 pending 进入 FundingIssue **之前**
- 退款：`FinanceAdjustment` **之后**、进网关之前

### 1）`request-payment`（线 10 主戏）

**干什么：** 模拟外部支付方；发 BPMN 消息 `payment-result`（关联键 = 病例号）；再完成 Send Task。

**核心逻辑（答辩就讲这三点）：**

1. 读 `case_reference` / `patientId` 和 `charge_amount`（默认 10.01）。没有病例号就 fail。  
2. **演示规则：** 金额**以 0 结尾** → 失败；否则成功，生成 `TX-xxxxxxxx`。  
3. `publishMessage("payment-result")` 用病例号做 correlationKey → 流程里的 Message Catch 才能醒过来。  
4. 若变量里已有 `payment_requested_once`，直接复用上次结果（防演示时重复扣）。

成功日志：`request-payment SUCCESS ... publishing payment-result`

**English:** Read case ID and amount. Amount ending in `0` fails. Publish message `payment-result` with that case ID so the catch event continues.

### 2）`mark-payment-investigate`（线 10 失败支）

**干什么：** 支付失败要进人工调查前，先在账本标 **INVESTIGATE**，业务上「可能已扣款、本院先核对」，**禁止自动再扣**。

**核心：** 按幂等键查 `payment_ledger`，没有就插入状态 INVESTIGATE，并写一条 `audit_event`（actor=`member-A`）。

**English:** Before Funding issue, mark the ledger INVESTIGATE so we never auto-charge again.

### 3）`request-refund`（线 13）

**干什么：** 财务表填完后，把退款/划转结果写入 `payment_ledger`。

**核心：**

1. 读 `financeAdjustment`：`resolved` → 状态 **SUCCESSFUL**；否则 **INVESTIGATE**。  
2. 幂等键：`病例号|refund|决定|金额` —— 同一意图重试**不插第二行**。  
3. 写审计后返回 `refund_status`、`refund_transaction_reference` 等变量给后续网关。

成功日志：`request-refund case=... decision=resolved status=SUCCESSFUL`

**English:** After Finance form: `resolved` → SUCCESSFUL refund row; `pending` → INVESTIGATE. Same key = reuse row on retry.

### 不想从头点表时（Modeler Test）— 四组 JSON 都备好

先开 c8run + `mvn spring-boot:run`，Modeler 连 `http://localhost:8080`。  
选中对应节点 → Test → Input 贴 JSON → Run test。空的 `{}` 会失败；红字 Couldn't connect = 没连上引擎。

#### ① 支付成功（选中 Send payment request）

```json
{
  "patientId": "DEMO-JAVA-01",
  "case_reference": "DEMO-JAVA-01",
  "charge_amount": "10.01",
  "fundingStatus": "patient_payment_required"
}
```

日志：`request-payment SUCCESS ... publishing payment-result`

#### ② 支付失败 → 调查（仍选 Send payment request；金额 10.00）

```json
{
  "patientId": "DEMO-JAVA-FAIL",
  "case_reference": "DEMO-JAVA-FAIL",
  "charge_amount": "10.00",
  "fundingStatus": "patient_payment_required"
}
```

日志：`request-payment UNSUCCESSFUL` → 流程进调查节点后出现  
`mark-payment-investigate ... status=INVESTIGATE`

若只测调查齿轮 **Mark payment investigate**（跳过支付），可另贴：

```json
{
  "patientId": "DEMO-JAVA-FAIL",
  "case_reference": "DEMO-JAVA-FAIL",
  "charge_amount": "10.00",
  "transaction_reference": "TX-DEMO01"
}
```

#### ③ 退款成功（选中齿轮 Request refund，不要选财务用户任务）

```json
{
  "patientId": "DEMO-001",
  "case_reference": "DEMO-001",
  "financeAdjustment": "resolved",
  "charge_amount": "25.50"
}
```

日志：`request-refund case=DEMO-001 decision=resolved status=SUCCESSFUL`

#### ④ 退款待调查 pending（仍选 Request refund）

```json
{
  "patientId": "DEMO-001",
  "case_reference": "DEMO-001",
  "financeAdjustment": "pending",
  "charge_amount": "25.50"
}
```

日志：`request-refund ... decision=pending status=INVESTIGATE`  
（对应表单选「提供方 / 批准结果待定」，网关会回到财务调整重试）

---

## 三、数据库（我这块）

**English (simple):** Camunda stores process state. Our H2 file stores business facts — my table is `payment_ledger`.

两套库不要混：

1. **Camunda 引擎库**（c8run 自带）—— 流程实例、用户任务、作业、消息关联。  
2. **应用领域库**（我们 Spring Boot 进程）—— 文件 H2：`Coursework/hospital-pathway/data/hospital-domain`

三张表：

| 表 | 谁写 | 存什么 |
|----|------|--------|
| **`payment_ledger`** | **我（退款/调查）**；支付既有 Worker 本阶段主要写流程变量 | 病例号、幂等键、金额、状态 SUCCESSFUL / UNSUCCESSFUL / INVESTIGATE、交易参考号 |
| `booking_slot` | B | 占号 / 资源 pending |
| `audit_event` | A/B/D 都会 append | 只追加审计；禁止改删业务方法 |

我答辩时强调：

- 退款、待调查的**可核对事实**在 `payment_ledger`，不是只活在 Tasklist 变量里。  
- 幂等：同一键再跑 Worker，复用原行，演示重试安全。  
- 查库前先**停 Java**（H2 文件锁），再用：

```sql
SELECT * FROM payment_ledger ORDER BY id;
SELECT * FROM audit_event WHERE actor = 'member-A' ORDER BY id;
```

JDBC 提示：`jdbc:h2:file:<模块绝对路径>/data/hospital-domain;IFEXISTS=TRUE`，用户 `sa`，密码空。

---

## 四、其他成员的 Java（熟悉即可）

### B｜占号 + 预约确认

| 类型 | 何时 | 写哪 |
|------|------|------|
| `check-slot` | 预约就诊之后 | `booking_slot` CONFIRMED（就诊档） |
| `reserve-appointment` | 治疗资源就绪之后、发确认之前 | `booking_slot` CONFIRMED（治疗档） |
| `flag-resource-unavailable` | 资源 pending | `booking_slot` PENDING + 重试计数 |
| `send-booking-confirmation`（既有） | 发送预约确认 Send Task | 主要写流程变量「已确认」；线 11 细讲 |

核心：占用键唯一；先查再写；和我的支付是不同表。

### D｜变更通知

| 类型 | 何时 | 写哪 |
|------|------|------|
| `notify-care-change` | 临床变更表单之后、进后续网关之前 | `audit_event` 一条回执 |

核心：缺授权可 SKIPPED；涉钱则状态带 FINANCE_REVIEW，**真正退款仍走我的线 13 / `request-refund`**。不写 `payment_ledger`。

### C｜诊后信 / 通知转诊方

计划类型：`dispatch-clinic-letter`、`notify-referrer`（总指引里；若图上尚未挂齐，答辩说「一责由 C 推进，写审计」即可）。

### 一句话对照

- **A**：钱 —— 付、查、退 → `payment_ledger`  
- **B**：号 —— 占、挂起、确认 → `booking_slot`  
- **D**：变更通知 → `audit_event`  
- **C**：信 / 转诊方通知 → 审计（待落地）

---

## 五、建议怎么讲（约 8–10 分钟）

1. 开场：P5/P7/P8/P13；线 4 审计、线 10 付钱、线 13 退钱。  
2. 线 4 快点（§一照着点）。  
3. 线 10 主演示（§一完整路径）或 Test 支付 JSON。  
4. 线 13（§一完整路径）+ `request-refund`。  
5. 数据库一句 + B/D Java 一句。

**English closing:**  
I explain treat-or-not (P5), who pays / refund / investigate (P7), urgent exception (P8), and audit (P13).  
Route 10 shows payment Java; Route 13 shows refund into `payment_ledger`.

启动：

```bash
cd Coursework/hospital-pathway
mvn spring-boot:run
```

不要同时开 `Ruby/hospital-pathway-zh-learn`。
