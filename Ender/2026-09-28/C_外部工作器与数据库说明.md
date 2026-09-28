# C / Ender：外部工作器与数据库说明

> 本说明依据组长在 `Est/est：外部工作器与领域数据库总指引.md` 中分配给 C 的部分撰写。今日（2026-09-28）完成实现、BPMN 挂接与推送。二责复核仍待 A／B 完成。

## 这个 Worker 做什么

C 负责两个独立的服务任务，都只把"已经做过的动作"以审计形式写入 H2 的 `audit_event` 表：不真正发信、不真正联系转诊方、也不新建任何领域表。

```text
P9：DispatchLetter（人填表）→ DispatchClinicLetter（Java, dispatch-clinic-letter）→ LetterOutcome 网关
P2：Redirect（人填表）      → NotifyReferrer（Java, notify-referrer）            → EndReferral
```

两个服务任务分别在 P9 的信件外发环节和 P2 的转诊重定向环节，由人完成用户任务后自动触发，写完审计即让流程继续。

## 只需要理解几步

打开 [MemberCPathwayWorkers.java](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/MemberCPathwayWorkers.java)。整个类 92 行，含导入、空行与中文注释。

### dispatch-clinic-letter（P9）

| 行号 | 做什么 | 讲解重点 |
|---|---|---|
| 34–35 | `@JobWorker(type = "dispatch-clinic-letter")` | 名字与图上 Job type 相同，Camunda 才会把 P9 的任务交给它 |
| 36–40 | 读取流程变量 | 病例号、信件状态、信件备注、操作人角色来自表单与 BPMN 映射 |
| 42–49 | 拼接待幂等键并写审计 | 用 `caseReference\|dispatch-clinic-letter` 作幂等键，复用 `audit_event` 记录 |
| 50 | 打印日志 | 日志含病例号、状态、回执号 |
| 52–55 | 返回两个结果变量 | Camunda 自动完成服务任务，继续走 LetterOutcome 网关 |

四个输入：`case_reference`（缺则回退 `patientId`）、`letterStatus`、`DispatchLetterNotes`、`staffRole`。
两个输出：`clinicLetterDispatchStatus`（固定 `dispatched`）、`clinicLetterDispatchReference`（回执号 `C-DISPATCH-<case>`）。

### notify-referrer（P2）

| 行号 | 做什么 | 讲解重点 |
|---|---|---|
| 58–59 | `@JobWorker(type = "notify-referrer")` | 名字与图上 Job type 相同，Camunda 才会把 P2 的任务交给它 |
| 60–63 | 读取流程变量 | 病例号、转诊备注、操作人角色来自表单与 BPMN 映射 |
| 65–71 | 拼接待幂等键并写审计 | 用 `caseReference\|notify-referrer` 作幂等键，复用 `audit_event` 记录 |
| 72 | 打印日志 | 日志含病例号、回执号 |
| 74–78 | 返回三个结果变量 | Camunda 自动完成服务任务，继续走到 EndReferral |

三个输入：`case_reference`（缺则回退 `patientId`）、`RedirectNotes`、`staffRole`。
三个输出：`referrerNotificationSent`（固定 `true`）、`referrerNotificationStatus`（固定 `sent`）、`referrerNotificationReference`（回执号 `C-REFERRER-<case>`）。

状态只有固定值：`dispatched` / `sent`，表示"已记录模拟外发／通知"，不区分更多分支。

## 数据库部分怎么看

[AuditEventWriter.java](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/domain/AuditEventWriter.java)：C 调用的是 5 参 `append(actor, action, caseReference, idempotencyKey, summary)` 重载，**先按 idempotencyKey 查询，有记录就返回，没有才新增**；普通 `@Transactional` 保证保存成功后才从方法返回。原四参数接口供其他同学继续使用。

重复检查键由"Worker 类型 + 病例号"组成（即 `caseReference|workerType`）。同一节点重试用相同的键；下一次新的信件／转诊有新键。数据库唯一列是基本防重复保护，不再加额外并发补偿框架。

库文件是 `Coursework/hospital-pathway/data/hospital-domain.mv.db`。查库方法见[运行说明](../../Coursework/hospital-pathway/README.md)。

```sql
SELECT id, actor, action, case_reference, payload_summary, occurred_at
FROM audit_event
WHERE actor = 'member-C'
ORDER BY occurred_at DESC;
```

应能看到 `dispatch-clinic-letter` 与 `notify-referrer` 两类记录，回执号分别为 `C-DISPATCH-...` 与 `C-REFERRER-...`。

## 如何运行与测试

1. 在正式包目录启动 `mvn spring-boot:run`（Java 21）；只开一套工作器程序。
2. 在 Modeler 选中 **P9 Dispatch clinic letter (audit)** 或 **P2 Notify referrer (audit)** 节点，点 Test → Run test。
3. 输入变量（见上"输入"），执行后应看到 worker 日志打印回执号，Operate 的 Variables 出现 `clinicLetterDispatchStatus=dispatched` / `referrerNotificationStatus=sent`。

注意：本机 Maven 的 `lib/boot/` 启动 jar 缺失，需用本机可用的 Maven 或手动 classpath 才能编译；连 GitHub 时若遇 `502 CONNECT tunnel failed`，是工作台托管代理拦截，清空 `https_proxy` 等环境变量后直连即可（见下）。

## 一句话讲法

> 我的两个 Worker 在 P9 信件外发和 P2 转诊重定向之后，把"已经外发／已经通知"的模拟结果写入审计库。写入成功后返回结果，Camunda 继续运行。同一个任务重试时会复用原记录。是否真正发信、是否真正联系转诊方仍由人决定。

## 今日（2026-09-28）完成记录

- 从组长指引 `Est/est：外部工作器与领域数据库总指引.md` 认领 C 的两个 Worker：`dispatch-clinic-letter`（P9）、`notify-referrer`（P2）。
- 新建 `Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/MemberCPathwayWorkers.java`（92 行，两个 `@JobWorker`，仅写 `audit_event`）。
- 修改 `Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`：在 `DispatchLetter→LetterOutcome` 间插入 `DispatchClinicLetter`，在 `Redirect→EndReferral` 间插入 `NotifyReferrer`；两个 serviceTask 的 `zeebe:taskDefinition type` 与 Java 注解一致，`retries=3`，diagram 同步更新，XML 校验通过。
- 未新增测试（按本人要求），未动 A／B／D 代码、未改表单、未新建数据表；推送前确认本地 `main` 与远端 `main` 同为 `ddeaaa7`，即其余部分均为仓库最新。
- 提交并推送：commit `943d935`（基于 `ddeaaa7`），已 `push origin main`，远端 `main` 现指向 `943d935`。
- 推送踩坑：第一发被工作台托管代理（`https_proxy=127.0.0.1:64667`）502 拦截，清空代理变量直连后成功。下次推送前缀：`env https_proxy= http_proxy= HTTPS_PROXY= HTTP_PROXY= git push origin main`。

## 本次范围声明

本次只做课堂模拟外发与通知记录，没有真实信件／邮件发送，也没有新增 BPMN Message 或通信记录表。支付、故障注入、额外并发处理均未涉及；可选通信记录表按本人决定暂未建。
