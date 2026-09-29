# AISD submission documents (UFCEP6-0-3)

The 29 September announcement requests a detailed operational BPMN, an Acceptance Test Plan, a Justification of Decisions and supporting editable/PDF files. The authoritative [Camunda 8 BPMN](../../Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn), [forms](../../Coursework/hospital-pathway/forms/) and [Java module](../../Coursework/hospital-pathway/) are shared with BPM&EA and stay under `Coursework/`.

| AISD written deliverable | PDF | Editable source |
| --- | --- | --- |
| Justification of Decisions for the whole A/B/C/D group | [Design decisions](Group_Design_Decisions_2026-09-29.pdf) | [Markdown](Group_Design_Decisions_2026-09-29.md) |
| Acceptance Test Plan and Results, with honest version/evidence limits | [Acceptance record](Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf) | [Markdown](Group_Acceptance_Test_Plan_and_Results_2026-09-29.md) |
| Readable operational BPMN export | [Nine-page vector PDF](Hospital_All_Processes_Camunda8_Export_2026-09-29.pdf) | [Editable Camunda 8 BPMN](../../Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn) |

The [shared evidence](../../Coursework/hospital-pathway/evidence/) contains twelve current Java tests (A/D), four BPMN structural checks and a live final-model G07 run to `COMPLETED` ([JSON](../../Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json)). The acceptance record distinguishes this selected self-pay route from unverified B/C exception branches, D's live change route and the known role-access failure. The BPMN PDF contains one zoomable overview and eight detail views.

These files were initially uploaded to the repository's `main` branch in `e8a6861`. The G07 run proves one route, not full acceptance of every business rule or browser-side form validation. Group second-owner review remains open.
