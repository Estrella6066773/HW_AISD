# est：成员B演示指导（P3/P4/P6 · 线9/10/11/14 · Java②）

**主笔**：Estrella（陈格平）  
**日期**：2026-09-28  
**状态**：演示用讲稿与操作脚本  
**范围**：BookVisit（P3/P4 预约、通知、到诊/取消）、BookTreatment（P6 确认预约）、`send-booking-confirmation`（Java② 预约确认）

> 你主讲：**BookVisit（P3/P4 预约、通知、到诊/取消）**、**BookTreatment（P6 确认预约）**、**send-booking-confirmation（Java② 预约确认）**。  
> 支付 Java① `request-payment` 是 A 主讲；你只要确认 Funding 后日志有 `request-payment SUCCESS`，流程才会走到你的 P6。  
> 你负责的路线：**线9、线10/11 的预约与 Java②、线14 取消/未到诊**。

---

## 0. 演示前准备

1. 只开一套工程，不要同时开中文学习版和英文版。

   ```bash
   cd "Ruby/hospital-pathway-zh-learn"
   mvn spring-boot:run
   ```

   或英文版：

   ```bash
   cd "Coursework/hospital-pathway"
   mvn spring-boot:run
   ```

2. 登录 Tasklist：`demo / demo`。
3. 开两个窗口：
   - 左边：Camunda Tasklist
   - 右边：Java 控制台日志（重点看 `request-payment` 和 `send-booking-confirmation`）
4. Tasklist 过滤 assignee：`demo`，否则可能看不到任务。
5. 启动流程：找到 **Hospital - All Business Processes (Simple Camunda 8)** → **Start process**。
6. 病例号建议：
   - 线9：`DEMO-B-09`
   - 线10：`DEMO-JAVA-01`，若老师要求与截图一致就用 `DEMO-001`
   - 线11：`DEMO-B-11`
   - 线14：`DEMO-B-14`
   全程同一条实例内保持一致即可。

---

## 1. 你负责的 gateway / form / message / service 怎么讲

| 类型 | 位置 | 名称/变量 | 你演示时的讲解口径 | 证据 |
|---|---|---|---|---|
| **Form** | P3/P4 | `BookVisit` 共用表 | 这是预约、通知、到诊共用表。`Outcome` 是路由关键，其他字段只记录 | Tasklist 表单 |
| **Gateway** | BookVisit 后 | `Outcome` | 排他网关：`Booked, notified and attended` → 正常到 ClinicalCare；`Cancelled / declined / did not attend` → 线14 进变更 | 下一步任务不同 |
| **Form** | P6 | `BookTreatment` | 确认已授权治疗与检查预约。选 `Resources available; booking confirmed` | Tasklist 表单 |
| **Gateway** | Funding 后 | `Funding outcome` | A 主讲：`Patient payment required` → Java①；`Hospital funding confirmed` → 跳过 Java①，直接到你的 BookTreatment | 日志有无 `request-payment` |
| **Service** | Java② | `send-booking-confirmation` | 不是用户任务，不占 Tasklist。Java worker 自动发送预约确认，日志出现 `SENT` | 控制台日志 |
| **Message** | Java② 发出 | 预约确认消息 | 流程把预约确认消息发给外部/患者；日志 `send-booking-confirmation SENT case=...` 就是消息已发出 | 控制台日志 |

---

## 2. 演示脚本

### 2.1 线9：最短护理出院（无 Java）——展示 BookVisit 正常到诊但不触发 Java

| 步骤 | 任务/表单 | 字段 | 填值 | 操作/讲解 |
|---|---|---|---|---|
| 1 | Start process | — | — | 启动流程 |
| 2 | Register | Patient / case ID | `DEMO-B-09` | `Request type` 选 `New referral - documents checked` |
|  |  | Specialty | `Oncology` |  |
|  |  | Priority | `Routine` |  |
|  |  | Timeframe | `within 6 weeks` |  |
|  |  | Request type | `New referral - documents checked` |  |
|  |  | Notes | `B route9 register` | → Complete |
| 3 | ReviewReferral | Clinician ID | `CONS-01` | Decision 选 `Accept` |
|  |  | Decision | `Accept` |  |
|  |  | Decision reason | `Suitable for clinic` | → Record decision |
| 4 | **BookVisit（你主讲）** | Outcome | `Booked, notified and attended` | **Gateway 讲解**：这里选正常到诊，排他网关去 ClinicalCare；如果选取消/未到诊，就会进线14 |
|  |  | Staff role | `booking clerk` |  |
|  |  | Notes | `attended` | → Complete |
| 5 | ClinicalCare | Outcome | `Authorise discharge / no further care` | 线9 短出院，不经过 Funding |
| 6 | DispatchLetter | Outcome | `Approved letter sent and recorded` | → Complete |
| 7 | 终点 | — | — | `Care episode ended` |

**预期**：没有任何 Java 日志。  
**话术**：“线9 证明正常预约到诊后可以直接出院，不触发支付和预约确认 Java。”

---

### 2.2 线10：完整路径 + Java②（你的重点）

| 步骤 | 任务/表单 | 字段 | 填值 | 操作/讲解 |
|---|---|---|---|---|
| 1 | Start process | — | — | 启动流程 |
| 2 | Register | Patient / case ID | `DEMO-JAVA-01` 或 `DEMO-001` | Request type 选 `New referral - documents checked` |
|  |  | Specialty | `Oncology` |  |
|  |  | Priority | `Routine` |  |
|  |  | Timeframe | `within 6 weeks` |  |
|  |  | Request type | `New referral - documents checked` |  |
|  |  | Notes | `B full path register` | → Complete |
| 3 | ReviewReferral | Clinician ID | `CONS-01` | Decision 选 `Accept` |
|  |  | Decision | `Accept` |  |
|  |  | Decision reason | `Suitable for clinic` | → Record decision |
| 4 | **BookVisit（你主讲）** | Outcome | `Booked, notified and attended` | **Gateway**：正常到诊 → ClinicalCare |
|  |  | Staff role | `booking clerk` |  |
|  |  | Notes | `attended` | → Complete |
| 5 | ClinicalCare | Outcome | `Authorise treatment / next cycle` | 授权治疗，进入经费段 |
| 6 | DispatchLetter | Outcome | `Approved letter sent and recorded` | → Complete |
| 7 | Funding（A 主讲） | Funding outcome | `Patient payment required - call provider` | **Gateway**：患者付费 → Java① |
|  |  | Charge amount | `10.01` | 成功后看日志 |
|  |  | Notes | `call provider` | → Complete |
| 8 | 看 Java① 日志 | — | — | 应出现：`request-payment SUCCESS case=... amount=10.01 tx=...` |
| 9 | **BookTreatment（你主讲）** | Outcome | `Resources available; booking confirmed` | **P6 确认预约**，选资源可用 |
| 10 | **Java② 自动执行（你主讲）** | — | — | 看日志：`send-booking-confirmation SENT case=...` |
|  |  |  |  | **Service 讲解**：这不是用户任务，Java worker 自动完成；**Message 讲解**：预约确认消息已发出 |
| 11 | ClinicalCare | Outcome | `Authorise discharge / no further care` | 第二次治疗复查后出院 |
| 12 | DispatchLetter | Outcome | `Approved letter sent and recorded` | → Complete |
| 13 | 终点 | — | — | `Care episode ended` |

**预期日志两行**：

```text
request-payment SUCCESS ... amount=10.01
send-booking-confirmation SENT case=DEMO-JAVA-01 ...
```

**话术**：“支付 Java① 成功后，流程到我的 P6 BookTreatment。我选资源可用，下一节点是我的 Java② `send-booking-confirmation`。它不占 Tasklist，日志 SENT 就表示预约确认消息已发出。”

---

### 2.3 线11：医院经费（跳过 Java①，仍跑 Java②）

| 步骤 | 任务/表单 | 字段 | 填值 | 操作/讲解 |
|---|---|---|---|---|
| 1 | Start process | — | — | 启动流程 |
| 2 | Register | Patient / case ID | `DEMO-B-11` | Request type 选 `New referral - documents checked` |
| 3 | ReviewReferral | Clinician ID | `CONS-01` | Decision 选 `Accept` |
| 4 | **BookVisit** | Outcome | `Booked, notified and attended` | 正常到诊 |
| 5 | ClinicalCare | Outcome | `Authorise treatment / next cycle` | 授权治疗 |
| 6 | DispatchLetter | Outcome | `Approved letter sent and recorded` | → Complete |
| 7 | Funding | Funding outcome | `Hospital funding confirmed` | **Gateway**：医院经费 → 跳过 Java① |
|  |  | Charge amount | 若必填填 `0.00` | 不调支付 Worker |
|  |  | Notes | `hospital funded` | → Complete |
| 8 | 看日志 | — | — | **不应出现** `request-payment` |
| 9 | **BookTreatment（你主讲）** | Outcome | `Resources available; booking confirmed` | P6 确认预约 |
| 10 | **Java② 自动执行** | — | — | 应出现：`send-booking-confirmation SENT case=DEMO-B-11 ...` |
| 11 | ClinicalCare | Outcome | `Authorise discharge / no further care` | → Complete |
| 12 | DispatchLetter | Outcome | `Approved letter sent and recorded` | → Complete |
| 13 | 终点 | — | — | `Care episode ended` |

**话术**：“线11 经费来源是医院经费，所以跳过支付 Java①；但我的 P6 和 Java② 仍然执行，预约确认照样发送。”

---

### 2.4 线14：取消/未到诊进变更（你负责前半段）

| 步骤 | 任务/表单 | 字段 | 填值 | 操作/讲解 |
|---|---|---|---|---|
| 1 | Start process | — | — | 启动流程 |
| 2 | Register | Patient / case ID | `DEMO-B-14` | Request type 选 `New referral - documents checked` |
| 3 | ReviewReferral | Clinician ID | `CONS-01` | Decision 选 `Accept` |
| 4 | **BookVisit（你主讲）** | Outcome | `Cancelled / declined / did not attend` | **Gateway 重点**：这里走取消/未到诊分支，进入 P11/P12 变更线 |
|  |  | Staff role | `booking clerk` |  |
|  |  | Notes | `DNA / cancelled` | → Complete |
| 5 | 下一任务 | Authorise modification, follow-up or cancellation | — | 这是 P11/P12 变更段，D 主讲；你可停在这里 |
| 6 | 可选后续 | — | — | 选 `Authorise stop / discharge - no financial impact` → 终点；或选需财务复核 → P7 财务调整 → 终点 |

**预期**：不会出现 `send-booking-confirmation`，因为没到 BookTreatment。  
**话术**：“BookVisit 的 Outcome 是排他网关条件。选正常到诊去治疗；选取消/未到诊就进变更线，这就是线14。”

---

## 3. 卡住排查

| 现象 | 原因 | 检查 |
|---|---|---|
| Funding 后一直没 BookTreatment | Java① 没开或失败，或 Funding outcome 选错 | 看日志有无 `request-payment SUCCESS`；线11 应选 `Hospital funding confirmed` |
| BookTreatment 后没日志 | Java② 没开，或 Outcome 没选 `Resources available; booking confirmed` | 看日志有无 `send-booking-confirmation SENT` |
| Tasklist 没任务 | assignee 过滤问题 | Tasks 过滤 assignee 试 `demo` |
| 流程不到你的 Java② | 上一网关选错 | 检查 BookVisit / Funding / BookTreatment 的 Outcome |
| 同时开两套工程 | 端口/worker 冲突 | 只保留一套 |

---

## 4. 建议演示顺序

1. **线9**：正常预约到诊，无 Java —— 2 分钟
2. **线10**：完整路径，重点看 Java② `send-booking-confirmation SENT` —— 5 分钟
3. **线11**：医院经费跳过 Java①，但仍跑 Java② —— 3 分钟
4. **线14**：BookVisit 选取消/未到诊，进变更线 —— 2 分钟

如果时间紧，至少跑 **线10 + 线14**：线10 展示你的 Java②，线14 展示你的 BookVisit 取消分支。
