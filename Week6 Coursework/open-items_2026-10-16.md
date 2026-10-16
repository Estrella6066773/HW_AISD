# 待办与决定清单

**日期**：2026-10-16
**用途**：这份文档不是提交件。它记录「已经改了什么」「已经定了什么」，以及「还剩什么没动」。

> 想知道「我们到底要解决什么问题」，看 `problems_2026-10-16.md`。那份是从问题出发的完整清单，含复核命令；这份是从动作出发的记录。

---

## 一、本轮已落地

### 1. 截止日期

仓库内由我们自己撰写的文档，第二版截止一律写 **2026-10-20 23:59**。

### 2. 新增的文件

| 文件 | 内容 |
| --- | --- |
| `Week6 Coursework/README.md` | 目录索引：每份产物在哪里、哪一份是唯一权威副本 |
| `Week6 Coursework/problems_2026-10-16.md` | 十项待解决问题，逐条写明依据与复核命令 |
| `Week6 Coursework/feedback/feedback-response_2026-10-16.md` | 反馈处置记录：反馈条目、决定、一二责、证据 |
| `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` | 操作图、战略图、SD 与三份 SR 的 V1 到 V2 改动对照 |
| `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md` | Sprint 3 与 Sprint 4 计划，按要求已按 PB 条目重排 |

### 3. 修正的既有文档

重点修的是一个**硬错误**：`03180bb`（2026-10-16）把整个 `Coursework/` 目录改名成了 `Week3 Coursework/`，但引用没跟着改。

| 文件 | 改了什么 |
| --- | --- |
| 全仓库 34 个文件 | 指向 `Coursework/hospital-pathway/` 的引用全部改指 `Week3 Coursework/hospital-pathway/` |
| `README.md`、三份 `submissions/` | 目录表补两行；截止日期改 2026-10-20；删掉已失效的 `Current main is 91a02c9` 与「没有最终发行标签」；证据指针由 `fc6293e` 改为标签 `submission-2026-09-29`（`f6fec99`） |
| `docs/p3-product-backlog.md` | 第二次发布十条登记为 `PB-30` … `PB-39`；Note 1 写明本文件是唯一权威编号 |
| `Est/est：part3产品待办.md` | 头部加 12 行编号对照表，标为存档草稿；正文未动 |
| `docs/p6-sprint-backlog.md` | Agile Workshop 两个路径改为 `W01/Agile Workshop.docx` 与 `Week3 Coursework/Agile Workshop-EN.docx` |

### 4. 删除的重复件（12 份）

| 删除 | 保留 |
| --- | --- |
| 根目录四份 `PB-16_V1_*`（三份 SR + 一份 SD） | `Week6 Coursework/istar/` 下的同名文件（字节相同） |
| `Week6 Coursework/acceptance/` 五份（PDF、两份计划、两份 run log） | `Ryan/2026-09-26/` 的计划与记录、`submissions/AISD/` 的 PDF（内容相同） |
| `Week6 Coursework/requirements/` 一份 | `docs/requirements-traceability-matrix.md`（字节相同） |
| `Week6 Coursework/strategic-bpmn/` 两份 | `docs/strategic-bpmn/`（内容相同） |

`Week6 Coursework/` 从此只放第二次发布新增或改动的东西，其余一律改为链接。删掉的内容在 git 历史里都还原得回来。

---

## 二、我上一版判错的两处，已经更正

1. **「三张 SD 图内容相同」不成立。** 核对哈希后三张互不相同，是三个版本：`Week6 Coursework/istar/V1_SD_diagram.png`（10 月 16 日，最新）、`Ryan/2026-10-15/PB-16_V1_SD_reviewed_2026-10-13.png`（10 月 15 日）、`docs/istar/PB-16_sd-overview.png`（10 月 13 日，第一版提交引用的那张）。**因此三张都没删**，删了会破坏第一版提交对图的引用。要收敛得先确认哪一版是现行 SD 图。

2. **「通知里的明天与课次对不上」不成立。** 你的更正是对的：通知发于 **2026-10-15（周四）**，所以通知里的「明天」就是**今天 2026-10-16（周五）**，那节课的 Standup 是**今天 15:55**。通知内部自洽，10 月 20 日也确实是周二。仓库里的规范原件印的是 22 October，与通知的 20 日不一致，这一条仍然存在。

另外还有一处漏查要说明：第一次扫描死链只查出 6 处，是因为 `git ls-files` 默认把中文路径转义成八进制，`Select-String -Path` 于是报「路径不存在」，**含中文名的文件全部被跳过**。改用原生枚举重扫后实际命中 **34 个文件**，包括 Est 与 Ruby 工作目录下一批中文名文档。

---

## 三、已经定下的决定

| 决定 | 内容 | 落点 |
| --- | --- | --- |
| **A1** 会议口径 | 按**个人 standup** 准备：每人讲自己那部分，各自带证据、下一步、阻塞 | `PB-37` |
| **B** 死链与错值 | 已全量改指；`evidence/` 三份捕获与 `Ryan` 的 PB-14 执行记录有意留旧路径，因为记的是当时实际工作目录，改掉等于篡改证据 | `PB-38` |
| **B3** 课号 | `W03/README.md` 第 3 行的 `UFCFAF-30-3` **仍未改**。这批 10 月课件讲的是战略 BPMN、流程编排、SOAP/REST、i\*、HCI，从内容看属于 BPM&EA，但仓库里没有 BPM&EA 的规范可以对照，所以我不替你猜 | 待你确认 |
| **C** 重复件 | 已收敛 12 份，见上表 | `PB-38` |
| **D** 计划编号 | Sprint 3/4 计划已**按 PB 条目重排**，不再用 `S3-xx` / `S4-xx`；一条计划行对应一个 `PB` 条目，第二次发布为 `PB-30` … `PB-39` | `PB-30` … `PB-39` |

---

## 四、剩下的没动（你说先不管）

### E 类 · 10 月 20 日之前必须补齐的交付物

> 第二版被判分的三块是 Further development 25%、Response to feedback 20%、Project plan evaluation 25%，另有 SU3/SU4 各 5%、SR3/SR4 各 10%。对应 `PB-30` … `PB-36`、`PB-37`。

- **E1** 补第二版演示幻灯片（`submissions/BPMEA/` 里那份是第一版的）→ `PB-36`
- **E2** 把「计划 vs 实际」评估从底稿填成正式稿 → `PB-35`
- **E3** 填写贡献记录表 `Est/est：PB-17贡献记录表.md`（目前是空模板）→ `PB-17`
- **E4** 补写 SU3、SU4 的个人 standup 记录（每位成员一份）→ `PB-37`
- **E5** 补写 SR3、SR4 的评审记录 → `PB-37`
- **E6** 落实第二版能不能真跑起来：这份副本里的 `Coursework/hospital-pathway/` 没有源码，`src/`、`bpmn/`、`forms/`、`scripts/`、`evidence/` 五个目录都在但内容为 0 个文件，只剩 `target/` 与 `data/`。**这份副本当前既不能出图也不能跑流程**（完整包在 `Week3 Coursework/hospital-pathway/`）→ `PB-32`

### F 类 · 模型与证据

- **F1** 给 `Hospital_All_Processes_V2.bpmn` 补一份可读的 PDF 导出（目前只有 9 月 29 日旧模型那份 9 页 PDF）→ `PB-30`
- **F2** 重跑 `pb14_acceptance.py` / `pb18_acceptance.py` 并归档新记录 → `PB-31`
- **F3** 四份 SR/SD 文件里 `V1 status` 的中文串是乱码；需要时补中文对照说明，或统一改成 ASCII

### G 类 · 无法在仓库内核实

- **G1** 今天 15:55 那节课的课次安排（仓库无课表）
- **G2** BPM&EA（UFCEP4-0-3）的评分规范与交付要求（`W01/` 里只有 AISD 的 UFCEP6-0-3 两份）
- **G3** 规范写的 22 October 与通知写的 10 月 20 日之间是否需要再确认

---

## 五、动手之前必须先做的一件事

**先 `git pull`。** 本地 `main` = `de555fd`，`origin/main` = `40297f2`，落后 2 个提交，而这两个提交改的正是：

- `Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`
- `Week6 Coursework/istar/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`
- `Ruby/2026-10-15/Hospital_All_Processes_V2_中文.bpmn`

拉取后还会带进来一个 `Ruby/2026-10-15/~$SR-中文图解.docx`，`~$` 开头是 Word 打开文档时生成的锁定文件，不该进仓库，需要单独清掉。
