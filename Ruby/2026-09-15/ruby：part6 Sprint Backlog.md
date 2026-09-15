# ruby：Part 6 Sprint Backlog（Sprint 1）

主笔：Hao Zheng。从 Product Backlog / 任务拆分中拉入 Sprint 1。  
16 Sep 第一次 Standup 交这份表并上传仓库；本 sprint **不要求**当场画图或写代码。

---

## Sprint 1 Goal

16 Sep 前：Product Backlog 与 Sprint 1 Backlog 定稿并上传 GitHub，全员已加入仓库。  

16 Sep 之后到 28 Sep：按本表推进「转诊核验 → 医生决策 → 新患预约（排班可 mock）」的规格与第一期实现。支付、信件、咨询分流不进本 sprint。

---

## Sprint 1 Backlog

| Sprint | Task ID | Task Description | First Owner | Second Owner | Estimate | Acceptance Conditions | Evidence | Status |
|--------|---------|------------------|-------------|--------------|----------|-----------------------|----------|--------|
| Sprint 1 | T01 | 列出转诊核验角色与权限（秘书可补件、不可接受转诊） | Hao Zheng | Geping Chen | 2h | 与案例第 3–4 段一致 | 权限说明（文档） | Done |
| Sprint 1 | T02 | 写清转诊主路径：收件 → 核材料 → 送医生 | Hao Zheng | Guanyan He | 3h | 步骤能对上案例原文 | 路径说明（文档；图留 28 Sep） | In progress |
| Sprint 1 | T03 | 写清医生四态：接受 / 拒绝 / 补材料 / 转专科；原因与操作人必填 | Hao Zheng | Geping Chen | 3h | 无原因或无操作人则不能往下走 | 决策字段与规则 | Not started |
| Sprint 1 | T04 | 写清拒绝 / 转专科后不再约第一次门诊 | Guanyan He | Hao Zheng | 2h | 拒绝后不进入新患预约 | 异常路径说明 | Not started |
| Sprint 1 | T05 | 仅在接受后才能生成第一次门诊预约请求（专科、优先级、时间窗、患者需求） | Hao Zheng | Minghao Qin | 3h | 未接受时行政不能约号 | 门禁规则 | Not started |
| Sprint 1 | T06 | 约定外部排班（可 mock）：有号则确认；没号则挂起并转路径组，禁止约到时间窗外 | Minghao Qin | Guanyan He | 5h | 无号为 pending/escalated | mock 约定 + 失败规则 | Not started |
| Sprint 1 | T07 | 通知规则：一般发信；两周内还要打电话并记下每次结果 | Geping Chen | Hao Zheng | 3h | ＜14 天必须有电话尝试记录 | 通知规则表 | Not started |
| Sprint 1 | T20 | 第一次 Standup / Review：Backlog 与本表已上传；说明未做图和代码 | Hao Zheng | Geping Chen | 2h | 仓库有 PB + Sprint Backlog；四人都在仓库里 | GitHub 链接与文件 | In progress |

合计约 23h。T08–T16、T17–T19（治疗授权、支付、信件、咨询、BPMN 文件、表单、测试执行）**不进入 Sprint 1**，留在 Product Backlog，供 Sprint 2。

---

## 16 Sep Standup 怎么对黑板

| 黑板 | 本文件对应 |
|------|------------|
| Complete Product Backlog | Part 3（Hao Zheng 同时主责，与本表 PB/T 编号对齐） |
| Sprint 1 Sprint Backlog | 本表 |
| GitHub 全员加入，并上传 PB / Sprint Backlog | 把 Part 3、Part 6 push 到仓库 |

---

## 范围说明

1. 本 sprint 只切「转诊 → 决策 → 第一次门诊预约 + 通知」这一段。  
2. 外部排班用 mock，验收里写明。  
3. 16 Sep 验收的是计划是否完整、是否上传；28 Sep 再验收图和可跑片段。  
4. Goal 不扩大。做不完的下一 sprint 再拉。
