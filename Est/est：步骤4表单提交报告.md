# est：步骤 4 表单提交报告

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**分支**：`java`
**范围**：治疗预约与付款这一段里，六个人类用户任务的 Camunda 表单。概念图未改。Java 程序未包含在本次提交中。

## 本次提交做了什么

为可执行模型里已经写好的六个 `formId` 各增加一张表单，并更新流程变量设计和可执行模型说明，使文档与表单一致。

| 用户任务 | 文件 | 表单编号 |
|----------|------|----------|
| 记录同意并授权治疗 | `Est/forms/AuthoriseTreatmentForm.form` | `AuthoriseTreatmentForm` |
| 准备临时预约 | `Est/forms/PrepareBookingForm.form` | `PrepareBookingForm` |
| 核对费用与资助 | `Est/forms/CheckFundingForm.form` | `CheckFundingForm` |
| 记录付款结果 | `Est/forms/RecordPaymentForm.form` | `RecordPaymentForm` |
| 确认治疗预约 | `Est/forms/ConfirmBookingForm.form` | `ConfirmBookingForm` |
| 保持待处理并跟进 | `Est/forms/FollowUpForm.form` | `FollowUpForm` |

说明文档：`Est/est：治疗预约与付款表单.md`。

## 校验

- 病例号、预约号、跟进说明为空时不能提交。
- 「已记录患者同意并授权治疗」「临时预约所需档期已经备好」「资助决定已经做出」未勾选时不能提交。
- 「患者需要自己付款」不勾选时，金额栏隐藏，允许提交。勾选之后金额必须填写，且不能小于 0.01。
- 「记录付款结果」中的付款状态、交易参考号、付款日期和应付金额为只读。财务组勾选「我已核对此次付款结果」后写入 `payment_result_acknowledged`，不改写 `payment_status`。
- 「保持待处理并跟进」只读显示付款状态，跟进说明写入 `follow_up_note`。
- 表单上没有卡号、安全码或病历正文。

## 一并更新的已有文档

- `Est/est：治疗预约与付款流程变量设计.md` 增加变量 `payment_result_acknowledged`，并写明「记录付款结果」写入的是这个核对标记。
- `Est/est：治疗预约与付款可执行模型.md` 标明表单文件已在 `Est/forms/`，与模型中的表单编号一致。

## 本次没有提交的内容

- 概念图 `Est/W02_Treatment_Booking_Payment.bpmn` 未修改。
- 分步计划仍在 `Est/参考/`，该目录不纳入版本库。
- 可执行模型和表单尚未放入组内目录 `docs/operational-bpmn/`。外部工作器尚未编写。
