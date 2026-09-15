# Dluffy：Part 2 交付物清单（Deliverable List）

**主笔**：Ender（23084402）
**复核**：Ruby
**依据**：Agile Workshop Part 2 · Task 1；案例《Hospital Patient Referral, Treatment and Administration System》
**日期**：2026-09-15

> 口径：本清单由全组共同圈定范围、主笔汇总成稿。Due Date 按 workshop 节奏——「分析与模型」与「Agile 过程证据」两类为本周三（计划增量）定稿；「实现与验证」类排到 28 Sep 的 Sprint。

---

## 一、分析与模型

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| 案例理解与问题总结 | 案例 8 问（背景 / 利益相关者 / 主流程 / 问题 / 规则 / 异常 / 外部系统 / 信息） | Part 1（Ruby、Ender） | 周三 | 8 问逐项有答案；推断项标注为假设 |
| 战略 BPMN | 主业务流程 | 全组对齐 | 周三 | 高层转诊路径完整、关键门禁（授权 / 支付 / 批准）可见 |
| 运营 / 可执行 BPMN | 主路径可跑 | 战略 BPMN | 28 Sep（Sprint 1 片段） | 转诊核验 → Consultant 决策片段可演示 |
| i*（SD / SR） | 利益相关者与依赖 | Part 1 | 周三 | 含外部组织依赖（排班、检验影像、支付） |
| 需求追溯矩阵 | 需求 ↔ 模型 ↔ 实现 ↔ 测试 | Part 3 / Part 4（Estrella、Ryan） | 28 Sep | 每行可回溯到 Backlog ID |
| 验收标准 | 按工作包 | Part 4（Ruby） | 周三 | 每条可测、有对应证据 |

## 二、Agile 过程证据

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| Product Backlog | Part 3 | Estrella 主笔 | 周三 | 12 字段齐全（ID / 名称 / 描述 / 优先级 / 关联需求 / 估算 / 一责 / 二责 / 依赖 / 验收 / 证据 / 状态） |
| Definition of Done | 全组约定 | Ender 提议 | 周三 | 含证据最低要求（Backlog ID + 文件/commit + 截图） |
| Sprint Backlog + Goal | Part 6 | Ender 主笔 | 周三 | Sprint 1 目标 + 条目带双负责人与验收 |
| Standup 记录与汇总 | Part 7 | 每人自写、Ryan 汇总 | 周三起每人 ≥ 1 次 | 含完成 / 证据 / 下一步 / 阻塞 / 支持 / 交接 |
| Sprint Review | Part 8 | Ruby 主笔 | 周三 | 展示分工、完成 / 未完成、证据、反馈 |
| 反馈与 Backlog 变更 | Part 8 | Ryan 维护 | 持续 | 变更可追溯 |

## 三、实现与验证

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| Camunda Forms | Part 4 · T18 | 转诊核验 / Consultant 决策 | 28 Sep | 必填校验生效，表单可打开 |
| External Workers | Part 4 · T06 / T09 / T10 / T11 | 外部排班与支付（可 mock） | 28 Sep | 无号挂起、支付失败可重试、无回执不自动再扣 |
| 测试计划 / 结果 | Part 4 · T19 | 主路径 + 拒绝路径 | 28 Sep | 有预期结果与实际结果栏 |
| 端到端演示说明 | 全组 | 当前增量 | 周三（计划）/ 28 Sep（实现） | 主路径可演示、证据对应 commit |

## 四、仓库与版本

| Deliverable | Related Requirement(s) | Dependencies | Due Date | Acceptance Criteria |
|-------------|------------------------|--------------|----------|---------------------|
| 仓库目录与分支约定 | 协作规则 | — | 持续 | `main` 保持可演示；功能分支 `feature/简短说明` |
| 个人工作区与分工文 | 协作规则 | 按日期建文件夹 | 持续 | 各成员在各自文件夹（Ruby / Est / Dluffy / Ryan）上传 |
| 关键里程碑记录 | 协作规则 | — | 里程碑时 | README 版本说明或 git tag |

---

## 本期判定

- **周三硬交付（计划增量）**：分析与模型类 + Agile 过程证据类。
- **28 Sep 交付（实现增量）**：实现与验证类。
- 仓库与版本类为全程持续项。
