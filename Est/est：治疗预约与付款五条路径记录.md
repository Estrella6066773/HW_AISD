# est：治疗预约与付款五条路径记录

**主笔**：Estrella（陈格平）
**日期**：2026-09-26
**依据**：步骤 7。流程定义 `TreatmentProcess`，引擎 http://localhost:8090 。工作器日志在运行中的 `src/workers` 进程里。
**状态**：五条路径都已在引擎上走完。Operate 页面截图未采集；浏览器打开 Operate 时页面停在空白。下面用流程实例键、结束状态和变量代替截图。在 Operate 搜索这些实例键可以打开对应路径。

登录 Operate / Tasklist 使用 `demo` / `demo`，地址是 http://localhost:8090/operate 和 http://localhost:8090/tasklist 。

## 结果

| 路径 | 流程实例键 | 结束位置 | 决定去向的变量 | 结果 |
|------|------------|----------|----------------|------|
| 不需要患者付款 | `2251799813861793` | 流程结束，状态 `COMPLETED`。没有进入「发出付款请求」 | `patient_payment_required = false`，随后 `confirmation_sent = true` | 没有 `payment_status`，没有交易参考号 |
| 付款成功 | `2251799813861835` | 流程结束，状态 `COMPLETED` | 金额 `10.01` 不以 0 结尾，工作器写入 `payment_status = successful` | 交易参考号 `TX-CASE-PAY-OK-1790424453237`，预约确认已发出 |
| 付款失败 | `2251799813861900` | 流程结束，状态 `COMPLETED`。停在待处理结束，没有确认预约 | 金额 `10.00` 以 0 结尾，`payment_status = unsuccessful` | 交易参考号为空，没有第二次扣款，`confirmation_sent` 没有写入 |
| 无效输入 | `2251799813861961` | 活动停在 `RequestPayment`。事件类型 `UNHANDLED_ERROR_EVENT`，状态仍为 `ACTIVE` | `patient_payment_required = true`，但没有金额 | 没有 `payment_status`，没有交易参考号。工作器日志记「付款请求输入无效」，错误码 `payment-input-invalid` |
| 重复领取付款任务 | `2251799813861995` | 第二次执行后停在 `PaymentReceived`（等待付款结果） | `payment_requested_once` 已为真 | 交易参考号两次都是 `TX-CASE-REPEAT-1790424469381`。工作器日志记「付款请求已经发出过，沿用原结果」。第二次没有再发消息，所以捕获事件一直等着 |

## 工作器日志中能对上的病例号

- `CASE-NOPAY`：发出预约确认，预约号 `BK-NOPAY`
- `CASE-PAY-OK`：付款请求结果 `successful`，然后发出预约确认
- `CASE-PAY-FAIL`：付款请求结果 `unsuccessful`
- `CASE-INVALID`：付款请求输入无效
- `CASE-REPEAT`：第一次结果 `successful`；第二次写明已经发出过并沿用原结果
