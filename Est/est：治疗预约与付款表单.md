# est：治疗预约与付款表单

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：[`Est/est：治疗预约与付款流程变量设计.md`](est：治疗预约与付款流程变量设计.md)。表单编号与 [`Est/W02_Treatment_Booking_Payment_Executable.bpmn`](W02_Treatment_Booking_Payment_Executable.bpmn) 里六个用户任务的 `formId` 一致。
**状态**：步骤 4 已写好表单文件。概念图未改。Java 程序尚未编写。

表单放在个人目录 `Est/forms/`。变量名与步骤 2 相同。表单上没有卡号、安全码或病历正文。

| 用户任务 | 表单文件 | 表单编号 | 人写入的变量 | 不能提交的情况 |
|----------|----------|----------|----------------|----------------|
| 记录同意并授权治疗 | `forms/AuthoriseTreatmentForm.form` | `AuthoriseTreatmentForm` | `case_reference`、`consent_recorded` | 病例号为空，或未勾选已记录同意 |
| 准备临时预约 | `forms/PrepareBookingForm.form` | `PrepareBookingForm` | `provisional_booking_ready` | 未勾选档期已经备好 |
| 核对费用与资助 | `forms/CheckFundingForm.form` | `CheckFundingForm` | `funding_resolved`、`patient_payment_required`、`charge_amount` | 未勾选资助决定已经做出；或者勾选了患者需要自己付款但金额为空或小于 0.01 |
| 记录付款结果 | `forms/RecordPaymentForm.form` | `RecordPaymentForm` | `payment_result_acknowledged` | 未勾选已经核对结果 |
| 确认治疗预约 | `forms/ConfirmBookingForm.form` | `ConfirmBookingForm` | `booking_reference` | 预约号为空 |
| 保持待处理并跟进 | `forms/FollowUpForm.form` | `FollowUpForm` | `follow_up_note` | 跟进说明为空 |

「患者需要自己付款」不勾选是允许的。此时金额栏隐藏，流程走「不需要付款」分支。勾选之后金额栏出现，并且必须填写。

「记录付款结果」把付款状态、交易参考号、付款日期和应付金额设成只读。勾选「我已核对此次付款结果」写入 `payment_result_acknowledged`，只表示财务组已经过目，不改写 `payment_status`。这个变量不在步骤 2 的原表里，是这张表单为了完成「确认已过目」而增加的。

「保持待处理并跟进」只读显示 `payment_status`，跟进说明写入 `follow_up_note`。付款状态控件不可编辑，因此提交不会把状态改成别的值。

在 Camunda Modeler 中打开 `Est/forms/` 下的表单文件可以预览。与可执行模型一起部署后，Tasklist 按 `formId` 打开对应表单。
