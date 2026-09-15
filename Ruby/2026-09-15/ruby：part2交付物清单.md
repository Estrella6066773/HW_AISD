# ruby：Part 2 交付物清单

题目要求每条写清：交付物、关联需求、依赖、截止日期、验收条件。

**16 Sep 2026 演示的是 Agile Workshop 计划（Part 1–8 文档），不画 BPMN/i*，不写代码。**  
图和实现放到 28 Sep 及之后。

---

## 16 Sep 要交（计划，无图无代码）

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| 案例理解与问题总结 | 背景、参与者、主流程、问题、规则、异常、外部系统、信息 | 全组讨论；Hao Zheng 汇总，Geping Chen 复核 | 16 Sep 2026 | 8 问有答案；假设单独标明；用文档即可 |
| 交付物清单（本文） | 明确以后交什么、何时交 | 案例摘要 | 16 Sep 2026 | 五列齐全；16 Sep 与 28 Sep 分开 |
| Product Backlog | 覆盖以后的建模、实现、测试、评审、证据 | Geping Chen 主笔，Guanyan He 复核 | 16 Sep 2026 | 12 字段齐全（含双负责人）；条目是计划，不是已完成代码 |
| 任务拆分 | 小到一个 sprint 能做完 | Minghao Qin 主笔，Guanyan He 复核 | 16 Sep 2026 | 无「做系统/做 BPMN」这种空任务；有验收与证据栏 |
| 依赖映射 | 先后顺序、延误知会、备份 | Guanyan He 主笔，Geping Chen 复核 | 16 Sep 2026 | 每项能回答前置/后继/通知谁/备份 |
| Sprint Backlog + Goal | 第一个 sprint 准备做什么 | Hao Zheng 主笔，Minghao Qin 复核 | 16 Sep 2026 | 有 Goal；条目来自 Product Backlog；讲计划不演示软件 |
| Standup 准备与记录 | 个人进度 | 每人自写；Guanyan He 汇总，Hao Zheng 复核格式 | 16 Sep 2026 | 完成/下一步/阻塞/证据；证据可以是文档与讨论记录 |
| Sprint Review 准备 | 演示本周的计划增量 | Hao Zheng 主笔，Geping Chen 复核 | 16 Sep 2026 | 能讲已完成文档、未做的图/代码、决策、下一步 |
| Definition of Done | 全组约定何为完成 | 全组确认 | 16 Sep 2026 | 16 Sep：文档有负责人+可检查；实现阶段再加 commit/截图 |
| 分工与贡献记录口径 | 谁主笔谁复核 | 分工表 | 16 Sep 2026 | 四人姓名、主笔/复核清楚 |

## 以后要交（28 Sep 起：图和代码）

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| 战略 BPMN | 主路径；临床/行政/财务分权 | 案例摘要、Backlog | 28 Sep 2026 | 高层路径与门禁可见（16 Sep 不必出图） |
| 可执行运营 BPMN | 未授权不能约号/约治疗；外部失败可挂起 | 战略 BPMN | 28 Sep 2026 | 转诊核验 → 医生决策 → 新患预约可跑 |
| i*（SD / SR） | 利益相关者依赖与冲突 | 案例摘要 | 28 Sep 2026 | 含排班、发信、支付等外部依赖 |
| 需求追溯矩阵 | 需求 ↔ 模型 ↔ 实现 ↔ 测试 | Backlog、模型 | 28 Sep 2026 | 每行回到 Backlog ID |
| Camunda Forms | 转诊核验、医生决策必填 | 运营 BPMN | 28 Sep 2026 | 表单可打开；必填校验生效 |
| External Workers | 排班/支付；无号挂起；无回执不自动再扣 | 运营 BPMN；可 mock | 28 Sep 2026 | 失败路径可证；不存完整卡号 |
| 测试计划与结果 | 权限、主路径、拒绝转诊 | BPMN、Forms、Workers | 28 Sep 2026 | 有预期与实际结果 |
| 端到端演示 | 转诊至新患预约切片 | 上述实现 | 28 Sep 2026 | 现场或录屏可复现 |
| 项目仓库里程碑 | 版本可查 | 持续提交 | 持续 / 里程碑 | 目录清楚；关键提交可定位 |

---

## 16 Sep 现场讲什么

讲清：案例怎么理解、要交哪些东西、Backlog 和任务怎么拆、本 sprint 准备做什么、每人 standup、Review 时计划增量是什么。  
不讲已画好的流程图，不演示 Camunda 或代码。
