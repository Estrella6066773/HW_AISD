# SR 格子对应 BPMN 方框原名

# SR elements mapped to the original BPMN box names

左边是临床 SR 图上的英文，下面附中文。右边每个 BPMN 方框先写 `Hospital_All_Processes_V2.bpmn` 上的英文原文，紧接着写 `Hospital_All_Processes_V2_中文.bpmn` 上同一方框的中文。换行各自按图抄。一个 SR 格子经常对上好几个方框。质量云（help / hurt 的终点）没有方框。

The left side is the English on the clinical SR diagram, with Chinese under it. Each BPMN box on the right is given first in the original English on `Hospital_All_Processes_V2.bpmn`, then in the Chinese of the same box on `Hospital_All_Processes_V2_中文.bpmn`. Line breaks follow each diagram. One SR element often maps to several boxes. Quality clouds (the ends of help / hurt links) have no boxes.

P13 那一块在这张临床 SR 里没有格子。它单独列在文末。

The P13 block has no element on this clinical SR. It is listed on its own at the end.

---

## 概括

## Summary

| SR 上的字 / Wording on the SR | BPMN 方框 / BPMN boxes |
| --- | --- |
| Checked referral package [M]<br>已核验的转诊材料包 [M]<br>D4 Checked referral package<br>D4 已核验的转诊材料包 | P1 / P10 / P13<br>Register request;<br>check documents and ID<br>登记请求；<br>核验材料与身份<br><br>P1 / P11<br>Obtain missing or<br>formally authorised records<br>补齐缺失或<br>正式授权的记录 |
| Review referral; record decision [M]<br>审阅转诊并记录决定 [M]<br>Referral decision recorded<br>转诊决定已记录<br>D2 Referral decision recorded<br>D2 转诊决定已记录 | P2<br>Consultant reviews referral;<br>records decision and reason<br>顾问审阅转诊；<br>记录决定和理由<br><br>Referral<br>decision?<br>转诊<br>决定？ |
| D5 Authorised acceptance before a new patient appointment<br>D5 新患者预约之前须先有已授权的接受 | 只有 `Referral decision?` / `转诊决定？` 的 **Accept** / **接受** 线进入<br>Only the **Accept** / **接受** flow from `Referral decision?` / `转诊决定？` enters<br><br>P3 / P4 / P12<br>Book visit; notify patient;<br>record attendance / contact<br>预约就诊；通知患者；<br>记录到诊 / 联系 |
| Assess patient; record clinical notes [M/P]<br>评估患者并记录临床笔记 [M/P]<br>Record care decision [M] (treatment / follow-up / discharge)<br>记录护理决定 [M]（治疗 / 复诊 / 出院）<br>Clinical care and plan recorded<br>临床护理与计划已记录<br>D12 Appropriate clinical assessment and care<br>D12 适当的临床评估与护理 | P5 / P9 / P12<br>Consult / treat / review;<br>authorise care and clinic letter<br>问诊 / 治疗 / 复查；<br>授权护理和诊后信<br><br>Clinical<br>plan?<br>临床<br>计划？ |
| Prepare / approve clinic letter [P]<br>撰写 / 批准诊后信 [P]<br>Clinic letter clinically approved [P]<br>诊后信已获临床批准 [P]<br>D7 Clinic letter clinically approved<br>D7 诊后信已获临床批准 | 批准写在上面那个 P5 方框的 *authorise … clinic letter* / *授权……诊后信*<br>Approval is written in *authorise … clinic letter* / *授权……诊后信* on the P5 box above<br><br>P9<br>Check and dispatch<br>approved clinic letter<br>核对并发送<br>已批准的诊后信<br><br>P9<br>Dispatch clinic<br>letter<br>发出诊后信 |
| Clinic and treatment appointments arranged after authorisation<br>授权之后安排门诊与治疗预约<br>D8 Arrange clinic and treatment appointments<br>D8 安排门诊与治疗预约 | 门诊：<br>Outpatient:<br>P3 / P4 / P12<br>Book visit; notify patient;<br>record attendance / contact<br>预约就诊；通知患者；<br>记录到诊 / 联系<br><br>P3<br>Check / reserve<br>outpatient slot<br>查询 / 占用<br>门诊号源<br><br>治疗：<br>Treatment:<br>P6<br>Confirm authorised treatment<br>and investigation appointments<br>确认已授权的治疗<br>和检查预约<br><br>P6<br>Reserve treatment<br>slot / resources<br>占用治疗<br>号源 / 资源<br><br>P6<br>Send booking<br>confirmation<br>发送预约<br>确认 |
| Authorise urgent care; record reason [M]<br>授权紧急护理并记录理由 [M]<br>Urgent pathway supported (when required)<br>需要时支持紧急路径<br>Clinical work not delayed solely by payment confirmation gaps<br>临床工作不因付款确认缺口而单独延误<br>D18 Urgent care not blocked solely by payment delay<br>D18 紧急护理不因付款延误而单独受阻 | P8<br>Clinician authorises<br>urgent care with reason<br>临床人员授权紧急治疗<br>并写下理由<br><br>Urgent care<br>authorised?<br>紧急治疗<br>已授权？<br><br>P8<br>Finance follows up<br>after urgent care<br>紧急治疗后<br>财务跟进 |
| Clinical pathway managed appropriately<br>临床路径得到适当管理 | 没有单独方框。就是上面 D2、D12、D7、D8 那几块加在一起<br>No box of its own. It is D2, D12, D7 and D8 above, taken together |
| Safe clinical decisions<br>安全的临床决定 | 没有方框<br>No box |
| Timely clinical care<br>及时的临床护理 | 没有方框<br>No box |

方框中文取自中文图，与英文图是同一批方框。左边 SR 英文下面的中文是对照，不是 SR 图上的字。

The Chinese on the boxes is taken from the Chinese diagram. These are the same boxes as on the English diagram. The Chinese under the SR English on the left is a gloss. It is not wording on the SR diagram.

---

## 1. 材料：Checked referral package [M]、D4

## 1. Documents: Checked referral package [M], D4

SR 这一格要的是一包已经核过的转诊材料。临床依赖行政。

This SR element is a referral package that has already been checked. Clinical work depends on admin.

对应两个方框，都在行政泳道：

It maps to two boxes, both in the admin lane:

```
P1 / P10 / P13
Register request;
check documents and ID
```

```
P1 / P10 / P13
登记请求；
核验材料与身份
```

```
P1 / P11
Obtain missing or
formally authorised records
```

```
P1 / P11
补齐缺失或
正式授权的记录
```

材料不够时，`Request type?` / `请求类型？` 或 `Referral decision?` / `转诊决定？` 走 **Missing documents** / **材料缺失**，或 **More info** / **补充材料**，进第二个方框，再回到第一个。

When the documents are incomplete, `Request type?` / `请求类型？` or `Referral decision?` / `转诊决定？` follows **Missing documents** / **材料缺失**, or **More info** / **补充材料**, enters the second box, then returns to the first.

这个登记方框第一行写了 P1 / P10 / P13，是因为咨询和报表也从这里进。对上 D4 的是方框正文里的 *check documents and ID* / *核验材料与身份*。P13 的报表是另一个方框，见文末。

The first line of this registration box says P1 / P10 / P13 because enquiries and reports also enter here. What matches D4 is *check documents and ID* / *核验材料与身份* in the box text. The P13 report is a different box; see the end.

---

## 2. 转诊决定：Review referral; record decision [M]、Referral decision recorded、D2

## 2. Referral decision: Review referral; record decision [M], Referral decision recorded, D2

对应临床泳道：

This maps to the clinical lane:

```
P2
Consultant reviews referral;
records decision and reason
```

```
P2
顾问审阅转诊；
记录决定和理由
```

接着是网关：

Then the gateway:

```
Referral
decision?
```

```
转诊
决定？
```

四条出去的线都算“决定已经写下”：

All four outgoing flows count as “the decision has been recorded”:

| 网关上的线 / Flow on the gateway | 下一方框 / Next box |
| --- | --- |
| Accept<br>接受 | 见下一节 D5<br>See D5 in the next section |
| Reject<br>拒绝 | 结束事件 `Referral rejected` / `转诊被拒绝`<br>End event `Referral rejected` / `转诊被拒绝` |
| Redirect<br>转科 | `P2 Record authorised redirect and notify referrer` / `P2 记录获授权的转科并通知转诊方`，然后 `P2 Notify referrer` / `P2 通知转诊方`，结束在 `Referral closed` / `转诊关闭`<br>`P2 Record authorised redirect and notify referrer` / `P2 记录获授权的转科并通知转诊方`, then `P2 Notify referrer` / `P2 通知转诊方`, ending at `Referral closed` / `转诊关闭` |
| More info<br>补充材料 | `P1 / P11 Obtain missing or formally authorised records` / `P1 / P11 补齐缺失或正式授权的记录` |

---

## 3. D5 Authorised acceptance before a new patient appointment

## 3. D5 新患者预约之前须先有已授权的接受

SR 没有再画一个新任务。D5 就是上一节那个 P2 方框，再加上网关的一条线。

The SR does not draw a new task. D5 is the P2 box from the previous section, plus one flow on the gateway.

只有这条：

Only this flow:

`Referral decision?` / `转诊决定？` → **Accept** / **接受** →

```
P3 / P4 / P12
Book visit; notify patient;
record attendance / contact
```

```
P3 / P4 / P12
预约就诊；通知患者；
记录到诊 / 联系
```

Reject、Redirect、More info 不到这个方框。

Reject, Redirect and More info do not reach this box.

---

## 4. 问诊和护理决定：Assess patient、Record care decision、Clinical care and plan recorded、D12

## 4. Consultation and care decision: Assess patient, Record care decision, Clinical care and plan recorded, D12

这四句 SR 对上临床泳道的同一个方框：

These four SR wordings map to the same box in the clinical lane:

```
P5 / P9 / P12
Consult / treat / review;
authorise care and clinic letter
```

```
P5 / P9 / P12
问诊 / 治疗 / 复查；
授权护理和诊后信
```

- *Assess patient; record clinical notes* 对上 *Consult / treat / review* / *问诊 / 治疗 / 复查*
- *Assess patient; record clinical notes* maps to *Consult / treat / review* / *问诊 / 治疗 / 复查*
- *Record care decision (treatment / follow-up / discharge)* 对上这个方框提交的决定
- *Record care decision (treatment / follow-up / discharge)* maps to the decision submitted by this box
- D12 是患者要的“得到评估和护理”，也是这个方框。进入它的线是 `Visit outcome?` / `就诊结果？` 的 **Attended** / **已到诊**
- D12 is what the patient wants: assessment and care. It is also this box. The flow that enters it is **Attended** / **已到诊** from `Visit outcome?` / `就诊结果？`

决定写完后，网关按三个值分开：

After the decision is recorded, the gateway splits on three values:

```
Clinical
plan?
```

```
临床
计划？
```

| 网关上的线 / Flow on the gateway | 下一方框 / Next box |
| --- | --- |
| Treatment<br>治疗 | `P7 Assess funding; record payment / approval status` / `P7 评估经费；记录付款 / 批复状态` |
| Follow-up<br>复诊 | 回到 `P3 / P4 / P12 Book visit; notify patient; record attendance / contact` / `P3 / P4 / P12 预约就诊；通知患者；记录到诊 / 联系`<br>Back to `P3 / P4 / P12 Book visit; notify patient; record attendance / contact` / `P3 / P4 / P12 预约就诊；通知患者；记录到诊 / 联系` |
| Discharge<br>出院 | 结束事件 `Care episode ended` / `本次护理结束`<br>End event `Care episode ended` / `本次护理结束` |

`Clinical plan?` / `临床计划？` 下面的 Treatment / 治疗 会进到经费方框。经费那一块本身不在这张临床 SR 里，见文末。

**Treatment** / **治疗** under `Clinical plan?` / `临床计划？` enters the funding box. Funding itself is not on this clinical SR; see the end.

---

## 5. 诊后信：Prepare / approve clinic letter [P]、Clinic letter clinically approved [P]、D7

## 5. Clinic letter: Prepare / approve clinic letter [P], Clinic letter clinically approved [P], D7

SR 的橙色六边形没有自己的 BPMN 方框。批准写在第 4 节那个方框的后半句：

The orange hexagon on the SR has no BPMN box of its own. Approval is written in the second half of the box in section 4:

```
P5 / P9 / P12
Consult / treat / review;
authorise care and clinic letter
```

```
P5 / P9 / P12
问诊 / 治疗 / 复查；
授权护理和诊后信
```

*authorise … clinic letter* / *授权……诊后信* 就是 Prepare / approve clinic letter。

*authorise … clinic letter* / *授权……诊后信* is Prepare / approve clinic letter.

行政真正发出去，是这两个方框：

Admin actually sends the letter in these two boxes:

```
P9
Check and dispatch
approved clinic letter
```

```
P9
核对并发送
已批准的诊后信
```

```
P9
Dispatch clinic
letter
```

```
P9
发出诊后信
```

中间有网关 `Letter status?` / `信件状态？`。**Sent** / **已发送** 才进 `Clinical plan?` / `临床计划？`。**Clinical correction** / **临床更正** 回到上面的 P5 方框。

Between them is the gateway `Letter status?` / `信件状态？`. Only **Sent** / **已发送** enters `Clinical plan?` / `临床计划？`. **Clinical correction** / **临床更正** returns to the P5 box above.

信如果延迟，还有一个方框，SR 没有单独格子，挂在发送后面：

If the letter is delayed, there is another box. The SR has no separate element for it. It sits after dispatch:

```
P9
Monitor delay; remind
and escalate if overdue
```

```
P9
监控延误；逾期则
提醒并升级
```

做完回到 P5 方框（线上的字是 Review / approve / 复查 / 批准）。

When that finishes, the flow returns to the P5 box. The wording on the flow is Review / approve / 复查 / 批准.

---

## 6. 预约：Clinic and treatment appointments arranged after authorisation、D8

## 6. Appointments: Clinic and treatment appointments arranged after authorisation, D8

SR 这一格对上行政泳道的两次订号。

This SR element maps to two bookings in the admin lane.

第一次门诊，在 D5 的 Accept / 接受 之后：

The first is the outpatient visit, after Accept / 接受 in D5:

```
P3 / P4 / P12
Book visit; notify patient;
record attendance / contact
```

```
P3 / P4 / P12
预约就诊；通知患者；
记录到诊 / 联系
```

```
P3
Check / reserve
outpatient slot
```

```
P3
查询 / 占用
门诊号源
```

治疗或检查，在 `Clinical plan?` / `临床计划？` 的 **Treatment** / **治疗** 并且经费已通过之后，或紧急授权之后：

Treatment or investigation comes after **Treatment** / **治疗** on `Clinical plan?` / `临床计划？`, once funding has been approved, or after urgent authorisation:

```
P6
Confirm authorised treatment
and investigation appointments
```

```
P6
确认已授权的治疗
和检查预约
```

```
P6
Reserve treatment
slot / resources
```

```
P6
占用治疗
号源 / 资源
```

```
P6
Send booking
confirmation
```

```
P6
发送预约
确认
```

号源不够时的方框，SR 没有单独格子：

When no slot is available, there is a box. The SR has no separate element for it:

```
P6
Flag resource
unavailable
```

```
P6
标记资源
不可用
```

它再回到上面的 P6 Confirm / P6 确认已授权的治疗和检查预约 方框。

It then returns to the P6 Confirm / P6 确认已授权的治疗和检查预约 box above.

---

## 7. 紧急：Authorise urgent care; record reason [M]、Urgent pathway supported、D18

## 7. Urgent care: Authorise urgent care; record reason [M], Urgent pathway supported, D18

```
P8
Clinician authorises
urgent care with reason
```

```
P8
临床人员授权紧急治疗
并写下理由
```

这就是 SR 的 *Authorise urgent care; record reason [M]*。

This is the SR element *Authorise urgent care; record reason [M]*.

它前面的入口在财务泳道。`Funding status?` / `经费状态？` 走 **Urgent review** / **紧急复核** 才到这个 P8。正常缴费的 `P7 Assess funding…` / `P7 评估经费……`、`P7 Send payment request to external provider` / `P7 向外部服务商发送付款请求`、`P7 Payment result received` / `P7 收到付款结果` 不在临床 SR 里。

The entry before it is in the finance lane. Only **Urgent review** / **紧急复核** from `Funding status?` / `经费状态？` reaches this P8. The ordinary payment boxes, `P7 Assess funding…` / `P7 评估经费……`, `P7 Send payment request to external provider` / `P7 向外部服务商发送付款请求` and `P7 Payment result received` / `P7 收到付款结果`, are not on the clinical SR.

P8 下面的网关：

The gateway under P8:

```
Urgent care
authorised?
```

```
紧急治疗
已授权？
```

| 网关上的线 / Flow on the gateway | 下一方框 / Next box |
| --- | --- |
| Authorised<br>已授权 | `P6 Confirm authorised treatment and investigation appointments` / `P6 确认已授权的治疗和检查预约`（不等付款结果）<br>`P6 Confirm authorised treatment and investigation appointments` / `P6 确认已授权的治疗和检查预约` (does not wait for the payment result) |
| Hold<br>暂缓 | 回到 `P7 Assess funding; record payment / approval status` / `P7 评估经费；记录付款 / 批复状态`<br>Back to `P7 Assess funding; record payment / approval status` / `P7 评估经费；记录付款 / 批复状态` |

问诊之后如果要财务补记，网关 `Urgent finance follow-up?` / `需要财务紧急跟进？` 走 **Yes** / **是**，到：

After the consultation, if finance must record the follow-up, `Urgent finance follow-up?` / `需要财务紧急跟进？` follows **Yes** / **是** to:

```
P8
Finance follows up
after urgent care
```

```
P8
紧急治疗后
财务跟进
```

*Clinical work not delayed solely by payment confirmation gaps* 和 D18 没有自己的方框。对应的就是 **Authorised** / **已授权** 这条线：先到 P6，付款由上面这个 P8 Finance follows up / P8 紧急治疗后财务跟进 事后做。

*Clinical work not delayed solely by payment confirmation gaps* and D18 have no box of their own. They correspond to the **Authorised** / **已授权** flow: it goes to P6 first, and payment is done afterwards by the P8 Finance follows up / P8 紧急治疗后财务跟进 box above.

*Urgent pathway supported (when required)* 也没有单独方框，就是这一整段 P8。

*Urgent pathway supported (when required)* has no separate box either. It is this whole P8 stretch.

*Safe clinical decisions*、*Timely clinical care* 是云，没有方框。

*Safe clinical decisions* and *Timely clinical care* are clouds. They have no boxes.

---

## 8. BPMN 上有方框、这张临床 SR 里没有格子

## 8. Boxes on the BPMN that have no element on this clinical SR

| BPMN 方框 / BPMN box | 和这张 SR 的关系 / Relation to this SR |
| --- | --- |
| P13<br>Authorised manager reviews<br>audit trail and pathway reports<br>授权管理人员查看<br>审计记录和路径报表 | 没有对应格子。做完结束在 `Report reviewed` / `报表已查看`<br>No matching element. It ends at `Report reviewed` / `报表已查看` |
| P10<br>Resolve administrative<br>enquiry; record response<br>处理行政咨询；<br>记录答复 | 没有对应格子。结束在 `Enquiry resolved` / `咨询已处理`<br>No matching element. It ends at `Enquiry resolved` / `咨询已处理` |
| P10<br>CNS / clinician responds<br>and records clinical advice<br>专科护士 / 临床人员答复<br>并记录临床建议 | 没有对应格子。结束在 `Enquiry resolved` / `咨询已处理`<br>No matching element. It ends at `Enquiry resolved` / `咨询已处理` |
| P10<br>Finance responds to<br>payment / funding enquiry<br>财务答复<br>付款 / 经费咨询 | 没有对应格子。结束在 `Enquiry resolved` / `咨询已处理`<br>No matching element. It ends at `Enquiry resolved` / `咨询已处理` |
| P7<br>Assess funding; record<br>payment / approval status<br>评估经费；记录<br>付款 / 批复状态 | 没有对应格子。只有它的 **Urgent review** / **紧急复核** 线接到第 7 节的 P8<br>No matching element. Only its **Urgent review** / **紧急复核** flow connects to the P8 in section 7 |
| P7<br>Send payment request<br>to external provider<br>向外部服务商<br>发送付款请求 | 没有对应格子<br>No matching element |
| P7<br>Payment result<br>received<br>收到<br>付款结果 | 没有对应格子<br>No matching element |
| P7<br>Resolve funding issue /<br>investigate missing receipt<br>处理经费问题 /<br>追查缺失回执 | 没有对应格子<br>No matching element |
| P7<br>Mark payment<br>investigate<br>标记付款<br>待追查 | 没有对应格子<br>No matching element |
| P7 / P11 / P12<br>Approve and record refund,<br>payment transfer or retention<br>批准并记录退款、<br>转账或保留费用 | 没有对应格子<br>No matching element |
| P7 / P11 / P12<br>Request refund /<br>record adjustment<br>请求退款 /<br>记录调整 | 没有对应格子<br>No matching element |
| P11 / P12<br>Authorise modification,<br>follow-up or cancellation<br>授权变更、<br>复诊或取消 | 没有对应格子。SR 里的 follow-up / 复诊 是第 4 节 `Clinical plan?` / `临床计划？` 的 **Follow-up** / **复诊** 线，回到 Book visit / 预约就诊<br>No matching element. Follow-up / 复诊 on the SR is the **Follow-up** / **复诊** flow from `Clinical plan?` / `临床计划？` in section 4, which returns to Book visit / 预约就诊 |
| P11 / P12<br>Notify care change<br>通知护理变更 | 没有对应格子<br>No matching element |
| P3<br>Appointment booked;<br>await attendance<br>已经预约；<br>等待到诊 | 没有对应格子。是 Book visit / 预约就诊 之后的等待<br>No matching element. It is the wait after Book visit / 预约就诊 |
| P4<br>Record declined<br>appointment<br>记录患者<br>拒绝预约 | 没有对应格子<br>No matching element |
| P4<br>Record did not<br>attend<br>记录<br>未到诊 | 没有对应格子<br>No matching element |

`Request type?` / `请求类型？` 用来把登记送进转诊、补材料、三类咨询、变更或报表。SR 只使用其中转到 P2 审阅的那条 **Referral** / **转诊**。

`Request type?` / `请求类型？` sends the registration on to a referral, missing documents, the three kinds of enquiry, a change, or a report. The SR uses only the **Referral** / **转诊** flow, which goes to the P2 review.

---

## 9. 第 10 组反馈改了哪些方框

## 9. Which boxes the Group 10 feedback changed

原版是 `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`。上面第 1–7 节的 P1、P2、P5、P6、P8、P9 方框原版就有，正文没有改名。

The original file is `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`. The P1, P2, P5, P6, P8 and P9 boxes in sections 1–7 were already there. Their text was not renamed.

反馈第 3 条是合并网关。图上是空菱形，没有 P 编号，也不写业务字。它们只挡在方框前面，把原来直接扎进方框的几条线先收成一条：

Feedback item 3 is the joining gateways. On the diagram they are empty diamonds. They have no P number and no business wording. They only sit in front of a box, and gather into one flow the flows that used to enter that box directly:

| 空菱形 / Empty diamond | 挡在这个方框前面 / Sits in front of this box |
| --- | --- |
| Join_BookVisit | P3 / P4 / P12 Book visit; notify patient; record attendance / contact<br>P3 / P4 / P12 预约就诊；通知患者；记录到诊 / 联系 |
| Join_VisitOutcome | Visit outcome? / 就诊结果？ |
| Join_ClinicalCare | P5 / P9 / P12 Consult / treat / review; authorise care and clinic letter<br>P5 / P9 / P12 问诊 / 治疗 / 复查；授权护理和诊后信 |
| Join_Funding | P7 Assess funding; record payment / approval status<br>P7 评估经费；记录付款 / 批复状态 |
| Join_BookTreatment | P6 Confirm authorised treatment and investigation appointments<br>P6 确认已授权的治疗和检查预约 |
| Join_ClinicalChange | P11 / P12 Authorise modification, follow-up or cancellation<br>P11 / P12 授权变更、复诊或取消 |
| Join_MarkPaymentInvestigate | P7 Mark payment investigate<br>P7 标记付款待追查 |

反馈第 4 条是把就诊结果拆开。原版 `Visit outcome?` / `就诊结果？` 上有一条线叫 **Cancel / DNA**，直接进 `P11 / P12 Authorise modification, follow-up or cancellation` / `P11 / P12 授权变更、复诊或取消`。

Feedback item 4 splits the visit outcome. On the original, `Visit outcome?` / `就诊结果？` had one flow called **Cancel / DNA**, which went straight into `P11 / P12 Authorise modification, follow-up or cancellation` / `P11 / P12 授权变更、复诊或取消`.

V2 的 `Visit outcome?` / `就诊结果？` 改成这些线，并多了三个方框、一个网关：

On V2, `Visit outcome?` / `就诊结果？` uses these flows, and three boxes plus one gateway were added:

| 线上的字 / Wording on the flow | 下一方框 / Next box |
| --- | --- |
| Attended<br>已到诊 | P5 / P9 / P12 Consult / treat / review; authorise care and clinic letter<br>P5 / P9 / P12 问诊 / 治疗 / 复查；授权护理和诊后信 |
| Booked<br>已预约 | P3 Appointment booked; await attendance<br>P3 已经预约；等待到诊 |
| Pending / retry<br>待定 / 重试 | 回到 P3 / P4 / P12 Book visit… / 预约就诊……<br>Back to P3 / P4 / P12 Book visit… / 预约就诊…… |
| Patient cancelled<br>患者取消 | P11 / P12 Authorise modification, follow-up or cancellation<br>P11 / P12 授权变更、复诊或取消 |
| Declined<br>已拒绝 | P4 Record declined appointment / P4 记录患者拒绝预约，然后再进上面的 P11 / P12<br>P4 Record declined appointment / P4 记录患者拒绝预约, then into the P11 / P12 box above |
| Did not attend<br>未到诊 | P4 Record did not attend / P4 记录未到诊，然后再进上面的 P11 / P12<br>P4 Record did not attend / P4 记录未到诊, then into the P11 / P12 box above |

Book visit / 预约就诊 之后多了网关 `Reserve a slot?` / `需要占号源？`。**Booked, attended or waiting** / **已预约、已到诊或等待中** 去 `P3 Check / reserve outpatient slot` / `P3 查询 / 占用门诊号源`。**Declined, cancelled or DNA** / **拒绝、取消或未到诊** 跳过查号，直接到 `Visit outcome?` / `就诊结果？`。

After Book visit / 预约就诊 there is a new gateway, `Reserve a slot?` / `需要占号源？`. **Booked, attended or waiting** / **已预约、已到诊或等待中** goes to `P3 Check / reserve outpatient slot` / `P3 查询 / 占用门诊号源`. **Declined, cancelled or DNA** / **拒绝、取消或未到诊** skips the slot check and goes straight to `Visit outcome?` / `就诊结果？`.

反馈第 1、第 2 条不增加方框。日期、金额、下拉和必填写在这些方框打开的表单上：Book visit / 预约就诊 的日期和时间、Review referral / 审阅转诊 的决定、Clinical care / 临床护理 的治疗 / 复诊 / 出院、Funding / 经费 的金额。

Feedback items 1 and 2 add no boxes. Dates, amounts, dropdowns and required fields sit on the forms these boxes open: the date and time on Book visit / 预约就诊, the decision on Review referral / 审阅转诊, treatment / follow-up / discharge on Clinical care / 临床护理, and the amount on Funding / 经费.
