# ruby：Part 1 讨论记录

> 会议总结（类飞书纪要）  
> **主题**：Case Study — Hospital Patient Referral, Treatment and Administration System  
> **时间**：2026-09-14  
> **参会**：  
> - A：Hao Zheng（Ruby Zheng，23084382）  
> - B：Geping Chen（Estrella Chen，23084393）  
> - C：Minghao Qin（Ender Qin，23084402）  
> - D：Guanyan He（HeGuanYan He，23084395）  

---

## 会议摘要

小组对照案例原文讨论 Part 1，明确患者路径从 GP/其他医院转诊开始，经就诊、诊断、治疗、随访与持续沟通；信息目前分散在医院系统、电子表单、邮件、电话、信件和手工记录中，难以监控进度、发现延迟并保留完整审计，因此拟引入 Hospital Patient Administration System。

---

## 发言记录

### A · Hao Zheng（Ruby Zheng）
1. 主流程按原文串：Medical Secretaries 收转诊并核材料 → Consultant 接受/拒绝/补信息/转专科 → 仅接受后方可约 New Patient Appointment → 就诊后授权 Treatment Booking Request → 治疗预约与资金/支付 → Clinic Letter → 咨询分流。  
2. 组织上须保持 clinical decisions、administrative responsibilities、financial activities 的区分，不能混权。

### B · Geping Chen（Estrella Chen）
1. 主要参与者包括 Medical Secretaries、Outpatient Bookings、Call Handling、CNS 及其行政支持、Treatment and Chemotherapy Bookings、Patient Pathway Coordinators、Consultants、Finance、Administrative Management，以及患者与转诊方。  
2. 关键规则：秘书不得评估临床适宜性或决定是否接受；决策须记录原因与决策人；无临床授权的治疗请求行政不得处理；Call handlers 不得诊断、解读化验或给出临床建议。

### C · Minghao Qin（Ender Qin）
1. 关键需求：支持完整患者路径与团队协同；关键动作可审计；按角色访问；对接外部排班、通信与支付；能反映积压、延迟信件、未完成支付与咨询等。  
2. 案例写明 urgent clinical 判定规则医院尚未完全约定，需向相关方（tutor）进一步确认，并记录合理假设。

### D · Guanyan He（HeGuanYan He）
1. 外部服务/组织：external scheduling、correspondence、Payment Service Provider，以及 external treatment / laboratory / imaging；另有 referring organisation、insurer/funding organisation。  
2. 异常要点：外部不可用则 booking pending 且防重复预约；支付成功但无回执须标调查而非自动再扣；改期须正式 Treatment Modification Request，口头/邮件无效。

---

## 待办

| 事项 | 负责人 |
|------|--------|
| 整理 Part 1 案例摘要成文 | 全组（见 `ruby：part1案例摘要.md`） |
| 紧急咨询判定规则确认 | 待问 tutor |
| 外部排班/支付本期 mock 边界写入假设 | Minghao Qin / Guanyan He |
