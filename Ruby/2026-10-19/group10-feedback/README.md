# 第10组反馈改动（先放在这里，未覆盖 Week6 / Week3 原文件）

来源图：`Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn`。  
原图没有改。这份是可以打开、可以部署的副本。

## 四条反馈现在怎样

| 条 | 原文 | 这次 |
| --- | --- | --- |
| 1 | 每个输入框要用对的数据类型 | 表单：预约用日期/时间，金额和周期用数字，决定用下拉。患者编号、姓名加上格式，纯数字不能通过。 |
| 2 | 缺项和非法输入不能提交 | 表单：必填、最短长度、编号/姓名格式。新预约不能选过去的日期。拒绝、取消、未到诊不再强迫填一个未来日期。选「已寄出」必须勾选临床已批准。 |
| 3 | 多条路径先汇合再进任务 | 组员已经加过 `Join_BookVisit`、`Join_ClinicalCare`、`Join_Funding`、`Join_BookTreatment`，以及就诊结果、临床变更、付款调查三处。这次补上仍然直接进任务的五处：`Join_Register`、`Join_GetDocuments`、`Join_ReviewReferral`、`Join_DispatchLetter`、`Join_FinanceAdjustment`。都是只汇合、不写条件。 |
| 4 | 选项要盖住相关业务情形 | 决定项的取值本来就已经对上网关，没有再加对不上条件的新值。临床护理的「复诊」改成写明「推迟本周期 / 要求复诊」，取值仍是 `follow_up`。 |

部分退款必须小于原收费：Camunda 表单不能拿两个字段互相比较。金额范围仍在表单上，大小关系仍由 `request-refund` 工作器拒绝。

## 文件夹

- `Hospital_All_Processes_V2.bpmn`：补了五个汇合网关的新图
- `forms/`：12 份表单
- `.process-application`：让 Modeler 把图和表单一起部署
- `istar/可提高处.md`：对照 i\* 之后建议改、以及不要改的地方

## 部署

用 Camunda Modeler 打开本文件夹（识别为 Process Application），部署整个应用，不要只部署 BPMN。表单是按 `formId` 引用的，只部署图的话任务会找不到表单。

流程 id 仍是 `Hospital_All_Processes_V2_C8`。

不要同时运行 `Week3 Coursework/hospital-pathway` 的 `mvn spring-boot:run`。那个程序部署的仍是旧图 `W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`，会把引擎里的流程换回第一版。
