# 正式作答 · 答辩批注（16 Sep）

对照：`Coursework/Agile Workshop-ZH.docx` / `Agile Workshop-EN.docx`  
批注来源：`ruby：案例段落精华-双语.md`  
用法：左边是交上去的正式口径，右边是老师追问时用的案例依据。英文斜体可直接讲。

**今天只交计划。不画图，不写代码。**  
*Today we present the plan only: backlog and sprint backlog. No diagrams, no code yet.*

---

## 0. 开场 30 秒（Ruby）

正式摘要（Part 1）：专科医院要把患者从转诊到就诊、治疗、付钱、写信、打电话串起来。现在信息太散。医生定医疗，财务定钱，行政只办事。Sprint 1 只切到第一次门诊预约。

批注：第1–2段讲背景和问题；第3–5段是本期刀口；第7段以后先放 Product Backlog。

> *This is a specialist hospital patient path: referral, first visit, treatment, payment, letters and phone. Information is messy now. Doctors decide care, finance decides money, admin only carries out the work. Sprint 1 stops at the first clinic booking.*

四人顺序（Part 8 正式版）：

| 顺序 | 谁 | 讲什么 |
|------|----|--------|
| 1 | Hao Zheng | 案例、Sprint Goal、完成/未完成 |
| 2 | Geping Chen | 业务规则、Product Backlog |
| 3 | Minghao Qin | 交付物、Sprint 1 任务 |
| 4 | Guanyan He | 异常、外部系统、校验计划 |

---

## Part 1：案例理解（正式口径 + 段落批注）

**主笔 Hao Zheng / 复核 Geping Chen。证据：本文件 Part 1。**

### 8 问（与 Word 一致）

**1. 组织 / 业务**  
专科医院服务。GP 或另一家医院转诊进来；就诊、诊断、治疗、随访、日常沟通。要上 Hospital Patient Administration System，临床 / 行政 / 财务分开。

> 批注 · 第1段。别说成「普通医院网站」。  
> *A specialist hospital. Many teams. Medical, admin and money must stay separate.*

**2. 利益相关者**  
患者与转诊方；顾问医生、专科护士；秘书、预约、接线、路径协调、行政管理；财务；外部排班、发信、支付、化验/影像。冲突：医生嫌记太多，管理要报表。

> 批注 · 第1段角色 + 第28段冲突 + 第29段患者偏好。财务在第9、13段，不是临床。  
> *Clinicians want less recording. Managers want reports. These goals conflict.*

**3. 主流程**  
秘书收材料 → 医生决定 → 才能约第一次门诊 → 看病后授权才能约治疗 → 分清谁出钱 → 诊后信、接线分流。全程留痕。

> 批注 · 第3→4→5→7→9→19/16段。本期演示只走到第5段。  
> *Secretary checks papers → doctor accepts or not → only then book the first visit.*

**4. 系统要解决的问题**  
信息散在旧系统、邮件、电话、信、手工本。看不清进度、延误、谁做了什么。系统协同团队、挡住越权；外部失败时不重复预约、不重复扣款。系统不替医生诊断。

> 批注 · 第2段是问题；第8、11、12段是失败时不能乱扣、乱约；第17段接线员不能诊断。  
> *Hard to see progress, delays, or who did what. So they want a new system.*

**5. 关键规则（老师最爱追）**

| 正式规则 | 批注（段落） | 口头英文 |
|----------|--------------|----------|
| 秘书只核材料、可要缺件，不能收/拒 | 第3段 | *Secretaries check papers. They cannot accept or reject.* |
| 只有授权医生接受后才能约第一次门诊 | 第4段 | *Book the first visit only after the doctor accepts.* |
| 决定必须记原因和是谁定的 | 第4段 | *Record the reason and who decided.* |
| 没医生授权，行政不能办治疗 | 第7段 | *Admin cannot book treatment without that authorisation.* |
| 先付钱的号：付成功（或豁免）才能确认；不存完整卡号 | 第10–11段 | *Do not store full card numbers. Confirm only after payment or exemption.* |
| 外面扣成功、本院没回执：标调查，禁止自动再扣 | 第12段 | *Mark it for check. Do not charge again automatically.* |
| 诊后信必须医生批准；超7天算延迟 | 第20–22段 | *The doctor must approve the letter. After seven days it is late.* |
| 接线员不能诊断、解读化验、建议治疗 | 第17段 | *Phone staff must not diagnose or suggest treatment.* |

**6. 异常**  
材料缺、拒绝/转专科、无号、电话失败、外部服务挂、支付失败/无回执、紧急先治、口头改期无效、信件超时、紧急咨询规则未定（TBC）。

> 批注 · 第3、4、6、8、11、12、15、18、22段。第18段「怎样算紧急」案例没写死，正式版标 TBC，不编政策。  
> *The hospital has not fully defined “urgent”. We ask the tutor. We do not invent policy.*

**7. 外部系统**  
外部排班、发信、支付公司、化验/影像/外部治疗、转诊方、保险/资助机构。

> 批注 · 第5段排班；第8段化验影像；第10段支付；第19段 GP/别的医院。Sprint 1 只 mock 排班。

**8. 要记什么**  
材料是否齐全；决定类型/原因/操作人；专科、优先级、时间窗；每次联系结果；治疗授权；资金批复；支付状态与流水（不要卡号）；信件时间戳；咨询分类。审计：谁、何时、做了什么，普通人改不了。

> 批注 · 第26–27段。配错病人、系统挂了事后补录，正式版放后期（PB-24、PB-25），今天不必展开。

### 小组假设（正式版三句）

1. 排班和支付可用 mock，必须写明边界。  
2. 紧急咨询如何判定未写死，问 tutor。  
3. 本期优先：转诊核验 → 医生决策 → 第一次门诊预约。

> 批注 · 第30段要求：案例没写清的，标出来，问老师，写下假设。这三条就是在执行第30段。

---

## Part 2：交付物（正式表怎么讲）

**主笔 Minghao Qin / 复核 Hao Zheng。**

正式口径：16 Sep 交文档计划；28 Sep 才交图和代码。

| 今天交 | 28 Sep 交 |
|--------|-----------|
| 案例摘要、交付物清单、PB、任务拆分、依赖、Sprint Backlog、Standup、Review、DoD | 战略/运营 BPMN、i*、Camunda Forms、Workers、测试结果 |

批注：第2段要的是「能看见进度和谁做了什么」，所以今天的交付物是计划表，不是系统。第30段「我们是需求组」，图和代码是下一刀。

> *Deliverables for 16 Sep are documents. BPMN, forms and workers are for 28 Sep.*

若问「为什么清单里有 BPMN 却没画？」：清单写了 Due Date 28 Sep，今天不算完成。

---

## Part 3：Product Backlog（正式编号怎么对上案例）

**主笔 Geping Chen / 复核 Guanyan He。29 条，12 字段。今天状态大多 Not started——这是计划增量，正常。**

Sprint 1 只从 P0 里拉 **PB-01 至 PB-04**，外加过程项 **PB-15（Review）**。其余留在 Product Backlog。

| 正式条目 | 案例批注 | 这个 sprint 做不做 |
|----------|----------|-----------------|
| PB-01 转诊核验 | 第3段：秘书核材料，不能收 | 本期做（T01、T02） |
| PB-02 医生复核 | 第4段：收/拒/补材料/转专科，记原因 | 本期做（T03、T04） |
| PB-03 新患预约 | 第4–6段：接受后才约；无号标出 | 本期做（T05、T06） |
| PB-04 通知 | 第5–6段：常规信；两周内再电话 | 本期做（T07） |
| PB-05 治疗授权 | 第7段：没签完行政不能办 | 本期不做，留在总清单 |
| PB-06 外部服务挂 | 第8段：挂起、通知、不重复建号 | 本期不做（规则可讲） |
| PB-07 资金与支付 | 第9–12段 | 本期不做，留在总清单 |
| PB-08 紧急先治 | 第12段 | 本期不做，留在总清单 |
| PB-09 诊后信 | 第19–23段 | 本期不做，留在总清单 |
| PB-10 咨询分流 | 第16–18段；紧急 TBC | 本期不做，留在总清单 |
| PB-11 审计 | 第26–27段 | 本期不做（计划里承认要留痕） |
| PB-19 改治疗正式申请 | 第15段：电话邮件不算 | 本期不做，留在总清单 |
| PB-20 退款 | 第13、25段：只有财务批钱 | 本期不做，留在总清单 |
| PB-23 化疗复查 | 第14段：只有临床能定继续 | 本期不做，留在总清单 |
| PB-26 报表 | 第28段冲突 | 本期不做，留在总清单 |
| PB-27 沟通偏好 | 第29段 | 本期不做，留在总清单 |

老师若问「为什么治疗这个 sprint 不做？」  
正式答：案例把治疗放在第一次门诊之后（第7段）。Goal 不能贪。  
*Treatment sits after the first visit in the case. We keep the sprint goal small.*

---

## Part 4 / Part 6：任务与 Sprint Backlog

**Part 4 主笔 Minghao Qin；Part 6 主笔 Hao Zheng。**

**Sprint 1 Goal（与 Word 一字不差的意思）**  
16 Sep 前完成并上传 Product Backlog 与 Sprint Backlog。第一刀：转诊核验 → 医生决策 → 第一次门诊预约（排班可 mock）。支付、诊后信、咨询分流不进本期。

| ID | 正式任务 | 状态 | 案例批注 |
|----|----------|------|----------|
| T01 | 秘书可补件，不可接受 | **Done** | 第3段 |
| T02 | 收件 → 核材料 → 送医生 | In progress | 第3–4段 |
| T03 | 医生四态；原因和操作人必填 | Not started | 第4段 |
| T04 | 拒绝后不约新患 | Not started | 第4段 |
| T05 | 接受后才能发预约请求 | Not started | 第4段门禁 |
| T06 | 外部排班可 mock；无号 pending，不约窗外 | Not started | 第5–6段 |
| T07 | 常规信；两周内电话并记结果 | Not started | 第5–6段 |
| T20 | 上传两表；四人在 GitHub；只交计划 | In progress | Workshop 硬检查 |

未完成不要说成完成。T03 没做表单，是因为 16 Sep 不实现。  
*T03 is planned, not implemented. No form today.*

关键路径（Part 5）：**T01 → T02 → T03 → T05 → T06**。最不能延误的是 T03、T05、T06。  
批注：第4段「只有医生接受后才能约」= T05 必须等 T03。

---

## Part 5：依赖（一句话）

**主笔 Guanyan He。**

正式口径：顺序跟案例门禁走。延误通知第二负责人和后继卡。备份：二责顶上；外部可 mock，但 pending、通知、不重复建号、不确定支付不自动再扣，一条都不能丢。

> 批注 · mock 不是省略失败路径。第8段和第12段写得很死。  
> *We may mock the outside calendar, but a failed slot still stays pending. We do not create two bookings.*

---

## Part 7：Standup（每人自己的表）

正式六栏：完成 / 证据 / 下一步 / 阻塞 / 要不要二责 / 要不要交接。

今天口径（与 Word 一致）：计划增量没有实现阻塞。证据是作业里的表或 GitHub，不要报本地文件夹路径。

---

## Part 8：Review 七条（老师按这个点名）

### 1. Completed

Part 1–6 计划表；T01 Done。T20、Part 7 进行中。

### 2. Unfinished（带原因）

T03–T07：今天是计划，不实现。T08 以后：不在 Goal 里。BPMN/Forms/测试：28 Sep。紧急规则：等 tutor（F05）。

### 3. Key decisions（各有案例出处）

| ID | 正式决策 | 批注 |
|----|----------|------|
| D01 | 临床 / 行政 / 财务分开 | 第1段 |
| D02 | Sprint 1 只到第一次门诊 | 第4段门禁 |
| D03 | 外部可 mock，失败路径仍按案例 | 第8段 |
| D04 | 案例没写清的不编政策 | 第18、30段 |
| D05 | 双负责人；没证据不算 Done | Workshop |
| D06 | 无回执不自动再扣；紧急先治要写原因 | 第12段（后期测） |

### 4. Integration

今天的集成 = 同一套 ID、同一条第一刀、同一个仓库。不是已经跑起来的 Camunda。  
PB-01↔T01/T02；PB-02↔T03/T04；PB-03↔T05/T06；PB-04↔T07。

### 5. Validation

文档校验过：秘书不能接受（Pass，文档）。可执行测试 Not executed，不填假结果。

### 6. Feedback

只有组内 F01–F05。**F06 老师反馈还没有，现场再记。不要编老师说过什么。**

### 7. Backlog updates

条目不删。治疗/支付/信件/咨询留在 Product Backlog。老师若要求加宽，再拉任务并改 Goal（F06），不私下扩范围。

---

## 老师追问速查

**Q. 秘书能不能拒收转诊？**  
不能。第3段：只查材料齐不齐。*They cannot accept or reject the patient.*

**Q. 没号怎么办？**  
挂起，通知路径组，不能偷偷约到窗外。第6段。*Keep it pending. Flag the pathway team. Do not book outside the window.*

**Q. 支付失败再扣一次？**  
可以再付，但不能重复预约，也不能自动再扣。没回执标调查。第11–12段。

**Q. 财务能不能决定要不要治？**  
不能。第13段：医生不批钱，财务不定治。*Doctors do not approve money. Finance does not decide if treatment is needed.*

**Q. 电话改治疗行不行？**  
不行。第15段必须系统里正式申请。紧急可先停，事后医生补授权。

**Q. 紧急咨询怎么分流？**  
第18段医院还没定死。我们标 TBC，问老师。*We should ask the tutor.*

**Q. 今天增量是什么？**  
Parts 1–8 这一份计划。*The current integrated increment is the agreed plan, not running software.*

**Q. 证据在哪？**  
作业 Word 里的表，或 GitHub。不要说 `Ruby/2026-09-15/...`。

---

## 四人各背 4 句

**Hao Zheng**  
1. *This is a hospital patient path: referral, first visit, treatment, payment, letters, phone.*  
2. *The problem: info is scattered, so delays and actions are hard to track.*  
3. *Key rule: secretaries check papers; only a doctor can accept and authorise treatment; finance handles money.*  
4. *Sprint 1 is the first booking slice. T01 is done. T03 to T07 are planned, not built.*

**Geping Chen**  
1. *Our product backlog has twenty-nine items from the case, not only the happy path.*  
2. *P0 includes referral, decision, booking, later treatment and payment.*  
3. *This sprint pulls PB-01 to PB-04 only.*  
4. *We do not invent urgency rules for enquiries.*

**Minghao Qin**  
1. *16 Sep deliverables are documents. 28 Sep is diagrams and workers.*  
2. *Tasks are small: T01 permissions, T03 four outcomes, T06 mock scheduling.*  
3. *If there is no slot, the booking stays pending. No duplicate booking.*  
4. *Evidence for Done is a table in the workbook or GitHub.*

**Guanyan He**  
1. *Exceptions: reject, no slot, external service down, lost payment confirmation.*  
2. *Rejected referrals must not enter new-patient booking.*  
3. *Dependencies follow the case gates: T03 before T05.*  
4. *Tests today are a plan. Actual run results come on 28 Sep.*
