# Est 个人待办

**归属**：Estrella（Geping Chen　陈格平，UWE ID 23084393）**个人**
**起表**：2026-10-16
**最近同步**：2026-10-20（`A-4` 已出——`submissions/AISD/AISD_Planning_Evidence.pdf` 8 页与同名 `.docx`：两版计划、任务与站会记录、SR1–SR4、两版风险记录与经验教训；SR2 无记录、SU3 无记录、SR3 按 16 笔提交反推，文内按缺口写明。此前：`A-1` 经一责 Ruby 复核定稿；`PB-12` 二责复核由本人签署；`A-2` 已落地——`submission-2026-09-29`（`f6fec99`）与 `submission-2026-10-20` 两个标签都在远端可认（修订版的 SHA 从标签上读），`Submission_Index` 的 `.docx` 与两页 PDF 已出，根 README 已有 `Releases` 一节；`A-3` 已出 PDF 11 页与同目录 `.docx`；并记入 V3 实跑结果、`B-3`／`B-4`、`B-6` 与验收证据各条；第四节结构不改）
**第二版截止**：2026-10-20 23:59（AISD 与 BPM&EA 两个模块，日期口径仍挂 `Est-13`）
**状态取值**：未开始 / 进行中 / 已完 / 待他人 / 待确认

---

## 这份表是什么

- 这份表是**本人的动作清单**，只对本人有效。编号 `Est-NN` 属于个人，全组不引用，也不占产品待办的位。
- **产品待办**（`../docs/p3-product-backlog.md`）只记产品工作。个人准备、汇报口径、过程记录一律不进产品待办，只进本表。
- 本人承担的产品条目仍用 `PB-xx` 指认。本表只写「我要做什么」，不改任何 `PB` 口径；两边的对应关系是：本表某一行的 `PB-xx` 指向权威表，权威表里该条目的负责人指向本人。
- 第四节是**提交清单**，以「交得出去的东西」为单位排列，不以工作项为单位。编号 `A-`（AISD）、`B-`（BPM&EA）、`C-`（两门都要、不占上传槽）供全文互引；`Est-NN` 仍是个人动作号。
- 本表放在个人工作区 `Est/`，不是提交件，也不进任何交付物清单。

---

## 一、10 月 20 日之前要交出去的


| ID     | 我要做什么                                                                                   | 对应              | 期限     | 证据落在哪                                                          | 状态  |
| ------ | --------------------------------------------------------------------------------------- | --------------- | ------ | -------------------------------------------------------------- | --- |
| Est-01 | 追溯矩阵按第二版刷新：26 条部分支持、4 条未支持的规则里，哪些在第二版动了、哪些没动；动了的要有证据，没动的要写清原因                           | `PB-39`         | 10-20  | `../docs/requirements-traceability-matrix.md` 第 4 节            | 已完成 |
| Est-02 | 收口两处未签的二责复核：`PB-12` 战略模型由本人签（2026-10-19 已签，签字见抽象说明第 7 节）；`PB-16` i SD/SR 由 Ryan 签（2026-10-20 已落签）。**两份已交**：`est：PB-12二责复核意见_2026-10-19.md`（A–D 已改入原文、一责已确认）、`est：PB-16二责复核备料_2026-10-19.md`（Ryan 按其中第三路线签署：缺口记在案，不勾第二项） | `PB-12`、`PB-16` | 10-20  | `../docs/strategic-bpmn/`；`../docs/istar/PB-16_istar-sd-sr.md` | 已完成（`PB-12` 2026-10-19 已签；`PB-16` 由 Ryan 于 2026-10-20 复核并落签，见模型注释第 11、12 节） |
| Est-03 | 反馈处置记录逐条落行：实际收到的反馈才写，未收到的留空，不凭推测补。**记录已出 PDF**（11 页）；六项逐条标明，`F-08` 已按 10 月 19 日归档的第 10 组四条转写拆为 `F-08a`／`F-08b`（原件仍未入库），`F-11` 记未实施并写明遗留风险 | `A-3`         | 10-20  | `../submissions/AISD/AISD_Feedback_Response_Record.pdf`；源文件 `../Week6 Coursework/feedback/feedback-response_2026-10-16.md` | 已完成 |
| Est-04 | 填贡献记录表：视图 A 按证据逐行登记、视图 B 按条目对账；每条证据要能打开并与条目负责人一致                                        | `C-3`         | 10-20  | `est：PB-17贡献记录表.md`（本目录）                                        | 已完成（视图 A 53 行，`E-001` 至 `E-053`；视图 B 已出，2026-10-20 更新） |
| Est-05 | 完成定义签字：一责 Ender，本人是二责，需要本人那一笔                                                           | `C-4`         | 10-20  | `../docs/definition-of-done.md`                                | 已完成（四人 2026-10-20 签署；31 项中 28 项勾选，3 项未勾并写明理由） |
| Est-06 | 自己那两行 Part 7 standup 记录：SU4（10-16 那场，已写）与 SU3（10-12 那场，已按实写「Not recorded」），按「完成 / 证据 / 下一步 / 阻塞 / 需要的支持 / 要交接的」六栏写自己的部分 | `C-1`         | 截止前 | `../Week6 Coursework/process/part7-standup-records.md`             | 已完成（SU4 有据可查，SU3 如实记未记录） |
| Est-20 | 签 `PB-12` 二责复核前，先核第 4 节的映射是否仍指旧模型。**已核完并已改入原文**：第 4 节两处、第 6 节一处过时，第 8 行衔接模型仍指 `Simple_C8`；意见见 `est：PB-12二责复核意见_2026-10-19.md`，四处已于 10-19 改入 `PB-12_abstraction-level_2026-09-29.md`，`BPMEA_Abstraction_Note.pdf` 随之重出（6 页） | `B-1`         | 10-20  | `est：PB-12二责复核意见_2026-10-19.md`；原件 `../docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` 第 4、6、7 节 | 已完成（一责 2026-10-19 确认改稿，二责已签） |
| Est-21 | 把需求对齐评估写成书面件：以 `../docs/requirements-traceability-matrix.md` 第 3、4 节为底稿，产出 `B-3`／`B-4` 那份书面评估的第一部分，最终形态必须是 `.docx` 或 PDF，Markdown 不算。**已按 V3 模型重写并定稿 Markdown；10 月 19 日模型在真机上跑通后，第二部分（验收标准评估）也已按实跑结果起草，`.docx` 与 PDF 已重出** | `B-3`、`B-4` | 10-20 | `../submissions/BPMEA/BPMEA_Written_Evaluation.docx` 与 `../submissions/BPMEA/BPMEA_Written_Evaluation.pdf`（23 页）；底稿为追溯表第 3、4 节与第 4.8、4.9 节 | 已完成（Markdown 定稿，`docx`／PDF 已导出；第二部分已按实跑成稿，`PB-31` 签认已于 2026-10-20 登记） |


`PB-34`（V1→V2 变更说明）本人一责，已完，不在表上。

`Est-06` 已按课表重排：上周那三天排的是 **Stand-up 03（10-12 周一）、Sprint Review 03（10-14 周三）、Stand-up 04（10-16 周五）**，依据 `../W01/Weekly-Schedule_2026-10-12_16.png`。`SR4` 不在这张周表里，规范只写 22 October 之前。16 日那场是 SU4 不是 SU3，原先按「16 日 = SU3」写的那一行已整行移到 SU4 表下；SU3（12 日）四行统一写「Not recorded」，表下注明这样写的理由。

10-12 当天其实有两笔本人的提交 `db289ae`、`6ec8191`，内容是归档 W03 课件与 piStar 工具，不是项目工作，不能拿来顶替当天的发言。我先前在记录里写过「12 日没有任何本人的提交」，这句是错的，已在 `part7` 的说明里改正。

`Est-21` 是 2026-10-19 新增的：权威表（End of Week 6 · Full Portfolio）把「需求对齐评估」与「验收标准评估」列为判分对象，并要求书面评估用 `.docx` 或 PDF。此前只做了分析，没有可交的书面件。

`Est-02` 两笔分开算：`PB-12` 在本人手上，`PB-16` 在 Ryan 手上。前者不能直接签——`PB-12_abstraction-level` 的复核清单第 4 项写的是「映射与 `Hospital_All_Processes_Simple_C8` 一致」，而第二版的运行模型已先后换成 `Hospital_All_Processes_V2_C8`、`Hospital_All_Processes_V3_C8`（V3 为当前模型）；第 5 项又要求「第 6 节与运行中的方案一致」。这两项照现状勾不上，所以单列为 `Est-20`。

---


## 二、个人准备（用于汇报，不进提交范围）


| ID     | 我要准备什么                                                                  | 用途           | 期限    | 状态  |
| ------ | ----------------------------------------------------------------------- | ------------ | ----- | --- |
| Est-07 | Standup 4（10-16）的发言：自报完成、下一步、阻塞、证据、交接，各一条，都能当场点到文件或提交。该场已过；底稿留在 `../Week6 Coursework/process/notes/SU4_2026-10-16.md`，剩下的用途是 SR4 现场的同一套口径 | SU4 个人 5%    | 已过（10-16） | 已完成（发言卡已备，记录已写） |
| Est-08 | 演示里本人讲的那一段：第二版相对 9 月 29 日改了什么，按 `PB-34` 的口径讲，不要临场另编说法。SR3（10-14）已过，留给 SR4 | SR4 现场    | SR4 前 | 进行中 |
| Est-09 | 问答底稿两条：一是待办为什么收窄为只记产品工作；二是工作簿 Part 3 原文写了含 review 与 evidence，本人如何解释这个偏移。SR3（10-14）已过，留给 SR4 | SR4 提问 | SR4 前 | 未开始 |
| Est-10 | 陈述本人贡献用的材料清单：把 `Est-01`、`Est-04` 的证据串成一条能当场演示的线                         | 配合 `Est-04`、`C-3`  | 10-20 | 未开始 |

---



## 三、待确认（要问人或要自己拍板）


| ID     | 待确认什么                                                   | 为什么卡住                                                                                                  | 状态  |
| ------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --- |
| Est-11 | `W03/README.md` 第 3 行的课号 `UFCFAF-30-3` 是否该改成 BPM&EA 的课号 | 这批 10 月课件从内容看属 BPM&EA，但仓库里没有 BPM&EA 的规范可对照，不能替本人猜                                                      | 待确认 |
| Est-12 | 补 BPM&EA（UFCEP4-0-3）的评分规范与交付要求                          | **内容已定（2026-10-19）**：权威表把第二版 BPM&EA 定为「End of Week 6 · Full Portfolio」，五项为战略 BPMN、i 模型、需求对齐评估、验收标准评估、支持文件。截图已存入 `../W01/BPMEA-Full-Portfolio-requirements_2026-10-19.png`。**仍未解决的只剩各项权重与原件出处**：权重表仓库内没有，原件（.docx 或 .pdf）也不在仓库里 | 已完 |
| Est-13 | 规范写的 22 October 与通知写的 10 月 20 日，以哪个为准 | `UFCEP6-0-3_Presentation_Assessment_Specification V2.docx` 第 3 节交付件表印 **22 October 2026**，同一份文件的封面 `Submission Date` / `Submission Time` 却是 **TBC**；通知写 10 月 20 日 23:59。两个日期并存，仓库内无法判定 | 待确认 |
| Est-14 | 10-16 那场是否算 Standup 3，且按个人计分 | **已确认**：课表最后一周把 Stand-up 03 排在 10-12（周一）、Sprint Review 03 排在 10-14（周三）、Stand-up 04 排在 10-16（周五），见 `../W01/Weekly-Schedule_2026-10-12_16.png`。站会按个人计分、评审按小组计分，这条规范也写明了。**仍未定的只剩 SR4 的日期**：它不在这张周表里，规范只说 22 October 之前 | 已确认（SR4 日期待定） |
| Est-18 | 四份 i 模型里的中文批注要不要统一改成英文                                  | 这是 `Est-17` 查出的后续选择：要改就在 piStar 里改再重新导出，不能手改文本（会与 `V1_SD_diagram.png` 脱节）；不改则保持现状，README 已注明用 UTF-8 打开 | 待确认 |
| Est-19 | 问清提交形态：单包 zip 还是分附件槽、有无命名规则、单件大小上限 | 两份 AISD 规范只写「Blackboard 小组提交」，格式只规定了幻灯片、PDF 导出与验收计划三处，打包与命名一字未提；这三条不确认，包结构只能自己定 | 待确认 |


---

## 四、提交清单（逐件）

> **判据**：能交出去的文件，不是工作项。每件给五项——最终文件名、格式的原文要求、必须包含的内容、从哪份源文件生成、谁负责。
> **截止**：通知写 2026-10-20 23:59；AISD 规范第 3 节印 22 October 2026，封面 TBC。仓库内判不了（`Est-13`）。按早的那个准备。
> **提交口**：Blackboard，小组提交，**不适用 48 小时宽限期**。
> **两门课交的不是同一批东西**：AISD 四个槽（演示、更新后的方案、反馈记录、规划证据）；BPM&EA 是模型与评估（战略模型、i 模型、两份评估、支持文件）。不要把一份包交到两个口。
> **文件名都是建议名**：规范没写命名规则（`Est-19`）。定下后全文替换。

**挡不挡提交**：`A-1` 幻灯片已定稿（`../submissions/AISD/AISD_Presentation_2026-10-19.pptx`，13 页，附同名 PDF；第 8、9 页已按 10 月 19 日的实跑结果改写），一责 Ruby 于 2026-10-19 复核，未要求改动。AISD 包仍不能整包提交：`A-2` 已不挡（两个发布标签在远端可认，`Submission_Index` 已出，根 README 有 `Releases` 一节），`A-3` 已出（`../submissions/AISD/AISD_Feedback_Response_Record.pdf`，11 页，六项逐条标明），`A-4` 已出（`../submissions/AISD/AISD_Planning_Evidence.pdf`，8 页，两版计划、评审记录与两版风险记录都在内，缺口按实留白）。`B-3`／`B-4` 书面评估三件已出（`BPMEA_Written_Evaluation`，23 页）：第一部分定稿，第二部分已按实跑成稿、`PB-31` 签认尚未登记；`B-1`／`B-5` 的可读 PDF 已出（战略 8 页、运营 16 页）。BPM&EA 包：`B-8` 已出第二版（`../submissions/BPMEA/Group_Project_and_Test_Plan_2026-10-20.pdf` ＋ `.docx`，9 页，六件验收用例按实跑记录、`AT-03` 记为失败，29 日版留作初始版记录）。`B-4` 的 `PB-31` 签认与 `B-2` 的二责签字都已于 2026-10-20 登记。**不再有缺件**，只剩一处不一致：`B-2` 的 Admin 图仍是改正九条箭头之前的样子，须在 piStar 里按 `…_2026-10-19.txt` 重出一张，否则包内源文件与图对不上。

---

### 4.1 AISD（UFCEP6-0-3）：四个槽

依据：`../W01/UFCEP6-0-3_Presentation_Assessment_Specification V2.docx` 第 3 节。

| 编号 | 要交的文件 | 格式（原文要求） | 必须包含 | 从哪份源文件来 | 负责 | 现状 |
| --- | --- | --- | --- | --- | --- | --- |
| `A-1` | `AISD_Presentation_2026-10-19.pptx` ＋ 同名 PDF | **`.pptx` 或 PDF**（两者之一即可，交付时两种都放更稳） | references；指向支持证据的可打开链接；每位成员能讲自己那部分 | 骨架用 `../submissions/BPMEA/Hospital_Pathway_BPMEA_Presentation_2026-09-29.pptx`（8 页，第一版），内容换第二版；事实依据为 `BPMEA_Written_Evaluation`、`feedback-response_2026-10-16` 与 10 月 19 日的 V3 实跑记录 | Ruby | **已定稿**：13 页，`.pptx` ＋ PDF 都在 `../submissions/AISD/`；一责 Ruby 于 2026-10-19 复核，未要求改动；每页备注写明由谁讲、讲哪几点 |
| `A-2` | 无独立文件：Blackboard 的说明框里填仓库链接；包内放 `Submission_Index.pdf` | 原文不指定文件格式，机制是 **repository link** | `identifiable initial release and revised versions`＋`updated run instructions` | `../README.md`、两个标签、`../Week3 Coursework/hospital-pathway/README.md` 的 How to run | Ruby | **已齐（标签重打之后）**：`submission-2026-09-29`（`f6fec99`）与 `submission-2026-10-20` 都在远端可认；`submission-2026-10-20` 指向最终提交的树，提交号从标签上读（`git rev-parse submission-2026-10-20^{commit}`）；`../submissions/Submission_Index.docx` 与两页 A4 的 `../submissions/Submission_Index.pdf` 已出，两个版本、两门课的交付件清单、验收证据与尚未到位的六项都在其中；根 README 有 `Releases` 一节，两版并排写明并指出修订版为当前版；运行说明已按目录树核过（`c8run.exe start --disable-connectors`、gRPC 26500、`mvn -B spring-boot:run` 与三个验收脚本） |
| `A-3` | `AISD_Feedback_Response_Record.pdf` | 无格式规定 | feedback、decision、action、evidence、outcome、outstanding work 六项齐；未实施的写理由与遗留风险 | `../Week6 Coursework/feedback/feedback-response_2026-10-16.md` | Estrella | **已出**：`../submissions/AISD/AISD_Feedback_Response_Record.pdf`（11 页）与同名 `.docx`；六项逐条标明，`F-08` 拆为 `F-08a`／`F-08b`，`F-11` 记未实施并写明遗留风险，导师栏留空；证据路径逐条核过 |
| `A-4` | `AISD_Planning_Evidence.pdf` | 无格式规定 | **初始版与修订版的计划**、任务记录、两次 sprint review、**风险记录** | `../Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md`＋`process/part7`、`part8`＋初始版冲刺待办 `../docs/p6-sprint-backlog.md` | Ender | **已出**：`../submissions/AISD/AISD_Planning_Evidence.pdf`（8 页，与同名 `.docx` 同版同页）与 `.docx`；两版计划、任务与站会记录、SR1–SR4 四栏（SR3 四栏按 16 笔提交反推、SR4 八栏齐并注明快照 `sr4-2026-10-20`）、两版风险记录（初始版六条各附据、写明做了什么与没做什么）、经验教训六条。仍弱处：SR2 无记录、SU3 四行未记、SR3 当日无实跑证据、初始版风险非当时在册，文内已按缺口写明 |

**第一次发布的三件不进第二版的槽**：Acceptance Test Plan、Justification of Decisions、详细运营 BPMN。它们通过 `A-2` 的仓库与 `A-4` 的记录继续支撑评分。要放进包里只能标注「初始版交付件，仅备查」，不能当本轮主件。

AISD 第一次发布的「支持文件」三项（可编辑 `.bpmn`、可读 PDF、验收计划）由 `A-2` 的仓库、`B-5` 的运营模型 PDF 与 Ryan 的验收记录覆盖，不另设文件。**现场演示不算上传件**，它靠 `A-1` 与 `A-2` 支撑，见 4.5。

---

### 4.2 BPM&EA（UFCEP4-0-3）：五项 ＋ 支撑件

依据：`../W01/BPMEA-Full-Portfolio-requirements_2026-10-19.png`（End of Week 6 · Full Portfolio）。

| 编号 | 要交的文件 | 格式（原文要求） | 必须包含 | 从哪份源文件来 | 负责 | 现状 |
| --- | --- | --- | --- | --- | --- | --- |
| `B-1` | `BPMEA_Strategic_Process.bpmn` ＋ `BPMEA_Strategic_Process.pdf` ＋ `BPMEA_Abstraction_Note.pdf` | `.bpmn` 可编辑；**可读 PDF 导出**；说明文档 | 组织职责、外部交互、与运营流程的衔接 | `../docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`、`PB-12_abstraction-level_2026-09-29.md` | Ruby，二责本人 | **三件已齐、内容已改**：可读导出 8 页；抽象说明 PDF 6 页，第 4 节已补 `VisitNeedsSlot` 与六路就诊结果，第 6 节退款一格记为已收口，卷首注明现行模型为 V3。**二责复核已于 2026-10-19 签署**（`Est-02`），签字见抽象说明第 7 节 |
| `B-2` | `iStar_SD.txt` ＋ `iStar_SD.png`；`iStar_SR_Admin.txt`／`_Clinical.txt`／`_Finance.txt` 各配一张图 | 可编辑源文件（`where supported`）— 即 piStar 导出的 `.txt`；图随文件 | 角色、目标、软目标、任务、资源、依赖 | `../Week6 Coursework/istar/V1_SD_diagram.txt`、`V1_SD_diagram.png`、三份 `PB-16_V1_*_SR_reviewed_*.txt` | Estrella | 源文件四份在，**四张图已齐**（Admin `_2026-10-19.png`、Finance、Clinical、SD 各一张，10-19 补齐）；Ryan 二责复核已于 2026-10-20 落签；九条 Admin 贡献链接当日改正（`…_2026-10-19.txt`），Finance 的 `D18` 与 `D14`–`D17` 已按第 5 节日录逐条复核，非元模型错误，按设计保留；Admin 图未重出 |
| `B-3` | 与 `B-4` 合为一份 `BPMEA_Written_Evaluation.docx`（另出 PDF） | **`.docx` 或 PDF**（原文点名） | 第一部分：需求对齐评估——逐条规则与模型／表单／worker／测试的对应，动了与没动都说清 | `../docs/requirements-traceability-matrix.md` 第 3、4 节 | Estrella（`PB-39`） | **已出**：`BPMEA_Written_Evaluation.docx`／PDF，23 页（`Est-21`） |
| `B-4` | 同上，第二部分 | 同上 | 第二部分：验收标准评估——初版与修订后的验收标准、实际测试结果、支持证据、已识别的失败，以及有理由的评估 | 10 月 19 日 V3 实跑的六件记录（`../Week3 Coursework/hospital-pathway/evidence/`）；`../submissions/AISD/Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf` | Ryan（`PB-31`），汇总人未定 | 已按实跑起草在 `BPMEA_Written_Evaluation` 第 4 节：六过一败，`AT-03` 两版同败；`PB-31` 签认已于 2026-10-20 登记 |
| `B-5` | `BPMEA_Supporting_Files/`：可编辑运营模型、部署配置、**两份可读 PDF**、i 源文件 | 可编辑 `.bpmn`＋部署配置；`readable PDF exports`（原文为**复数**） | 运营模型 `Hospital_All_Processes_V3_C8`；部署配置；运营与战略各一份可读导出 | `../Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`；`../Week6 Coursework/code/src/main/resources/application.yaml`、`config/application.example.yaml` | Ruby（`PB-30`） | **两份可读导出已出**（10-19）：运营 `BPMEA_Operational_Process_Readable_2026-10-19.pdf`（16 页，A3 横版，75 个节点无一被页边切断）、战略同上（8 页）。脚本 `../Week6 Coursework/scripts/render_bpmn_readable_pdf.py` 可复现 |

**随仓库交付、第二版不另设槽的支撑件**（9 月 29 日布告 BPM&EA 第 2、3、4 项的要求）：

| 编号 | 文件或位置 | 格式 | 必须包含 | 负责 | 现状 |
| --- | --- | --- | --- | --- | --- |
| `B-6` | `../Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/`、`pom.xml`、两份 yaml | 源码 ＋ 依赖 ＋ 配置模板 | 17 个 Java 文件、10 个作业类型 | Ender 等 | 在；29 日之后有改动，10 月 19 日在 `dbc0a33` 干净重跑，19 项测试全过（`evidence/Java_Clean_Build_Test_2026-10-19.txt`） |
| `B-7` | `../Week6 Coursework/forms/`（12 份 `.form`；`../Week3 Coursework/hospital-pathway/forms/` 是 10 月 19 日输入校验之前的旧版） | 可编辑 form 文件 ＋ 任务绑定 | 绑定写在 BPMN 各任务的 `formDefinition`；`await_attendance` 是第二版新增 | Estrella（`PB-13`） | 在 |
| `B-8` | `../submissions/BPMEA/Group_Project_and_Test_Plan_2026-10-20.pdf`（29 日版留作初始版记录） | 未规定 | 产品待办、冲刺待办、规划证据、测试计划、测试结果、测试证据 | Ruby | **第二版已出**：`.pdf` ＋ `.docx`，9 页；六件验收用例带实例号与证据文件，`AT-03` 记失败，未跑的判据逐条写 NOT EXECUTED。规范 7.4：**这一件不允许使用生成式 AI**，文中只填已落盘的实跑结果 |

---

### 4.3 两门课都要，但不占上传槽

规范对这四件用的是 `Retain`／`Preserve`，不是 `Submit`：不上传独立附件，但**仓库里打不开就等于没交**。

| 编号 | 文件 | 要求（原文） | 必须包含 | 负责 | 现状 |
| --- | --- | --- | --- | --- | --- |
| `C-1` | `../Week6 Coursework/process/part7-standup-records.md` | *Retain a brief record of blockers, next actions and handovers* | 每人每场一行；六栏：完成／证据／下一步／阻塞／需要的支持／要交接的 | 每人写自己那行，Ruby 收 | SU4（10-16）：本人一行已写；Ruby、Ryan 两行的「完成／证据」按当日提交补出，发言四栏留「—」；Ender 当日无提交，只记这一事实。SU3（10-12）：四行记「Not recorded」 |
| `C-2` | `../Week6 Coursework/process/part8-sprint-review-records.md` | *Preserve a version or snapshot for each review*；每次评审后开回顾并记下下一冲刺的改进 | SR3、SR4 各七个字段（完成项、未完成项、关键决策、集成证据、测试证据、收到的反馈、待办变更）＋回顾两栏 | Ruby，二责 Ryan | SR3 八个字段已成文：完成／未完成／关键决定／集成证据四栏与回顾两栏按 `f6fec99..25f53f7` 的 16 笔提交反推，出席与反馈不臆测；SR4 八栏齐，快照 `sr4-2026-10-20`（`a0d8f55`）。SR1（9-16）、SR2（9-28）已在同一文件开头列明各有什么、缺什么、为什么不事后补写 |
| `C-3` | `est：PB-17贡献记录表.md`（本目录） | *Retain contribution evidence for tutor moderation* | 视图 A 逐条证据、视图 B 按条目对账；每条能打开 | Estrella | 已填：视图 A 53 行（`E-001` 至 `E-053`），视图 B 已出，2026-10-20 更新（`Est-04`） |
| `C-4` | `../docs/definition-of-done.md` | 该约定须 *accessible to the team* | 四名成员各一笔签字 | Ender，二责本人 | 四人已于 2026-10-20 签署（`Est-05`） |

---

### 4.4 AISD 判分对照：分落在哪件上

规范第 4 节的原表（BPM&EA 没有权重表，见下）。

| 判分块 | 权重 | 靠哪几件 | 现状 |
| --- | --- | --- | --- |
| Further development | 25% | `A-2`（仓库里的模型、worker、表单）＋ 运营模型的可读 PDF（与 `B-5` 里那份是同一个文件） | 模型与表单在；可读导出已出（10-19）；第二版已于 10-19 实跑：G07 走到 `COMPLETED`，六件过、`AT-03` 仍败 |
| Response to feedback | 20% | `A-3` | 反馈共 12 条（同伴 7 条、自查 5 条）已成文并出 PDF（11 页）；导师反馈未收到 |
| Project plan evaluation and justification | 25% | `A-4` | 已出（8 页）：两版计划、任务与站会记录、SR1–SR4、两版风险记录、经验教训；计划与实际对照在文内第 2、3、8 节。缺口照实写：SR2 无记录、SU3 无记录、SR3 当日无实跑证据 |
| Standup 3 | 5%（个人） | `C-1` | 记为 Not recorded |
| Standup 4 | 5%（个人） | `C-1` | 本人已写，其余三人空 |
| Sprint review 3 | 10%（小组） | `C-2` | 已成文：四栏按 16 笔提交反推，出席与反馈不臆测 |
| Sprint review 4 | 10%（小组） | `C-2` | 日期未公布 |

小组分受个人贡献约束：`C-3` 不单独计分，但贡献认定不了，小组分会被调。

**BPM&EA 没有权重表。** 权威表只写要交哪五项，没写各项占比。能确定的是判分对象为 `B-1` 至 `B-5`。

---

### 4.5 本人要交的

小组包由一人上传（谁未定，见 4.8）。下面是本人要在包内交出去、或现场自己交代的部分。

| 要交的 | 性质 | 落在哪 | 现状 |
| --- | --- | --- | --- |
| `A-3` 反馈处置记录（一责） | 20% 那一块 | 见 4.1 | 已出（`Est-03`） |
| `B-3` 书面评估第一部分：需求对齐（一责） | BPM&EA 全套第 3 项 | 见 4.2 | 已出（`Est-21`） |
| `B-2` i 模型源文件（一责），并追 Ryan 签二责 | BPM&EA 全套第 2 项 | 见 4.2 | 源文件在；二责已于 2026-10-20 落签（`Est-02`）；Admin 图待重出 |
| `C-1` Standup 4 本人那一行（10-16） | 个人 5% | 见 4.3 | 已写（`Est-06`） |
| `C-1` Standup 3 本人那一行（10-12） | 个人 5% | 见 4.3 | 按实写「Not recorded」 |
| `C-3` 贡献证据行 | 供 tutor 核查 | 见 4.3 | 已填 53 行（`E-001` 至 `E-053`）＋视图 B（`Est-04`） |
| `C-4` 完成定义本人签字 | 二责那一笔 | 见 4.3 | 已签，2026-10-20（`Est-05`） |
| `B-1` 战略模型二责签字 | 二责那一笔 | `../docs/strategic-bpmn/` | 已签（2026-10-19）；签前已核映射（`Est-20`）。三件交付物已齐，签字见抽象说明第 7 节 |
| `A-1` 幻灯片二责复核 | 一责 Ruby | `../submissions/AISD/` | 已定稿（13 页，`.pptx` ＋ PDF）；一责 Ruby 于 2026-10-19 复核，未要求改动 |
| SR4 现场本人那一段与答辩 | 规范要求每位成员能解释自己的贡献 | 现场 | 准备见 `Est-08`、`Est-09` |
| `PB-34` V1→V2 变更说明（一责） | 支撑 `B-1`、`B-2` 的对照 | `../Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` | 已完成 |

---

### 4.6 从现在到截止，按「挡不挡提交」排

1. **`A-1` 第二版幻灯片**：已定稿（`../submissions/AISD/AISD_Presentation_2026-10-19.pptx` ＋ 同名 PDF，13 页；第 8、9 页换成了 10 月 19 日的实跑结果与边界），一责 Ruby 于 2026-10-19 复核，未要求改动。AISD 的 25%＋20% 两块靠它当场呈现，这一件已落地。
2. **`A-4` 规划证据汇总**：已收口。PDF 8 页与同名 `.docx` 都在 `submissions/AISD/`，两者同版同页（此前 PDF 停在 7 页的旧版、与 13:12 的 docx 不同版，已重出对齐）。两版计划、任务与站会记录、SR1–SR4、两版风险记录、经验教训齐。初始版风险六条按 9 月记录成文，每条写明做了什么、没做什么；SR2 无记录、SU3 四行未记、SR3 当日无实跑证据，文内按缺口写明。
3. **修订版标签与根 README**（`A-2`）：已收口，但以标签重打之后为准。`submission-2026-09-29`（`f6fec99`）与 `submission-2026-10-20` 都在远端可认；`submission-2026-10-20` 指向最终提交的树，提交号用 `git rev-parse submission-2026-10-20^{commit}` 读；根 README 已加 `Releases` 一节，两版并排写明、修订版标为当前版。`standup-1-2026-09-16`、`sr3-2026-10-14` 不是发布标签；规范要的初始版**和**修订版，现在都认得出。
4. **`B-4` 书面评估第二部分**：第二部分已按 19 日实跑成稿（`BPMEA_Written_Evaluation` 第 4 节，六过一败，`AT-03` 两版同败），`PB-31` 的签认也已登记；验收证据本身不再是阻塞项。
5. **`B-1` 抽象说明的四处改稿**：已收口。A–D 已改入原文，一责 Ruby 于 2026-10-19 确认改后文本，二责复核同日签署 accepted；三件交付物齐，签字见抽象说明第 7 节。
6. **`C-2` 的 SR3 七个字段**：已收口。快照 `sr3-2026-10-14`（指向 `25f53f7`）；八个字段中「完成／未完成／关键决定／集成证据」四栏与回顾两栏按 `f6fec99..25f53f7` 的 16 笔提交反推成文，每句都指名提交号，可逐条开 diff 核对；「出席」与「反馈」两栏不臆测，前者记「未留出席名单」，后者只写已在手的班级反馈表。「未完成／测试证据」如实记当日无运行记录。SR4 按 2026-10-20 的定稿会成文，快照 `sr4-2026-10-20`（指向 `a0d8f55`），八个字段＋回顾三栏齐。
7. **`B-8` 项目与测试计划的第二版**：已收口。`Group_Project_and_Test_Plan_2026-10-20.pdf` ＋ `.docx`（9 页）在 `submissions/BPMEA/`，六件验收用例逐条带实例号与证据文件，`AT-03` 记失败，未跑的判据写 NOT EXECUTED，29 日版留作初始版记录；仍注意 7.4 的 AI 禁用，文中只填实跑结果。
8. **`C-3` 贡献记录**：不单独计分，但影响小组分的个人认定。
9. **`A-3` 反馈处置记录**：已收口。PDF 11 页与同目录 Markdown 都在 `submissions/AISD/`；`F-08` 已按第 10 组四条转写拆为 `F-08a`／`F-08b`，导师反馈截至 10-19 一条未收到，第 2 节按事实留白。
10. **`C-4` 与二责签字**：已收口。完成定义四人于 2026-10-20 签署；`B-1`、`B-2`、`B-4`、`B-5`、`B-6`、`B-7` 的二责复核也已登记。
11. **计划 B 部分缺「依赖」一列**：规范要求每个活动都有 owner 两名、estimate、acceptance conditions、**dependencies**、status；`sprint3-4-plan` 的 A 部分有 `Depends on`，B 部分没有。

---

### 4.7 怎么打包、怎么上传

**原文能定的**

- 两门课**两个提交口各交一份**，不合并成一个包。
- 附件优先，仓库链接作补充：原文是 `Submit through Blackboard with accessible repository links where appropriate`，链接不能替代附件。
- 仓库地址同时出现在三处：提交说明框、包内说明文件、幻灯片末页。
- 一人上传，其余三人确认；上传后截图，记下提交时间与回执编号。

**包结构（建议）**

```text
UFCEP4-0-3_Group<组号>_SecondRelease_<日期>.zip      ← BPM&EA：按五项排
├─ 00_README.txt              组号、成员与 UWE ID、仓库地址、两个标签、哪份文件对哪条评分
├─ 01_B-1_Strategic_BPMN/     战略模型 .bpmn ＋ 可读 PDF ＋ 抽象说明 PDF
├─ 02_B-2_iStar/              SD 与三份 SR 的 .txt ＋ 四张图
├─ 03_B-3-B-4_Written_Evaluation.docx（附 PDF）
├─ 04_B-5_Supporting_Files/   可编辑运营模型 .bpmn ＋ 部署配置 ＋ 运营模型可读 PDF
├─ 05_B-6-B-7_Workers_and_Forms/  src/、pom.xml、两份 yaml、12 份 .form
├─ 06_B-8_Project_and_Test_Plan.pdf
└─ 07_Presentation.pptx
```

```text
UFCEP6-0-3_Group<组号>_SecondRelease_<日期>.zip      ← AISD：按四个槽排
├─ 00_README.txt                 仓库地址与两个标签、四件各对哪条评分
├─ 01_A-1_Presentation.pptx（附 PDF）
├─ 02_A-2_Submission_Index.pdf   Updated solution：仓库链接、两个版本、运行说明
├─ 03_A-3_Feedback_Response_Record.pdf
└─ 04_A-4_Planning_Evidence.pdf  初始版与修订版计划、任务记录、两次评审与回顾、风险记录
```

AISD 那一份**不放** 29 日的验收计划与设计决策作主件：四个槽里没有它们，放进去会让 tutor 分不清哪份是本轮交付。

**仓库侧四件事**

1. 最后一批改动之后打修订版标签（例如 `submission-2026-10-20`），保留 `submission-2026-09-29`。**已做**：`submission-2026-10-20` 已重打并推到远端，指向最终提交的树（提交号从标签上读：`git rev-parse submission-2026-10-20^{commit}`），`submission-2026-09-29` 保留，见 4.1 的 `A-2` 行。
2. 根 `README.md` 写明「本次提交对应哪个标签」，并链到 `../Week3 Coursework/hospital-pathway/README.md` 的 How to run。**已做**：根 README 已加 `Releases` 一节，两版并排，运行说明链已放进去。
3. 无痕窗口打开一次，确认不登录也能看文件与标签。
4. 评审快照：SR3 已打 `sr3-2026-10-14`（`25f53f7`，10-14 15:07，评审前最后一笔；当天 21:01 的 `2d09f5a` 不计入）；SR4 已打 `sr4-2026-10-20`，指向 `a0d8f55`（18:16 定稿会那一笔）；`submission-2026-10-20` 指向 `bab36f9`（19:01 最后一笔）。两者指向不同提交，性质也不同，各记各的。快照与提交标签是两回事，不能互相顶替。SR1 与 SR2 没有专门快照：`standup-1-2026-09-16` 指 `93dfaf5`，那是站会标签，只能算「最接近」，不要当评审快照用。

**仓库没写、别自己当规范**

| 没写的 | 后果 |
| --- | --- |
| 单包 zip 还是分附件槽 | 决定包结构；分槽时 PDF 与 `.pptx` 各自单独传 |
| 文件命名规则 | 老师辨认最终版只能靠包内说明 |
| 单件大小上限、是否允许 zip | 源码加 PDF 可能超限，要提前试传 |
| 是否需要封面页或成员名单 | 规范只写 group submission |
| 谁上传、是否每人各自确认 | 见 4.8 第一行 |
| 仓库链接填在哪个字段 | 提交说明框、附件文本，还是只在幻灯片里 |
| 是否要 AI 使用声明 | 规范 7.4：**Project & Test Plan 不允许使用生成式 AI**，直接约束 `B-8` |

---

### 4.8 这一节还不能定的六件事

| 待确认 | 为什么要紧 |
| --- | --- |
| 谁在 Blackboard 上传组包 | 两门课两个提交口，具体由谁操作仓库里查不到 |
| 截止是 20 日还是 22 日 | 规范交付件表印 22 日，通知写 20 日 23:59，见 `Est-13` |
| BPM&EA 规范原件与权重 | 五项已定，截图存 `../W01/BPMEA-Full-Portfolio-requirements_2026-10-19.png`；**缺原件与各项权重**，见 `Est-12` |
| 单包还是分槽、命名规则、大小上限 | 规范一字未提，见 `Est-19` |
| 修订版标签打在哪一笔 | **已定**：`submission-2026-10-20` 就是修订版的发布标识，指向最终提交的树，提交号从标签上读（`git rev-parse submission-2026-10-20^{commit}`）。这条曾挂着，理由是「`HEAD` 还在 `c452381`、第二版还在改，标签要等最后一批改动之后再打」；现在不必再等 |
| SR4 开在哪一天 | **已定**：2026-10-20，即 `../docs/definition-of-done.md` 签署记录所记的那次定稿会，四人到场；快照 `sr4-2026-10-20` |
| 合并后的模型能否部署 | 决定现场走整条流程，还是按 9 月 29 日布告的备选方案改成每人一个小模型 |

---



## 五、不在本人名下（列出来免得混淆）

- `A-1` 第二版幻灯片、`B-1` 战略模型、`A-2` 仓库标签：一责 Ruby。其中 `A-1` 的 13 页幻灯片（Ruby 已于 2026-10-19 复核，未要求改动）与 `B-1` 的两份可读导出，均为本人本次产出。
- `B-4` 验收标准评估（书面评估第二部分）、`PB-31` 验证：一责 Ryan。10 月 19 日的实跑已完成，`PB-31` 的验证结果写进 `BPMEA_Written_Evaluation` 第 4 节；该条的签认已于 2026-10-20 登记。
- `A-4` 规划证据与计划评估：一责 Ender。
- `C-2` SR3／SR4 评审记录：一责 Ruby，二责 Ryan。
- `B-6` worker 源码：Ender 等。
- 仓库一致性与重复件收敛：2026-10-16 已完成。

以上如有需要本人以二责介入，改本表的对应行，不动产品待办。
