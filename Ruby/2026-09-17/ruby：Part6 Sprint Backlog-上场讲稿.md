# Part 6 Sprint Backlog · 上场讲稿（17 Sep）

**文件**：`docs/p6-sprint-backlog.md`  
**用法**：先扫中文，上场只说斜体英文。中文是心里过一遍的。  
**时长**：老师只看情况 → 用「90 秒版」。老师指着表问 → 用「指着表讲」。  
**今天是什么**：看我们 Sprint 1 做到哪。不是交成品，不是跑 Camunda。

---

## 这场在问什么

老师要看三件事：

1. Part 6 是不是 **Sprint Backlog**（本期承诺），不是再写一份总清单  
2. Sprint Goal 切到哪、为什么不把治疗/支付塞进来  
3. 表上的状态是不是实话：Done / In progress / Not started

*Today you are looking at our situation. This is Part 6, the Sprint 1 backlog. The increment is the plan, not a running system.*

中文：今天看情况。Part 6 是 Sprint 1 待办。增量是计划，不是能跑的系统。

---

## Part 6 是什么

作业原文：*Select tasks from the product backlog for each sprint.*

| 中文 | 开口英文 |
|------|----------|
| Part 3 是全部愿望清单 | *The product backlog is the full wish list.* |
| Part 6 是这一期真正承诺做的 | *The sprint backlog is what we promise now.* |
| 不是把 29 条都塞进这一周 | *Not everything goes in.* |
| 每张卡：双负责人、估算、验收、证据、状态 | *Each row has two owners, a time estimate, a done-check, and evidence.* |

**开口一句（表不想解释时）**

*Part 6 is our Sprint 1 to-do list. We pick tasks from the product backlog. Not everything goes in.*

中文：Part 6 是 Sprint 1 要做的小事清单。从总 Backlog 里挑出来，不是全部工作。

---

## Sprint Goal

打开表上的 Goal 行。

中文：16 Sep 交并上传 Product Backlog 和这张 Sprint 表。第一刀：核材料 → 医生决定 → 第一次门诊。外面排班可以 mock。付钱、写信、接电话不进这一期。

*Sprint 1 goal: finish and upload the product backlog and this sprint backlog. First slice: referral check → consultant decision → first clinic booking. We may mock the outside calendar. Payment, letters and phone routing stay on the product backlog.* 〔第3–5段；作业硬检查；mock 授权第30段〕

**为什么只切这一刀**

*In the case, treatment comes after the first visit.* 〔第7段〕 *We keep the sprint goal small.*

---

## 今天的真实情况

按 `docs/p6-sprint-backlog.md` 报，不要美化。

| 状态 | 任务 | 中文 | 开口英文 |
|------|------|------|----------|
| Done | T01 | 权限写清了：秘书可补件，不能接受转诊 | *T01 is done. Secretaries may request missing papers. They cannot accept a referral.* 〔第3段〕 |
| In progress | T02 | 主路径还在用文字写：收件 → 核材料 → 送医生。不画图 | *T02 is in progress. Write the main path in words. No diagram yet.* 〔第3–4段〕 |
| In progress | T20 | 两张表上传；四人在 GitHub | *T20 is in progress. Upload both tables. All members are on GitHub.* 〔作业硬检查〕 |
| Not started | T03–T07 | 已经选进这一期，但还没做。计划有了，实现没有 | *T03 to T07 are in this sprint, but not started. They are planned, not built.* |
| 故意不进本期 | 治疗、支付、信件、咨询 | 案例里它们在第一次门诊之后 | *Treatment, payment, letters and phone routing stay on the product backlog.* 〔第7段以后〕 |

**开口一句（老师问 where are you now）**

*We are on track for the plan. T01 is done. T02 and T20 are still open. T03 to T07 are selected, but not started, because this increment is the plan. We are not late on diagrams. Diagrams were never in this sprint goal.*

中文：计划这条线是齐的。T01 完成。T02、T20 还在收尾。T03–T07 进了 sprint，但没开工，因为今天的增量就是计划。图和代码本来就不在 Goal 里，所以不是逾期。

---

## 90 秒版（今天主用）

斜体英文直接说。每段先看中文。

### 开场（20 秒）

中文：这是 Part 6。Sprint 1 待办。不是整张项目表。今天看情况，只交计划。

*This is Part 6, our Sprint 1 backlog. It is not the whole project. We pulled tasks from the product backlog. We only promise a small slice. Today you are looking at our situation. We show the plan, not a running system.*

### Goal（20 秒）

中文：第一刀只到第一次门诊。排班可假。付钱、信、电话留下期。

*Sprint goal: finish and upload the product backlog and this sprint backlog. First slice: referral check, then consultant decision, then the first clinic booking. We may mock the outside calendar. Payment, letters and phone routing stay on the product backlog.*

### 进度（35 秒）

中文：按状态讲。Done / 进行中 / 还没开始。没证据不报完。

*Current status. T01 is done: secretaries may request missing papers, but they cannot accept a referral. Evidence is the permission rule in Part 1. T02 is in progress: the main path in words, receive, check papers, send to the doctor. T20 is in progress: both tables are in the repo, all members are on GitHub. T03 to T07 are in this sprint, but not started yet. They are planned, not built. No diagram, no Camunda, no code today.*

### 收尾（15 秒）

中文：所以今天看的是计划增量。图和代码 28 Sep。

*So today you are looking at our plan increment. Diagrams and code come later, on 28 September.*

---

## 指着表讲（老师一看表就停在这里）

按**状态**讲，不要从 T01 念到 T20。

### Goal 行

*This sprint only covers check papers, doctor yes or no, and the first booking.* 〔第3–5段〕

### Done

*T01 is done. Evidence is the permission rule in Part 1. Secretaries check papers. Only a consultant can accept.* 〔第3段〕

### In progress

*T02: we are writing the main path. No BPMN yet, because this increment is documents only.* 〔第3–4段；作业：16 Sep 不画图〕

*T20: upload the product backlog and this table. Four members on GitHub. Plan only.* 〔作业硬检查〕

### Not started，但已经进这一期

*T03: four doctor outcomes. Cannot continue without reason and who decided.* 〔第4段〕  
*T04: if rejected, do not book the first visit.* 〔第4段〕  
*T05: admin cannot book before accept.* 〔第4段门禁〕  
*T06: confirm a slot, or keep pending if no slot. Mock is OK. Do not book outside the doctor’s time.* 〔第5–6段〕  
*T07: letter as normal; phone if within two weeks; log every call.* 〔第5–6段〕

### 一句收住

*Each row has two owners, a time estimate, a done-check, and evidence. We do not mark T03 done, because there is no form yet.*

*So this sprint is only T01 to T07, plus T20. Diagrams and code come later, on 28 September.*

---

## 30 秒版（老师只让讲一句）

*Part 6 is our Sprint 1 list. We only do referral check, doctor decision, and first booking. T01 is done. The rest is planned. Today you see the plan, not the system.*

中文：Part 6 是 Sprint 1 清单。只做核材料、医生决定、第一次预约。T01 完成。其余是计划。今天看计划，不是系统。

---

## 被追问

**Product Backlog 和 Sprint Backlog 有什么区别？**  
*The product backlog is the full wish list. The sprint backlog is what we promise now.* 〔作业 Part 3 vs Part 6〕

**为什么治疗不做？**  
*In the case, treatment comes after the first visit. We keep the sprint goal small.* 〔第7段〕

**为什么很多是 Not started？算不算没干活？**  
*Not started means not built. The tasks are already chosen and owned. Today we show the plan, not the software.*

**Increment 在哪？**  
*Today the increment is one plan: same IDs in Part 3, 4 and 6, one sprint slice, one GitHub repo. Not a running process yet.*

**谁负责？你卡住了怎么办？**  
*I am first owner for T01, T02, T03, T05 and T20. Second owner can take over if I am stuck.*

**排班是假的，算不算糊弄？**  
*We may mock the calendar, but we keep the failure rule: no suitable slot stays pending. We do not book outside the doctor’s time.* 〔第5–6段；第30段允许假设〕

**Done 怎么判定？**  
*Done needs evidence. A draft is not done. T01 has a permission rule, so it is done. T03 has no form, so it is not done.*

**紧急咨询怎么处理？**  
*The hospital has not fully defined urgency. We ask you. We do not invent a rule.* 〔第18、30段〕

老师给新意见时接一句：  
*We will record the feedback with a decision, owner and backlog change. We will not grow the sprint goal on the spot.*

---

## 八张卡对照（自己过一遍，不必全念）

| Task ID | 中文 | 开口英文 | 案例 | 状态 |
|---------|------|----------|------|------|
| Goal | 第一刀：核材料 → 医生决定 → 第一次门诊；排班可 mock | *First slice: check papers → doctor decision → first booking. Mock calendar is OK.* | 第3–5段；mock 第30段 | 口述 |
| T01 | 秘书可补件，不可接受 | *Secretaries check papers. They cannot accept a referral.* | 第3段 | Done |
| T02 | 收件 → 核材料 → 送医生 | *Receive → check papers → send to the doctor. No diagram yet.* | 第3–4段 | In progress |
| T03 | 医生四态；原因和操作人必填 | *Accept, reject, ask for more papers, or send to another service. Record why and who.* | 第4段 | Not started |
| T04 | 拒绝后不约新患 | *If rejected, do not book the first visit.* | 第4段 | Not started |
| T05 | 接受后才能约第一次门诊 | *Book the first visit only after the doctor accepts.* | 第4段 | Not started |
| T06 | 有号确认；无号 pending；不约窗外；可 mock | *Find a slot, or keep pending. Do not book outside the doctor’s time. Mock is OK.* | 第5–6段 | Not started |
| T07 | 常规信；两周内再电话；每次都记 | *Letter as normal. Phone if within two weeks. Log every call.* | 第5–6段 | Not started |
| T20 | 上传 PB + Sprint 表；四人在 GitHub | *Upload both tables. All four members are on GitHub. Plan only.* | 作业硬检查 | In progress |

---

## 现场别说的

- 不要说已经测过支付、已经跑过流程、已经画好 BPMN。  
- 不要把 T03–T07 说成 Done。规则在第 4–6 段，实现还没有。  
- 不要把 Part 3 的 29 条都说成这一期要做完。  
- 不要编「怎样算紧急」的医院政策。原文第 18 段写明还没定。  
- 证据说 GitHub 和作业表格，不要报自己电脑上的文件夹路径。  
- 老师给新意见，记下来再改 backlog，不要当场把范围偷偷加大。  
- 指段落时说 *paragraph 3 of the case study*，不要说 Word 批注文件名。

---

## 和作业其他部分的关系

| 部分 | 它是什么 | 今天怎么提一句 |
|------|----------|----------------|
| Part 3 | 全部工作 | *Part 3 is the full wish list. Part 6 is what we do now.* |
| Part 4 | 任务拆分，编号与 Part 6 相同 | *Same IDs as Part 4. T01 here is T01 there.* |
| Part 7 | Standup：完成 / 下一步 / 阻塞 | 老师若改问个人进度，用 90 秒版里的状态三句 |
| Part 8 | Sprint Review：已完成 / 未完成 / 决策 | 今天不是完整 Review。被问 increment 再用 Part 8 那句 |

现场打开的文件：`docs/p6-sprint-backlog.md`。你主笔 Part 6，这张表就是证据。
