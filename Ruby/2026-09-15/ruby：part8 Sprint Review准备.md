# ruby：Part 8 Sprint Review 准备

**主笔**：Ruby（Hao Zheng，23084382）  
**复核**：Estrella（Geping Chen，23084393）  
**依据**：Agile Workshop Part 8；Case Study — *Hospital Patient Referral, Treatment and Administration System*；Part 3 / 4 / 5 / 6  
**日期**：2026-09-15  
**对应 Backlog**：PB-15 / T20

---

## Workshop 原文与翻译

来源：`W01/Agile Workshop.docx` → **Part 8: Prepare For Sprint Reviews**

**原文**

> Part 8: Prepare For Sprint Reviews
>
> At each sprint review, the group must demonstrate the current integrated increment.
>
> You should be ready to show:
>
> 1. Completed tasks.
> 2. Unfinished tasks.
> 3. Key decisions.
> 4. Evidence of integration.
> 5. Testing or validation evidence.
> 6. Feedback received.
> 7. Backlog updates.

**翻译**

> 第 8 部分：准备 Sprint Review（冲刺评审）
>
> 每一次冲刺评审，小组必须演示**当前已经集成在一起的增量**（不是各人手里互不相干的草稿）。
>
> 你们要准备好当场出示：
>
> 1. **已完成的任务**
> 2. **未完成的任务**
> 3. **关键决策**
> 4. **集成证据**（各部分对得上同一套 ID / 同一条路径）
> 5. **测试或校验证据**
> 6. **已收到的反馈**
> 7. **Backlog 更新**（因反馈或范围变化改了什么）

16 Sep 的「当前增量」是 **计划增量**：案例理解、交付物、Product Backlog、任务拆分、依赖映射、Sprint 1 Backlog、Standup、本 Review 讲稿。不画 BPMN、不写代码、不跑 Camunda。实现增量放到 28 Sep。

*On 16 Sep we demonstrate the plan increment. No diagrams. No code. Implementation comes on 28 Sep.*

---

## 这次要证明什么

**Sprint Goal（与 Part 6 一致）**

Finish and upload the Product Backlog and the Sprint 1 Backlog by 16 Sep. Then specify the first slice: referral check → doctor decision → first clinic booking (scheduling may be mocked). Payment, clinic letters and enquiry routing are out of this sprint.

*本 sprint 交计划，并说清第一刀只切到：秘书核材料 → 医生决定 → 第一次门诊预约（排班可 mock）。付钱、写信、接电话不进这一期。*

现场四个人都要能讲自己那一段。分数按个人贡献算，不能一个人代讲完全部。

---

## 展示顺序（建议 8–10 分钟）

| 顺序 | 主讲 | 对应 Part 8 条目 | 讲什么 | 英文可直接说 |
|------|------|------------------|--------|----------------|
| 1 | Ruby | 案例 + Goal + 已完成/未完成总览 | 这是专科医院转诊路径；本期只演示计划；第一刀切到第一次门诊 | *This is a specialist hospital pathway. Today we show the plan only. Sprint 1 is referral check → consultant decision → first booking.* |
| 2 | Estrella | 关键决策 + Product Backlog | 硬性规则来自案例；P0 全表在 Part 3；本期从 P0 里只拉 PB-01 至 PB-04 | *Secretaries check papers. Only a consultant can accept. We do not invent urgency rules.* |
| 3 | Ender | 交付物 + Sprint Backlog | 16 Sep 交文档；28 Sep 才交图和代码；Sprint 1 拉取 T01–T07、T20 | *Deliverables for 16 Sep are documents. BPMN, forms and workers are for 28 Sep.* |
| 4 | Ryan | 异常、外部系统、测试/校验 | 拒绝后不能约号；没号要挂起；支付无回执不自动再扣；今天只交测试打算 | *Rejected referrals are not booked. No slot stays pending. Unconfirmed payment is investigated, never charged again automatically.* |

---

## 1. Completed tasks（已完成）

对照 Part 6。只有证据已经在仓库里的，才报完成。

| Task / 交付物 | Owner | 证据 | 状态 |
|---------------|-------|------|------|
| Part 1 案例摘要与 8 问讨论 | Ruby 汇总；全组起草 | `Ruby/2026-09-14/ruby：part1案例摘要.md`；`Ruby/2026-09-15/ruby：part1回答.md` | Done（计划级） |
| Part 2 交付物清单 | Ender 主笔；Ruby 复核 | `Dluffy/2026-09-15/` 与 `Ruby/2026-09-15/ruby：part2交付物清单.md` | Done（计划级） |
| Part 3 Product Backlog（29 条，12 字段） | Estrella 主笔；Ryan 复核 | `Est/part3产品待办.md` | 已成稿，待上传仓库作 16 Sep 硬检查 |
| Part 4 任务拆分 T01–T20 | Ender 主笔；Ryan 复核 | `Ruby/2026-09-15/ruby：part4任务拆分.md` | 初稿完成 |
| Part 5 依赖映射 | Ryan 主笔；Estrella 复核 | `Ryan/2026-09-15/Ryan：part5依赖映射.md` | Done（计划级） |
| Part 6 Sprint 1 Backlog + Goal | Ruby 主笔；Ender 复核 | `Ruby/2026-09-15/ruby：part6 Sprint Backlog.md` | 已成稿 |
| Part 7 Standup 准备 | 每人自写；Ryan 汇总 | `Ryan/2026-09-15/` 下 standup 文件 | 进行中（格式已定） |
| T01 角色与权限边界 | Ruby / Estrella | 权限说明：秘书可补件，不得接受转诊 | Done |
| T02 转诊主路径文字 | Ruby / Ryan | 路径说明：receive → check papers → send to Consultant | In progress |
| T20 Review / 仓库上传准备 | Ruby / Estrella | 本文件；GitHub 四人加入 | In progress |

**口头一句**  
*Completed: case summary, deliverable list, product backlog, task breakdown, dependency map, sprint backlog, and the referral permission rules.*

---

## 2. Unfinished tasks（未完成）

未完成要当场说原因，不要装成已经实现。

| 项 | 原因 | 下一步 |
|----|------|--------|
| T03 医生四态（接受/拒绝/补材料/转专科） | 16 Sep 只交计划；字段规则已对齐案例，尚未写成可执行表单 | 会后补决策字段说明；28 Sep 进 Camunda Form |
| T04 拒绝/转出路径 | 依赖 T03 | Ryan 出异常路径文字；拒绝后不进入新患预约 |
| T05 约号门禁 | 依赖 T03 | 未接受则行政不能约号 |
| T06 外部排班 mock | 依赖 T05；16 Sep 不写 worker | 28 Sep：有号确认 / 无号 pending，禁止约到窗外 |
| T07 通知规则 | 依赖预约成立 | Estrella 出规则表：常规信；两周内再电话并记每次结果 |
| T08–T16 治疗、支付、信件、咨询、审计实现 | **不在 Sprint 1 Goal 内** | 下一 sprint 再拉；P0 里其余条目仍留在 Product Backlog |
| 战略/运营 BPMN、i*、Forms、Workers | 16 Sep 明确不画图、不写代码 | 28 Sep |
| 测试截图与端到端演示 | 没有可运行增量 | 16 Sep 只说明打算测什么；28 Sep 才填实际结果 |
| Part 7 全员个人 standup 收齐 | 汇总还缺部分自述 | 每人补自己的 standup，Ryan 再汇总 |

**口头一句**  
*Unfinished on purpose: diagrams, code, payment, letters and phone routing. They are in the product backlog, not in this sprint.*

---

## 3. Key decisions（关键决策）

每条都能指回案例原文，不是组里临时发明的。

| # | 决策 | 案例依据 | 对本期的影响 |
|---|------|----------|----------------|
| 1 | 临床决定、行政执行、财务处理分开。系统做门禁，不靠人记住。 | *maintaining a clear distinction between clinical decisions, administrative responsibilities and financial activities* | Backlog 和任务都按角色拆；秘书账号不能点「接受」 |
| 2 | 第一刀只打通：转诊核验 → 医生决策 → 第一次门诊预约。 | *A New Patient Appointment may only be arranged after an authorised Consultant has accepted the referral.* | Sprint 1 = T01–T07 + T20。治疗、支付、信件、咨询不进本期 |
| 3 | 外部排班、发信、支付本期用 mock，但 mock 必须表现失败行为。 | *If an external service is temporarily unavailable, the booking must remain pending… without creating duplicate appointments.* | 报告写明模拟边界；无号 = pending，不是省略这条路径 |
| 4 | 案例没写死的规则不编政策。紧急咨询如何判定标「待确认」，问 tutor。 | *the hospital has not yet agreed a complete set of rules for determining urgency* | PB-10 不在 Sprint 1；不把猜测写进验收条件 |
| 5 | 每张卡第一 + 第二负责人；二责能顶上。缺证据不得报 Done。 | Workshop：双负责人；Part 5 延误通知与备份 | T01 标 Done 是因为有权限说明；T03 未开始就不报完成 |
| 6 | 不确定支付禁止自动再扣；紧急先治必须记原因并转财务。 | *marked for investigation rather than automatically requesting another payment* | 写入后续测试清单，不在 16 Sep 演示软件 |

**口头一句**  
*Doctors decide care. Finance decides money. Admin only carries out authorised work. We mock external services, but we keep the failure rules from the case.*

---

## 4. Evidence of integration（集成证据）

16 Sep 集成的是**同一套计划**，不是同一套可运行软件。要能当场指出：Part 3、Part 4、Part 6 用同一套编号。

| 集成点 | 怎么对得上 | 证据位置 |
|--------|------------|----------|
| 编号一条线 | PB-01↔T01/T02；PB-02↔T03/T04；PB-03↔T05/T06；PB-04↔T07；PB-15↔T20 | Part 3、Part 4、Part 6 |
| 范围一条线 | Sprint Goal = 转诊核验 → 医生决策 → 第一次预约 | Part 1 摘要、Part 5 关键路径、Part 6 Goal |
| 角色一条线 | 秘书 / Consultant / 预约组 / 路径组 | T01 权限；案例第 3–6 段 |
| 失败路径一条线 | 拒绝不约号；无号 pending；不重复建号 | Part 1 异常路径；Part 5 备份；T04/T06 |
| 仓库 | 四人已加入；计划文件按人、按日期放 | GitHub；`Ruby/` `Est/` `Dluffy/` `Ryan/` |

28 Sep 的集成证据才是：同一条 Camunda 流程上，转诊表单 → 医生决策 → mock 排班，四人能指出自己改过的文件与 commit。

**口头一句**  
*Integration today means one ID scheme and one sprint slice, not a running process yet.*

---

## 5. Testing or validation evidence（测试 / 校验证据）

今天**没有**系统运行结果。校验做了两件事：（1）对照案例核对规则；（2）写清 28 Sep 必测什么。不把空的「实际结果」填成已通过。

**已按案例核对（文档级）**

| 规则 | 原文要点 | 本期如何验收 |
|------|----------|----------------|
| 秘书不能接受转诊 | *they are not permitted to … decide whether the referral should be accepted* | T01：权限表与案例一致 |
| 决策必须有原因和操作人 | *The reason for the decision and the identity of the person making it must be recorded* | T03：不填则不能继续 |
| 未接受不能约新患 | *A New Patient Appointment may only be arranged after an authorised Consultant has accepted* | T04/T05：拒绝路径不进预约 |
| 无号不能偷约窗外 | *rather than being silently booked outside the clinically requested period* | T06：pending / 转 pathway |
| 两周内必须电话并记结果 | *if the appointment is due … within the following two weeks, the patient must also be contacted by telephone* | T07：14 天内要有电话尝试记录 |

**28 Sep 计划必测（有预期栏；实际栏那时再填）**

1. 错误角色越权：秘书点接受 / 行政处理未授权治疗 → 应被拒绝  
2. 主路径：核材料 → 医生接受 → 生成预约请求 → mock 有号 → 确认  
3. 拒绝路径：医生拒绝 → 不生成新患预约  
4. 无号挂起：时间窗内无号 → pending，通知路径组，不重复建号  
5. （下一期）支付失败可重试；已扣款无回执不自动再扣  

**口头一句**  
*Validation today is against the case study text. Executable tests come with the 28 Sep increment. We will not mark tests as passed in advance.*

---

## 6. Feedback received（已收到的反馈）

Tutor 正式评审尚未开始。下面只记**已经发生**的组内反馈，不编造老师评语。

| ID | 来源 | 内容 | 决策 | 落到哪 |
|----|------|------|------|--------|
| F01 | 组内 | 不要只做 happy path | 采纳 | 已拆 T04、T09、T11、T12 |
| F02 | 组内 | 外部系统来不及真接 | 采纳；标假设 | Sprint 1 排班 mock；支付 mock 放到治疗段 |
| F03 | 组内（Part 4 复核） | 有的依赖只写「Part 1 摘要」，太粗 | 采纳 | Part 5 收到具体 Task ID |
| F04 | 组内（Part 4 复核） | T01 标 Done 必须有证据路径 | 采纳 | 缺路径则不算解除依赖 |
| F05 | 案例原文 | 紧急咨询规则未定 | 不编政策；问 tutor | 不进 Sprint 1；PB-10 留待确认 |
| F06 | Tutor | （尚未收到） | — | Review 当场记；会后写入本表，不补假记录 |

现场若老师给意见，用这一句接：  
*We will record the feedback with a decision, owner and backlog change. We will not invent a rule the case has not agreed.*

---

## 7. Backlog updates（Backlog 更新）

相对 14–15 日讨论基线，本轮明确了这些变化。原条目不删，只改优先级或移出 Sprint 1。

| 变化 | 为什么 | 现在放哪 |
|------|--------|----------|
| Sprint 1 从 P0 中只拉「转诊 → 决策 → 第一次预约」 | 16 Sep 只交计划；Goal 不能贪 | Part 6：T01–T07、T20 |
| 治疗授权、外部治疗失败、支付（T08–T11 / PB-05–07）不进本期演示 | 案例顺序上它们在第一次门诊之后 | 留在 Product Backlog；下一 sprint |
| 信件 7 天升级、咨询分流后置 | 案例有，但不是第一刀 | PB-09、PB-10 = P1 |
| 保留异常类：拒绝转诊、无号升级、孤儿支付、紧急先治 | 组内反馈 F01；案例写明 | T04、T06、T11、T12 仍在总 Backlog |
| 审计至少覆盖转诊决定与治疗授权 | 案例第 26 段核心动作 | PB-11 建议第一期做这两项；实现不在 16 Sep |
| 若 tutor 要求第一期更宽 | 等当场反馈 F06 | 再拉 T13–T15 并改 Sprint Goal，不私下加范围 |

**口头一句**  
*The product backlog still holds the full case. This sprint only pulled the first booking slice. Unfinished work stays visible.*

---

## 每人上场要能答的一句话

| 成员 | 我做了什么 | 证据 | 下一步 |
|------|------------|------|--------|
| Ruby | Part 1 摘要、Part 6 Sprint Backlog、本 Review 顺序；T01 权限 | 上述 md | 锁 T02 路径文字；会后补 T03 字段 |
| Estrella | Part 3 全表；通知规则（T07）待做；复核 Part 1/5/8 | `Est/part3产品待办.md` | 上传 PB；写 T07 规则表 |
| Ender | Part 2 清单、Part 4 拆分与复核；T06 排班 mock 约定 | Part 2 / Part 4 | 28 Sep 做 mock worker |
| Ryan | Part 1 异常与外部系统、Part 5 依赖、Part 7 汇总；T04 拒绝路径 | `Ryan/2026-09-15/` | 拒绝路径说明；测试计划（T19） |

---

## 明天口头 4 句（开场兜底）

1. *This review shows our integrated plan, not a running system.*  
2. *Sprint 1 is only: check papers → consultant yes or no → first clinic booking.*  
3. *Completed: backlog, tasks, dependencies and permission rules. Unfinished: diagrams, code, payment and letters.*  
4. *Key rule from the case: secretaries check documents; only a doctor can accept; no slot stays pending; we do not invent urgency policy.*

现场不要说已经测过支付，也不要演示不存在的流程图。老师若问「increment 在哪」，指仓库里同一套 Part 1–8 文档，以及 Sprint 1 已选定的 T01–T07。
