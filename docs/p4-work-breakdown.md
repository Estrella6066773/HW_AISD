# Part 4 任务拆分

将 Product Backlog 拆成可在一个 sprint 内完成的小任务。Backlog ID（PB-xx）供 Part 3 对齐。

| Task ID | Backlog ID | Task Description | First Owner | Second Owner | Estimate | Dependency | Acceptance Conditions | Evidence Required | Status |
|---------|------------|------------------|-------------|--------------|----------|------------|----------------------|-------------------|--------|
| T01 | PB-01 | 列出转诊核验涉及的角色与权限边界（秘书可补件、不可接受转诊） | Ruby | Estrella | 2h | Part 1 摘要 | 角色表与案例规则一致 | Part 1 摘要中的权限规则 | Done |
| T02 | PB-01 | 起草转诊主路径：收件 → 核材料 → 送 Consultant | Ruby | Ryan | 3h | T01 | 主路径步骤可对应案例原文 | BPMN 草稿 | In progress |
| T03 | PB-02 | 增加 Consultant 四态：接受 / 拒绝 / 补材料 / 转专科；原因与操作人必填 | Ruby | Estrella | 3h | T02 | 无原因或无操作人则无法提交 | 决策表单字段说明 | Not started |
| T04 | PB-02 | 增加拒绝/转专科后的结束或转出路径 | Ryan | Ruby | 2h | T03 | 拒绝后不进入新患预约 | 异常路径图 | Not started |
| T05 | PB-03 | 仅在接受后生成 New Patient Appointment 预约请求（专科、优先级、时间窗、患者需求） | Ruby | Ender | 3h | T03 | 未接受时行政无法约号 | 门禁说明 + 模型 | Not started |
| T06 | PB-03 | 对接/模拟外部排班：有号则确认，无号则高亮并转 pathway，禁止 silently 约到窗外 | Ender | Ryan | 5h | T05 | 无号时状态为 pending/escalated | worker 日志或 mock 记录 | Not started |
| T07 | PB-04 | 实现通知规则：常规发信；预约在两周内须另记电话联系及每次结果 | Estrella | Ruby | 3h | T05 | ＜14 天必须有电话尝试记录 | 通知规则表 + 表单 | Not started |
| T08 | PB-05 | 治疗请求：记录同意并创建已授权 Treatment Booking Request（治疗、开始日、周期、复查、资源） | Ruby | Estrella | 3h | T05 | 无临床授权则行政不能处理 | 表单校验说明 | Not started |
| T09 | PB-06 | 外部治疗/检验/影像不可用时：booking pending、通知负责团队、防重复预约 | Ender | Ryan | 4h | T08 | 不产生重复预约记录 | 失败路径测试记录 | Not started |
| T10 | PB-07 | 确认治疗前判定资金来源；需付款则发支付请求；不存完整卡号 | Ender | Estrella | 5h | T08 | 回写状态/流水/金额/日期；无卡号存储 | worker + 字段清单 | Not started |
| T11 | PB-07 | 支付失败可重试；Provider 成功但无回执则标调查，禁止自动再扣 | Ender | Ryan | 4h | T10 | 三条路径可演示 | 测试用例结果 | Not started |
| T12 | PB-08 | 紧急先治：记录临床原因并转 Finance 事后处理 | Ryan | Ruby | 2h | T10 | 原因必填且可审计 | 异常路径 + 审计点 | Not started |
| T13 | PB-09 | Clinic Letter：医生批准后秘书才可分发；秘书不得改临床含义 | Estrella | Ruby | 3h | T08 | 未批准不可外发 | 表单权限说明 | Not started |
| T14 | PB-09 | 信件超 7 天标延迟；约 1 月 / 3 月升级；完成后停止催办 | Ryan | Estrella | 3h | T13 | 升级层级与案例一致 | 监控规则说明 | Not started |
| T15 | PB-10 | 咨询分流：行政 / 财务 / 临床分类、优先级、指派；接线员禁止临床建议 | Estrella | Ender | 3h | T01 | 临床类必须转到 CNS/临床 | 分流表单 | Not started |
| T16 | PB-11 | 审计点：转诊决策、治疗授权、信件批准、支付/退款、治疗修改；普通用户不可改审计 | Ryan | Ruby | 3h | T03, T08, T10 | 记录含用户、时间、动作 | 审计字段表 | Not started |
| T17 | PB-12 | 起草战略 BPMN 主图并与运营模型对齐 | Ruby | Estrella | 4h | T02–T08 | 高层路径完整、门禁可见 | .bpmn 文件 | Not started |
| T18 | PB-13 | 绑定转诊核验与 Consultant 决策的 Camunda Form | Estrella | Ruby | 4h | T03, T17 | 必填校验生效 | 表单 + 截图 | Not started |
| T19 | PB-14 | 编写主路径与拒绝转诊两条验收测试 | Ryan | Ender | 3h | T03, T06 | 有预期结果与实际结果栏 | 测试计划 | Not started |
| T20 | PB-15 | 准备第一次站会：上传产品待办与本表，四人入仓 | Ruby | Estrella | 2h | 当前增量 | 仓库内有产品待办与本表，四人已加入 | GitHub 链接 + Part 3 与 Part 6 文件 | In progress |

估算为第一负责人工时。Part 3 定稿后如编号有变，只改 Backlog ID 列即可。

T01 的角色与权限规则已按案例第 3 段写进 Part 1 摘要，证据列据此指向该摘要；Dluffy 的复核意见要求补证据位置，即为此处。T02 沿用 Sprint Backlog 的记法，同为 In progress，故 `docs/p3-product-backlog.md` 的 PB-01 记进行中。T20 与 Part 6 的 Sprint 1 范围一致，指第一次站会的上传动作。
