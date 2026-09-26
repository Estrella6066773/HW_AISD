# est：治疗预约与付款可执行模型

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：[`Est/est：治疗预约与付款活动设计.md`](est：治疗预约与付款活动设计.md)、[`Est/est：治疗预约与付款流程变量设计.md`](est：治疗预约与付款流程变量设计.md)
**状态**：步骤 3 已在个人目录放好可执行副本。步骤 4 已按表单编号放好表单，见 [`Est/est：治疗预约与付款表单.md`](est：治疗预约与付款表单.md)。概念图未改。Java 程序尚未编写。

可执行副本：[`Est/W02_Treatment_Booking_Payment_Executable.bpmn`](W02_Treatment_Booking_Payment_Executable.bpmn)

概念图原件仍是 [`Est/W02_Treatment_Booking_Payment.bpmn`](W02_Treatment_Booking_Payment.bpmn)，流程属性保持不可执行。副本的医院流程属性为可执行。支付服务泳池仍是黑盒，里面没有内部步骤。两池之间原来的两条消息流保留：医院发出付款请求指向支付服务，支付服务把付款结果指回「收到付款结果」。

组内目录 `docs/operational-bpmn/` 先不放入这份副本。可执行模型和表单都仍在个人目录，等程序写好并一起走通后再放入组内目录。

## 程序执行的服务任务

概念图上的两个发送任务在副本里改成服务任务。元素编号未改，图上的位置未改。

| 图上的名称 | 元素编号 | 任务类型 |
|------------|----------|----------|
| 发出付款请求 | `RequestPayment` | `request-payment` |
| 发出预约确认 | `NotifyPatient` | `send-booking-confirmation` |

「发出预约确认」不另设等待它的捕获事件。程序写回 `confirmation_sent`。因此副本里没有名为 `booking-confirmation` 的消息。

## 付款结果消息

| 项 | 取值 |
|----|------|
| 消息编号 | `Message_PaymentResult` |
| 消息名 | `payment-result` |
| 谁发出 | 执行 `request-payment` 的程序 |
| 谁等待 | 医院流程里的「收到付款结果」`PaymentReceived` |
| 关联键 | `=case_reference` |

## 网关

每个排他网关把「否」设为默认出口，这样条件不成立时流程仍有唯一去向。

| 网关 | 「是」的条件 | 「是」的出口 | 默认出口（「否」） |
|------|----------------|--------------|---------------------|
| 患者是否需要付款 | `=patient_payment_required = true` | 发出付款请求 | 确认治疗预约 |
| 付款是否成功 | `=payment_status = "successful"` | 确认治疗预约 | 保持待处理并跟进 |

## 用户任务上的表单

六个用户任务都指定处理人 `demo`，并挂上表单编号。表单文件已在 `Est/forms/`，编号与下表相同。

| 用户任务 | 表单编号 |
|----------|----------|
| 记录同意并授权治疗 | `AuthoriseTreatmentForm` |
| 准备临时预约 | `PrepareBookingForm` |
| 核对费用与资助 | `CheckFundingForm` |
| 记录付款结果 | `RecordPaymentForm` |
| 确认治疗预约 | `ConfirmBookingForm` |
| 保持待处理并跟进 | `FollowUpForm` |

Camunda Modeler 打开这份副本时，可以对齐任务类型、消息名、关联键和网关条件。与 `Est/forms/` 一起部署后，Tasklist 按表单编号打开对应表单。
