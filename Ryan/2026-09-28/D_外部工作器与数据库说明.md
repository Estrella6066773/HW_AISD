# D / Ryan：一个 Worker 的学生精简版

只保留必做 `notify-care-change`。当前正式文件在 `Coursework/hospital-pathway/`，可选学习包尚未同步。组长要求的二责复核仍待 A／B 完成。

## 这个 Worker 做什么

医生在表单中确认治疗变更，Java 把“已通知路径管理团队”的模拟结果保存到 H2，再让流程继续。

```text
变更授权 Form → Notify care change（Java）→ 授权／财务网关 → 后续流程
```

问询仍由人填写答复后直接结束。图上只保留 D 的一个新增服务任务。

## 只需要理解四步

打开 [CareChangeWorkers.java](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/CareChangeWorkers.java)。整个类包含导入、空行和中文注释。

| 行号 | 做什么 | 讲解重点 |
|---|---|---|
| 23–24 | `@JobWorker(type = "notify-care-change")` | 名字与图上 Job type 相同，Camunda 才会把任务交给它 |
| 25–34 | 读取、检查流程变量 | 病例号、医生、变更目标和是否影响费用来自原来的表单与 BPMN 映射 |
| 36–43 | 判断通知结果 | 已授权则模拟通知；缺授权就跳过；涉钱时标记需要 Finance 审核 |
| 45–50 | 保存数据库回执并打印日志 | 使用 B 的共享 `audit_event` 表，同一任务重试复用记录 |
| 52–55 | 返回三个结果变量 | Camunda 自动完成服务任务，继续走原来的网关 |

四个输入：`patientId`、`clinicianId`、`changeTarget`、`moneyAffected`。其中后两个由 `ClinicalChange` 的输出映射从表单选择生成，Java 不重复计算一套网关规则。

三个输出：`careChangeNotificationSent`（是否模拟通知成功）、`careChangeNotificationStatus`（结果状态）、`careChangeNotificationReference`（数据库回执号）。

状态只有：

- `SENT`：已记录模拟通知。
- `SENT_FINANCE_REVIEW_REQUIRED`：已记录模拟通知，费用问题仍由 Finance 决定。
- `SKIPPED_UNAUTHORISED`：缺少正式授权，跳过通知，原网关回到补资料。

## 数据库部分怎么看

[AuditEventWriter.java](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/domain/AuditEventWriter.java) 的 24–39 行：**先查询，有记录就返回，没有才新增**。普通 `@Transactional` 保证保存成功后才从方法返回。原四参数接口供其他同学继续使用。

重复检查键由“Worker 类型 + 流程实例编号 + 节点实例编号”组成。同一节点重试用相同的键；下一次新的变更有新键。数据库唯一列是基本防重复保护，不再加额外并发补偿框架。

库文件是 `Coursework/hospital-pathway/data/hospital-domain.mv.db`。查库方法见[运行说明](../../Coursework/hospital-pathway/README.md)。既有演示记录保留；可按自己的新病例号查看本次记录。

```sql
SELECT id, actor, action, case_reference, payload_summary
FROM audit_event
WHERE case_reference = 'D-DEMO-SIMPLE-001';
```

## 课堂演示

1. 启动 c8run，然后在正式包目录启动 `mvn spring-boot:run`（Java 21）；只开一套工作器程序。
2. Tasklist 新开 Hospital 总流程，登记虚构病例 `D-DEMO-SIMPLE-001`，选择 **Authorised change / follow-up / cancellation**。
3. 在变更表填写医生和说明，选择 **Authorise stop / discharge - no financial impact**，提交。
4. Java 自动记录通知，流程走到结束。Operate 的流程级 Variables 可看到 `SENT`、`true` 和 `AUD-…`；数据库中有同一病例的记录。

简单讲法：

> 我的 Worker 接收表单产生的变更信息，判断能否通知，然后把模拟通知结果写入数据库。写入成功后返回结果，Camunda 继续运行。同一个任务重试时会复用原记录。医生和财务的决定仍由人填写。

本次只做课堂模拟通知，没有真实邮件／短信发送，也没有新增 BPMN Message。支付统计、故障注入、可选问询回执和额外并发处理均已删除。
