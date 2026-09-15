# Ryan：Part 5 Dependency Mapping

**主笔**：Ryan（23084395）  
**复核**：Estrella（23084393）  
**依据**：Agile Workshop Part 5；Case Study — *Hospital Patient Referral, Treatment and Administration System*；Part 4 任务拆分（T01–T20）  
**日期**：2026-09-15

> 口径：Part 4 已给出每张卡的前置任务。Part 5 不重写任务表，只把**每张卡**补全作业要求的四问，并说明依赖来自案例原文哪一条规则。依赖只有在前置任务的验收条件真正满足后才算解除，不能口头说「差不多了」。

---

## 作业要求（原文）

For each task, identify:

1. What must be completed first?
2. Which task depends on this task?
3. Who needs to be informed if this task is delayed?
4. What is the backup plan?

---

## 一、案例原文决定的业务顺序

任务依赖不是随意排的。案例把临床决定、行政执行、财务处理拆开，并且写明了先后门禁。下面按原文顺序抽出必须先完成的环节；任务卡必须服从这条链，不能跳步。

| 顺序 | 案例原文（节选） | 对本组任务的含义 |
|------|------------------|------------------|
| 1 | *When a new patient is referred to the specialist service, the referral is initially received by the Medical Secretaries. They check whether it contains the expected supporting information… they are not permitted to assess the patient’s clinical suitability or decide whether the referral should be accepted.* | 先有角色边界与核验路径（T01、T02），才能进入医生决策。秘书不能接受转诊。 |
| 2 | *Once the available documents have been checked, the referral is sent to the appropriate Consultant for clinical review. The Consultant may accept the referral, reject it, request further information or redirect it to another specialist service. The reason for the decision and the identity of the person making it must be recorded.* | 主路径（T02）完成后才能加四态决策（T03）。原因与操作人是后续所有分支的前提。 |
| 3 | *A New Patient Appointment may only be arranged after an authorised Consultant has accepted the referral.* | 预约请求（T05）硬依赖接受。拒绝/转出路径（T04）必须先于任何约号。 |
| 4 | *The team must identify an appropriate appointment using the hospital’s external scheduling service and confirm the booking within the Hospital Patient Administration System. The patient is normally informed by a letter… if the appointment is due to take place within the following two weeks, the patient must also be contacted by telephone.* | 外部排班（T06）依赖已生成的预约请求。通知规则（T07）依赖预约已成立；两周内还要记每次电话结果。 |
| 5 | *If an external service is temporarily unavailable, the booking must remain pending, the responsible team must be notified and further attempts must be recorded without creating duplicate appointments.* | 无号或外部不可用不是失败就停，而是挂起 + 通知 + 防重复。这既是 T06/T09 的规则，也是延误时的业务备份。 |
| 6 | *If the patient agrees to proceed with treatment, the Consultant records the patient’s consent and creates an authorised Treatment Booking Request. … A request that has not been completed and authorised by an appropriate clinical professional must not be processed by administrative staff.* | 治疗请求（T08）只能在新患就诊与授权之后。没有授权，行政任务不得往下做。 |
| 7 | *Before a treatment appointment is confirmed, the system must determine whether the patient’s treatment is funded by the hospital, covered by an approved insurer or funding organisation, or requires payment by the patient.* | 资金判定与支付（T10、T11）依赖已授权的治疗请求（T08），不能与约号并行提前确认治疗。 |
| 8 | *In such circumstances, the transaction must be marked for investigation rather than automatically requesting another payment. Clinical staff must still be able to authorise urgent treatment when delaying care would create a risk to the patient, but the reason for proceeding without confirmed payment must be recorded and referred to the Finance Team.* | 无回执 → 调查、禁止自动再扣（T11）。紧急先治（T12）依赖支付路径已定义，且必须记原因并转财务。 |
| 9 | *The Consultant remains responsible for the clinical content of the letter and must approve it before it can be distributed. … If a letter remains incomplete or unapproved more than seven days after the appointment, it is considered delayed…* | 信件分发（T13）依赖就诊后的临床内容与批准；升级催办（T14）依赖信件流程已存在。 |
| 10 | *Following the New Patient Appointment, the patient… may also contact the hospital through the Call Handling Team, which must determine whether an enquiry is administrative, financial or clinical. Call handlers must not diagnose…* | 咨询分流（T15）业务上发生在第一次门诊之后；实现上先要角色权限（T01）。 |
| 11 | *The system must… record significant actions, including… referral decisions, … clinical authorisations, correspondence approvals, … payment requests, funding decisions and refunds. Audit records must identify the user, date, time and nature of each action and must not be editable by ordinary users.* | 审计（T16）依赖转诊决策、治疗授权、支付等动作已经定义，不能先做空审计。 |

**小组假设（与 Part 1 一致，不改变上述门禁）**：16 Sep 只交计划；外部排班与支付可用 mock，但 mock 也必须表现案例写明的失败行为（pending / 调查 / 不重复建号 / 不自动再扣）。「紧急咨询如何判定」案例未写死，不编政策。

---

## 二、任务级依赖映射（T01–T20）

表中「必须先完成」以 Part 4 的 Dependency 列为准；若案例原文还要求更严的顺序，写在括号里，供复核时收紧，不擅自改 Part 4 编号。

知会对象：延误时由**本卡第一负责人**通知第二负责人，以及所有后继卡的第一负责人。Sprint 1 关键路径延误时额外通知全组。

| Task ID | What must be completed first? | Which task depends on this task? | Who needs to be informed if delayed? | What is the backup plan? |
|---------|-------------------------------|----------------------------------|--------------------------------------|--------------------------|
| T01 | Part 1 案例摘要（角色与权限已对齐原文：秘书只核材料，不能接受转诊） | T02, T15 | Estrella（二责）；Ruby（T02）；Estrella（T15） | 二责 Estrella 按案例第 3 段收口权限表。16 Sep 可先用文字权限说明，不阻塞主路径起草。 |
| T02 | T01 | T03, T17 | Ryan（二责）；Ruby（T03、T17） | 二责 Ryan 用文字主路径顶上（receive → check papers → send to Consultant）。16 Sep 允许先交路径说明，BPMN 可后补。 |
| T03 | T02 | T04, T05, T16, T18, T19；T17 也覆盖本卡 | Estrella（二责）；Ryan（T04）；Ruby（T05）；全组（Sprint 1 关键路径） | **关键路径。** 二责 Estrella 按原文四态补字段：accept / reject / request further information / redirect；无原因、无操作人则不能提交。T05 在 T03 完成前不得生成约号。 |
| T04 | T03 | T19（拒绝路径测试需要本卡；Part 4 未写进 Dependency，但案例要求拒绝后不得约新患） | Ruby（二责）；Ryan（T19） | 二责 Ruby 接手。若图未画完，先用文字规则：*A New Patient Appointment may only be arranged after an authorised Consultant has accepted the referral.* 拒绝/转出不进入 T05。 |
| T05 | T03（案例：仅 authorised Consultant 接受之后） | T06, T07, T08, T17 | Ender（二责）；Ender（T06）；Estrella（T07）；Ruby（T08）；全组 | **关键路径。** 未接受则行政不能约号。二责 Ender 先写门禁规则。T06/T07/T08 全部停，直到「已接受」可判定。 |
| T06 | T05 | T19 | Ryan（二责）；Ryan（T19）；全组 | **关键路径。** 外部排班按组假设用 mock。无号或服务不可用时按原文：*remain pending, the responsible team must be notified… without creating duplicate appointments*；禁止 silently 约到窗外。mock 未就绪则先演示 pending / escalated 状态。 |
| T07 | T05（案例更严：应在预约确认之后，即 T06 之后再发通知） | 本期无后继实现卡；T20 演示需能讲清通知规则 | Ruby（二责）；Ruby（T20） | 二责 Ruby 先出规则表：常规 letter；两周内必须 telephone，并记录每次 unanswered / incorrect number / alternative appointment。不阻塞 T06 的排班 mock。 |
| T08 | T05（案例：患者已参加 New Patient Appointment 并同意治疗后） | T09, T10, T13, T16, T17 | Estrella（二责）；Ender（T09、T10）；Estrella（T13） | 无临床授权则行政不得处理。二责 Estrella 先锁授权字段（treatment, start date, cycles, reviews, resources）。Sprint 1 若只演示到约号，本卡可标未完成并移入下一 sprint，不扩大 Goal。 |
| T09 | T08 | 后续集成测试（PB-18 / 实现 Sprint）；不进 16 Sep 硬路径 | Ryan（二责）；Ender（T10 同属外部失败） | 按原文挂起 + 通知 + 记重试 + 不重复建号。外部治疗/检验/影像一律 mock。Owner 延误则二责 Ryan 先写失败路径说明。 |
| T10 | T08 | T11, T12, T16 | Estrella（二责）；Ender（T11）；Ryan（T12） | 先判定 hospital / insurer / patient 谁出钱，再发支付请求。不存完整卡号。二责 Estrella 先出资金字段清单。支付 worker 未就绪时只演示「未判定资金则治疗预约不能确认」。 |
| T11 | T10 | T16（支付/不确定交易必须可审计） | Ryan（二责）；Ryan（T16） | 三条路径必须可讲：失败可再付但不重复建号、不重复扣款；Provider 成功但本院无回执 → *marked for investigation rather than automatically requesting another payment*。禁止用「再扣一次」当备份。 |
| T12 | T10 | T16（紧急放行必须留痕） | Ruby（二责）；Ryan（T16） | 延误等待付款会危及患者时，医生可先治，但必须记原因并转 Finance。不写原因不能走紧急放行。二责 Ruby 用异常路径说明顶上。不得让财务或行政代替临床决定。 |
| T13 | T08 | T14, T16 | Ruby（二责）；Ryan（T14） | 未批准不可外发；秘书只改格式，不改临床含义。怀疑写错退回 Consultant。本卡不进 Sprint 1 Goal；延误则整段信件后置，不临时拉进 16 Sep 演示。 |
| T14 | T13 | 无直接后继实现卡 | Estrella（二责） | 超 7 天 = delayed；约 1 月升 Administrative Manager；约 3 月再往上。完成后停止催办。二责 Estrella 先出升级规则表。T13 未完成则本卡不得开始。 |
| T15 | T01（案例：Following the New Patient Appointment，业务上还依赖第一次门诊已发生） | 无直接后继实现卡 | Ender（二责） | 接线员可答行政问题；钱的问题转 Finance；临床必须转 CNS/临床，禁止诊断或建议治疗。紧急判定案例未写死：标待确认、问 tutor，不编规则。不进 Sprint 1。 |
| T16 | T03, T08, T10 | T19 的权限/审计检查；PB-18 补充测试 | Ruby（二责）；Ryan（T19） | 先覆盖转诊决定与治疗授权两条审计（案例核心动作），支付/信件/改期可第二期补。普通用户不能改审计。Owner 延误则二责 Ruby 先出字段表（user, date, time, nature of action）。 |
| T17 | T02–T08 | T18 | Estrella（二责）；Estrella（T18） | 16 Sep 不要求画图。延误时用 T02–T08 的文字路径作为战略模型草稿，并写明抽象层级：高层只画门禁与外部系统，不画表单细节。 |
| T18 | T03, T17 | T19（表单未绑则主路径测试不完整） | Ruby（二责）；Ryan（T19） | 28 Sep 再绑 Camunda Form。16 Sep 用字段说明代替表单。必填：专科、紧急程度、时间窗、患者需求、决策类型、原因。 |
| T19 | T03, T06（拒绝路径建议同时依赖 T04） | T20 | Ender（二责）；Ruby（T20） | 16 Sep 只交测试计划（主路径 + 拒绝转诊），不跑系统。实现未完成则预期/实际两栏如实留空，失败项写原因，不伪造成已测过。 |
| T20 | 当前增量（Sprint 1：T01–T07 + 本卡；仓库中的 PB 与 Sprint Backlog） | 无后继；直接服务 16 Sep Review | Estrella（二责）；全组 | 未完成项当场说明原因与下一 sprint。二责 Estrella 按 Part 8 讲稿分段：Ruby / Estrella / Ender / Ryan。缺证据的条目不得报 Done。 |

---

## 三、Sprint 1 关键路径

Sprint 1 Goal（与 Part 6 对齐）：**转诊核验 → Consultant 决策 → 第一次门诊预约**（排班可 mock）。支付、诊后信、咨询分流不进本期。

```text
T01 角色权限
  └─ T02 转诊主路径
        └─ T03 医生四态（原因 + 操作人）
              ├─ T04 拒绝/转出（不约新患）
              └─ T05 仅接受后才能约号          ← 业务门禁
                    ├─ T06 外部排班 mock（无号 pending）
                    └─ T07 通知规则（信；两周内再电话）
T20 与计划增量并行：PB + Sprint Backlog 上传，16 Sep 只演示计划
```

**最不能延误的三张卡**：T03、T05、T06。T03 一停，拒绝路径、约号门禁、表单、测试全部停。T05 一停，排班和通知没有合法输入。T06 一停，主路径测试（T19）缺「有号 / 无号」两种结果。

后继关系简图（实线 = Part 4 已写；虚线 = 案例要求、建议收紧）：

```text
T01 → T02 → T03 → T04
              T03 → T05 → T06 → T19
              T03 → T05 → T07
              T03 → T05 → T08 → T09
                              T08 → T10 → T11
                              T08 → T10 → T12
                              T08 → T13 → T14
              T03 ──→ T16 ←── T08, T10
              T03 → T18 ← T17 ← T02–T08
        T01 → T15
              T03, T06 → T19 → T20
                    T04 ⋯→ T19
                    T06 ⋯→ T07
```

---

## 四、延误时谁必须知道

| 延误的任务 | 必须通知 | 原因 |
|------------|----------|------|
| T02 / T03 | Ruby、Estrella、Ryan、全组 | 卡住 Sprint 1 全部临床决策工作 |
| T05 | Ruby、Ender、Estrella、全组 | 约号、排班、通知、治疗授权全部没有入口 |
| T06 | Ender、Ryan、全组 | 主路径测试与 28 Sep worker 演示依赖本卡 |
| T08 | Ruby、Estrella、Ender | 治疗、外部资源、资金三条线同时停 |
| T10 / T11 | Ender、Estrella、Ryan | 支付失败与无回执路径无法定义；禁止用自动再扣当补救 |
| T13 / T14 | Estrella、Ryan | 信件批准与升级链断裂 |
| 任一张卡的第一负责人缺席 | 该卡第二负责人 + Ryan（Part 5 / Standup 汇总） | 二责必须能顶上；Standup 要记录交接 |

第一负责人延误时，由本人（或 standup 汇总人 Ryan）在当日通知后继卡第一负责人，并写明：当前状态、缺什么验收、预计何时解除、是否启用备份。

---

## 五、备份原则（一律服从案例，不另发明政策）

1. **人的备份**：每张卡已有不同的第二负责人。交接最低限度：Task ID、当前文件、已满足/未满足的验收、阻塞原因、下一步、接收的第二负责人。不在交接记录里写账号密码。
2. **外部服务备份**：排班、发信、支付、检验/影像一律允许 mock，但必须保留原文失败行为——pending、通知负责团队、记录重试、不重复预约、不确定支付只标调查、不自动再扣。
3. **业务门禁备份**：任何延误都不能用「先约号再补医生意见」或「先确认治疗再补授权」来赶进度。原文禁止行政代替临床、禁止财务决定治不治。
4. **范围备份**：16 Sep 只演示计划。T08 及之后（治疗、支付、信件、咨询、审计实现）若来不及，保持可见、移入下一 sprint，不塞进 Sprint 1 Goal。
5. **未写清的规则**：紧急咨询如何判定等，标 ambiguity、问 tutor，不用猜测当备份方案。

---

## 六、依赖解除规则

- 前置任务的 **Acceptance Conditions** 满足，并且 **Evidence** 已放到对应日期文件夹或仓库，依赖才算解除。
- 状态标 Done 但证据路径缺失（例如 T01 权限表未附位置）= 依赖未解除。
- 复核人 Estrella 抽查：后继卡是否在前置未完成时提前开工；若有，退回并在 standup 记录。

## 证据

- 本文件：`Ryan/2026-09-15/Ryan：part5依赖映射.md`
- 任务来源：Part 4（T01–T20）；Sprint 1 范围：Part 6
- 业务依据：`W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
