# BPM&EA submission documents (UFCEP4-0-3)

The 29 September announcement asks for operational BPMN, external-worker source/dependencies/configuration, editable Forms and bindings, a Project and Test Plan with results/evidence, an accessible repository and presentation slides. The technical implementation is the **shared** [`Coursework/hospital-pathway/`](../../Coursework/hospital-pathway/) module. It is not copied into this folder.

| BPM&EA item | Location or current status |
| --- | --- |
| Group Project and Test Plan | [PDF](Group_Project_and_Test_Plan_2026-09-29.pdf) · [editable Markdown](Group_Project_and_Test_Plan_2026-09-29.md) |
| Operational Camunda 8 BPMN | [Editable BPMN](../../Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn) |
| Readable process diagram | [Nine-page vector PDF](../AISD/Hospital_All_Processes_Camunda8_Export_2026-09-29.pdf), exported from the shared editable BPMN |
| Worker code, dependencies and configuration | [Java module](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/) · [pom.xml](../../Coursework/hospital-pathway/pom.xml) · [runnable application.yaml](../../Coursework/hospital-pathway/src/main/resources/application.yaml) · [configuration template](../../Coursework/hospital-pathway/config/application.example.yaml) |
| Editable Forms and bindings | [11 forms](../../Coursework/hospital-pathway/forms/) · bindings in the shared BPMN |
| Planning sources | [Product backlog](../../docs/p3-product-backlog.md) · [Sprint backlog](../../docs/p6-sprint-backlog.md) · [work breakdown](../../docs/p4-work-breakdown.md) · [Definition of Done](../../docs/definition-of-done.md) |
| Strategic BPMN | [Non-executable model](../../docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn) · [abstraction note](../../docs/strategic-bpmn/PB-12_abstraction-level_2026-09-29.md). Added in `7be65b4`. Second-owner review is still unsigned. |
| i\* SD/SR | [Notes](../../docs/istar/PB-16_istar-sd-sr.md) · [SD](../../docs/istar/PB-16_sd.md) · [SR](../../docs/istar/PB-16_sr.md). Added in `7be65b4`. Second-owner checklist is still unsigned. |
| Alignment evaluation | [Traceability matrix](../../docs/requirements-traceability-matrix.md): BR-01 to BR-42, 12 supported, 26 partial, 4 unsupported, with the second-release plan in section 3 |
| Test results/evidence | [Shared test logs and live final-model G07 JSON](../../Coursework/hospital-pathway/evidence/) · historical PB-14/PB-18 logs described in the Project and Test Plan. Executable evidence baseline remains `fc6293e`. |
| Repository | `https://github.com/Estrella6066773/HW_AISD` — current `main` is `91a02c9`. The submission pack was first uploaded in `e8a6861`. Group second-owner review remains open. There is no final release tag. |
| Presentation slides | [Eight-slide editable BPM&EA deck](Hospital_Pathway_BPMEA_Presentation_2026-09-29.pptx). The group has given the presentation. |

The strategic BPMN and the i\* models are separate from the executable Camunda model. Acceptance gaps that the recorded tests still leave open are listed in the [BPM&EA plan](Group_Project_and_Test_Plan_2026-09-29.md) and the [AISD detailed results](../AISD/Group_Acceptance_Test_Plan_and_Results_2026-09-29.md).
