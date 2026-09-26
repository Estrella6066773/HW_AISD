# est：治疗预约与付款流程变量设计

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：[`Est/est：治疗预约与付款活动设计.md`](est：治疗预约与付款活动设计.md) 中已纳入的 14 个元素。概念图 `Est/W02_Treatment_Booking_Payment.bpmn` 写明：记录付款结果包含状态、交易参考号、日期和金额。
**状态**：步骤 2 已规定变量名。概念图未改，没有写代码。两个网关条件已写入可执行副本。人工填写的变量要等步骤 4 的表单才会进入流程。

本文件放在个人目录 `Est/`。一条流程实例只用一个病例号。消息关联键等于变量 `case_reference` 的值。

## 变量

| 变量名 | 类型 | 谁写入 | 写入发生在 | 谁读取 | 含义 |
|--------|------|--------|------------|--------|------|
| `case_reference` | 文本 | 顾问 | 用户任务「记录同意并授权治疗」 | 发出付款请求的程序、发出预约确认的程序、消息捕获事件 | 病例号。消息关联键等于这个值 |
| `consent_recorded` | 是否 | 顾问 | 用户任务「记录同意并授权治疗」 | 治疗预约组，在准备临时预约之前 | 顾问是否已记录患者同意。未记录时表单不得提交，流程不进入准备临时预约 |
| `provisional_booking_ready` | 是否 | 治疗预约组 | 用户任务「准备临时预约」 | 财务组，在核对费用与资助之前 | 临时预约所需档期是否已经备好。准备临时预约不确认最终预约 |
| `funding_resolved` | 是否 | 财务组 | 用户任务「核对费用与资助」 | 「患者是否需要付款」网关之前的表单校验 | 资助决定是否已经做出。未做出时表单不得提交 |
| `patient_payment_required` | 是否 | 财务组 | 用户任务「核对费用与资助」 | 排他网关「患者是否需要付款」 | 为真时患者需要自己付款；为假时有效资助或已授权安排已经覆盖费用 |
| `charge_amount` | 数字 | 财务组 | 用户任务「核对费用与资助」 | 发出付款请求的程序、「记录付款结果」展示金额 | 需要患者支付的金额。不需要患者付款时留空 |
| `payment_status` | 文本 | 发出付款请求的程序 | 发送任务「发出付款请求」完成时 | 排他网关「付款是否成功」；财务组在「记录付款结果」中只查看、不改写 | `successful` 或 `unsuccessful` |
| `transaction_reference` | 文本 | 发出付款请求的程序 | 发送任务「发出付款请求」完成时 | 财务组在「记录付款结果」中查看 | 模拟产生的交易参考号。付款不成功时为空 |
| `payment_date` | 日期 | 发出付款请求的程序 | 发送任务「发出付款请求」完成时 | 财务组在「记录付款结果」中查看 | 模拟交易日期。付款不成功时为空 |
| `payment_requested_once` | 是否 | 发出付款请求的程序 | 该程序成功发出付款请求之后 | 同一程序在重试时读取 | 为真表示这个病例号已经发过一次付款请求。再次执行时沿用已有状态和交易参考号，不产生第二笔扣款记录 |
| `booking_reference` | 文本 | 治疗预约组 | 用户任务「确认治疗预约」 | 发出预约确认的程序 | 已确认的预约号 |
| `confirmation_sent` | 是否 | 发出预约确认的程序 | 发送任务「发出预约确认」完成时 | 流程结束在「预约已确认」之前 | 为真表示预约确认已经发出。重复执行时保持为真 |
| `follow_up_note` | 文本 | 财务组 | 用户任务「保持待处理并跟进」 | 本段结束前留在流程实例上 | 付款不成功之后的跟进说明。这张表单不改写 `payment_status` |

开始事件「治疗已同意」不写变量。结束事件「预约已确认」和「待处理结束」不写变量。

## 网关条件

| 网关 | 为「是」时的条件 | 条件读取的变量 | 谁把这个变量写入流程 |
|------|------------------|----------------|----------------------|
| 患者是否需要付款 | `patient_payment_required = true` | `patient_payment_required` | 财务组，在用户任务「核对费用与资助」 |
| 付款是否成功 | `payment_status = "successful"` | `payment_status` | 发出付款请求的程序，在发送任务「发出付款请求」 |

「患者是否需要付款」为否时，流程不读取 `payment_status`。此时 `charge_amount`、`transaction_reference` 和 `payment_date` 保持为空。

「付款是否成功」为否时，`payment_status` 的值为 `unsuccessful`。财务组随后写入 `follow_up_note`，流程结束在「待处理结束」。

## 每个纳入元素与变量的关系

| 元素 | 写入 | 读取 |
|------|------|------|
| 治疗已同意 | 无 | 无 |
| 记录同意并授权治疗 | `case_reference`、`consent_recorded` | 无 |
| 准备临时预约 | `provisional_booking_ready` | `consent_recorded` |
| 核对费用与资助 | `funding_resolved`、`patient_payment_required`、`charge_amount` | `provisional_booking_ready` |
| 患者是否需要付款 | 无 | `patient_payment_required` |
| 发出付款请求 | `payment_status`、`transaction_reference`、`payment_date`、`payment_requested_once` | `case_reference`、`patient_payment_required`、`charge_amount`、`payment_requested_once` |
| 收到付款结果 | 无。程序把 `payment_status`、`transaction_reference`、`payment_date` 随消息带回 | 关联键等于 `case_reference` |
| 记录付款结果 | 无。财务组确认已看到结果，不改写付款状态 | `payment_status`、`transaction_reference`、`payment_date`、`charge_amount` |
| 付款是否成功 | 无 | `payment_status` |
| 保持待处理并跟进 | `follow_up_note` | `payment_status` |
| 待处理结束 | 无 | 无 |
| 确认治疗预约 | `booking_reference` | `patient_payment_required`。若来自付款成功分支，同时能读到 `payment_status` |
| 发出预约确认 | `confirmation_sent` | `case_reference`、`booking_reference` |
| 预约已确认 | 无 | `confirmation_sent` |
