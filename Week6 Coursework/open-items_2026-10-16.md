# 待办与决定清单

**日期**：2026-10-16
**用途**：这份文档不是提交件。它记录「已经改了什么」「已经定了什么」，以及「还剩什么没动」。

> 想知道「我们到底要解决什么问题」，看 `problems_2026-10-16.md`。那份是从问题出发的完整清单，含复核命令；这份是从动作出发的记录。

---

## 三、已经定下的决定


| 决定          | 内容                                                                                                                                | 落点                |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **A1** 会议口径 | 按**个人 standup** 准备：每人讲自己那部分，各自带证据、下一步、阻塞                                                                                          | `process/part7-standup-records.md`（过程记录，不是待办条目）           |
| **B** 死链与错值 | 已全量改指；`evidence/` 三份捕获与 `Ryan` 的 PB-14 执行记录有意留旧路径，因为记的是当时实际工作目录，改掉等于篡改证据                                                          | 仓库一致性（已完成，不是待办条目）           |
| **B3** 课号   | `W03/README.md` 第 3 行的 `UFCFAF-30-3` **仍未改**。这批 10 月课件讲的是战略 BPMN、流程编排、SOAP/REST、i、HCI，从内容看属于 BPM&EA，但仓库里没有 BPM&EA 的规范可以对照，所以我不替你猜 | 待你确认              |
| **C** 重复件   | 已收敛 12 份，见上表                                                                                                                      | 仓库一致性（已完成，不是待办条目）           |
| **D** 计划编号  | Sprint 3/4 计划已**按 PB 条目重排**，不再用 `S3-xx` / `S4-xx`；产品行对应 `PB` 条目，过程行不带 `PB` 号（产品待办只记产品工作）；第二次发布的产品条目为 `PB-30`、`PB-31`、`PB-34`、`PB-39`                                      | 产品条目 `PB-30`、`PB-31`、`PB-34`、`PB-39` |
| **A2** 待办口径 | 产品待办只记产品工作（见 `docs/p3-product-backlog.md` 头部与 Note 9）。过程与举证类条目——`PB-15`、`PB-17`、`PB-29`，以及第二次发布草稿里的 `PB-32`、`PB-33`、`PB-35`、`PB-36`、`PB-37`、`PB-38`——已撤出待办 | 冲刺计划 B 部分 + `process/` |


---

## 四、剩下的没动（你说先不管）

### E 类 · 10 月 20 日之前必须补齐的交付物

> 第二版被判分的三块是 Further development 25%、Response to feedback 20%、Project plan evaluation 25%，另有 SU3/SU4 各 5%、SR3/SR4 各 10%。其中只有 Further development 落在产品待办条目上（`PB-30`、`PB-34`）；其余是过程记录，见计划的 B 部分。

- **E1** 补第二版演示幻灯片（`submissions/BPMEA/` 里那份是第一版的）→ 计划 B 部分（不是待办条目）
- **E2** 把「计划 vs 实际」评估从底稿填成正式稿 → 计划 B 部分（不是待办条目）
- **E3** 填写贡献记录表 `Est/est：PB-17贡献记录表.md`（目前是空模板）→ 计划 B 部分（不是待办条目）
- **E4** 补写 SU3、SU4 的个人 standup 记录（每位成员一份）→ `process/part7-standup-records.md`
- **E5** 补写 SR3、SR4 的评审记录 → `process/part8-sprint-review-records.md`
- **E6** 落实第二版能不能真跑起来：这份副本里的 `Coursework/hospital-pathway/` 没有源码，`src/`、`bpmn/`、`forms/`、`scripts/`、`evidence/` 五个目录都在但内容为 0 个文件，只剩 `target/` 与 `data/`。**这份副本当前既不能出图也不能跑流程**（完整包在 `Week3 Coursework/hospital-pathway/`）→ `PB-31`

### F 类 · 模型与证据

- **F1** 给 `Hospital_All_Processes_V3.bpmn` 补一份可读的 PDF 导出（目前只有 9 月 29 日旧模型那份 9 页 PDF）。V2 已在 `357528e` 被 V3 取代，导出对象随之为 V3 → `PB-30`
- **F2** 重跑 `pb14_acceptance.py` / `pb18_acceptance.py` 并归档新记录 → `PB-31`

> **2026-10-19 夜补记（事实已变，原文保留）**：`PB-31` 的复跑已经做了。V3 部署到本地 Camunda 8.10.0-alpha5（`c8run.exe start --disable-connectors`）后，六个验收用例加 G07 在同一次连续会话里对 V3 重跑：`AT-01`、`AT-02`、`AT-04`、`AT-05`、`AT-06` 通过，G07 走到 `COMPLETED`（9 个人工任务、无活动事件），**`AT-03` 仍失败**（模型没有 candidate group，秘书仍能完成 Consultant Accept）。记录在 `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`，结论写入 `submissions/BPMEA/BPMEA_Written_Evaluation.pdf` 第 4 节与 `docs/requirements-traceability-matrix.md` 第 4.9 节。`F2` 因此关闭；`E6` 里「副本跑不起来」仍成立（那份副本本身没有源码），只是完整包已经跑通。
- **F3** 已查明并处置：四份 i\* 模型文件（`istar/V1_SD_diagram.txt` 与三份 `*_SR_reviewed_2026-10-13.txt`）是**合法 UTF-8（无 BOM）、JSON 校验通过**，磁盘上没有乱码；花屏是查看器按 GBK 解码所致。处置见 `Week6 Coursework/README.md` 的「Encoding of the i\* model files」一节。是否把中文批注统一改成英文，另列为待定。

### G 类 · 无法在仓库内核实

- **G1** 今天 15:55 那节课的课次安排（仓库无课表）
- **G2** BPM&EA（UFCEP4-0-3）的评分规范与交付要求（`W01/` 里只有 AISD 的 UFCEP6-0-3 两份）
- **G3** 规范写的 22 October 与通知写的 10 月 20 日之间是否需要再确认

---

## 五、拉取（已完成）

**已拉取并合并，无需再拉。** `40297f2`（及合并提交 `2f9264b`）已并入本地 `main`，与 `origin/main` 同步（`behind/ahead = 0 0`）。这两个提交改的是：

- `Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`
- `Week6 Coursework/istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`
- `Ruby/2026-10-15/Hospital_All_Processes_V2_中文.bpmn`

随拉取进来的 `Ruby/2026-10-15/~$SR-中文图解.docx` 是 Word 打开文档时生成的锁定文件，已从版本管理移除并从磁盘删除，`~$*` 已写进 `.gitignore`（2026-10-16）。