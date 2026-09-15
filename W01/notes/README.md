# 课程讲义笔记 · BPM&EA / AISD

> 来源：`W01/` 下的 6 份 PPTX 讲义，转为 Markdown 并做中英对照翻译。
> 翻译由 AI 生成，仅供阅读辅助；**以英文原文为准**（考试/作业术语请沿用讲义英文表述）。

---

## 目录

| 笔记 | 原文件 | 页数 | 主题 |
| --- | --- | --- | --- |
| [S01 · 课程导论](S01%20-%20Introduction%20to%20BPM%20and%20EA%20and%20AISD.md) | S01 - Introduction to BPM & EA AND AISD.pptx | 12 | 教学团队、两个单元的编号/学习成果、推荐阅读、考核构成 |
| [S02 · 分组与环境搭建](S02%20-%20Group%20Allocation%20and%20Environment%20Setup.md) | S02 - Group Allocation and Environment Setup (c8).pptx | 15 | 分组规则、Camunda 8 本地安装与部署流程 |
| [S03 · 考核说明与备考](S03%20-%20Assessment%20Introduction.md) | S03 - Assessment Introduction(1).pptx | 28 | 两个单元的作业任务（Task 01–04）、评分方式、贡献度计算 |
| [S04–S06 · 敏捷开发实践](S04-S06%20-%20Agile%20Software%20Development%20in%20Practice.md) | S04 - S06 Agile Software Development in Practice.pptx | 26 | Agile/Scrum 原理、Backlog、DoD、站会与冲刺评审 |
| [S07 · 版本控制（上）](S07%20-%20Version%20Control%20(1of2).md) | S07 - Version Control.pptx | 9 | 版本控制概念与用途、集中式 vs 分布式 VCS、核心功能 |
| [S08 · 版本控制（下）](S08%20-%20Version%20Control%20(2of2).md) | S08 - Version Control.pptx | 20 | 修订/分支/合并/冲突、分支合并场景、Git 常用命令 |

---

## 两门单元速查

| | BPM&EA | AISD |
| --- | --- | --- |
| 单元编号 | IN3344 | IN3345 |
| 学习成果数 | 3 | 6 |
| 时长 | 6 周 | 6 周 |
| 考核 | 课程作业 50% + 汇报演示 50%（均为小组） | 同左 |

**小组**：5 人，两个单元全程同一组，确定后不可更换；个人成绩按贡献系数调整。
**分组提交截止**：2026 年 9 月 15 日 12:00（见 S03）。

---

## 贯穿全程的几条硬性要求

这些在 S03、S04 中反复出现，基本决定了作业能否拿分：

1. **第一负责人 + 第二负责人**——每项任务都必须有两个负责人，standup 上会被问到交接情况。
2. **一切都要有证据**——任务板、仓库、模型、测试记录；口头说"做完了"不算。
3. **完成定义（Definition of Done）**——未评审、未集成的工作不算完成。
4. **反馈要进 Backlog**——收到反馈却不记录，是讲义明确列出的扣分项。
5. **Review 看产品，Retro 看过程**——冲刺评审展示能跑的增量，不是放 PPT。
6. **演示要展示能跑的 BPMN**——模型必须部署到 Camunda 引擎并实际执行。

---

## 关键术语对照

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| BPMN | 业务流程建模标注 | 画业务流程的标准记号 |
| Enterprise Architecture (EA) | 企业架构 | 业务与 IT 的整体对齐 |
| i\* / SD / SR | i\* 框架 / 战略依赖模型 / 战略理由模型 | 社会技术建模，面向目标 |
| Repository | 仓库 | 版本控制中存放代码的地方 |
| Working copy / Index / HEAD | 工作副本 / 暂存区 / 当前提交指针 | Git 的三个"树" |
| Commit / Diff | 提交 / 差异 | 一次提交 = 一组文件 + 差异 + 元数据 |
| Branch / Merge / Conflict | 分支 / 合并 / 冲突 | 冲突必须手工解决 |
| Product backlog | 产品待办列表 | 全部工作的优先级清单 |
| Sprint backlog | 冲刺待办列表 | 本次冲刺选中的工作 |
| Increment | 增量 | 冲刺结束时产出的可用成果 |
| Definition of Done | 完成定义 | 判定"完成"的门槛 |
| Standup | 站会 | 短会，讲进度/下一步/阻碍 |
| Sprint Review | 冲刺评审 | 检视产品增量 |
| Sprint Retrospective | 冲刺回顾 | 检视团队工作方式 |
| External Worker | 外部工作器 | Camunda 8 中由外部程序执行的任务 |
| Contribution factor | 贡献系数 | 个人贡献 ÷ 平均贡献，用于调整小组分 |

---

## 原始文件与工具

- 原始 PPTX：`../W01/`
- 提取的纯文本（未翻译，供全文检索）：`../_extract/`
- 提取脚本：`../_tools/pptx_extract.py`（纯标准库，可重复运行）

重新生成提取文本：

```powershell
python "_tools\pptx_extract.py" "W01" "_extract"
```

> 提示：若 PPT 正被 PowerPoint 打开，脚本会因文件占用而失败（Windows 上 `Copy-Item` 可绕开）。先关闭 PowerPoint 再运行即可。
