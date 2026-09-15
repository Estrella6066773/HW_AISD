# ruby：Part 6 理解笔记（双语）

## Workshop 原文与翻译

来源：`W01/Agile Workshop.docx` → **Part 6: Create Sprint Backlogs**

**原文**

> Part 6: Create Sprint Backlogs
>
> Select tasks from the product backlog for each sprint.

**翻译**

> 第 6 部分：创建 Sprint Backlog（冲刺待办清单）
>
> 从产品待办清单（Product Backlog）里，为每一个 sprint 选出要做的任务。

题目就这两句。意思是：Part 3 是全部工作；Part 6 不是再写一份总清单，而是**按 sprint 往外拉**已经拆好的任务。表格表头也是作业要求，必须按这个填：

| 原文表头 | 翻译 | 这一格填什么 |
|----------|------|----------------|
| Sprint | 第几个冲刺 | 例如 Sprint 1 |
| Task ID | 任务编号 | 与 Part 4 一致，如 T01 |
| Task Description | 任务说明 | 这张卡具体做什么 |
| First Owner | 第一负责人 | 主做的人 |
| Second Owner | 第二负责人 | 复核、顶上的人 |
| Estimate | 估算 | 第一负责人大约几小时 |
| Acceptance Conditions | 验收条件 | 怎样算做完、怎样算过关 |
| Evidence | 证据 | 拿什么证明做完了（文件、截图、仓库） |
| Status | 状态 | Done / In progress / Not started |

原文没有单独写 Sprint Goal。我们表上仍要写 Goal，是为了把「这一期只做哪一段」说清楚，避免把 Part 3 整张表都塞进来。

---

明天讲：这是 **Sprint 1 要做哪些小事的清单**。从总 Backlog 里挑出来，不是全部工作。

*Part 6 is the Sprint 1 to-do list. We pick some items from the big Product Backlog. Not everything goes in.*

16 Sep 只交这张表并上传。不画图，不写代码。

*On 16 Sep we show this plan and upload it. No diagrams. No code.*

Sprint 1 只做这一段：秘书收材料 → 医生决定收不收 → 约第一次门诊（外面排班可以先假的）。付钱、写信、接电话不进这一期。

*Sprint 1 only covers: check papers → doctor yes/no → book the first visit (fake calendar is OK). Payment, letters and phone routing wait for later.*

---

## 这张表要你学会什么

1. **Sprint ≠ 全部项目**  
   一个 sprint 是一小段时间里承诺能完成的工作。  
   *A sprint is a short time box. We only promise a small slice.*

2. **从 Backlog 里“拉”任务**  
   Part 3 是全部愿望清单。Part 6 是本期真正做的。  
   *Part 3 is the full wish list. Part 6 is what we do now.*

3. **每条都要能检查**  
   谁做、谁备岗、大概几小时、怎样算过关、拿什么当证据。  
   *Each row needs owner, backup, time, how we know it is done, and evidence.*

4. **Goal 不能贪**  
   做不完就下一期再拉，不要临时加支付、写信。  
   *Do not grow the goal. Unfinished work goes to the next sprint.*

---

## 逐条：要做什么 / 你怎么讲

**T01 — 谁能点什么（已完成）**  
写出：秘书只能查材料、要缺件；不能点“接受转诊”。  
*Write who can do what. Secretaries check papers only. They cannot accept a referral.*  
要学会：岗位权限。讲的时候说 *secretaries check papers, doctors decide*。

**T02 — 转诊主路怎么走**  
用文字写清：收件 → 核材料 → 送给医生。先不用画 BPMN。  
*Write the main path in words: receive → check papers → send to the doctor. No diagram yet.*  
要学会：先写清步骤，再以后画图。

**T03 — 医生四个选择**  
接受、拒绝、再要材料、转到别的专科。必须记下原因和是谁定的。  
*Doctor can accept, reject, ask for more papers, or send to another service. Always record why and who.*  
要学会：临床决策要留痕。

**T04 — 拒绝以后怎么办**  
拒绝或转走之后，不能再约第一次门诊。  
*If rejected, do not book the first clinic visit.*  
要学会：异常路径，不只会写顺利的那条。

**T05 — 约号的门禁**  
只有医生接受后，才能生成第一次门诊预约（专科、急不急、时间段、患者需求）。  
*Book the first visit only after the doctor accepts.*  
要学会：系统里要有“门”，不是靠人记住。

**T06 — 外面帮我们排班**  
用医院外面的日历找号。有号就确认；没号就挂起并告诉路径组。不能偷偷约到医生要的时间外面。本期可以先假装这个日历（mock）。  
*An outside calendar finds slots. If none, keep pending and tell the pathway team. Do not book outside the doctor’s time. We may fake this service for now.*  
要学会：外部依赖、失败时怎么停、什么是 mock。

**T07 — 怎么通知病人**  
一般写信。如果两周内就要来，还要打电话，每次打了都要记结果。  
*Usually send a letter. If the visit is within two weeks, also phone, and log each try.*  
要学会：通知也是规则，不是“发一下就完了”。

**T20 — 明天 Standup 要亮出来的**  
总 Backlog 和这张 Sprint 表已经在 GitHub；四个人都进了仓库。说明我们交的是计划。  
*Upload the Product Backlog and this Sprint Backlog. All four members are on GitHub. We present the plan only.*  
要学会：Standup 要有证据（文件在仓库里），不是口头说做了。

---

## 明天口头 4 句

1. *Part 6 is our Sprint 1 list, not the whole project.*  
2. *This sprint is only referral → doctor decision → first booking.*  
3. *Each task has two owners, time, a done-check, and evidence.*  
4. *Tomorrow we upload the tables. Diagrams and code come later.*

---

## 和黑板的对应

| 老师写的 | 你拿出的 |
|----------|----------|
| Complete Product Backlog | Estrella 的 Part 3 |
| Sprint 1 Sprint Backlog | 这份 Part 6 表格 |
| GitHub, all members, upload PB / Sprint Backlog | 两份表 push 上去，四人都在仓库里 |
