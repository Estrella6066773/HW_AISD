# 操作流程图、临床 SR、战略图

中文图：`Hospital_All_Processes_V2_中文.bpmn`  
英文可执行图：`Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`  
临床 SR：`Ruby/2026-10-13/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`  
战略图：`docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`

中文图只改了图上的名称。编号、箭头、网关条件都和英文 V2 一样。这张中文图不要部署。

The Chinese file only changes the labels. The numbers, arrows and gateway rules stay the same as the English V2. Do not deploy the Chinese file.

---

## 1. 操作流程图怎么看

这张图是患者从进来到做完的步骤。它按时间往下走。

This picture is the patient pathway, step by step, in time order.

医院里有三条泳道。

The hospital has three lanes.

| 泳道 | 谁在做 | 做什么 |
| --- | --- | --- |
| 行政 | 秘书、预约、呼叫处理 | 登记、补材料、预约、发信、行政咨询 |
| 临床团队 | 顾问、专科护士 | 决定接不接、看病、批信、紧急授权、变更 |
| 财务 | 财务人员 | 经费、付款、退款、紧急治疗后的跟进 |

图外面还有三方。转诊机构送来材料。患者收到预约和治疗安排。支付服务商收付款请求，再返回结果。

Outside the hospital there are three parties. The referrer sends documents. The patient receives the appointment and the treatment plan. The payment provider takes a payment request and sends back a result.

### 主路径

一条普通转诊，按这个顺序走。

A normal referral follows this order.

1. **登记请求。** 行政核验材料和身份。
2. **请求类型选“转诊”。** 交给临床。
3. **顾问审阅转诊。** 写下决定和理由。
4. **接受。** 行政才能预约第一次就诊，并通知患者。
5. **需要占号源。** 系统去查门诊号源。
6. **就诊结果是“已到诊”。** 进入临床问诊。
7. **问诊 / 治疗 / 复查。** 临床在这里授权护理，也在这里写诊后信。
8. **通常不走财务紧急跟进。** 行政核对并发送已批准的信。
9. **信已发出。** 回到临床计划。
10. **计划是“治疗”。** 财务评估经费。
11. **医院付、保险已批，或患者已付款。** 行政确认治疗和检查预约。
12. **资源就绪。** 占用号源，给患者发确认。然后回到临床，做治疗或复查。

Register the request. Choose referral. The consultant decides. After accept, admin books the first visit. After the patient attends, the clinician records care and the letter. Admin sends the approved letter. If the plan is treatment, finance checks funding. Then admin books the treatment.

### 几条会分开的路

这些不是每人都走。

These paths are only for some cases.

- **拒绝。** 转诊直接结束。
- **转科。** 记录转科，通知转诊方，然后关闭。
- **还要材料。** 回到“补齐记录”，再重新登记。
- **已预约，人还没来。** 停在“等待到诊”，之后再选结果。
- **患者拒绝、取消，或未到诊。** 进入“授权变更、复诊或取消”。
- **没有合适号源，或治疗资源不够。** 标成待定，可以重试。同一请求不要订两次。
- **经费未清，或付款失败。** 标成待追查，再处理。
- **等付款会有风险。** 临床写下理由，可以先授权紧急治疗。财务事后跟进。
- **变更碰到已付款或已批复。** 财务决定退款、转账或保留费用。临床不批退款。
- **咨询。** 行政、临床、财务各答各的，然后结束。
- **报表。** 管理人员查看审计和路径报表，然后结束。

Reject stops the referral. Redirect tells the referrer and closes. Missing documents go back for another check. Decline, cancel and did-not-attend go to a change. No slot, failed payment and urgent care each have their own branch. Enquiries and reports end on their own.

图上的 P1、P2 这些编号，是为了和英文图、案例段落对上。中文图没有删掉它们。

The P1, P2 numbers stay on the Chinese diagram so you can match the English diagram and the case paragraphs.

---

## 2. 临床 SR 怎么看

这张图不讲先后顺序。它讲临床团队要达成什么，以及谁依赖谁。

This picture is not a time order. It shows what the clinical team must achieve, and who depends on whom.

虚线框里面是临床团队。框外是患者、转诊机构、行政团队、财务。

Inside the dashed box is the clinical team. Outside are the patient, the referrer, the admin team and finance.

### 先看懂一条线

虚线框是临床团队自己的理由。框外四个圆是别人：患者、转诊机构、行政、财务。

The dashed box is the clinical team's own reasoning. The four circles outside are other people: patient, referrer, admin, finance.

每一条带 D 的线都停三下：需要的人，中间那个写着 D 编号的图形，然后是要交出来的人。

Every D line has three stops: the one who needs something, the labelled shape in the middle, then the one who must provide it.

D 是箭头，不是装饰。它从需要的人指向要交出来的人。D 朝着谁，谁就是被依赖的那一个。需要的人在另一头。

D is an arrow. It points from the one who needs something to the one who must provide it. The person the D points at is the one being depended on. The one who depends stands at the other end.

中间图形的形状，只说明“要的是哪一种东西”。在这张图上，椭圆才是要一个结果。矩形不是目标。七条依赖里，矩形只有 D4，那是一包材料。六边形只有 D8，那是一件指定要做的事。云形只有 D18。

The shape says what kind of thing is wanted. On this diagram, the ovals are the wanted results. The rectangle is not a goal. Among the seven dependencies, the only rectangle is D4, a pack of documents. The only hexagon is D8, a specified job. The only cloud is D18.

框里的线只有三种。

Inside the box there are only three kinds of line.

- 小横杠贴在椭圆上：下面这几件一起撑住上面的结果。AND. The small bar sits on the oval. The pieces below together support that result.
- 黑点：上面的六边形要用下面的矩形。Black dot: the hexagon above needs the rectangle below.
- help / hurt：这条线在底部的云结束。它表示有帮助，或会拖慢。它不是下一项任务。help / hurt: the line ends on a cloud at the bottom. It means the work helps that quality, or slows it. It is not the next task.

### 线 1：患者进来以后，总目标分成四条

患者 Patient  
→ D12 Appropriate clinical assessment and care / 恰当的临床评估和护理  
→ Clinical pathway managed appropriately / 临床路径得到恰当管理

D 指向框内。患者依赖临床团队。要的结果是得到恰当的评估和护理。

The D points into the box. The patient depends on the clinical team.

这个椭圆自己不再往下做一件事。它用四条带小横杠的线分出去。四条都要有，这个总目标才算站住。

This oval does not do one job by itself. Four lines with a small bar leave it. All four are needed.

**1a，左转诊。**  
→ Referral decision recorded / 转诊决定已记录  
→ Review referral; record decision [M] / 审阅转诊，记下决定

小横杠在“转诊决定已记录”上。审阅并记下决定，这个结果才成立。决定可以是接受、拒绝、再要材料或转科。

The bar sits on “Referral decision recorded”. Reviewing and writing the decision is how that result is met. The decision may be accept, reject, more documents, or redirect.

这个六边形后面还有三条线，分别是线 2 的黑点、线 2 的 help、线 5 的另一头。

This hexagon continues on three more lines: the black dot and the help line in line 2, and the other end of line 5.

**1b，中问护理。**  
→ Clinical care and plan recorded / 临床护理和计划已记录  
→ 再分成线 3 的两个六边形。

The bar sits on “Clinical care and plan recorded”. It then splits into the two hexagons in line 3.

**1c，左下诊后信。**  
→ Clinic letter clinically approved [P] / 诊后信已获临床批准  
→ Prepare / approve clinic letter [P] / 准备并批准诊后信

小横杠在橙色椭圆上。下面的橙色六边形是准备并批准这封信。线再从六边形出框，见线 4。

The bar sits on the orange oval. The orange hexagon prepares and approves the letter. The line then leaves the box. See line 4.

**1d，右上预约。**  
→ Clinic and treatment appointments arranged after authorisation / 授权之后安排门诊和治疗预约

小横杠在总目标与这个椭圆之间。这个椭圆再出框，见线 5。

The bar sits between the top goal and this oval. The oval then leaves the box. See line 5.

### 线 2：左列，从转诊决定走到材料，再弯到“安全”

转诊机构 Referring organisation  
→ D2 Referral decision recorded / 转诊决定已记录  
→ Referral decision recorded / 转诊决定已记录  
→ Review referral; record decision [M] / 审阅转诊，记下决定

D 指向框内。转诊机构依赖临床团队。框内的椭圆和框外的 D2 是同一件事：决定已经写下来。接受、拒绝、再要材料、转科都算。

The D points into the box. The referrer depends on the clinical team. The oval inside and D2 outside are the same result: a decision is written down.

竖线继续往下，中间有一个黑点：

→ Checked referral package [M] / 已核验的转诊材料  
→ D4 Checked referral package / 已核验的转诊材料  
→ 行政 Admin team

黑点的意思是：审阅这个六边形要用下面那包材料。D 从材料指向行政。临床依赖行政把材料核好交过来。

The black dot means the review hexagon needs the package below it. The D points at admin. The clinical team depends on admin for the checked documents.

同一六边形还有一条弯线，写着 help，终点是云：

→ Safe clinical decisions / 安全的临床决定

把决定和理由记下来，有助于安全的临床决定。线在这朵云结束。

Writing the decision and the reason helps safe clinical decisions. The line ends on this cloud.

行政还有一条线扎进同一个六边形：

行政 Admin team  
→ D5 Authorised acceptance before a new patient appointment / 新患者门诊前须已授权接受  
→ Review referral; record decision [M] / 审阅转诊，记下决定

D 指向六边形。行政依赖临床团队。这条比 D2 窄：新患者第一次门诊之前，必须已经是“接受”。拒绝、再要材料、转科只停在 D2，不完成 D5。

The D points at the hexagon. Admin depends on the clinical team. This line is narrower than D2. A first visit for a new patient needs “accept”. Reject, more documents and redirect stop at D2. They do not finish D5.

### 线 3：中间列，评估走向“及时”，决定走向“安全”

Clinical pathway managed appropriately / 临床路径得到恰当管理  
→ Clinical care and plan recorded / 临床护理和计划已记录

小横杠在下面这个椭圆上。它再分成两个六边形。

The bar sits on the lower oval. That oval splits into two hexagons.

**3a**  
→ Assess patient; record clinical notes [M/P] / 评估患者，记下临床记录  
→ hurt  
→ Timely clinical care / 及时的临床护理

评估要花时间，所以这根线标 hurt，终点是“及时的临床护理”。线在云上结束。`[M/P]` 表示人来判断，系统不自动诊断。

Assessment takes time, so this line is marked hurt and ends on “Timely clinical care”. `[M/P]` means a person judges. The system does not diagnose.

**3b**  
→ Record care decision [M] (treatment / follow-up / discharge) / 记下护理决定（治疗 / 复诊 / 出院）  
→ help  
→ Safe clinical decisions / 安全的临床决定

一次就诊记下一个决定：治疗、复诊或出院。这根线标 help，终点同样是底部那朵“安全”的云。

One encounter records one decision: treatment, follow-up, or discharge. This line is marked help and ends on the same “safe” cloud.

### 线 4：橙色诊后信，从行政穿进框，再接到总目标

行政 Admin team  
→ D7 Clinic letter clinically approved / 诊后信已获临床批准  
→ Prepare / approve clinic letter [P] / 准备并批准诊后信  
→ Clinic letter clinically approved [P] / 诊后信已获临床批准  
→ Clinical pathway managed appropriately / 临床路径得到恰当管理

D 指向框内的橙色六边形。行政依赖临床团队。行政要的是信已经批准。六边形上面的橙色椭圆用小横杠接住它，这根横杠再接到线 1 的总目标，所以它就是线 1c。

The D points at the orange hexagon. Admin depends on the clinical team for an approved letter. The orange oval above the hexagon carries the small bar, and that bar joins the top goal in line 1. This is line 1c.

`[P]` 和橙色表示：现在系统里主要还是临床任务上的一段备注，没有单独的批准栏。

`[P]` and the orange colour mean the current system mainly keeps a note on the clinical task. There is no separate approval field.

### 线 5：预约椭圆有两头，出框才到行政

这一头从总目标来：

Clinical pathway managed appropriately / 临床路径得到恰当管理  
→ Clinic and treatment appointments arranged after authorisation / 授权之后安排门诊和治疗预约

另一头从左列的六边形来：

Review referral; record decision [M] / 审阅转诊，记下决定  
→ Clinic and treatment appointments arranged after authorisation / 授权之后安排门诊和治疗预约

两头都用小横杠接到这个椭圆上。审阅时如果写下“接受”，新门诊才订得成，所以左列的六边形也撑着这个预约结果。

Both lines meet this oval with a small bar. If the review records “accept”, the new visit can be booked. That is why the left hexagon also supports this appointments result.

椭圆再出框：

→ D8 Arrange clinic and treatment appointments / 安排门诊和治疗预约  
→ 行政 Admin team

D 指向行政。临床依赖行政去订号。中间是六边形，因为要的是“去安排”这件事。第一次门诊还要先完成线 2 的 D5。治疗预约要等线 3b 记下“治疗”。

The D points at admin. The clinical team depends on admin to make the booking. The middle shape is a hexagon because the wanted thing is the job of arranging it. The first visit also needs D5 from line 2. Treatment booking waits until line 3b records “treatment”.

### 线 6：右边紧急路径，三条 help 都结束在“及时”

Urgent pathway supported (when required) / 需要时支持紧急路径

这个椭圆在总目标旁边。它没有小横杠连回“临床路径得到恰当管理”。只有付款等待会让患者有风险时才用。

This oval sits beside the top goal. It has no bar back to “Clinical pathway managed appropriately”. It is used only when waiting for payment would put the patient at risk.

它下面两条线的小横杠贴在它自己身上：

→ Authorise urgent care; record reason [M] / 授权紧急治疗并写下理由

→ Clinical work not delayed solely by payment confirmation gaps / 临床工作不单因付款确认缺口被拖延

然后有三条 help，终点都是 Timely clinical care / 及时的临床护理：

- Urgent pathway supported (when required) / 需要时支持紧急路径 → help → Timely clinical care / 及时的临床护理
- Authorise urgent care; record reason [M] / 授权紧急治疗并写下理由 → help → Timely clinical care / 及时的临床护理
- Clinical work not delayed solely by payment confirmation gaps / 临床工作不单因付款确认缺口被拖延 → help → Timely clinical care / 及时的临床护理

这三根线都在“及时”这朵云结束。

All three lines end on the “timely” cloud.

付款那朵云再出框：

→ D18 Urgent care not blocked solely by payment delay / 紧急治疗不单因付款延迟被挡住  
→ 财务 Finance

D 指向财务。临床依赖财务。临床可以先写下理由做，财务事后跟进。

The D points at finance. The clinical team depends on finance. Clinical staff may go ahead with a written reason. Finance follows up afterwards.

### 两条线会汇合的地方

Safe clinical decisions / 安全的临床决定  
这朵云是线 2 的 help 和线 3b 的 help 的终点。

Timely clinical care / 及时的临床护理  
这朵云是线 3a 的 hurt，以及线 6 三条 help 的终点。

两朵云都不再往下连任务。

The “safe” cloud is where the help lines from line 2 and line 3b end. The “timely” cloud is where the hurt line from line 3a and the three help lines from line 6 end. Neither cloud continues into another task.

---

## 3. 三张图怎么连

先记住三句话。

Keep these three sentences.

- **临床 SR** 讲临床为什么做，以及和谁有依赖。
- **战略图** 把整条医院路径收成几个大阶段，并画出外部机构。
- **操作流程图 V2** 把阶段拆成可以在 Camunda 里走的任务、网关和消息。

The clinical SR says why the clinical team acts, and who depends on whom. The strategic diagram turns the hospital pathway into a few big stages and shows outside organisations. V2 splits those stages into tasks, gateways and messages that Camunda can run.

SR 的 AND 不是时间顺序。战略图的一个方框，在 V2 里通常是好几个任务。

AND in the SR is not a time order. One box on the strategic diagram is usually several tasks in V2.

### 临床 SR 对上 V2 的哪几步

| 临床 SR | V2 上的步骤 |
| --- | --- |
| D4 已核验的转诊材料 | 登记请求；补齐缺失记录 |
| 审阅转诊，记下决定；D2 | 顾问审阅转诊；转诊决定 |
| D5，接受之后才能订新门诊 | 决定是“接受”之后，才进入预约就诊 |
| 拒绝或转科 | 拒绝结束；或记录转科并通知转诊方 |
| 评估患者；记下治疗 / 复诊 / 出院 | 问诊 / 治疗 / 复查；后面的“临床计划” |
| D8，授权后由行政预约 | 接受之后的预约就诊；治疗授权之后的确认治疗预约 |
| 准备并批准诊后信；D7 | 问诊任务里的信；然后行政核对并发送 |
| 授权紧急治疗；D18 | 临床授权紧急治疗；财务在紧急治疗后跟进 |
| 患者得到评估和护理；D12 | 已到诊之后的问诊 / 治疗 / 复查 |

D4 matches register and get-documents. D2 matches the consultant review. D5 matches “accept”, then book the visit. Care notes and the care decision match the consult task and the clinical-plan gateway. D8 matches both the first booking and the later treatment booking. D7 matches the letter written in the consult task and sent by admin. D18 matches urgent authorisation and the later finance follow-up. D12 matches care after the patient has attended.

### 战略图卡在中间

战略图也是三条泳道：临床、行政、财务。一个任务就是一个阶段。

The strategic diagram uses the same three lanes. One task is one stage.

和临床有关的阶段是这些。

These are the stages that belong to clinical work.

| 战略图上的阶段 | 临床 SR | V2 |
| --- | --- | --- |
| 记录临床决定 | 转诊决定已记录 | 顾问审阅转诊 |
| 预约第一次门诊并通知患者 | D5，以及 D8 里的门诊部分 | 预约就诊；通知患者 |
| 授权治疗预约 | 护理决定里的“治疗” | 问诊任务里的授权 |
| 撰写并批准诊后信 | 诊后信已获临床批准 | 问诊任务里的信 |
| 发送已批准的诊后信 | D7，行政在临床批准之后发送 | 核对并发送；发出诊后信 |
| 回答临床咨询 | 这张临床 SR 没画咨询 | 专科护士 / 临床人员答复 |
| 授权变更或复诊 | 护理决定里有复诊；单独的变更任务没画进这张 SR | 授权变更、复诊或取消 |
| 确定经费和付款 | D18 只覆盖“不要只因付款把紧急治疗挡住” | 评估经费；付款；紧急授权 |

### 三张图并不完全一样的地方

这几处要能讲出来。

These are the differences you should be able to explain.

**信和治疗计划的先后。**  
战略图在患者到诊后分成两条，一起走：一条是护理计划，一条是诊后信。付款不必等信批完。  
V2 是一条线：先问诊，再发信，再选临床计划，再做经费。  
临床 SR 把“护理计划”和“诊后信”都放在总目标下面。它只说两件都要有。它没有规定谁先谁后。

On the strategic diagram, after attendance the care plan and the clinic letter run side by side. Payment does not have to wait for the letter. V2 is one line: consult, send the letter, choose the plan, then funding. The SR says both the care plan and the letter are required. It does not set which one comes first.

**第一次门诊和治疗预约。**  
D5 管的是新患者第一次门诊：必须先接受转诊。  
D8 管的是行政去订号，而且要在相应的临床授权之后。  
V2 把这两次预约都画出来了。战略图也把“第一次门诊”和“确认外部治疗资源”分成两个阶段。

D5 is the first new-patient visit: the referral must be accepted first. D8 is admin booking a slot after the matching clinical authorisation. V2 draws both bookings. The strategic diagram also keeps the first visit and the later treatment resources as two stages.

**诊后信还是部分支持。**  
SR 把信标成 `[P]`。V2 的问诊任务名称里写了授权诊后信，发送也有单独步骤。可是批准还不是一个单独字段，也挡不住“没批准就发出去”。

The SR marks the letter `[P]`. V2 names letter authorisation on the consult task, and it has a send step. Approval is still not a separate field, and nothing stops a letter going out before approval.

**紧急治疗。**  
SR 把它放在主目标旁边，只在需要时使用。  
战略图把它写进“确定经费和付款”这个阶段里面，没有单独画一条线。  
V2 把它画成了看得见的分支：临床写理由授权，财务事后跟进。

The SR places urgent care beside the main goal, and only when needed. The strategic diagram folds it into “determine funding and payment”, with no separate line. V2 draws it as a visible branch: clinical authorisation with a reason, then finance follow-up.

**图外的机构。**  
战略图还有外部排班、检验影像、保险公司。  
这张临床 SR 没有把这三个外部机构画出来。预约通过 D8 交给行政。  
V2 外面只画了转诊机构、患者和支付服务商。排班和检查资源在任务里完成，没有单独的池。

The strategic diagram also shows external scheduling, laboratory and imaging, and the insurer. This clinical SR does not draw those three. Booking is handed to admin through D8. V2 only draws the referrer, the patient and the payment provider. Scheduling and clinical resources stay inside tasks. They have no pool of their own.

**这张 SR 没有覆盖的 V2 步骤。**  
临床咨询、报表、退款金额，都不在这张临床 SR 里。咨询属于另一张视图。退款是财务的决定。报表在这期 SR 里不算已承诺的能力。

Clinical enquiries, reports and the refund amount are not in this clinical SR. Enquiries belong in another view. The refund is a finance decision. Reports are not a committed capability in this release of the SR.
