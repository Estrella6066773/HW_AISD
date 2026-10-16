# 操作流程图、临床 SR、战略图

中文图：`Hospital_All_Processes_V2_中文.bpmn`  
英文可执行图：`Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`  
临床 SR：`Ruby/2026-10-13/PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`  
战略图：`Week6 Coursework/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`

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

### 图上的形状

| 形状 | 意思 |
| --- | --- |
| 圆角矩形 | 目标。要达成的结果 |
| 六边形 | 任务。为了目标要做的事 |
| 矩形 | 资源。任务要用到的东西 |
| 云形 | 软目标。希望更好，很难用“完成了”来勾掉 |
| 带 D 的小元素 | 依赖。框外的人向框内要的东西，或框内向框外要的东西 |
| help | 有帮助 |
| hurt | 会带来压力或变慢 |
| 黑点连线 | AND。这几项一起支撑上面的目标 |

`[M]` 表示这件事主要靠人做。`[P]` 表示案例要求有，当前系统只做了一部分。诊后信那两块是橙色，就是因为它们是 `[P]`。

`[M]` means a person does the work. `[P]` means the case asks for it, but the current system only covers part of it. The two orange letter shapes are `[P]`.

### 框外的七条依赖

读法：谁依赖谁，依赖什么。

Read each line as: who depends on whom, and for what.

| 编号 | 谁依赖谁 | 依赖什么 |
| --- | --- | --- |
| D2 | 转诊机构依赖临床团队 | 转诊决定已经记下 |
| D4 | 临床团队依赖行政团队 | 已经核过的转诊材料 |
| D5 | 行政团队依赖临床团队 | 新患者门诊之前，必须先有“接受” |
| D7 | 行政团队依赖临床团队 | 诊后信先经过临床批准 |
| D8 | 临床团队依赖行政团队 | 在授权之后，去安排门诊和治疗预约 |
| D12 | 患者依赖临床团队 | 得到恰当的评估和护理 |
| D18 | 临床团队依赖财务 | 紧急治疗不单单因为付款没完成就被挡住 |

D4 和 D8 的方向要记清楚。材料是行政准备好，临床才用。预约是临床先授权，行政再去订。

D4 and D8 point opposite ways. Admin prepares the documents, then clinical uses them. Clinical authorises first, then admin books.

### 框里的目标

最上面的目标是：**临床路径得到恰当管理。**

The top goal is: the clinical pathway is managed properly.

它下面用 AND 连着四块。四块都要有，才算这个目标站住。

Four parts sit under it with AND. All four are needed.

**1. 转诊决定已记录**

任务是：审阅转诊，记下决定。决定可以是接受、拒绝、再要材料，或转科。

这个任务需要资源：已核验的转诊材料。这就是 D4。

每次审阅都满足 D2。只有选了“接受”，才满足 D5，行政才能订新患者门诊。

这条任务对“安全的临床决定”是 help。

The task is to review the referral and record the decision. The decision can be accept, reject, ask for more documents, or redirect. The task needs the checked package. Every review meets D2. Only “accept” meets D5. This task helps safe clinical decisions.

**2. 临床护理和计划已记录**

两件任务：

- 评估患者，写下临床记录。对人做判断，系统不自动诊断。
- 记下护理决定：治疗、复诊，或出院。一次就诊记一个决定。

评估对“及时的临床护理”是 hurt。完整评估要花时间。记下决定对“安全的临床决定”是 help。

One task assesses the patient and writes notes. The system does not diagnose. The other task records one decision: treatment, follow-up, or discharge. A full assessment can slow timely care. Recording the decision helps safe decisions.

**3. 诊后信已获临床批准**

任务是：准备并批准诊后信。这块是橙色 `[P]`。

当前系统里，信的内容主要还是临床任务上的一段备注。没有单独的批准栏，也没有检查“没批准就不能发”。

The letter goal is orange and marked `[P]`. In the current system the letter is mainly a note on the clinical task. There is no separate approval field, and no check that blocks sending before approval.

**4. 授权之后才安排门诊和治疗预约**

这是临床这边的目标。真正去订号的是行政，所以它连到 D8。

第一次门诊，要等转诊被接受。治疗预约，要等临床授权治疗。

This is the clinical goal. Admin does the booking, so the goal links to D8. The first clinic waits for an accepted referral. Treatment booking waits for a treatment authorisation.

旁边还有一个目标：**需要时才走的紧急路径。** 它不在那四块 AND 里面。只有付款等待会让患者有风险时才用。

Beside them is a separate goal: support the urgent path when it is needed. It is not one of the four AND parts. Use it only when waiting for payment would put the patient at risk.

它下面有：

- 任务：授权紧急治疗，并写下理由。可以授权，也可以暂缓。
- 软目标：临床工作不因为付款确认还没回来就被拖住。

紧急授权，以及这个软目标，都对“及时的临床护理”是 help。财务事后跟进。临床不替财务批退款。这就是 D18。

Under it, the clinician authorises urgent care and writes the reason, or holds it. A softgoal says clinical work should not wait only because payment confirmation is missing. Both help timely care. Finance follows up afterwards. Clinical staff do not approve refunds. That is D18.

框底还有两个软目标：**安全的临床决定**，**及时的临床护理**。它们是希望达到的质量，不是已经证明系统做到了。

Two softgoals sit at the bottom: safe clinical decisions, and timely clinical care. They are qualities the team wants. They are not proof that the system already achieves them.

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
