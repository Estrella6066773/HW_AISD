# est：领域数据库设计（成员 B）

**主笔**：Estrella（陈格平）  
**日期**：2026-09-28  
**角色**：成员 B（领域库设计；并一责预约域新工作器）  
**状态**：本切片只落地应用领域库（表结构、仓储、审计只写接口）；**不改**已实现的 `request-payment` / `send-booking-confirmation`  
**实现位置**：`Coursework/hospital-pathway/`（包 `io.camunda.demo.hospital.domain`）  
**总顺序与全员分工**：[`Est/est：外部工作器与领域数据库总指引.md`](est：外部工作器与领域数据库总指引.md) 第 6 节（**A/B/C/D 均须开发 JobWorker**）

### 与 A / B / C / D 的衔接（摘要）

| 谁 | 对本库的关系 |
|----|----------------|
| 成员 B | 设计并实现本库；一责排班占号、资源不可用等工作器并写入 `booking_slot` |
| 成员 A | 一责退款 / 待调查类工作器；按契约读写 `payment_ledger` |
| 成员 C | 一责诊后信外发、转诊方通知等工作器；写入审计（及可选通信记录） |
| 成员 D | 一责变更通知、问询回执等工作器；写入审计；涉钱变更时只读流水 |

四人共用**这一份**文件库，禁止另起数据库文件。

---

## 1. 目标

为医院路径工作器进程提供**受维护的文件型领域库**，与 Camunda / c8run 引擎自带库分离，保存：

1. 支付流水（防重复扣款、可查交易参考号）  
2. 预约占用（防重复建号、pending / escalated）  
3. 审计事件（只追加、可按病例号查询）

本切片不把现有两个 JobWorker 接到库上；后续工作器按契约读写本库即可。

---

## 2. 技术选型

| 项 | 选择 | 说明 |
|----|------|------|
| 引擎 | Spring Data JPA + Hibernate | 与现有 Spring Boot 4 / Java 21 同进程 |
| 库 | H2 文件模式 | `jdbc:h2:file:./data/hospital-domain` |
| 建表 | `spring.jpa.hibernate.ddl-auto=update` | 保留演示数据；不用 `create-drop` |
| 数据目录 | `Coursework/hospital-pathway/data/` | 已加入模块 `.gitignore`，勿提交库文件 |

启动成功后日志应出现类似：

```text
领域库就绪（H2 文件 ./data/hospital-domain）：payment_ledger=0 行, booking_slot=0 行, audit_event=0 行
```

用 IDE 的 Database 工具连接同一 JDBC URL 即可查看表（本模块未开 Web 版 H2 Console，避免与 Camunda 8080 抢端口）。

---

## 3. 表与字段契约

### 3.1 `payment_ledger`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `case_reference` | 病例号 | 非空；与消息关联键一致 |
| `idempotency_key` | 幂等键 | **唯一**；建议 `病例号\|金额` 或调用方另行约定 |
| `transaction_reference` | 交易参考号 | 可空（失败时） |
| `amount` | 金额文本 | 非空；与流程变量 `charge_amount` 对齐 |
| `status` | 枚举字符串 | `SUCCESSFUL` / `UNSUCCESSFUL` / `INVESTIGATE` |
| `payment_date` | 日期 | 可空 |
| `created_at` | 时间戳 | 非空 |

Java：`PaymentLedger`、`PaymentLedgerStatus`、`PaymentLedgerRepository`。

### 3.2 `booking_slot`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `case_reference` | 病例号 | 非空 |
| `occupancy_key` | 占用键 | **唯一**；建议含病例号 + 时间窗 + 资源类型 |
| `time_window` | 时间窗说明 | 可空，便于演示阅读 |
| `status` | 枚举字符串 | `CONFIRMED` / `PENDING` / `ESCALATED` |
| `retry_count` | 重试次数 | 默认 0 |
| `last_retry_at` | 最近重试时间 | 可空 |
| `created_at` | 时间戳 | 非空 |

Java：`BookingSlot`、`BookingSlotStatus`、`BookingSlotRepository`。

### 3.3 `audit_event`

| 列 | 类型语义 | 约束 |
|----|----------|------|
| `id` | 自增主键 | |
| `actor` | 操作者 | 非空 |
| `action` | 动作性质 | 非空 |
| `case_reference` | 病例号 | 可空 |
| `occurred_at` | 发生时间 | 非空 |
| `payload_summary` | 摘要 | 最长 512；禁止卡号与病历正文 |

写入：仅 `AuditEventWriter.append(...)`。  
查询：`AuditEventRepository`。  
**不提供**业务层 update / delete 方法。

---

## 4. 包内类型一览

| 类型 | 职责 |
|------|------|
| `PaymentLedger` / `BookingSlot` / `AuditEvent` | JPA 实体 |
| `PaymentLedgerRepository` / `BookingSlotRepository` / `AuditEventRepository` | 查询与（支付/预约）持久化 |
| `AuditEventWriter` | 审计只追加 |
| `DomainDatabaseConfig` | 启动探测日志 |

**明确不改**：`HospitalPathwayWorkers.java` 中已有两个 `@JobWorker`。

---

## 5. 禁止写入的内容

- 完整卡号、安全码  
- 病历正文或临床叙述全文  
- 把本文件库路径指到 c8run 引擎数据目录  

---

## 6. 后续如何接到新工作器（本切片不做编码）

A / B / C / D 各自一责的工作器按总指引第 6 节领取任务类型后：

1. 注入对应 `Repository` 或 `AuditEventWriter`。  
2. 支付 / 退款（成员 A）：先 `findByIdempotencyKey`，有则复用，无则 `save` 后再对外交互。  
3. 占号（成员 B）：先 `findByOccupancyKey`，无号写 `PENDING`，确认写 `CONFIRMED`。  
4. 信件 / 转诊通知（成员 C）、变更 / 问询（成员 D）：完成外部 mock 后 `append` 审计。  
5. **不要回头修改**已演示稳定的两个既有 JobWorker 方法体，除非全组另有决议。

---

## 7. 本地验证步骤

1. 先启动本机 Camunda（c8run）。  
2. `cd Coursework/hospital-pathway` → `mvn spring-boot:run`。  
3. 确认日志中有「领域库就绪」。  
4. 确认生成 `data/hospital-domain.mv.db`（或同前缀文件）。  
5. （可选）用 IDE 连 `jdbc:h2:file:./data/hospital-domain` 用户 `sa`、空密码，查看三张表。
