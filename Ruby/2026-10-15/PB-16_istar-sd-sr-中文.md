# PB-16 · i\* 战略依赖（SD）与战略理由（SR）模型

**待办条目**：PB-16 · i\* SD/SR 模型  
**第一负责人**：Estrella  
**第二负责人**：Ryan / Guanyan He  
**范围**：医院患者管理系统（Hospital Patient Administration System）的首期发布  
**日期**：2026-09-29  

**相关来源**：

- 考核任务 02：`W01/S03 - Assessment Introduction(1).pptx`
- 案例：`W01/Case Study - Hospital Patient Referral, Treatment and Administration System.docx`
- 可执行范围仅作对照：`Week3 Coursework/hospital-pathway/README.md` 与 `Week3 Coursework/hospital-pathway/bpmn/Hospital_All_Processes_V2.bpmn`
- 图文件：[`PB-16_sd.md`](../../docs/istar/PB-16_sd.md)、[`PB-16_sr.md`](../../docs/istar/PB-16_sr.md)、演示用图 [`PB-16_sd-overview.png`](../../docs/istar/PB-16_sd-overview.png)

> 本文是 `docs/istar/PB-16_istar-sd-sr.md` 的中文译本，供 Ruby 对照改图与答辩；正式交稿以英文原文为准。

---

## 1. 目的

本文件给出首期发布的 i\*（读作 “i star”）模型。i\* 是一种社会技术建模语言。SD（战略依赖）模型说明：谁依赖谁、依赖什么。SR（战略理由）模型展开每个参与者内部的目标、软目标、任务与资源，并说明这些元素如何支撑 SD 中的依赖。

考核要求小组识别关键参与者、目标、软目标、任务、资源与依赖；解释建模选择与假设；并保持 SD 与 SR 彼此一致。

---

## 2. 建模选择

1. **按首期发布做抽象。** 参与者按战略职责合并，而不是按案例里每一个职位单独画。医务秘书、门诊预约、治疗与化疗预约、呼叫处理、患者路径协调员、行政管理一并归为 `AdministrativeTeam`。顾问医生、专科护士团队及其他获授权临床人员一并归为 `ClinicalTeam`。不同外部服务仍分开建模，因为失败模式与依赖物不同。
2. **PB-16 要求的五类依赖。** SD 覆盖转诊机构、临床、行政、财务与外部组织相关的依赖。患者与医院患者管理系统也建模，因为案例核心是患者路径协调。
3. **依赖物类型。** 每条 SD 边标注一种 i\* 依赖物类型：目标（goal）、软目标（softgoal）、任务（task）或资源（resource）。
4. **可执行 BPMN 不是战略模型。** Camunda 路径只用来确认首期打算支持哪些阶段。它不能替代 SD/SR；课堂里的外部排班/支付/通信模拟记为假设，不当成真实外部能力。
5. **本期不承诺的能力。** 管理报表、身份去重、患者沟通偏好、离线补录等列在第 8 节，作为本 SR 范围外，即使案例提到也不画进本期交付能力。

---

## 3. 假设

| ID | 假设 |
|----|------|
| A1 | 首期支持主路径：转诊核验、顾问决策、门诊预约、治疗授权、经费判定、支付处理（含失败与回执缺失）、正式治疗变更及财务跟进、诊后信管理、咨询分流。 |
| A2 | 课堂实现中外部排班与支付接口是模拟的。i\* 仍把外部组织当作真实被依赖方；模拟是实现边界，不是否认依赖。 |
| A3 | 基于角色的登录强制（PB-22）是待办要求，本 SR **不**把它当作已交付能力。模型记录“角色相称访问”软目标，但不声称强制认证已实现。 |
| A4 | 普通用户不得改写重大动作的审计记录。生产级不可变审计存储可能超出课堂存储能力；软目标仍然保留。 |
| A5 | 医院尚未定完整的临床咨询紧急分级规则。模型要求紧急临床问题升级给临床人员，但不编造完整分级政策。 |
| A6 | 临床决策、行政执行与财务审批保持分离。行政或财务不得越权接受转诊、授权治疗或批准退款；权限以案例分配为准。 |
| A7 | “ExternalClinicalServices” 合并为治疗预约提供可用性的外部治疗、化验与影像服务。 |
| A8 | 同一套参与者与假设 A1–A8 同时适用于 SD 与 SR。 |

---

## 4. 参与者

| 参与者 ID | 名称 | PB-16 覆盖类别 | 理由 |
|----------|------|----------------|------|
| RO | ReferringOrganisation（转诊机构） | 转诊机构 | 全科医生或其他医院提交转诊，并可能需要路径结果信息 |
| PT | Patient（患者） | 利益相关者（患者路径） | 接受护理、预约、信件、收费与临床建议 |
| CL | ClinicalTeam（临床团队） | 临床 | 顾问与获授权临床人员：决定转诊、护理、信件与变更 |
| AD | AdministrativeTeam（行政团队） | 行政 | 秘书、预约、呼叫处理与路径协调，执行非临床路径工作 |
| FI | FinanceTeam（财务团队） | 财务 | 经费判定、支付请求、退款与财务咨询 |
| ESS | ExternalSchedulingService（外部排班服务） | 外部组织 | 提供门诊及相关预约号源 |
| ECS | ExternalClinicalServices（外部临床服务） | 外部组织 | 提供外部治疗、化验或影像可用性 |
| ECSND | ExternalCorrespondenceService（外部通信服务） | 外部组织 | 投递已批准信件及相关外发通信 |
| PSP | PaymentServiceProvider（支付服务商） | 外部组织 | 处理支付与退款交易并返回核验结果 |
| FO | FundingOrganisation（资助机构） | 外部组织 | 保险公司或资助方，出具经费批复 |
| HPAS | HospitalPatientAdministrationSystem（医院患者管理系统） | 社会技术系统 | 协调路径工作、记录决策、中介外部请求 |

---

## 5. SD 依赖目录

读法：**依赖者（Depender）** 依赖 **被依赖者（Dependee）** 以获得 **依赖物（dependum）**。下表每一行都出现在 [`PB-16_sd.md`](../../docs/istar/PB-16_sd.md)，并在 [`PB-16_sr.md`](../../docs/istar/PB-16_sr.md) 中有对应。

| ID | 依赖者 | 被依赖者 | 类型 | 依赖物 | 案例依据（摘要） |
|----|--------|----------|------|--------|------------------|
| D1 | AdministrativeTeam | ReferringOrganisation | 资源 | Supporting referral documents（转诊支持材料） | 秘书核验信件、结果与报告；可向转诊方索取缺件 |
| D2 | ReferringOrganisation | ClinicalTeam | 目标 | Referral decision recorded（转诊决定已记录） | 顾问接受、拒绝、要求补材料或转专科；原因与决策人须记录 |
| D3 | ReferringOrganisation | AdministrativeTeam | 任务 | Communicate pathway outcome to referrer when required（必要时向转诊方通报路径结果） | 拒绝、转诊、爽约或出院等路径可能需要通知转诊方 |
| D4 | ClinicalTeam | AdministrativeTeam | 资源 | Checked referral package（已核验的转诊材料包） | 行政核验材料后才能开始临床审阅 |
| D5 | AdministrativeTeam | ClinicalTeam | 目标 | Authorised acceptance before a new patient appointment（新患者门诊预约前须有授权接受） | 仅在获授权顾问接受转诊后，才可安排新患者门诊。后续随访由临床提出，不属于本依赖 |
| D6 | AdministrativeTeam | ClinicalTeam | 资源 | Authorised treatment booking request（已授权的治疗预约请求） | 行政不得处理未经授权的治疗请求 |
| D7 | AdministrativeTeam | ClinicalTeam | 目标 | Clinic letter clinically approved（诊后信已获临床批准） | 秘书仅在顾问批准后分发；不得改动临床含义 |
| D8 | ClinicalTeam | AdministrativeTeam | 任务 | Arrange clinic and treatment appointments（安排门诊与治疗预约） | 预约组在临床授权后使用排班与外部临床服务 |
| D9 | AdministrativeTeam | ExternalSchedulingService | 资源 | Available appointment slot（可用预约号源） | 门诊与随访预约使用外部排班服务 |
| D10 | AdministrativeTeam | ExternalClinicalServices | 资源 | External treatment, laboratory or imaging availability（外部治疗/化验/影像可用性） | 部分治疗预约依赖外部提供方。不可用时预约保持挂起且不重复建号。假设 A7 将治疗、化验、影像并为一个被依赖方。排班见 D9 |
| D11 | AdministrativeTeam | ExternalCorrespondenceService | 任务 | Send appointment letters and approved clinic letters（发送预约信与已批准诊后信） | 通信服务向患者发预约信，并向顾问指定的收件人发已批准诊后信。收件人可包括患者、GP、其他医院或其他专业人员 |
| D12 | Patient | ClinicalTeam | 目标 | Appropriate clinical assessment and care（恰当的临床评估与护理） | 会诊、诊断、治疗选项、专科护士建议、继续治疗适宜性等 |
| D13 | ClinicalTeam | Patient | 目标 | Informed consent to treatment（知情同意治疗） | 仅在患者同意且同意已记录后才推进治疗 |
| D14 | AdministrativeTeam | FinanceTeam | 目标 | Normal-route clearance before treatment confirmation（正常路径下治疗确认前的经费/支付清讫） | 正常路径确认治疗预约前，财务须记录本院经费、保险批复、已核验患者付款、豁免或其他授权安排。临床因付款未到而授权的紧急治疗属 D18，不算 D14 失败 |
| D15 | FinanceTeam | FundingOrganisation | 资源 | Funding approval record（经费批复记录） | 财务记录机构、授权参考号、金额与限制 |
| D16 | FinanceTeam | PaymentServiceProvider | 资源 | Verified payment or refund result（已核验的支付或退款结果） | 提供方返回状态、交易参考号、日期与金额；回执缺失应调查，不得自动再扣一笔 |
| D17 | Patient | FinanceTeam | 目标 | Charging and refunds follow the recorded rules（收费与退款遵循已记录规则） | 支付失败或不完整时须告知患者。再次尝试不得对同一预约产生第二次扣款。退款仅在授权财务决定之后 |
| D18 | ClinicalTeam | FinanceTeam | 软目标 | Urgent care not blocked solely by payment delay（紧急护理不得仅因付款延迟被挡住） | 临床可凭记录原因授权紧急治疗；财务事后处理 |
| D19 | FinanceTeam | ClinicalTeam | 资源 | Treatment and modification context for charges（收费用的治疗与变更上下文） | 财务需要临床治疗或变更事实，才能判定经费、支付或退款 |
| D20 | Patient | AdministrativeTeam | 任务 | Recorded appointment notification and contact attempts（已记录的预约通知与联系尝试） | 信件，外加两周内电话联系；每次尝试与结果须记录 |
| D21 | AdministrativeTeam | ClinicalTeam | 任务 | Handle escalated clinical enquiry（处理升级后的临床咨询） | 接线员不得诊断或给临床建议；临床咨询转专科护士或获授权临床人员 |
| D22 | AdministrativeTeam | HospitalPatientAdministrationSystem | 软目标 | Traceable pathway without duplicate bookings（可追溯路径且无重复预约） | 系统支持挂起预约、重试与路径可见性，不虚构重复预约 |
| D23 | FinanceTeam | HospitalPatientAdministrationSystem | 软目标 | Auditable payment trail without full card storage（可审计支付轨迹且不存完整卡号） | 系统不得存储完整卡号；重大支付动作仍可审计 |
| D24 | ClinicalTeam | HospitalPatientAdministrationSystem | 软目标 | Recorded clinical authorisations for ordinary-user immutability（已记录的临床授权对普通用户不可改） | 转诊决定、治疗授权、信件批准与变更须记录，使普通用户无法改写 |

**依赖条数**：24。

五类覆盖示例：

| 类别 | 示例依赖 ID |
|------|-------------|
| 转诊机构 | D1, D2, D3 |
| 临床 | D2, D4–D8, D12, D13, D18, D19, D21, D24 |
| 行政 | D1, D3–D11, D14, D20–D22 |
| 财务 | D14–D19, D23 |
| 外部组织 | D9–D11, D15, D16 |

---

## 6. 按参与者列出的目标、软目标、任务与资源

以下是 SR 用语。首期**不**承诺作为产品功能交付的软目标，会在第 8 节再次列出。

### 6.1 ReferringOrganisation（转诊机构）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Referral decision recorded（转诊决定已记录） | 依赖 D2。决定可为接受、拒绝、要求补材料或转专科 |
| 任务 | Submit referral with supporting documents（提交转诊及支持材料） | 提供 D1 |
| 软目标 | Timely feedback on rejection, redirect or DNA（对拒绝、转诊或爽约的及时反馈） | 经 D3 支持 |

### 6.2 Patient（患者）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Receive appropriate specialist care（获得恰当专科护理） | 依赖 D12 |
| 目标 | Charging and refunds follow the recorded rules（收费与退款遵循已记录规则） | 依赖 D17 |
| 任务 | Attend or respond to appointment contacts（出席或回应预约联系） | 患者在被联系后的自身回应 |
| 目标 | Give or withhold informed consent（给予或拒绝知情同意） | 提供 D13 |
| 软目标 | Timely, understandable communication（及时、可理解的沟通） | 依赖 D20。D11 是行政对通信服务的依赖，不是患者的。偏好见第 8 节 |

### 6.3 ClinicalTeam（临床团队）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Make safe referral and treatment decisions（做出安全的转诊与治疗决定） | 使用 D4；提供 D2、D6、D7。仅当记录的决定是接受新患者转诊时才提供 D5 |
| 目标 | Clinic and treatment appointments arranged after authorisation（授权后安排门诊与治疗预约） | 依赖 D8 |
| 目标 | Obtain informed consent before treatment（治疗前取得知情同意） | 依赖 D13 |
| 任务 | Review referral and record decision（审阅转诊并记录决定） | 提供 D2。仅当决定为接受时才提供 D5 |
| 任务 | Authorise treatment booking request（授权治疗预约请求） | 提供 D6 |
| 任务 | Approve clinic letter content（批准诊后信内容） | 提供 D7 |
| 任务 | Respond to escalated clinical enquiries（回应升级后的临床咨询） | 提供 D21 |
| 任务 | Authorise treatment modification when care must change（护理须变更时授权治疗修改） | 供给 D19 |
| 资源 | Checked referral package（已核验的转诊材料包） | 来自 D4 |
| 软目标 | Clinical work not delayed solely by payment confirmation gaps（临床工作不得仅因支付确认缺口而延误） | 依赖 D18 |
| 软目标 | Clinical authorisations remain recorded and protected from ordinary alteration（临床授权保持记录且防普通改写） | 依赖 D24 |

### 6.4 AdministrativeTeam（行政团队）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Keep the patient pathway moving within clinical authorisations（在临床授权范围内推进患者路径） | 在覆盖范围内使用 D6、D7 |
| 目标 | Authorised acceptance before a new patient appointment（新患者门诊预约前须有授权接受） | 来自 D5。仅适用于新患者门诊，不适用于后续随访 |
| 任务 | Check referral documents and request missing items（核验转诊材料并索取缺件） | 消耗 D1；提供 D4 |
| 任务 | Book clinic and treatment appointments（预约门诊与治疗） | 提供 D8。门诊预约用 D9；治疗预约用 D10；新患者门诊还用 D5；正常路径治疗确认用 D14 |
| 任务 | Notify patient and record contact attempts（通知患者并记录联系尝试） | 提供 D20；预约信用 D11 |
| 任务 | Distribute approved clinic letters（分发已批准诊后信） | 使用 D7，诊后信用 D11 |
| 任务 | Route enquiries; escalate clinical matters（分流咨询；升级临床事项） | 使用 D21 |
| 任务 | Communicate pathway outcome to the referrer when required（必要时向转诊方通报路径结果） | 提供 D3 |
| 资源 | Authorised treatment booking request（已授权的治疗预约请求） | 来自 D6 |
| 资源 | Available appointment slot（可用预约号源） | 来自 D9 |
| 资源 | External treatment, laboratory or imaging availability（外部治疗/化验/影像可用性） | 来自 D10 |
| 软目标 | No duplicate bookings when external services fail（外部服务失败时不产生重复预约） | 依赖 D22 |

### 6.5 FinanceTeam（财务团队）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Record normal-route clearance before treatment confirmation（正常路径治疗确认前记录清讫） | 提供 D14；使用 D15、D19。付款未到却紧急治疗属 D18 |
| 目标 | Collect or refund money correctly（正确收款或退款） | 使用 D16；提供 D17 |
| 任务 | Record funding approval details（记录经费批复明细） | 使用 D15 |
| 任务 | Request payment or refund via the provider（经提供方请求支付或退款） | 使用 D16 |
| 任务 | Investigate missing payment confirmation without automatic re-charge（调查缺失支付回执且不自动再扣） | 使用 D16、D23 |
| 资源 | Treatment and modification context（治疗与变更上下文） | 来自 D19 |
| 资源 | Funding approval record（经费批复记录） | 来自 D15 |
| 资源 | Verified payment or refund result（已核验的支付或退款结果） | 来自 D16 |
| 软目标 | Separate financial authority from clinical necessity decisions（财务权限与临床必要性决策分离） | 支持 D18，对齐 A6。该软目标不是正常路径清讫目标的实现手段 |
| 软目标 | Auditable payments without storing full card data（可审计支付且不存完整卡数据） | 依赖 D23 |

### 6.6 ExternalSchedulingService（外部排班服务）

| 种类 | 名称 | 关联 |
|------|------|------|
| 资源 | Available appointment slot（可用预约号源） | 提供 D9 |
| 软目标 | Return availability reliably enough for pending/retry handling（足够可靠地返回可用性以支持挂起/重试） | 支持 D22 |

### 6.7 ExternalClinicalServices（外部临床服务）

| 种类 | 名称 | 关联 |
|------|------|------|
| 资源 | External treatment, laboratory or imaging availability（外部治疗/化验/影像可用性） | 提供 D10 |
| 软目标 | Signal unavailability so bookings stay pending without duplicates（标明不可用，使预约挂起且不重复） | 支持 D22 |

### 6.8 ExternalCorrespondenceService（外部通信服务）

| 种类 | 名称 | 关联 |
|------|------|------|
| 任务 | Deliver outbound correspondence（投递外发通信） | 提供 D11 |

### 6.9 PaymentServiceProvider（支付服务商）

| 种类 | 名称 | 关联 |
|------|------|------|
| 任务 | Process payment or refund（处理支付或退款） | 支持 D16 |
| 资源 | Verified payment or refund result（已核验的支付或退款结果） | 提供 D16 |

### 6.10 FundingOrganisation（资助机构）

| 种类 | 名称 | 关联 |
|------|------|------|
| 资源 | Funding approval record（经费批复记录） | 提供 D15 |

### 6.11 HospitalPatientAdministrationSystem（医院患者管理系统）

| 种类 | 名称 | 关联 |
|------|------|------|
| 目标 | Coordinate referral, booking, funding, payment and letter stages（协调转诊、预约、经费、支付与信件阶段） | 支持 D22–D24 |
| 软目标 | Traceable pathway without duplicate bookings（可追溯路径且无重复预约） | 锚定 D22 |
| 软目标 | Auditable payment trail without full card storage（可审计支付轨迹且不存完整卡号） | 锚定 D23 |
| 软目标 | Recorded clinical authorisations with ordinary-user immutability（已记录临床授权且对普通用户不可改） | 锚定 D24 |
| 软目标 | Role-appropriate access（角色相称访问；承认需求，不声称已强制交付） | 见 A3 与第 8 节 |

---

## 7. SD–SR 相互印证表

每条 SD 依赖都必须出现在 SR 中。下表把每条依赖映射到承载它的 SR 位置。

| SD ID | SR 位置（参与者内部元素 ↔ 依赖物） |
|-------|-------------------------------------|
| D1 | 行政任务「核验转诊材料…」↔ 转诊机构任务「提交转诊及支持材料」 |
| D2 | 转诊机构目标「转诊决定已记录」↔ 临床任务「审阅转诊并记录决定」 |
| D3 | 转诊机构软目标「及时反馈…」↔ 行政任务「必要时向转诊方通报路径结果」 |
| D4 | 临床资源「已核验的转诊材料包」↔ 行政任务「核验转诊材料…」 |
| D5 | 行政目标「新患者门诊预约前须有授权接受」↔ 临床任务「审阅转诊并记录决定」，且仅当该决定为接受 |
| D6 | 行政资源「已授权的治疗预约请求」↔ 临床任务「授权治疗预约请求」 |
| D7 | 行政信件分发任务 ↔ 临床任务「批准诊后信内容」 |
| D8 | 临床目标「授权后安排门诊与治疗预约」↔ 行政任务「预约门诊与治疗」 |
| D9 | 行政资源「可用预约号源」↔ 外部排班服务同名资源 |
| D10 | 行政资源「外部治疗/化验/影像可用性」↔ 外部临床服务同名资源 |
| D11 | 行政通知/信件任务 ↔ 外部通信服务任务「投递外发通信」 |
| D12 | 患者目标「获得恰当专科护理」↔ 临床目标「做出安全的转诊与治疗决定」 |
| D13 | 临床目标「治疗前取得知情同意」↔ 患者目标「给予或拒绝知情同意」 |
| D14 | 行政任务「预约门诊与治疗」↔ 财务目标「正常路径治疗确认前记录清讫」 |
| D15 | 财务资源「经费批复记录」↔ 资助机构同名资源 |
| D16 | 财务资源「已核验的支付或退款结果」↔ 支付服务商同名资源。提供方任务「处理支付或退款」产出该资源 |
| D17 | 患者目标「收费与退款遵循已记录规则」↔ 财务目标「正确收款或退款」 |
| D18 | 临床软目标「临床工作不得仅因支付…延误」↔ 财务软目标「财务权限与临床必要性决策分离」 |
| D19 | 财务资源「治疗与变更上下文」↔ 临床授权/变更任务 |
| D20 | 患者依赖行政任务「通知患者并记录联系尝试」；患者软目标「及时、可理解的沟通」仅部分由该任务承载 |
| D21 | 行政任务「分流咨询…」↔ 临床任务「回应升级后的临床咨询」 |
| D22 | 行政软目标「不产生重复预约…」↔ 系统软目标「可追溯路径且无重复预约」 |
| D23 | 财务软目标「可审计支付且不存完整卡数据」↔ 系统同意图软目标 |
| D24 | 临床软目标「临床授权保持记录…」↔ 系统软目标「已记录临床授权…」 |

图交叉检查：打开 [`PB-16_sd.md`](../../docs/istar/PB-16_sd.md) 与 [`PB-16_sr.md`](../../docs/istar/PB-16_sr.md)，确认每个 `D1`–`D24` 标签在两份文件中都出现。

---

## 8. 本 SR（首期）明确不在范围内

以下主题出现在案例或待办中，但**不**作为首期已承诺能力画进 SR 图：

| 主题 | 为何不作为本期承诺能力 |
|------|------------------------|
| 管理报表（量、等待时间、路径看板） | P2 待办；不承诺为首期 SR 已交付能力 |
| 跨机构患者身份去重 | 案例关切；首期不声称有专门身份匹配能力 |
| 患者沟通偏好（纸质 vs 电子、无障碍格式、代表） | P2 待办；冲突偏好仍是医院未统一做法 |
| 系统或外部服务故障后的离线补录 | 案例提到需求；首期不承诺完整离线补录流程 |
| 强制基于角色的登录 | 案例与 PB-22 要求；课堂路径目前用 demo 任务、无强制角色登录。软目标已承认；不声称已交付 |

外部排班与支付仍是真实战略被依赖方（D9、D16），即使课堂 worker 是模拟的。

---

## 9. 一致性声明

- SD 与 SR 使用同一套 11 个参与者与同一套假设 A1–A8。
- SD 目录中的每条依赖 D1–D24 都出现在第 7 节与 SR 的 Mermaid 图中。
- 属于需求但课堂构建尚未强制执行的软目标已标明（尤其是 A3 下的基于角色登录）。

---

## 10. 第二负责人复核

第二负责人：**Ryan / Guanyan He**。下列项留给人工勾选。

- [ ] 第二负责人确认参与者集合与案例及首期边界一致
- [ ] 第二负责人确认每条 SD 依赖 D1–D24 都出现在 SR 图中
- [ ] 第二负责人确认第 8 节范围外项与约定发布边界一致
- [ ] 第二负责人确认模型未声称强制角色登录已实现
- [ ] 第二负责人确认 Mermaid 图可渲染且边标签可读
