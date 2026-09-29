# AISD-3 Justification of Decisions（关键设计决策论证）


## 模型事实速览（用于追溯）

| 维度 | 数量 / 取值 | 说明 |
|---|---|---|
| 可执行流程 | 1（`Hospital_All_Processes_Simple_C8`） | 仅 HOSPITAL 池内承载 |
| 参与者（池） | 4 | HOSPITAL + 3 个外部黑盒参与者 |
| 泳道（Lane） | 3 | Finance / Clinical team / Administration |
| 排他网关 | 28 | **每个网关均设 `default` 默认分支** |
| 消息流 | 5 | 跨池交互 |
| 外部工作器任务类型 | 10（`zeebe:taskDefinition`） | Java JobWorker / send 连接器 |
| 用户任务 | 38 | 人工步骤 |
| 表单绑定 | 19（`zeebe:formDefinition` / `formId`） | 关联 11 个 `.form` 文件 |
| 中间捕获事件 | 2 | 其中 `PaymentReceived` 用于关联外部支付回执 |

---

## 1. Process structure（流程结构）

**决策**：采用**单一可执行流程**承载"患者就诊主路径 + 配套支持服务（财务、问询、审计）"，而不是把各业务拆成互不相连的多个流程。

**论证**：
- 入口为 `Start request` → `Register request`（P1/P10/P13，Administration 泳道）→ `Request type?` 排他网关，按请求类别分派到 7 条工作流：转诊（P2）、补材料（P1/P11）、行政问询（P10）、临床问询（P10）、财务问询（P10）、变更/随访（P11/P12）、报表（P13）。
- 临床主线程连贯可见：`Register → Referral decision? → Book visit → Visit outcome? → Clinical care → Clinical plan? → Funding → Funding status? → Book treatment → Resources ready? → Care episode ended`。
- 紧急照护有独立分支：`Urgent authorisation`（P8）→ `Urgent care authorised?` → `Urgent finance follow-up`（P8），避免紧急个案被常规排队阻塞。
- 财务/支付子线程：`Funding → Funding status? → Send payment request`（send task 至外部支付方）→ `Payment result received`（中间捕获事件）→ `Payment result?`。
- 信件子线程：`Dispatch clinic letter`（P9）→ `Letter status?` → `Monitor letters`（逾期提醒/升级）。
- 选择"单流程"而非"多独立流程"，是因为本课程的运营模型要求在一张图内展示 Participants / Responsibilities / Activities / Decisions / Messages / Business rules / Exceptions / System boundaries / External services 九要素；单一流程让跨参与者的消息流与端到端路径一目了然，也满足合并后模型可部署的前提（详见假设与权衡）。

---

## 2. Participant boundaries（参与者边界）

**决策**：建模 **4 个池（Participant）**，其中只有 `HOSPITAL` 是白盒可执行流程，其余 3 个为**黑盒外部参与者**，仅通过消息流交互。

**论证**：
- `HOSPITAL | Patient pathway and supporting services` —— 系统边界内，承载全部可执行逻辑。
- `Referring organisation | GP / Other hospital` —— 转诊来源，发起 `Msg_Referral`（referral documents）进入 Register。
- `Patient / authorised representative` —— 接收 `Msg_Contact`（预约/联系）、`Msg_Treatment`（治疗安排）。
- `External Payment Service Provider` —— 接收 `Msg_PaymentRequest`（支付请求），回传 `Msg_Payment`（verified transaction result）。
- 这样划分清晰标定了**系统边界**：进入 HOSPITAL 池的、由 Camunda 8 编排与执行的，是本小组负责的流程；转诊方、患者、支付服务方是被调用/被通知的外部实体，其内部流程不建模。这同时满足 AISD-1 对 *System boundaries* 与 *External services* 的要求，也避免把外部组织的内部业务强加进本系统。

---

## 3. Task allocation（任务分配）

**决策**：人工步骤按**职能泳道**分配责任；可自动化步骤交给**外部 Java 工作器（External Worker）**，每个工作器类由固定组员认领并理解其执行机制。

**论证（泳道 → 职责）**：
- **Administration**：`Register request`（P1/P10/P13）、`Admin enquiry`（P10）、`Audit reports`（P13）。
- **Clinical team**：`Review referral` / `Redirect`（P2）、`Book visit`（P3/P4/P12）、`Clinical care`（P5/P9/P12）、`Dispatch clinic letter` / `Monitor letters`（P9）、`Urgent authorisation`（P8）、`Clinical enquiry`（P10）、`Book treatment`（P6）、`Clinical change`（P11/P12）。
- **Finance**：`Funding assessment`（P7）、`Funding issue`（P7）、`Send payment request`（P7 send task）、`Finance adjustment`（P7/P11/P12）、`Urgent finance follow-up`（P8）、`Finance enquiry`（P10）。

**外部工作器归属（10 个 `zeebe:taskDefinition` 任务类型）**：

| Job type（与 `@JobWorker(type=…)` 一致） | 流程步骤 | 认领组员（工作器类） |
|---|---|---|
| `dispatch-clinic-letter` | P9 Dispatch clinic letter | **Member C / Ender — LetterWorkers** |
| `notify-referrer` | P2 Notify referrer | **Member C / Ender — LetterWorkers** |
| `notify-care-change` | P11/P12 Notify care change | **Member D / Ryan — CareChangeWorkers** |
| `request-refund` | P7/P11/P12 Request refund / record adjustment | **Member A / Ruby — RefundWorkers** |
| `check-slot` | P3 Check / reserve outpatient slot | **Member B / Est — BookingWorkers** |
| `reserve-appointment` | P6 Reserve treatment slot / resources | **Member B / Est — BookingWorkers** |
| `send-booking-confirmation` | P6 Send booking confirmation | **Member B / Est — BookingWorkers** |
| `flag-resource-unavailable` | P6 Flag resource unavailable | **Member B / Est — BookingWorkers** |
| `request-payment` | P7 Send payment request（send task） | Finance / P7 支付簇工作器 |
| `mark-payment-investigate` | P7 Mark payment investigate | Finance / P7 支付簇工作器 |

- 用户任务通过 19 个 `formId` 绑定到 Camunda Forms（`Coursework/hospital-pathway/forms/` 下 11 个 `.form` 文件），保证"用户填表 → 变量进入流程 → 工作器读取变量"的闭环。

---

## 4. Gateways（网关）

**决策**：全程使用**排他网关（exclusive gateway）**做分支/汇聚，且**每个网关都配置 `default` 默认分支**。模型共 28 个排他网关。

**论证**：
- 关键决策点：`Request type?`、`Referral decision?`、`Visit outcome?`、`Clinical plan?`、`Funding status?`、`Payment result?`、`Resources ready?`、`Formal request authorised?`、`Financial impact?`、`Letter status?`、`Urgent care authorised?` 等。
- 每个网关都设默认流（如 `Request type?` 默认 `Select type`、`Referral decision?` 默认 `Select decision`），确保**任何未显式命中的条件都有兜底路径**，避免流程在 Zeebe 中因无匹配序列流而卡死（incident / dead-end）。
- 这是确定性路由，而非依赖 LLM/规则引擎推断，符合本课程"契约清晰、可部署、可测试"的运营模型定位。

---

## 5. External interactions（外部交互）

**决策**：跨系统/跨组织交互一律通过**消息流（message flow）+ 外部工作器/send 任务**表达，不在本流程内模拟对方内部逻辑。

**论证（5 条消息流）**：
- `Msg_Referral`：Referrer → `Register`（转诊资料进入）。
- `Msg_Contact`：`BookVisit` → Patient（预约/联系）。
- `Msg_Treatment`：`SendBookingConfirmation` → Patient（治疗安排）。
- `Msg_PaymentRequest`：`RequestPayment` → PaymentProvider（支付请求，send task）。
- `Msg_Payment`：PaymentProvider → `PaymentReceived`（已验证交易结果，中间捕获事件关联）。
- 此外，10 个外部工作器是"系统与代码边界"：例如 `notify-referrer` 模拟通知转诊方、`dispatch-clinic-letter` 模拟外发 Clinic Letter，均只写审计不真正发信，把"真实外部副作用"留在系统边界之外（见假设与权衡）。

---

## 6. Exception handling（异常处理）

**决策**：以"**网关默认分支 + 用户任务重入 + 工作器重试 + 幂等审计**"四层组合处理异常，不引入独立的补偿/ saga 框架。

**论证**：
- **结构性兜底**：28 个网关均有 `default`，异常/未预见条件走默认流而非中断。
- **业务拒绝/异常终止**：`Referral rejected` → `End rejected`；`Visit outcome? = Cancel/DNA` → `Clinical change`（改约/取消）；`Formal request authorised? = Missing/invalid` → `GetDocuments`（退回补材料）。
- **支付异常**：`Payment result? = Unsuccessful` → `Mark payment investigate`（工作器）；`Funding status? = Pending/investigate` → 同一工作器或 `Funding issue`（人工复核）→ 回到 `Funding`。
- **资源异常**：`Resources ready? = Pending/retry` → `Flag resource unavailable`（工作器）→ 重试。
- **信件逾期**：`Letter status? = Delay/follow-up` → `Monitor letters`（提醒/升级）→ 回 `Clinical care`。
- **工作器韧性**：自动化任务设 `retries="3"`（`notify-care-change`、`request-refund`、`mark-payment-investigate`、`notify-referrer`、`dispatch-clinic-letter`）；审计写入以**幂等键**（`caseReference|workerType`）先查后插，重试不产生重复记录。

---

## 7. Assumptions（假设）

1. **合并模型可部署**：公告给出的"若合并模型无法部署则每人拆独立 BPMN"的应急方案**未被触发**——本合并模型 `isExecutable="true"` 且 XML 校验通过，已在 c8run 本地集群部署验证，因此采用单流程方案。
2. **外部参与者为黑盒**：Referrer / Patient / Payment Provider 仅以池 + 消息流表示，不建模其内部流程。
3. **工作器为模拟实现**：所有"发信/通知/支付"仅写入 H2 `audit_event` 审计表，不产生真实邮件、真实信件或真实资金变动——符合课程演示定位，也无外部凭证依赖。
4. **存储**：审计使用 H2（文件库 `data/hospital-domain.mv.db`），未新建额外领域表；唯一列提供基本防重保护。
5. **运行环境**：Java 21 + Spring Boot 工作器，`mvn spring-boot:run` 启动；c8run 提供 Zeebe / Operate / Tasklist。
6. **表单**：19 个 `formId` 绑定到 `forms/` 下 Camunda Forms，用户任务经表单采集变量。

---

## 8. Alternatives considered（考虑过的其他方案）

1. **每人独立 BPMN（公告应急方案） vs 单一合并流程**：应急方案能保证每人都有可部署模型，但会丢失跨参与者的端到端消息流与整体视图；因合并模型成功部署，故采用单流程。
2. **建模外部组织内部流程 vs 黑盒池 + 消息流**：前者信息更全但严重超出本课程系统边界与工作量；后者边界清晰、范围可控，被采用。
3. **真实邮件/支付集成 vs 审计模拟工作器**：真实集成需外部凭证与网络，且不适合演示；审计模拟可重复、可观测，被采用。
4. **并发补偿框架（saga）保证幂等 vs 数据库唯一键 + 幂等键**：saga 实现成本高、易出错；唯一键 + 先查后插足以覆盖课程场景的重试去重，被采用。
5. **用 LLM/智能体动态决定分支 vs 确定性网关**：智能体路径不可控、难测试、违背"可部署运营模型"定位；确定性排他网关被采用。

---

## 9. Trade-offs（方案之间的权衡）

| 选择 | 收益 | 代价 / 风险 | 缓解 |
|---|---|---|---|
| 单一合并流程 | 端到端视图完整、跨池消息一目了然、满足 AISD-1 九要素 | 模型较大，单人讲解难度高 | 每位组员深入理解自己工作器 + 能解释整体流程（公告要求） |
| 外部参与者黑盒化 | 系统边界清晰、范围可控 | 转诊方/支付方内部不可见 | 课程范围足够，且消息流已表达交互契约 |
| 审计模拟工作器 | 安全、可重复演示、无需外部凭证 | 非生产级真实副作用 | 课程定位接受；代码清晰标注"模拟" |
| 每网关设默认流 | 无死端、强韧 | 未建模的边角条件会被"静默"走默认，可能掩盖需求缺口 | 默认流命名明确，配合测试计划复核 |
| 唯一键幂等（非 saga） | 简单、够用 | 弱于完整补偿的事务保证 | 课程重试场景已被幂等键覆盖 |
| 按职能泳道分工 | 责任清晰 | 单条请求横跨多泳道（跨职能） | 用网关与消息流串起跨泳道协作 |

