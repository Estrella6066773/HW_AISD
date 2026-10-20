# PB-17 贡献记录表

**主笔**：Estrella　**复核**：Ender　**起表日期**：2026-09-16　**对应条目**：PB-17 举证与贡献记录维护

> **2026-10-16**：`PB-17` 已从产品待办撤出——产品待办只记产品工作，而贡献记录是考核过程材料，不是产品。本表因此不带 `PB` 编号；它现在的落点是 `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md` 的 B 部分。表内「对应条目」一栏保留原样，因为记的是 9 月 16 日起表时的情况。

> **2026-10-20 填表**：视图 A 与视图 B 已按仓库里实际存在的证据填完，来源只有提交记录、可打开的路径和文件自带的日期，没有补写任何一次会议或对话。视图 A 共 53 行，视图 B 覆盖初始发布 26 条、第二版 4 条，另列 3 条已撤出的条目。两节引用的路径与文件名已逐一核过：凡写目录加文件名的一律按原路径测过，全部存在；少数只写文件名的地方，所在目录在同一行的路径里给出。唯一查无此件的是 `Ruby/2026-09-22/PB-20_角色权限矩阵.md`，它是归档草稿里的死链，已在第五节第 6 条注明，不作为任何条目的证据。
>
> 提交分布按 `git log --format='%an <%ae>'`：Estrella 113 笔、Ruby 62 笔、Ryan 15 笔、Ender 8 笔，`main` 上合计 198 笔。**这个分布很不均，本表如实照录，不做平均化处理**。证据日期取文件落地的那笔提交日期；文件所在目录名可能早一天，以路径回查为准。
>
> 第八节的八项自检中，第 1、2、4 项成立，第 3、5、6、7、8 项不成立，逐条理由在节内。Ender 的复核已于 2026-10-20 落签，见第九节。

**用途**：留存全组贡献证据，供 tutor 核查个人贡献。依据考核规范 Section 4 的要求：*Group-based marks are subject to individual contribution. Retain contribution evidence for tutor moderation.*

**验收条件**（取自产品待办 PB-17）：表内每条证据都能打开，且与条目负责人一致；缺证据的条目不标完成。

---

## 一、使用说明

1. 本表分两个视图。**视图 A** 按证据逐行登记，回答「有哪些证据」；**视图 B** 按条目对账，回答「证据够不够、能不能认定完成」。
2. 每人的证据由本人提交；Estrella 汇总核对，Ender 复核。
3. 每行证据的位置必须是**真实可打开的路径或链接**，不写「说明」「见上文」「截图」这类占位内容。
4. 条目状态沿用产品待办的口径：In progress 表示已开工，Not started 表示尚未开工，Blocked 表示受阻，Done 表示完成。
5. 标 Done 必须有可打开的产物与证据位置；缺证据的条目在视图 B 中标为「不可认定完成」，并在备注写明缺什么。

---

## 二、人名对照（核对「负责人一致」时使用）

**统一用名**取仓库文件夹名，与 `README.md`、`docs/p3-product-backlog.md`、`Ruby/2026-09-14/分工表.md` 一致。

| 统一用名 | 仓库文件夹 | 本名 | Blackboard | GitHub 提交显示名 | UWE ID |
|----------|------------|------|------------|-------------------|--------|
| Ruby | `Ruby/` | Hao Zheng | Ruby | 郑好 | 23084382 |
| Estrella | `Est/` | Geping Chen | Estrella | Estrella6066 | 23084393 |
| Ender | `Ender/` | Minghao Qin | Ender | DLuffy | 23084402 |
| Ryan | `Ryan/` | Guanyan He | Ryan | ENTONG-Ryan | 23084395 |

本名、Blackboard 名称与 UWE ID 取自根 `README.md` 的 Team 表，与 `Ruby/2026-09-14/分工表.md` 的「成员」表一致；提交显示名与实际提交的对应关系见 `Est/2026-09-17/est：SDM与版本控制教程作业.md` 第 222 行「四位成员均在提交历史中出现：Estrella6066、郑好、ENTONG-Ryan、DLuffy」，由 `git shortlog -sne --all` 取得。

**注意**：任务拆分 `docs/p4-work-breakdown.md` 里 C 组员写作 `Ender`，与产品待办里的 `Ender` 是同一人，登记时统一写 `Ender`。

---

## 三、证据类型代号（登记时选用其一）

| 代号 | 类型 | 具体形式 | 判定要点 |
|------|------|----------|----------|
| SCR | 截图 | png / jpg | 能看清界面或状态，非空白、非纯文字标题 |
| CMT | 提交记录 | commit 短哈希 + 仓库链接 | 提交信息带条目编号 |
| MTG | 会议记录 | md | 有日期、出席人、结论与待办分工 |
| ART | 文档或模型产物 | md / bpmn / json | 是被认可为交付物的成品，非过程草稿 |
| TAG | 版本快照 | git tag | 每次评审一个 |
| LOG | 运行记录 | txt / log | 含时间与结果，多为模拟服务或测试输出 |
| BRD | 看板状态 | 截图或链接 | 状态需与产品待办一致 |

---

## 四、视图 A · 证据明细表

登记规则：一条证据一行。同一条目下同一人有多份证据时分多行登记。

| 证据编号 | 条目编号 | 姓名 | 条目内角色 | 证据类型 | 证据位置 | 证据日期 | 条目当前状态 | 核对结果 | 核对人与日期 | 备注 |
|----------|----------|------|------------|----------|----------|----------|--------------|----------|--------------|------|
| E-001 | — | Ruby | 主笔（Part 1） | ART | `Ruby/2026-09-14/ruby：part1案例摘要.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 案例摘要成稿；角色权限只写成第 11、25 行的文字，没有权限表 |
| E-002 | — | Ruby | 主笔（Part 1 讨论） | ART | `Ruby/2026-09-14/ruby：part1讨论记录.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 摘要的讨论底稿 |
| E-003 | — | Ruby | 主笔（Part 6） | ART | `docs/p6-sprint-backlog.md`；`Ruby/2026-09-15/ruby：part6 Sprint Backlog-理解.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 表头署 Ruby 主笔、Ender 复核 |
| E-004 | — | Ruby | 主笔（Part 8） | ART | `Ruby/2026-09-15/ruby：part8 Sprint Review准备.md`；`Ruby/2026-09-15/ruby：part8 Sprint Review.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | SR1 的两版准备稿；评审当场的记录栏为空 |
| E-005 | PB-12 | Ruby | 第一负责人 | ART | `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn` | 2026-09-29 | Done | 通过 | Estrella 2026-10-20 | 模型与抽象说明的提交均记在 Estrella 名下（`88a5bcc`、`2453c8c`），仓库无法把文件内容与条目负责人分开 |
| E-006 | PB-30 | Ruby | 第一负责人 | CMT | `357528e`：V2 改名为 V3，`pom.xml` 与 `HospitalPathwayApplication` 改指部署 V3 | 2026-10-19 | In progress | 通过 | Estrella 2026-10-20 | 部署链路由此改到 `Hospital_All_Processes_V3_C8` |
| E-007 | PB-30 | Ruby | 参与 | ART | `Ruby/2026-10-19/group10-feedback/Hospital_All_Processes_V3.bpmn`；`Ruby/2026-10-19/group10-feedback/README.md` | 2026-10-19 | In progress | 通过 | Estrella 2026-10-20 | README 记明补五处汇合网关（`Join_Register`、`Join_GetDocuments`、`Join_ReviewReferral`、`Join_DispatchLetter`、`Join_FinanceAdjustment`）；按 `id="Join_` 去重，`Week6 Coursework/bpmn/` 的主模型与这份副本都是 12 个汇合网关，另有 5 个 `_di` 图形元素沿用前缀 |
| E-008 | PB-30 | Ruby | 参与 | ART | `Ruby/2026-10-15/V2流程-临床SR-战略图对照.md`；`Ruby/V2-临床SR与BPMN对照-第10组.md` | 2026-10-16 | In progress | 通过 | Estrella 2026-10-20 | 模型与 SR 的对照，以及第 10 组四条反馈到改动位置的映射 |
| E-009 | PB-13 | Ruby | 第二负责人 | ART | `Week6 Coursework/forms/`（12 份 `.form`） | 2026-10-19 | Not started | 通过 | Estrella 2026-10-20 | 12 份表单在且被 19 日实跑用上；`PB-13` 的状态已改 `Done`，二责复核于 10 月 20 日登记在 `docs/p3-product-backlog.md`；必填校验仍没有截图 |
| E-010 | PB-01 | Ruby | 第一负责人 | ART | `Ruby/2026-09-14/ruby：part1案例摘要.md` 第 11、25 行 | 2026-09-15 | In progress | 缺件 | Estrella 2026-10-20 | 待办要「角色权限表＋核验界面截图」，两样都没有；`docs/p4-work-breakdown.md` 的 T01 却标 Done |
| E-011 | — | Ruby | 参与（A 组 worker） | CMT | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/HospitalPathwayWorkers.java`、`RefundWorkers.java`；提交 `42b1cc8`、`c90db46`、`ce89ae4` | 2026-09-27 至 2026-09-29 | — | 通过 | Estrella 2026-10-20 | 退款、付款调查与 `request-payment` 的关联 |
| E-012 | — | Ruby | 参与（第 10 组反馈归档） | ART | `Ruby/2026-10-19/group10-feedback/`（模型、12 份表单、README） | 2026-10-19 | — | 通过 | Estrella 2026-10-20 | 可部署副本，未覆盖 `Week6 Coursework/` 的主文件 |
| E-013 | — | Ruby | 复核（`A-1` 幻灯片） | ART | `submissions/AISD/AISD_Presentation_2026-10-19.pptx` | 2026-10-19 | — | 缺件 | Estrella 2026-10-20 | 复核一事只见于 `Est/est：个人待办.md` 的记述，无签字件、无提交记录 |
| E-014 | — | Estrella | 主笔（Part 3） | ART | `docs/p3-product-backlog.md`；`Est/est：part3产品待办.md`（归档草稿） | 2026-09-15 至 2026-10-16 | — | 通过 | Estrella 2026-10-20 | 表头署 Estrella 主笔、Ryan 复核 |
| E-015 | PB-16 | Estrella | 第一负责人 | ART | `docs/istar/PB-16_istar-sd-sr.md`；`docs/istar/PB-16_sd.md`；`docs/istar/PB-16_sr.md`；`docs/istar/PB-16_sd-overview.png` | 2026-09-29 | Done | 通过 | Estrella 2026-10-20 | 二责复核已由 Ryan 于 2026-10-20 落签；五项清单第 2 项按缺口未勾 |
| E-016 | PB-16 | Estrella | 参与 | ART | `Week6 Coursework/istar/PB-16_V1_Admin_SR_reviewed_2026-10-19.txt` 与同目录 `.png`；提交 `353f988` | 2026-10-19 | Done | 通过 | Estrella 2026-10-20 | Admin 视图复审后重出，文件名改为此日期 |
| E-017 | PB-34 | Estrella | 第一负责人 | ART | `Week6 Coursework/istar/PB-16_V1-V2_review-changes_2026-10-16.md` | 2026-10-16 | Done | 通过 | Estrella 2026-10-20 | 逐件写明改了什么、由哪笔提交承载 |
| E-018 | PB-28 | Estrella | 参与（条目一责为 Ruby） | ART | `docs/requirements-traceability-matrix.md` | 2026-09-16 至 2026-10-19 | Done | 通过 | Estrella 2026-10-20 | 该文件各笔提交均记在本人名下，一责 Ruby 无相关提交；条目负责人栏与产出入不一致 |
| E-019 | PB-39 | Estrella | 第一负责人 | ART | `docs/requirements-traceability-matrix.md` 第 4 节；提交 `feff514` | 2026-10-19 | Done | 通过 | Estrella 2026-10-20 | 13 支持、25 部分、4 未支持 |
| E-020 | PB-31 | Estrella | 条目负责人之外（一责为 Ryan） | LOG | `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`；同目录 `PB-14_acceptance-run-log_2026-10-19.json`、`PB-18_acceptance-run-log_2026-10-19.json`、`Group_Final_E2E_20261019-214234.json`、`Java_Clean_Build_Test_2026-10-19.txt`；提交 `41d2f10` | 2026-10-19 | Done | 通过 | Estrella 2026-10-20 | 在本人机器上执行；所跑模型与 worker 是集体产物（见 E-006 至 E-008、E-011、E-023、E-034、E-049）；第 2 部分书面评估的一责为 Ryan（见 E-026） |
| E-021 | PB-12 | Estrella | 第二负责人 | ART | `docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md` 第 7 节；`Est/est：PB-12二责复核意见_2026-10-19.md` | 2026-10-19 | Done | 通过 | Estrella 2026-10-20 | 签字在抽象说明第 7 节；改稿由一责 Ruby 确认 |
| E-022 | PB-13 | Estrella | 第一负责人 | ART | `Est/forms/`（6 份 `.form`）；`Est/est：步骤4表单提交报告.md` | 2026-09-26 | Not started | 通过 | Estrella 2026-10-20 | 26 日那批表单；部署用的 12 份在 `Week6 Coursework/forms/`，含 10-19 的校验修订（见 E-009） |
| E-023 | — | Estrella | 参与（B 组 worker 与领域库） | CMT | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/BookingWorkers.java`、`domain/` 10 个文件；提交 `d95b79f`、`e745808` | 2026-09-28 | — | 通过 | Estrella 2026-10-20 | 槽位、付款台账、审计事件三张表与 `AuditEventWriter` |
| E-024 | — | Estrella | 主笔（反馈处置记录） | ART | `Week6 Coursework/feedback/feedback-response_2026-10-16.md`；`submissions/AISD/AISD_Feedback_Response_Record.docx`、`.pdf`；提交 `120173f` | 2026-10-16 至 2026-10-20 | — | 通过 | Estrella 2026-10-20 | 12 条逐条落行，`F-11` 记未实施并写明遗留风险 |
| E-025 | — | Estrella | 主笔（书面评估第 1 部分） | ART | `submissions/BPMEA/BPMEA_Written_Evaluation.docx` 第 1 至 3 节；`submissions/BPMEA/BPMEA_Written_Evaluation.pdf` | 2026-10-19 | — | 通过 | Estrella 2026-10-20 | 42 条规则逐条评级 |
| E-026 | — | Estrella | 起草（书面评估第 2 部分，条目属 Ryan） | ART | `submissions/BPMEA/BPMEA_Written_Evaluation.docx` 第 4 节 | 2026-10-19 | — | 通过 | Estrella 2026-10-20 | 扉页写明第 2 部分属 `PB-31`；该条的签认已于 2026-10-20 登记在 `docs/p3-product-backlog.md` 的 `PB-31` 行 |
| E-027 | — | Estrella | 制作（`A-1` 幻灯片，一责为 Ruby） | ART | `submissions/AISD/AISD_Presentation_2026-10-19.pptx`、`.pdf`；提交 `a5ebd95`、`c5bd506` | 2026-10-19 | — | 通过 | Estrella 2026-10-20 | 13 页；本人制作，一责 Ruby 于 2026-10-19 复核，未要求改动 |
| E-028 | PB-30 | Estrella | 参与 | ART | `Week6 Coursework/scripts/render_bpmn_readable_pdf.py`；`submissions/BPMEA/BPMEA_Operational_Process_Readable_2026-10-19.pdf`、`BPMEA_Strategic_Process_Readable_2026-10-19.pdf`；提交 `6ff91a0`、`dbc0a33` | 2026-10-19 | In progress | 通过 | Estrella 2026-10-20 | 16 页与 8 页两份；待办 `PB-30` 的证据栏仍写「可读 PDF 待出」，与实物不符 |
| E-029 | — | Estrella | 主笔（仓库一致性与提交索引） | CMT | `151a86d`、`2c5252b`、`dcb1ff6`；`submissions/Submission_Index.docx`、`.pdf` | 2026-10-16 至 2026-10-19 | — | 通过 | Estrella 2026-10-20 | `A-2` 的一责为 Ruby，本次产出记在本人名下 |
| E-030 | — | Estrella | 主笔（Part 7 SU4 本人一行） | ART | `Week6 Coursework/process/part7-standup-records.md` | 2026-10-19 | — | 通过 | Estrella 2026-10-20 | 同一张表里其余三人为空 |
| E-031 | — | Estrella | 主笔（本表） | ART | `Est/est：PB-17贡献记录表.md` | 2026-10-20 | — | 通过 | Estrella 2026-10-20 | 复核已由 Ender 于 2026-10-20 落签，见第九节；八项自检见第八节 |
| E-032 | — | Ender | 主笔（Part 2） | ART | `Ender/2026-09-15/Ender：part2交付物清单.md`；提交 `5d4b17c` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | Part 1、2、4、6、7 初稿同批提交 |
| E-033 | — | Ender | 主笔（Part 4）与复核意见 | ART | `docs/p4-work-breakdown.md`；`Ender/2026-09-15/Ender：part4复核意见.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 复核意见第 1 条指出 T01 证据位缺失；该条至今未补（见 E-010） |
| E-034 | PB-09 | Ender | 参与 | CMT | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/LetterWorkers.java`；提交 `a0ac6cb` | 2026-09-28 | Not started | 通过 | Estrella 2026-10-20 | `dispatch-clinic-letter` 与 `notify-referrer` 两个作业 |
| E-035 | — | Ender | 主笔（C 组工作器与数据库说明） | ART | `Ender/2026-09-28/C_外部工作器与数据库说明.md`；提交 `4a09173` | 2026-09-28 | — | 通过 | Estrella 2026-10-20 | 与 D 组说明同一模板 |
| E-036 | — | Ender | 主笔（AISD-3 设计决策） | ART | `submissions/AISD/AISD-3_Justification_of_Decisions.md`；`submissions/AISD/Group_Design_Decisions_2026-09-29.pdf`；提交 `e0a8cb0` | 2026-09-29 | — | 通过 | Estrella 2026-10-20 | 英文版提交（`6278748` 切换了版本） |
| E-037 | — | Ender | 主笔（贡献矩阵） | ART | `submissions/BPMEA/contribution matrix.docx`；提交 `6278748` | 2026-09-29 | — | 通过 | Estrella 2026-10-20 | 30/24/24/22 的比例是自报，不能由提交记录或文件量推出；矩阵只按 worker 类别切分，未覆盖建模、测试与记录工作；矩阵把团队验收计划的牵头记在 A（Ruby）名下，与待办把 `PB-14`、`PB-18` 一责记为 Ryan 不一致（见第五节第 10 条） |
| E-038 | PB-16 | Ender | 参与（一责 Estrella，二责 Ryan） | ART | `Week6 Coursework/istar/PB-16_V1_Finance_SR_reviewed_2026-10-13.txt`；`Ender/2026-10-17/PB-16_V1_Finance_SR_reviewed.png`；提交 `e098d2c` | 2026-10-17 | Done | 通过 | Estrella 2026-10-20 | Finance 一视图的模型与图 |
| E-039 | — | Ender | 主笔（W02 Clinic Letter 模型） | ART | `Ender/2026-09-25/W02_Clinic_Letter.bpmn`；提交 `dcba26d` | 2026-09-25 | — | 通过 | Estrella 2026-10-20 | 第 2 周练习模型 |
| E-040 | — | Ender | 复核（本表） | ART | `Est/est：PB-17贡献记录表.md` 第九节 | 2026-10-20 | — | 通过 | Ender 2026-10-20 | 分工表把贡献记录的二责给 Ender；2026-10-20 落签，复核意见见第九节 |
| E-041 | — | Ryan | 主笔（Part 5） | ART | `Ryan/2026-09-15/Ryan：part5依赖映射.md` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 文件在本人文件夹；仓库内引入该文件的是 Ruby 的 `fb3e7b3`，没有被记在 Ryan 名下的提交 |
| E-042 | — | Ryan | 主笔（Part 7） | ART | `Ryan/2026-09-15/Ryan：part7 standup.md`；`Ryan/2026-09-15/Ryan：part7 standup汇总.md`；提交 `1b4577a` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 模板与汇总格式；两次正式站会记录另在 `Week6 Coursework/process/`（见第八节第 7 项） |
| E-043 | — | Ryan | 参与（Part 1 分工题） | ART | `Ryan/2026-09-15/Ryan：part1外部系统.md`；`Ryan/2026-09-15/Ryan：part1异常路径.md`；提交 `1b4577a` | 2026-09-15 | — | 通过 | Estrella 2026-10-20 | 分工表把这两题记为他起草 |
| E-044 | PB-14 | Ryan | 第一负责人 | ART | `Ryan/2026-09-26/PB-14_acceptance-test-plan_2026-09-29.md` | 2026-09-29 | In progress | 通过 | Estrella 2026-10-20 | 文件署他为一责且可打开；该文件的两笔提交（`43b3f22`、`151a86d`）均为 Estrella，作者身份不能由仓库证明 |
| E-045 | PB-14 | Ryan | 第一负责人 | LOG | `Ryan/2026-09-26/PB-14_acceptance-run-log_2026-09-29.json`；`Ryan/2026-09-26/PB-14_执行记录_20260929-004206.json` | 2026-09-29 | In progress | 通过 | Estrella 2026-10-20 | 两份同为 2512 字节、同一 run id，是同一份日志的两个名字；提交为 `43b3f22` |
| E-046 | PB-18 | Ryan | 第一负责人 | ART | `Ryan/2026-09-26/PB-18_acceptance-test-plan_2026-09-29.md` | 2026-09-29 | In progress | 通过 | Estrella 2026-10-20 | 文件署他为一责且可打开；该文件的两笔提交（`246f0cc`、`151a86d`）均为 Estrella，作者身份不能由仓库证明；`AT-03` FAIL 与处理建议写在案 |
| E-047 | PB-18 | Ryan | 第一负责人 | LOG | `Ryan/2026-09-26/PB-18_acceptance-run-log_2026-09-29.json` | 2026-09-29 | In progress | 通过 | Estrella 2026-10-20 | 四个例外路径的实际结果 |
| E-048 | — | Ryan | 主笔（D 组工作器与数据库说明） | ART | `Ryan/2026-09-28/D_外部工作器与数据库说明.md`；`docs/superpowers/plans/2026-09-28-member-d-notifications.md`；提交 `0695a4a`、`9cd42b2` | 2026-09-28 | — | 通过 | Estrella 2026-10-20 | `PB-21` 的实现边界写在这里 |
| E-049 | PB-21 | Ryan | 第一负责人 | CMT | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/CareChangeWorkers.java`、`domain/AuditEvent.java`；提交 `0695a4a`、`9cd42b2` | 2026-09-28 | In progress | 通过 | Estrella 2026-10-20 | 只做了护理变更通知；改期、停治的正式申请未实现。`9cd42b2` 当日曾加入 `evidence/PB-21_member-D_simple_2026-09-28/` 六件运行证据，同日被 `57d0b36` 删除，现仓库内已无运行证据（见第五节第 9 条） |
| E-050 | PB-16 | Ryan | 第二负责人 | ART | `Week6 Coursework/istar/V1_SD_diagram.txt`、`V1_SD_diagram.png`；`Ryan/2026-10-15/PB-16_V1_SD_reviewed_2026-10-13.png`；提交 `c8b371e`、`5398f2c`、`13abe30` | 2026-10-15 至 2026-10-16 | Done | 通过 | Estrella 2026-10-20 | SD 模型改版由他做；二责复核已于 2026-10-20 落签，改与签仍是两件事 |
| E-051 | PB-11 | Ryan | 第一负责人 | CMT | `Week3 Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/domain/AuditEvent.java`、`AuditEventWriter.java`、`AuditEventRepository.java`；提交 `0695a4a` | 2026-09-28 | Not started | 通过 | Estrella 2026-10-20 | 三份审计实现文件在，提交 `0695a4a` 在；「普通用户改不动审计记录」仍没有验证，待办要的拒绝截图不存在 |
| E-052 | — | Ryan | 参与（W02 Referral 模型） | ART | `Ryan/2026-09-21/W02_Referral.bpmn`；提交 `396b6ad` | 2026-09-21 | — | 通过 | Estrella 2026-10-20 | 转诊协作模型，第 2 周练习 |
| E-053 | PB-31 | Ryan | 第一负责人 | — | 仓库内没有他名下与 `PB-31` 相关的提交或文件；实跑记录记在 Estrella 名下（见 E-020） | — | Done | 缺件 | Estrella 2026-10-20 | 仓库内没有他名下与 `PB-31` 相关的提交或文件；实跑记录记在 Estrella 名下（见 E-020）；待办把 `PB-31` 记为 Done、一责为他 |

**这 53 行按人分段**：E-001 至 E-013 属 Ruby，E-014 至 E-031 属 Estrella，E-032 至 E-040 属 Ender，E-041 至 E-053 属 Ryan。同一件产物由多人经手时分行登记，各自写明做了什么，不把两人并列为唯一作者。行数不等于工作量：Ender 的 9 行里有 7 行是 9 月的课程材料（E-032 至 E-037、E-039），1 行是 10 月的 i* 图（E-038），另 1 行是「无证据」的复核登记（E-040）。

**字段说明**

| 列 | 填写要求 |
|----|----------|
| 证据编号 | 形如 `E-001`，顺序编，便于口头引用 |
| 条目编号 | `PB-xx`；有任务卡时并列写出，如 `PB-01 / T01` |
| 姓名 | 用第二节的「统一用名」 |
| 条目内角色 | 第一负责人 / 第二负责人 / 参与 |
| 证据类型 | 用第三节的代号 |
| 证据位置 | 仓库内可打开的路径或链接 |
| 证据日期 | 证据产生日期，非录入日期 |
| 条目当前状态 | 抄产品待办，录入时抄一次 |
| 核对结果 | 通过 / 缺件 / 待补 / 待核 |
| 核对人与日期 | 由 Estrella 核对，Ender 复核 |

---

## 五、视图 B · 条目覆盖检查表

负责人与优先级取自 `docs/p3-product-backlog.md`；状态栏按该文件 2026-10-20 晚重读后的值逐条复制，模板里 9 月 16 日的旧值不再使用，两处不再各记一套。状态栏回答「条目交付到哪一步」，可否认定完成回答「这位成员的证据能不能承担这一条」，两栏不互相推断。`PB-30`、`PB-31`、`PB-34`、`PB-39` 是第二版新增条目，模板里没有，本轮补入；`PB-15`、`PB-17`、`PB-29` 已于 2026-10-16 撤出，行位保留并改记落点，不删行。右侧五列按本轮核对结果填写。

| 条目编号 | 优先级 | 第一负责人 | 第二负责人 | 条目当前状态 | 已有证据条数 | 证据是否均可打开 | 负责人是否一致 | 可否认定完成 | 备注 |
|----------|--------|------------|------------|--------------|--------------|------------------|----------------|--------------|------|
| PB-01 | P0 | Ruby | Estrella | In progress | 1 | 是（路径可开，但不是待办要的权限表） | 是 | 不可认定完成 | 只有摘要第 11、25 行的文字规则（E-010）；`docs/p4-work-breakdown.md` 的 T01 记 Done，与此冲突，本轮仍不认定 |
| PB-02 | P0 | Ruby | Ryan | Done | 0 | —（无直接证据） | — | 部分 | 19 日 `AT-02` 走通拒绝路径并留存决策与理由（E-020）；条目证据栏要的决策表单截图没有 |
| PB-03 | P0 | Ruby | Ender | Done | 0 | —（无直接证据） | — | 部分 | `AT-04`（无可用档期）通过、G07 在接诊后完成 `BookVisit`（E-020）；证据栏要的「预订模型截图＋无档期记录」未单独出件 |
| PB-04 | P0 | Estrella | Ruby | In progress | 0 | — | — | 不可认定完成 | 10 天／14 天的通知规则没有实现，也没有对应测试 |
| PB-05 | P0 | Ruby | Estrella | In progress | 0 | — | — | 不可认定完成 | 有 `Week6 Coursework/forms/urgent_authorisation.form`，没有授权门禁的验证 |
| PB-06 | P0 | Ender | Ryan | In progress | 0 | — | — | 不可认定完成 | 外部服务不可用的模拟日志与重复预订验证都没有 |
| PB-07 | P0 | Ender | Estrella | Done | 0 | —（无直接证据） | — | 部分 | `AT-05`（付款失败后重试）、`AT-06`（缺确认）通过，G07 付款成功（E-020）；证据栏要的模拟收据与测试结果没有单独出件，状态仍记 Not started |
| PB-08 | P1 | Ryan | Ruby | In progress | 0 | — | — | 不可认定完成 | 例外路径说明不在仓库 |
| PB-09 | P1 | Estrella | Ryan | In progress | 1 | 是 | 否 | 部分 | `LetterWorkers` 实现分发（E-034），G07 记 `letterStatus=sent`；但实现记在 Ender 名下，一责 Estrella 无对应提交（第五节第 5 条）；批准门禁与 7 天升级没有测过 |
| PB-10 | P1 | Estrella | Ender | In progress | 0 | — | — | 不可认定完成 | 分流表单没有截图，路由规则未测 |
| PB-11 | P0 | Ryan | Ruby | In progress | 1 | 是 | 是 | 部分 | 审计写入在（E-051）；不可篡改与拒绝访问的截图没有 |
| PB-12 | P0 | Ruby | Estrella | Done | 2 | 是 | 是 | 可认定完成 | 模型、抽象说明、二责签字三件齐（E-005、E-021） |
| PB-13 | P1 | Estrella | Ruby | Done | 2 | 是 | 是 | 部分 | 12 份表单在且被 19 日实跑用上（E-009、E-022）；必填校验没有截图；待办状态与实物不一致 |
| PB-14 | P1 | Ryan | Ender | Done | 2 | 是 | 是（署名一致，提交均非本人） | 部分 | 29 日两案 PASS（E-044、E-045），19 日复跑在 E-020；二责 Ender 无签字 |
| PB-18 | P1 | Ryan | Ender | Done | 2 | 是 | 是（署名一致，提交均非本人） | 部分 | `AT-03` FAIL 如实记录，`AT-04` 至 `AT-06` PASS（E-046、E-047） |
| PB-15 | P0 | Ruby | Estrella | 已撤出（2026-10-16） | 0 | — | 不适用 | 不适用 | 撤出后由 `Week6 Coursework/process/part7-standup-records.md` 与 `part8-sprint-review-records.md` 承载 |
| PB-16 | P0 | Estrella | Ryan | Done | 4 | 是 | 是 | 可认定完成（附一处过程缺口） | 模型与四张图齐（E-015、E-016、E-038、E-050）；二责复核已于 2026-10-20 落签，但五项清单的第 2 项按缺口未勾（八条依赖不在 piStar 源内）；Admin 图未按改正后的源重出 |
| PB-17 | P0 | Estrella | Ender | 已撤出（2026-10-16） | 1 | 是 | 是 | 不适用 | 落点即本表（E-031）；待办 Note 9 指到 `Est/est：PB-17贡献记录表.md` |
| — | — | — | — | In progress（重复行） | 0 | — | — | — | 模板录入时 `PB-18` 出现两次；上一条为准，此行不另计证据，保留以说明模板问题 |
| PB-19 | P1 | Ender | Ryan | In progress | 0 | — | — | 不可认定完成 | 正式的变更申请未实现 |
| PB-20 | P1 | Ender | Estrella | In progress | 0 | — | — | 不可认定完成 | 退款只做了 `RefundWorkers`（E-011）；退款权限与关联查询没有 |
| PB-21 | P1 | Ryan | Ender | In progress | 1 | 是 | 是 | 部分 | 只实现护理变更通知（E-049）；无档期告警与非到诊三选一未实现 |
| PB-22 | P0 | Ruby | Estrella | Not started | 0 | — | — | 不可认定完成 | `AT-03` 的失败正是本条未交付的直接证据（E-020）；`Est/est：part3产品待办.md` 曾指 `Ruby/2026-09-22/PB-20_角色权限矩阵.md`，该文件在仓库里不存在 |
| PB-23 | P2 | Ryan | Ruby | Not started | 0 | — | — | 不可认定完成 | 无产物 |
| PB-24 | P2 | Ryan | Ender | Not started | 0 | — | — | 不可认定完成 | 无产物 |
| PB-25 | P2 | Ryan | Ruby | Not started | 0 | — | — | 不可认定完成 | 无产物 |
| PB-26 | P2 | Estrella | Ender | In progress | 0 | — | — | 不可认定完成 | 十项报表一项未出 |
| PB-27 | P2 | Estrella | Ryan | Not started | 0 | — | — | 不可认定完成 | 无产物 |
| PB-28 | P0 | Ruby | Ryan | Done | 1 | 是 | 否 | 可认定完成 | 42 条与第 4 节齐（E-018）；一责 Ruby、二责 Ryan，文件各笔提交都在 Estrella 名下，而她不在负责人栏 |
| PB-29 | P0 | Ender | Estrella | 已撤出（2026-10-16） | 0 | — | 不适用 | 不适用 | 落点 `docs/definition-of-done.md`；四人已于 2026-10-20 签署，31 项中 28 项勾选、3 项未勾并写明理由 |
| PB-30 | P0（第二版） | Ruby | Ender | Done | 4 | 是 | 否 | 部分 | 模型、补入的汇合网关、两份可读 PDF 都在（E-006 至 E-008、E-028），验收条件「有可读导出」已满足；但多数模型改动与两份导出记在 Estrella 名下，她不在负责人栏；待办证据栏仍写「可读 PDF 待出」 |
| PB-31 | P0（第二版） | Ryan | Ruby | Done | 1 | 是（记录本身可开） | 否 | 部分 | 实跑与 19 项单测记录完整（E-020）；一责 Ryan 名下无任何相关提交，E-053 就是这条空登记；第 2 部分书面评估的 `PB-31` 签认已于 2026-10-20 登记；一责名下无产物这一点不因签认而消失 |
| PB-34 | P0（第二版） | Estrella | Ryan | Done | 1 | 是 | 是 | 可认定完成 | 变更说明逐件给出文件与提交（E-017） |
| PB-39 | P0（第二版） | Estrella | Ryan | Done | 1 | 是 | 是 | 可认定完成 | 第 4 节给出 13／25／4 与每条未动的原因（E-019） |

**首轮已知反例（须如实标出，不要掩盖）**

任务拆分 `docs/p4-work-breakdown.md` 的 **T01** 状态标 `Done`，但证据列只写「Part 1 摘要中的权限规则」，没有可打开的路径。按完成定义与 PB-17 的验收条件，此项**不可认定完成**。处理方式二选一，在备注写明：

- 由 Ruby 补齐权限表路径与截图后重新认定；或
- 状态改回 `In progress`，待补齐后再标完成。

**本轮结果（2026-10-20）**：两条路都没走。`Ruby/2026-09-14/ruby：part1案例摘要.md` 里仍只有文字规则，没有权限表，也没有核验界面截图；`PB-01` 在待办里记 `In progress`，`T01` 仍记 `Done`。本表按验收条件判为**不可认定完成**（视图 B 的 `PB-01` 行、视图 A 的 E-010），不改 `docs/p4-work-breakdown.md`。

**本轮核对发现的其他口径不一致（只登记，不改原件）**

1. **`PB-30` 已于 2026-10-20 收口。** 证据栏原写「可读 PDF 导出仍需产出」，而 `submissions/BPMEA/` 下两份早在（16 页运营、8 页战略，2026-10-19）；本轮把状态改为 `Done` 并登记二责复核，这条不再成立，留在此处只记改前的样子。
2. **`PB-13` 已于 2026-10-20 收口。** 12 份表单在 `Week6 Coursework/forms/`，被 19 日实跑用上；状态由 `Not started` 改为 `Done` 并登记二责复核。仍缺的是必填校验的浏览器截图：约束已定义并绑定，但 19 日的驱动走 REST 直发，没有证明表单拦下过空值。
3. **`PB-31` 记 `Done`，但一责名下没有一笔相关提交。** 实跑与日志全部记在 Estrella 名下（`41d2f10`）。签认已于 2026-10-20 补登记，与状态不再错位；但该条的验收条件之一是「记下结果由其产出」，而仓库仍证明不了 Ryan 写过其中任何一件。
4. **`PB-16` 记 `Done`，五项清单的第 2 项仍未勾。** 二责已于 2026-10-20 落签，签认不再缺失；未勾的是第 2 项——`D3, D11, D13, D19, D21, D22, D23, D24` 这八条不在 piStar 源里。本表把它记为「可认定完成（附一处过程缺口）」，不替它抹平。
5. **负责人栏与产出的落点不一致的条目有六条。** `PB-09`（Estrella／Ryan，实现 `a0ac6cb` 记在 Ender 名下）、`PB-14`、`PB-18`（一责 Ryan、二责 Ender）、`PB-28`（Ruby／Ryan）、`PB-30`（Ruby／Ender）、`PB-31`（Ryan／Ruby）：能打开的产物或提交记在负责人栏之外的人名下，负责人本人名下没有对应提交。其中三条落在 Estrella 名下，而她在 `PB-28`、`PB-30`、`PB-31` 三条的负责人栏里一个都不是。视图 B 的「负责人是否一致」按条目逐条填，上列六条填「否」；`PB-16` 虽由 Ender 补了 Finance 一图，但一责 Estrella 与二责 Ryan 各自有件，仍填「是」。
6. **归档草稿里有一处死链。** `Est/est：part3产品待办.md` 的 `PB-20`（现 `PB-22`）行把证据写成 `Ruby/2026-09-22/PB-20_角色权限矩阵.md`；该文件在仓库里不存在，`Ruby/2026-09-22/` 下只有紧急治疗模型。草稿已归档，但它把「角色权限矩阵」说成有件，容易被当成 `PB-22` 的证据。
7. **模板自身有两处问题，已按原样保留并标注。** `PB-18` 在视图 B 出现两次；`PB-15`、`PB-17`、`PB-29` 三行仍以在办状态列出，而它们 2026-10-16 已撤出。
8. **`submission-2026-10-20` 标签比 `main` 尖端早一笔。** 尖端那一笔是 2026-10-20 生成反馈记录 PDF 的提交，只增文档；按根 `README.md` 的说法这是允许的，但读标签的人看到的不是树尖。记在此处备查，不改标签。
9. **`PB-21` 的运行证据曾被加入，同日被同一人删除。** `9cd42b2`（2026-09-28）在仓库根建了 `evidence/PB-21_member-D_simple_2026-09-28/`，含 `README.md`、`bpmn-tests.txt`、`java-tests.txt`、`database-rows.txt`、`runtime-log.txt`、`runtime.json` 六件；`57d0b36`「remove uploaded execution evidence」把这些文件连同 `evidence/` 目录一起删掉，现仓库内查无此目录。因此 `PB-21` 只剩实现，没有可打开的运行证据；这也是第六节第 1 条「在根目录建 `evidence/PB-xx/`」的一次实际尝试，试过又撤回。
10. **验收计划的一责，两份记录各说各话。** 产品待办把 `PB-14`、`PB-18` 的第一负责人记为 Ryan；`submissions/BPMEA/contribution matrix.docx` 在 A（Ruby）的「Key deliverables」里写「led the team acceptance test plan (S1–S10)」；而实际文件 `Ryan/2026-09-26/PB-14_acceptance-test-plan_2026-09-29.md`、`PB-18_acceptance-test-plan_2026-09-29.md` 放在 Ryan 文件夹、两笔提交都在 Estrella 名下。三份记录指向三个人，本表按产品待办记 Ryan 为一责（E-044 至 E-047），并把这处不一致留在明面上。
11. **本表在计划里的状态已过期。** `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md` 的 Part B 把「Contribution record」一行记为 `Not started`；本表已填完，但那行没有回改，也不该由本表代改。读计划的人应以本表为准，计划行留给下一轮更新。

---

## 六、待全组确认项（过会拍板后回写）

| # | 事项 | 建议 | 状态 |
|---|------|------|------|
| 1 | 存放位置 | 仓库根目录新建 `evidence/PB-xx/`，个人日期文件夹只放工作草稿 | 已确认（2026-10-20 全组）：采用本建议，个人日期文件夹继续留作草稿 |
| 2 | 人名统一 | 统一用仓库文件夹名，按第二节对照表 | 已确认（2026-10-20 全组）：统一用 Ruby／Estrella／Ender／Ryan |
| 3 | 表头列数 | 采用视图 A 的 11 列，或删减到已约定的 5 列加最少增补 | 已确认（2026-10-20 全组）：采用视图 A 的 11 列 |
| 4 | 视图 B 维护人 | Estrella 汇总，Ender 复核 | 已确认（Ender 2026-10-20 复核，见第九节） |
| 5 | Ruby 的提交身份 | 现有两个身份，其中一个为 Gitee 邮箱；建议此后改用 GitHub 账号邮箱，历史提交不改写、如实说明 | 已确认（2026-10-20 全组）：此后改用 GitHub 邮箱，历史提交不改写，如实说明 |

---

## 七、相邻记录

| 记录 | 说明 |
|------|------|
| 标记站会个人记录 | 每人一份，作为 `MTG` 类证据登记；两次站会共 10% 为个人分，必须逐人留档 |
| 反馈行动记录 | 考核规范 Section 6 要求留存，字段为提出点、回应、第一与第二负责人、完成证据；另表同模板，初稿可用 Part 8 评审准备里的 F01 至 F06 反馈表 |
| 版本快照 | 每次冲刺评审一个 git tag，作为该次评审的增量快照 |

---

## 八、完成自检

- [x] 四个人都有证据，不存在一人多、一人空 —— **成立，但「一人多」确实存在，如实照录**：`main` 上 Estrella 113 笔、Ruby 62 笔、Ryan 15 笔、Ender 8 笔（合计 198 笔）。四人都有可打开的产物（E-001 至 E-052 逐行给出路径），没有一人为空；E-040、E-053 两行如实写「无证据」，登记的是缺什么，不替任何人补一件。Ender 的 8 笔里有 7 笔是产物或文档、1 笔是改名，视图 A 只登记得出 9 行。
- [x] 每个位置都真实可打开，没有占位内容 —— **成立**：视图 A 与视图 B 引用的路径与文件名于 2026-10-20 逐一核过，按原路径测过的一律存在；少数只写文件名的地方，所在目录由同一行给出，也已核到。没有「见上文」「截图」这类占位写法，`E-040`、`E-053` 两行直接写「无证据」。唯一的例外是 `Ruby/2026-09-22/PB-20_角色权限矩阵.md`，它出现在第五节的死链说明里，不是证据行。
- [ ] 每行姓名与产品待办登记的负责人一致 —— **不成立**：`PB-09`、`PB-14`、`PB-18`、`PB-28`、`PB-30`、`PB-31` 六条的产物或提交落在负责人栏之外，负责人本人名下没有对应提交；视图 B 的「负责人是否一致」据实把这六条填「否」（见第五节第 5 条）。本表按「谁做了什么就记谁」登记，不把名字改回负责人栏来凑这一条。
- [x] 标完成的条目全部有可打开证据，反例如实标出 —— **成立**：待办 20 日晚重读后为 Done 的 13 条（`PB-02`、`PB-03`、`PB-07`、`PB-12`、`PB-13`、`PB-14`、`PB-16`、`PB-18`、`PB-28`、`PB-30`、`PB-31`、`PB-34`、`PB-39`）各有可开路径或已归档的验收记录，证据格见 `docs/p3-product-backlog.md`；T01 缺权限表、`AT-03` 两版同败、`PB-16` 五项清单第 2 项未认证三处反例都写在表内，没有一处被改成「完成」。本表第五节的「可否认定完成」另判一层：条目状态为 Done 不等于某位成员的证据足以承担该条。
- [ ] 提交记录类证据带条目编号，显示名与邮箱能对应到人 —— **不成立**：`main` 的 198 笔里，整条提交信息带 `PB-xx` 的 18 笔、带 `Txx` 的 1 笔；题名为 `1` 的 8 笔、`2` 的 2 笔、`更新` 的 2 笔，`Merge branch 'main'` 22 笔，长度不足 9 个字符的共 23 笔。承载 19 日实跑证据的 `41d2f10` 题名是「Execute the revised model against a live Camunda engine and record the results」，没有条目编号。显示名与邮箱在 `main` 上是四人对四人，能对应（见第二节）；但 Ruby 另有一个 Gitee 身份 `16025137+Rubyzheng@user.noreply.gitee.com`，共 17 笔，2026-09-14 至 15，全部不在 `main` 的历史上，只在旧线上可见。
- [ ] 每次评审有版本快照 —— **不成立**：SR3 有 `sr3-2026-10-14`（指向 `25f53f7`），SR4 有 `sr4-2026-10-20`（指向 `a0d8f55`，10 月 20 日定稿会那一笔）；SR1、SR2 没有，`standup-1-2026-09-16` 只能算「最接近」，`submission-2026-09-29` 是次日的发布标签，不能顶替。这一项按「每次」不成立，缺的是 SR1、SR2 两个快照。
- [ ] 站会个人记录逐人留档 —— **不成立**：`Week6 Coursework/process/part7-standup-records.md` 里 SU3 四人全记「Not recorded」，因为 10-12 当天只有两笔归档提交，没有项目提交可推。SU4 只有 Estrella 一行是当日成文；Ruby、Ryan 两行的「完成／证据」已按 10-16 当天的提交补出并逐条指名提交号，但「下一步／阻塞／需要的支持／要交接的」四栏留「—」，Ender 当天无提交只记这一事实。补出的两栏是提交事实，不是本人留档，所以这一项仍不成立。视图 A 只登记得出 E-030 一行。
- [x] 全组对表头与存放位置无异议，核对结果经 Ender 复核 —— **成立（2026-10-20）**：Ender 已于当日复核并落签，见第九节；第六节四项「待确认」（存放位置、人名统一、表头列数、Ruby 的提交身份）同日晚由全组逐项拍定，状态已回写本节上方表格；`docs/definition-of-done.md` 的四人签署同日完成。

**小结**：八项成立四项（第 1、2、4、8 项）。不成立的四项里，第 3、5 项是记录口径与提交习惯的问题，第 6、7 项缺的是别人的动作（评审快照、三人站会行），都不是本表能补出来的；第 8 项已于 2026-10-20 由全组拍定并回写。

---

## 九、二责复核记录

| 项 | 内容 |
|---|---|
| 复核人 | Minghao Qin（Ender），分工表与第一节登记的本表二责 |
| 日期 | 2026-10-20 |
| 复核对象 | 视图 A 全 53 行（`E-001` 至 `E-053`）、视图 B 条目覆盖表、第八节八项自检 |
| 结论 | 通过，附三条限定 |

**复核确认的事项**：

1. 视图 A 每一行的证据位置在仓库内可打开，抽查的分段覆盖四人：`E-001` 至 `E-013`（Ruby）、`E-014` 至 `E-031`（Estrella）、`E-032` 至 `E-040`（Ender）、`E-041` 至 `E-053`（Ryan），不存在整段无路径的行。
2. 提交分布按 `git log --format='%an <%ae>'` 复核为 Estrella 113 笔、Ruby 62 笔、Ryan 15 笔、Ender 8 笔，与第一节所记一致，本表没有做平均化处理。
3. 视图 B 的负责人栏与产品待办不一致的六条（`PB-09`、`PB-14`、`PB-18`、`PB-28`、`PB-30`、`PB-31`）已逐条对上，留「否」而不改回，符合「谁做了什么就记谁」的登记口径。
4. 第八节的五项不成立自检没有一处被改成「成立」，缺什么写在节内。

**限定**：

- 复核的是登记与证据位置，不是每一笔提交的内容是否恰当。
- 第六节仍有四项待确认（存放位置、人名统一、表头列数、Ruby 的提交身份），复核不代替这些决定。
- `E-040`、`E-053` 两行登记的是「缺什么」，本次复核未替任何人补出一件产物。

签字：Ender（Minghao Qin），2026-10-20。

### 9.2 逐行复核结论（2026-10-20）

视图 A 原有 11 行停在「待补」或「待核」。复核人逐行给出结论：10 行转「通过」，1 行转「缺件」，限定一律写回备注。转「通过」不是认可该行的全部陈述，备注里保留原判断；「通过」指的是这一行的证据位置在仓库内成立。

| 证据 | 原结论 | 现结论 | 依据 |
|---|---|---|---|
| `E-009` | 待补 | 通过 | `Week6 Coursework/forms/` 的 12 份 `.form` 在；`PB-13` 的状态已于 10 月 20 日改为 `Done` 并登记二责复核，「待办仍记 Not started」的不一致已消除 |
| `E-013` | 待补 | 缺件 | `A-1` 幻灯片的一责复核只见于个人待办的记述，仓库内没有签字件、没有对应提交，也没有可打开的复核记录 |
| `E-026` | 待补 | 通过 | 书面评估第 2 部分属 `PB-31`，而 `PB-31` 的签认已于 10 月 20 日登记，「签认尚未登记」的空缺已补 |
| `E-031` | 待核 | 通过 | 第九节 9.1 即 Ender 的落签，台账八项自检见第八节 |
| `E-037` | 待补 | 通过 | 矩阵文件与提交 `6278748` 均在；30/24/24/22 的比例仍是自报，备注照录，不改数字 |
| `E-041` | 待补 | 通过 | `Ryan/2026-09-15/Ryan：part5依赖映射.md` 在；引入它的提交记在 Ruby 名下，此点已在备注注明 |
| `E-044` | 待补 | 通过 | 计划文件在且可开；两笔提交均为 Estrella，作者身份不能由仓库证明 |
| `E-045` | 待补 | 通过 | 两份日志同为 2512 字节、同一 run id，提交 `43b3f22` 在 |
| `E-046` | 待补 | 通过 | 计划文件在且可开；两笔提交均为 Estrella，`AT-03` FAIL 如实写在案 |
| `E-047` | 待补 | 通过 | 日志在且可开，四个例外路径的结果已登记 |
| `E-051` | 待补 | 通过 | 三份审计实现文件在，提交 `0695a4a` 在；「普通用户改不动审计记录」仍没有验证 |
| `E-053` | 缺件 | 缺件 | 维持原判：`PB-31` 名下的提交或文件确实不存在。备注里「签认尚未登记」一句随 `E-026` 的复核删去，缺件的理由只剩「一责名下没有产物」这一条 |

复核后的分布：视图 A 全 53 行中「通过」50 行、「缺件」3 行（`E-010`、`E-013`、`E-053`）、「待补」0 行、「待核」0 行。三行缺件都不是登记不全，而是确无可打开的件：`E-010` 是权限表与界面截图都没有，`E-013` 是复核动作没有留下痕迹，`E-053` 是 `PB-31` 名下没有任何提交。三处按「谁做了什么就记谁」的口径照实留空，不替任何人补一件。

此次转「通过」不改变第五节视图 B 的判定。视图 B 判的是条目能否认定完成，与单行证据是否成立是两件事：`PB-13` 与 `PB-31` 都保持「部分」。`PB-13` 的验收条件是「必填字段为空时提交被拦下」，这条没有截图，12 份表单在、状态已改、二责已签都推不出该条件已满足；`PB-31` 一责名下无提交这一点，也不因签认补登记而消失。

