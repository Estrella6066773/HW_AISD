# AISD submission documents (UFCEP6-0-3)

The 29 September announcement requests a detailed operational BPMN, an Acceptance Test Plan, a Justification of Decisions and supporting editable/PDF files. Those documents describe the **initial release**, which used the [29 September Camunda 8 BPMN](<../../Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn>), the [forms](<../../Week3 Coursework/hospital-pathway/forms/>) and the [Java module](<../../Week3 Coursework/hospital-pathway/>), all shared with BPM&EA under `Week3 Coursework/hospital-pathway/`.

The 29 September model's process id is `Hospital_All_Processes_Simple_C8`. It does not contain the split visit outcomes. The improved model for the second release is [`Hospital_All_Processes_V2.bpmn`](<../../Week6 Coursework/bpmn/Hospital_All_Processes_V2.bpmn>), process id `Hospital_All_Processes_V2_C8`; see the [Week 6 folder index](<../../Week6 Coursework/README.md>) for the full second-release working set.

| AISD written deliverable | Submitted file |
| --- | --- |
| Justification of Decisions for the whole A/B/C/D group | [Design decisions](Group_Design_Decisions_2026-09-29.pdf) |
| Acceptance Test Plan and Results, with honest version/evidence limits | [Acceptance record](Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf) |
| Readable operational BPMN export | [Nine-page vector PDF](Hospital_All_Processes_Camunda8_Export_2026-09-29.pdf). Editable model: [29 September Camunda 8 BPMN](<../../Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn>) |

The [shared evidence](<../../Week3 Coursework/hospital-pathway/evidence/>) contains twelve current Java tests (A/D), four BPMN structural checks and a live final-model G07 run to `COMPLETED` ([JSON](<../../Week3 Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json>)). The acceptance record distinguishes this selected self-pay route from unverified B/C exception branches, D's live change route and the known role-access failure. The BPMN PDF contains one zoomable overview and eight detail views.

These files were first uploaded to `main` in `e8a6861`. The G07 run and the Java tests remain tied to the initial-release source, tagged `submission-2026-09-29` (`f6fec99`); worker source, forms and the executable BPMN have changed since then, so those results describe that tagged baseline rather than the current tree. The G07 run proves one route, not full acceptance of every business rule or browser-side form validation. Group second-owner review remains open. The local c8run environment is not available for a repeat run.
