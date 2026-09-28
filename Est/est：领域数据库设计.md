# est：领域数据库设计（成员 B）

**主笔**：Estrella（陈格平）  
**日期**：2026-09-28  
**角色**：成员 B（领域库设计；一责预约域新工作器）  
**状态**：本切片落地应用领域库（表结构、仓储、审计只追加接口）；既有 `request-payment` / `send-booking-confirmation` 保持现状  
**行文**：正向写清存什么、谁写、怎么查；易混处用对照划界  
**实现位置**：`Coursework/hospital-pathway/`（包 `io.camunda.demo.hospital.domain`）  
**总顺序与分工**：[`Est/est：外部工作器与领域数据库总指引.md`](est：外部工作器与领域数据库总指引.md) 第 6 节

### 与 A / B / C / D 的衔接

| 谁 | 对本库的关系 |
|----|----------------|
| 成员 B | 设计并实现本库；一责占号 / 资源不可用工作器，写入 `booking_slot` |
| 成员 A | 一责退款 / 待调查类工作器；按契约读写 `payment_ledger` |
| 成员 C | 一责诊后信外发、转诊方通知等工作器；写入审计 |
| 成员 D | 本次只做变更通知工作器；写入审计；财务判断由既有人工任务处理 |

四人共用同一文件库与契约。

---

## 1. 目标

为医院路径工作器进程提供**受维护的文件型领域库**，与 Camunda / c8run 引擎库分离，保存：

1. 支付流水（幂等键唯一、可查交易参考号）  
2. 预约占用（占用键唯一、pending / confirmed / escalated）  
3. 审计事件（只追加、可按病例号查询）

本切片范围：建表、仓储、审计写入接口。既有两类 JobWorker 仍按原设计写回流程变量；新工作器（含成员 B 占号类）按契约读写本库。

---

## 2. 技术选型

| 项 | 选择 | 说明 |
|----|------|------|
| 引擎 | Spring Data JPA + Hibernate | 与 Spring Boot 4 / Java 21 同进程 |
| 库 | H2 文件模式 | `jdbc:h2:file:./data/hospital-domain` |
| 建表 | `spring.jpa.hibernate.ddl-auto=update` | 关机后保留演示数据 |
| 数据目录 | `Coursework/hospital-pathway/data/` | 已 `.gitignore`；本地生成、版本库只保留代码 |

启动成功后日志示例：

```text
领域库就绪（H2 文件 ./data/hospital-domain）：payment_ledger=0 行, booking_slot=0 行, audit_event=0 行
```

用 IDE Database 工具连接同一文件查看表。当前配置 `AUTO_SERVER=FALSE`，先停止 Java 工作器释放文件锁，再用数据库文件的绝对路径连接，查完后重启 Java；加 `IFEXISTS=TRUE` 可避免路径写错时新建空库。

---

## 3. 表与字段契约

### 3.1 `payment_ledger`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `case_reference` | 病例号 | 必填；与消息关联键一致 |
| `idempotency_key` | 幂等键 | **唯一**；建议 `病例号\|金额` 或调用方约定 |
| `transaction_reference` | 交易参考号 | 可空（失败时） |
| `amount` | 金额文本 | 必填；与 `charge_amount` 对齐 |
| `status` | 枚举字符串 | `SUCCESSFUL` / `UNSUCCESSFUL` / `INVESTIGATE` |
| `payment_date` | 日期 | 可空 |
| `created_at` | 时间戳 | 必填 |

Java：`PaymentLedger`、`PaymentLedgerStatus`、`PaymentLedgerRepository`。

### 3.2 `booking_slot`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `case_reference` | 病例号 | 必填 |
| `occupancy_key` | 占用键 | **唯一**；建议病例号 + 时间窗 + 资源类型 |
| `time_window` | 时间窗说明 | 可空，便于演示阅读 |
| `status` | 枚举字符串 | `CONFIRMED` / `PENDING` / `ESCALATED` |
| `retry_count` | 重试次数 | 默认 0 |
| `last_retry_at` | 最近重试时间 | 可空 |
| `created_at` | 时间戳 | 必填 |

Java：`BookingSlot`、`BookingSlotStatus`、`BookingSlotRepository`。

### 3.3 `audit_event`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `actor` | 操作者 | 必填 |
| `action` | 动作性质 | 必填 |
| `case_reference` | 病例号 | 可空 |
| `occurred_at` | 发生时间 | 必填 |
| `payload_summary` | 业务摘要 | 最长 512；只写短文本摘要 |
| `idempotency_key` | D 通知任务执行键（2026-09-28 增补） | 可空、最长 256、唯一；既有调用继续为 NULL，D 重试沿用同一键 |

写入：仅 `AuditEventWriter.append(...)`。  
查询：`AuditEventRepository`。  
业务层对外暴露追加与查询。

**D 增补，待 B 复核**：五参数 `append(actor, action, caseReference, idempotencyKey, payloadSummary)` 使用普通 `@Transactional`：先查键，已有记录就返回，否则追加。唯一约束防止重复保存；数据库异常交给 Camunda 的普通作业重试处理。原四参数接口保留。D 本次只做变更通知，不操作支付表。详见 [D 说明](../Ryan/2026-09-28/D_外部工作器与数据库说明.md)。

---

## 4. 包内类型一览

| 类型 | 职责 |
|------|------|
| `PaymentLedger` / `BookingSlot` / `AuditEvent` | JPA 实体 |
| `PaymentLedgerRepository` / `BookingSlotRepository` / `AuditEventRepository` | 查询与持久化 |
| `AuditEventWriter` | 审计只追加 |
| `DomainDatabaseConfig` | 启动探测日志 |
| `MemberBPathwayWorkers` | 成员 B：`check-slot` / `reserve-appointment` / `flag-resource-unavailable` |

既有 `HospitalPathwayWorkers` 中两类 `@JobWorker` 保持现状。

---

## 5. 本库字段边界（正向）

本库存放与演示相关的：病例号、幂等/占用键、金额、状态、交易参考号、日期、操作者、动作摘要。  
对齐 BR-07：财务相关列仅为上述业务必要项。路径落在 `hospital-pathway/data/`，与 c8run 引擎数据目录分开。

---

## 6. 后续工作器如何接入

按总指引第 6 节领取任务类型后：

1. 注入对应 `Repository` 或 `AuditEventWriter`。  
2. 支付 / 退款（成员 A）：先 `findByIdempotencyKey`，有则复用，无则 `save` 后再对外交互。  
3. 占号（成员 B）：先 `findByOccupancyKey`；确认写 `CONFIRMED`，挂起写 `PENDING` 并累加重试。  
4. 信件 / 转诊（成员 C）、变更（成员 D）：外部 mock 完成后 `append` 审计。
5. 既有两类 JobWorker 保持现状；新能力用新类型承接。  
6. 改 Java 时同步改全院 BPMN（总指引第 4.4 节）；若使用学习包则同步改图。

---

## 7. 本地验证步骤

1. 启动本机 Camunda（c8run）。  
2. `cd Coursework/hospital-pathway` → `mvn spring-boot:run`。  
3. 确认日志中有「领域库就绪」。  
4. 确认生成 `data/hospital-domain.mv.db`（或同前缀文件）。  
5. （可选）停止 Java 后用 IDE 连接同一文件的绝对路径，用户 `sa`、空密码，查看三张表，查完重启 Java。
6. 走通含 `BookVisit` / `BookTreatment` 的线路，日志出现 `check-slot` / `reserve-appointment` 或 `flag-resource-unavailable`。
