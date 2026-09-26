# est：全院流程路径记录

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：`Coursework/hospital-pathway/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`，流程编号 `Hospital_All_Processes_Simple_C8`，版本 1，流程定义键 `2251799813868529`，部署键 `2251799813868527`。引擎 http://localhost:8090 。
**状态**：Java 程序与图、表单同在 `Coursework/hospital-pathway/`：部署全院图和共用表单 `hospital_task_form`，并运行 `request-payment` / `send-booking-confirmation` 两个 service-task worker。下面六条路径是在引擎上提交用户任务后读到的停靠位置。

这张图比 `Est/W02_Treatment_Booking_Payment.bpmn` 新。图上的支付服务、排程和信函服务只出现在协作图的消息箭头上。流程内部没有服务任务，也没有消息捕获。付款是否通过，由财务在用户任务 `Funding` 里选择 `action`，输出映射写入 `fundingStatus`。

到达 `Funding` 之前，每条主路径都用同一组选择：`Register` 的 `requestKind=referral`，`ReviewReferral` 的 `referralDecision=accept`，`BookVisit` 的 `visitOutcome=attended`，`ClinicalCare` 的 `careDecision=treatment`，`DispatchLetter` 的 `letterStatus=sent`。`Register` 同时把 `urgentCase` 写成 false。

| 路径 | 实例键 | 在 `Funding` 或 `Register` 写入的决定 | 停下的活动 | 结果 |
|------|--------|----------------------------------------|------------|------|
| 付款已核对，预约后结束诊疗 | `2251799813868565` | `fundingStatus=patient_paid`，随后 `BookTreatment` 的 `treatmentSlotStatus=ready`，再在下一次 `ClinicalCare` 选择 `discharge` | 实例状态 `COMPLETED`，结束事件 `EndCare` | 财务核对通过后才确认治疗预约 |
| 付款待处理 | `2251799813868758` | `fundingStatus=pending` | 用户任务 `FundingIssue` | 进入财务调查，不进入 `BookTreatment`，引擎没有第二次扣款 |
| 支付成功但确认缺失 | `2251799813868874` | `fundingStatus=investigate` | 用户任务 `FundingIssue` | 与待处理走同一个默认分支，先调查，不自动再扣款 |
| 财务请求紧急例外且医生授权 | `2251799813868988` | `fundingStatus=urgent_review`，随后 `urgentDecision=authorise`，`urgentCase=true` | 用户任务 `BookTreatment` | 医生授权后才能预约治疗 |
| 医生不授权紧急例外 | `2251799813869118` | `fundingStatus=urgent_review`，随后 `urgentDecision=hold` | 用户任务 `Funding` | 流程回到财务核对，不进入预约 |
| 登记时的请求类型无法识别 | `2251799813869248` | `requestKind=not-a-request-type` | 用户任务 `Register` | 网关条件都不成立，默认流回到登记任务 |
