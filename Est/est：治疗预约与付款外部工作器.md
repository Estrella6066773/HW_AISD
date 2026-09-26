# est：治疗预约与付款外部工作器

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：[`Est/est：治疗预约与付款流程变量设计.md`](est：治疗预约与付款流程变量设计.md)、[`Est/est：治疗预约与付款可执行模型.md`](est：治疗预约与付款可执行模型.md)、[`Est/W02_Treatment_Booking_Payment_Executable.bpmn`](W02_Treatment_Booking_Payment_Executable.bpmn)
**状态**：步骤 5 的行为已实现在 `src/workers/`。步骤 6 已在本机部署流程和表单，程序已订阅两个任务类型。Java 源文件：`src/workers/src/main/java/io/camunda/demo/treatment_booking/`。

本文件放在个人目录 `Est/`。程序是一个保持运行的 Spring Boot 进程，使用 Camunda Java 客户端连接本机 Camunda。它等待引擎分配任务，不提供患者或员工使用的网页。程序不读取卡号、安全码或病历正文。

## 与已有名称的对照

下列名称在流程变量设计、可执行模型和本文件中一致，因此可以在下一步按此编写程序。

| 名称 | 流程变量或模型中的写法 | 本文件中的写法 |
|------|------------------------|----------------|
| 发出付款请求的任务类型 | `request-payment` | `request-payment` |
| 发出预约确认的任务类型 | `send-booking-confirmation` | `send-booking-confirmation` |
| 付款结果消息名 | `payment-result` | `payment-result` |
| 关联键 | 模型表达式 `=case_reference`，值来自变量 `case_reference` | 发布消息时，关联键等于 `case_reference` 的文本值 |
| 付款成功取值 | `payment_status = "successful"` | `successful` |
| 付款不成功取值 | 网关默认出口 | `unsuccessful` |
| 预约确认是否已发出 | `confirmation_sent` | `confirmation_sent` |

「发出预约确认」不发布名为 `booking-confirmation` 的消息。可执行模型里没有等待这封消息的事件。

## `request-payment`

该方法 `autoComplete = false`。程序先发布消息，再手动完成任务。

读取：`case_reference`、`charge_amount`、`patient_payment_required`、`payment_requested_once`。若后三个尚不存在，分别视为空、假、假。

按下面顺序处理，命中一条就停止。

1. **输入无效。** 病例号为空，金额为空，或 `patient_payment_required` 不为真。向引擎抛出错误，错误码 `payment-input-invalid`。不发布消息，不生成交易参考号，不把 `payment_requested_once` 设为真。
2. **同一次付款请求已经发出过。** `payment_requested_once` 已经为真。不再生成新的交易参考号，不再发布第二封消息。把流程里已有的 `payment_status`、`transaction_reference`、`payment_date` 原样交回，然后完成任务。
3. **第一次处理这笔付款。** 把金额格式化成两位小数。该文本以字符 `0` 结尾时，`payment_status` 为 `unsuccessful`，`transaction_reference` 和 `payment_date` 为空。这包括 `10.00` 和 `12.50`。不以字符 `0` 结尾时，`payment_status` 为 `successful`，写入新的交易参考号，`payment_date` 为程序执行当天的日期。这包括 `10.01` 和 `12.51`。这是课堂演示规则，用来走出失败路径。付款不成功仍是一次完整的付款结果，不是错误码 `payment-input-invalid`。
4. **发布消息，成功之后才留下“已经请求过”的标记。** 消息名 `payment-result`。关联键等于 `case_reference` 的文本值。消息变量包含 `payment_status`、`transaction_reference`、`payment_date`。消息保留十分钟，供「收到付款结果」激活后取用。发布成功后，把 `payment_requested_once` 设为真，并与上述三个变量一起提交来完成任务。发布失败时，减少剩余重试次数并写明失败原因，不把 `payment_requested_once` 设为真，也不完成任务。下一次领取时标记仍为假，程序重新执行第 3 步。由于上一封消息没有发出，新的交易参考号不会和已经发出的扣款记录并存。标记一旦为真，以后的领取都走第 2 步，沿用已写回的参考号，不再发布第二封消息。

## `send-booking-confirmation`

该方法由客户端在方法返回变量后自动完成任务。

1. 读取 `case_reference` 和 `booking_reference`。病例号记入日志，供对照消息关联键，但病例号为空不单独构成错误。预约号为空时向引擎抛出错误，错误码 `booking-input-invalid`，并且不把 `confirmation_sent` 设为真。
2. 预约号有内容时写入 `confirmation_sent = true` 并完成任务。
3. 若 `confirmation_sent` 已经为真，保持为真并完成任务。不额外发布消息，也不生成第二份确认。

## 程序不处理的路径

患者不需要自己付款时，网关不会把流程送到 `request-payment`。该程序不为这条路径发布付款消息。退款、紧急治疗和全院其他流程不在这两个方法里实现。
