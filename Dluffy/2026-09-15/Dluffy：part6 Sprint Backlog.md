# Dluffy：Part 6 Sprint Backlog（Sprint 1）

**主笔**：C · Minghao Qin（Ender Qin / Dluffy，23084402）
**复核**：D · Guanyan He
**依据**：Agile Workshop Part 6；从 Part 3 Product Backlog / Part 4 任务拆分拉取
**日期**：2026-09-15

---

## Sprint 1 Goal

> 完成案例理解与计划基线，并说明第一期将演示「转诊核验 → Consultant 决策 → 新患预约（外部排班可 mock）」的可运行片段。

---

## Sprint 1 Backlog（从 Part 4 拉取：T02–T11）

| Sprint | Task ID | Task Description | First Owner | Second Owner | Estimate | Acceptance Conditions | Evidence | Status |
|--------|---------|------------------|-------------|--------------|----------|-----------------------|----------|--------|
| Sprint 1 | T02 | 起草转诊主路径：收件 → 核材料 → 送 Consultant | A Hao Zheng | D Guanyan He | 3h | 主路径步骤可对应案例原文 | BPMN 草稿 | Not started |
| Sprint 1 | T03 | 增加 Consultant 四态：接受 / 拒绝 / 补材料 / 转专科；原因与操作人必填 | A Hao Zheng | B Geping Chen | 3h | 无原因或无操作人则无法提交 | 决策表单字段说明 | Not started |
| Sprint 1 | T04 | 增加拒绝 / 转专科后的结束或转出路径 | D Guanyan He | A Hao Zheng | 2h | 拒绝后不进入新患预约 | 异常路径图 | Not started |
| Sprint 1 | T05 | 仅在接受后生成 New Patient Appointment 预约请求 | A Hao Zheng | C Minghao Qin | 3h | 未接受时行政无法约号 | 门禁说明 + 模型 | Not started |
| Sprint 1 | T06 | 对接 / 模拟外部排班：有号则确认，无号则高亮并转 pathway | C Minghao Qin | D Guanyan He | 5h | 无号时状态为 pending / escalated | worker 日志或 mock 记录 | Not started |
| Sprint 1 | T07 | 实现通知规则：常规发信；预约在两周内须另记电话联系及每次结果 | B Geping Chen | A Hao Zheng | 3h | < 14 天必须有电话尝试记录 | 通知规则表 + 表单 | Not started |
| Sprint 1 | T08 | 治疗请求：记录同意并创建已授权 Treatment Booking Request | A Hao Zheng | B Geping Chen | 3h | 无临床授权则行政不能处理 | 表单校验说明 | Not started |
| Sprint 1 | T09 | 外部治疗 / 检验 / 影像不可用时：booking pending、通知负责团队、防重复预约 | C Minghao Qin | D Guanyan He | 4h | 不产生重复预约记录 | 失败路径测试记录 | Not started |
| Sprint 1 | T10 | 确认治疗前判定资金来源；需付款则发支付请求；不存完整卡号 | C Minghao Qin | B Geping Chen | 5h | 回写状态 / 流水 / 金额 / 日期；无卡号存储 | worker + 字段清单 | Not started |
| Sprint 1 | T11 | 支付失败可重试；Provider 成功但无回执则标调查，禁止自动再扣 | C Minghao Qin | D Guanyan He | 4h | 三条路径可演示 | 测试用例结果 | Not started |

> 估算沿用 Part 4 口径（第一负责人工时）。T01 已完成（角色权限边界表），不列入本期。

---

## 容量与范围说明

1. **列入本期**：转诊核验 → Consultant 决策 → 新患预约 → 通知规则，共 10 条（合计约 35h）。
2. **后置 Sprint 2**：信件批准 / 分发与 7 天升级（T13、T14）、深度咨询分流（T15）、审计点（T16）——除非进度超预期。
3. **外部依赖**：本期排班与支付可 mock，报告中标明边界与假设。
4. **口径**：未完成项下一 sprint 再拉，不扩大 Goal，保证 Sprint Review 可演示。
