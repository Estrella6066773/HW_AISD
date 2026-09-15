# est：Part 6 Sprint Backlog 合并建议

**提出人**：B · Geping Chen（Estrella Chen，23084393）
**日期**：2026-09-15
**依据**：`Dluffy/2026-09-15/Dluffy：part6 Sprint Backlog.md`、`Ruby/2026-09-15/ruby：part6 Sprint Backlog.md`、`Ruby/2026-09-15/ruby：part4任务拆分.md`、`Ruby/2026-09-14/分工表.md`、`Est/part3产品待办.md`、工作簿 Part 6 表头

---

## 一、为什么要合并

仓库里现在有两份 Sprint Backlog，都叫 Sprint 1，但范围与目标不一致。老师明天看仓库时若同时打开这两份，会认为小组对本期范围没有共识。这份建议只做一件事：把两份合成一份可采纳的版本，并列出差异点由大家拍板。

---

## 二、两份现状对照

| 对照项 | Dluffy 版 | Ruby 版 |
|--------|-----------|---------|
| 文件位置 | `Dluffy/2026-09-15/Dluffy：part6 Sprint Backlog.md` | `Ruby/2026-09-15/ruby：part6 Sprint Backlog.md` |
| 声明的主笔 | Ender（C），复核 Ryan | Hao Zheng（A） |
| 本期条目 | T02 至 T11，共 10 条 | T01 至 T07 加 T20，共 8 条 |
| 是否含治疗与支付 | 含 T08 至 T11 | 明确写「支付、信件、咨询分流不进本 sprint」 |
| 本期工作性质 | 规格加第一期实现，目标含 28 Sep 可运行片段 | 只做规格与计划，写明「本 sprint 不要求当场画图或写代码」 |
| Sprint Goal 表述 | 完成案例理解与计划基线，并说明第一期将演示「转诊核验 → 决策 → 新患预约」片段 | 16 Sep 前把 Product Backlog 与 Sprint 1 Backlog 定稿并上传 GitHub，全员加入仓库 |
| 估算合计 | 约 35h | 约 23h |
| T01 的处理 | 注明已完成，不列入本期 | 列入本期，状态 Done |
| 是否含 T20 | 不含 | 含（第一次 standup 与 Review 准备） |
| 状态取值 | 全部 Not started | T01 Done、T02 与 T20 In progress |

---

## 三、差异清单

| # | 差异 | 两份的写法 | 为什么必须统一 |
|---|------|------------|----------------|
| 1 | 本期范围含不含 T08 至 T11 | Dluffy 含，Ruby 不含 | 老师问「本期几条、哪些」，两份答不一致 |
| 2 | 本期是否要做实现 | Dluffy 含实现，Ruby 明确不做 | 直接决定这周各人干什么 |
| 3 | Goal 的落点 | Dluffy 落在 28 Sep 片段，Ruby 落在 16 Sep 上传 | Goal 决定验收口径 |
| 4 | T01 是否算本期 | Dluffy 排除，Ruby 列入 | 影响本期条目数与合计工时 |
| 5 | Part 3 的主笔 | Ruby 版写「Part 3（Hao Zheng 同时主责）」 | 与 `分工表.md` 冲突：Part 3 主笔是 B（Est），A 是 Part 1、4、8 主笔 |
| 6 | T01 标 Done 的依据 | 两份都写 Done | 仓库里没有「权限说明」文件，Done 无凭证；Part 4 复核意见已就 T01 提过同样问题 |
| 7 | 人名写法 | Dluffy 用 Ender、Ruby、Estrella、Ryan；Ruby 版用中文全名 | 与 Blackboard 显示名对不上，贡献核对困难 |
| 8 | 状态取值语言 | Dluffy 全用英文，Ruby 混用中英 | 同一张表应统一 |

---

## 四、建议口径

**建议一：本期定为 T01 至 T07 加 T20，T08 至 T11 留到 Sprint 2。**
理由：明天是第一次 standup，S03 对第一次站会的考核点是进度、证据、下一动作、阻塞、二责支持与交接，而不是已经跑起来的东西；Ruby 版已经写明「16 Sep 不要求当场画图或写代码」，Part 2 也写着「16 Sep 不必出图」。把治疗与支付放进 Sprint 1，会在只有一天的窗口里挂上一批必然做不完的条目。

**建议二：把 Sprint 1、Sprint 2 的窗口写出来，Sprint 2 承担 28 Sep 的增量。**
理由：两份都只写了 Sprint 1，而 28 Sep 要交的 Camunda Forms、外部工作器与测试计划必须有归属。按「Sprint 1 到本周、Sprint 2 到 9 月 28 日」划分，28 Sep 的交付就有着落，也不会让 Sprint 1 名不副实。

**建议三：Goal 写成一句话，同时包含 16 Sep 与 28 Sep 两个落点。**
理由：两版 Goal 各说了半件事，合成后既回应明天的站会，也不丢掉第一期的目标。

**建议四：T01 先不标 Done，等权限说明落仓库再改。**
理由：Done 必须有可打开的凭证。仓库里目前没有这份文件；文件到位后，把 Part 6 与产品待办两处同时改。

**建议五：人名统一用「代号加姓名」。**
用 `A Hao Zheng`、`B Geping Chen`、`C Minghao Qin`、`D Guanyan He`，与 `分工表.md` 和 Blackboard 一致，避免第三方对不上人。

---

## 五、合并后的 Sprint Backlog

### Sprint 1 目标

> 16 Sep 第一次 standup 前完成 Product Backlog 与 Sprint 1 Backlog 并推送到仓库、全员加入仓库；随后按本表推进「转诊核验 → 医生决策 → 新患预约（外部排班可 mock）」的规格工作，为 28 Sep 的第一期增量打底。

窗口：2026-09-15 至 2026-09-20。性质：规格与计划，不出图、不写代码。

| Sprint | Task ID | Task Description | First Owner | Second Owner | Estimate | Acceptance Conditions | Evidence | Status |
|--------|---------|------------------|-------------|--------------|----------|-----------------------|----------|--------|
| 1 | T01 | 转诊核验的角色与权限边界：秘书可补件、不可接受转诊 | A Hao Zheng | B Geping Chen | 2h | 与案例第 3 至 4 段一致；角色表与正文可逐条对应 | 角色权限边界表（文件落仓库后改 Done） | In progress |
| 1 | T02 | 转诊主路径规格：收件 → 核材料 → 送医生 | A Hao Zheng | D Guanyan He | 3h | 步骤能对应案例原文每一段 | 路径说明；图放到 28 Sep | In progress |
| 1 | T03 | 医生四态规格：接受、拒绝、补材料、转专科；原因与操作人必填 | A Hao Zheng | B Geping Chen | 3h | 无原因或无操作人则不能往下走 | 决策字段与规则说明 | Not started |
| 1 | T04 | 拒绝与转专科后的路径：不进入第一次门诊预约 | D Guanyan He | A Hao Zheng | 2h | 拒绝后不生成新患预约 | 异常路径说明 | Not started |
| 1 | T05 | 仅在接受后生成第一次门诊预约请求，含专科、优先级、时间窗、患者需求 | A Hao Zheng | C Minghao Qin | 3h | 未接受时行政约不了号 | 门禁规则说明 | Not started |
| 1 | T06 | 外部排班（可 mock）：有号则确认；无号则挂起并转路径组，禁止约到时间窗外 | C Minghao Qin | D Guanyan He | 5h | 无号时状态为待处理或已升级，且不产生窗口外预约 | mock 约定加失败规则 | Not started |
| 1 | T07 | 通知规则：常规发信；两周内就诊须另加电话联系并记录每次结果 | B Geping Chen | A Hao Zheng | 3h | 14 天以内（含第 14 天）必须有电话尝试记录 | 通知规则表 | Not started |
| 1 | T20 | 第一次 standup 与 Review 准备：确认 PB 与本表已上传、全员已加入仓库 | A Hao Zheng | B Geping Chen | 2h | 仓库内有 Product Backlog 与 Sprint Backlog；四人都在协作者列表 | 仓库链接与文件路径 | In progress |

合计 23h。

### Sprint 2 目标

> 把「转诊核验 → 医生决策 → 新患预约」做成可运行的片段，并补齐治疗授权与资金支付，交出第一期增量。

窗口：2026-09-21 至 2026-09-28。

| Sprint | Task ID | Task Description | First Owner | Second Owner | Estimate | Acceptance Conditions | Evidence | Status |
|--------|---------|------------------|-------------|--------------|----------|-----------------------|----------|--------|
| 2 | T08 | 治疗授权请求：记录同意并创建已授权的治疗预约申请 | A Hao Zheng | B Geping Chen | 3h | 无临床授权则行政不能处理 | 表单校验说明 | Not started |
| 2 | T09 | 外部治疗、检验、影像不可用时：预约挂起、通知负责团队、防重复预约 | C Minghao Qin | D Guanyan He | 4h | 不产生重复预约记录 | 失败路径测试记录 | Not started |
| 2 | T10 | 确认治疗前判定资金来源；需付款则发起支付请求；不存完整卡号 | C Minghao Qin | B Geping Chen | 5h | 回写状态、流水、金额、日期；无卡号存储 | 工作器加字段清单 | Not started |
| 2 | T11 | 支付失败可重试；外部已扣款无回执则标待调查，禁止自动再扣 | C Minghao Qin | D Guanyan He | 4h | 三条路径可演示 | 测试用例结果 | Not started |
| 2 | T17 | 战略 BPMN 主图，并与运营模型对齐 | A Hao Zheng | B Geping Chen | 4h | 关键环节齐全；临床、行政、财务边界可辨；抽象层级有说明 | .bpmn 文件加说明 | Not started |
| 2 | T18 | 绑定转诊核验与医生决策的 Camunda 表单 | B Geping Chen | A Hao Zheng | 4h | 必填校验生效；变量可传递 | 表单文件加截图 | Not started |
| 2 | T19 | 主路径与拒绝转诊两条验收测试 | D Guanyan He | C Minghao Qin | 3h | 含预期与实际两列；失败项写明原因 | 测试计划与结果 | Not started |

合计 27h。

### 后续 Sprint 待排

i\* SD/SR 模型、需求追溯矩阵、完成定义、信件与咨询分流、审计等条目尚无 T 编号，待拆分后按同样格式补入。i\* 的截止日两份 Part 2 写法不一致（Dluffy 写周三，Ruby 写 28 Sep），需要定一个。

---

## 六、需要两人确认的三点

| # | 事项 | 请谁定 |
|---|------|--------|
| 1 | 本期范围定为 T01 至 T07 加 T20，T08 至 T11 移入 Sprint 2，是否同意 | A、C 两位作者 |
| 2 | T01 先标 In progress，待角色权限边界表落仓库后再改 Done | A |
| 3 | 删除一份、保留一份，或把两版都改成指向同一份合并稿 | A、C |

---

## 七、采纳后的动作

1. 以本稿替换 `Ruby/2026-09-15/ruby：part6 Sprint Backlog.md` 与 `Dluffy/2026-09-15/Dluffy：part6 Sprint Backlog.md` 中不一致的 Sprint 1 表，或在两份文件顶部各加一行指向 `docs/sprint-backlog.md`，避免两处并存。
2. 修正 Ruby 版中「Part 3 由 Hao Zheng 主责」的表述，与 `分工表.md` 一致。
3. 若本稿被采纳，把 `Est/part3产品待办.md` 说明第 4、5 条中的 Sprint 口径同步为「Sprint 1 为 T01 至 T07 加 T20，PB-01 至 PB-07 在 Sprint 1 至 2 内闭环」。

---

## 八、我没做的事

本稿只做合并与对照，未改动任何他人的文件。两份原文保持原样，等 A、C 确认后再动手。
