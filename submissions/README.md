# Course-specific submission documents

The project uses one shared case study and one authoritative implementation. Course-specific written deliverables are kept separately:

| Course | Folder | Main document |
| --- | --- | --- |
| Business Process Modelling and Enterprise Architecture (BPM&EA / UFCEP4-0-3) | [`BPMEA/`](BPMEA/README.md) | Group Project and Test Plan |
| Advanced Information Systems Development (AISD / UFCEP6-0-3) | [`AISD/`](AISD/README.md) | Design Decisions and Acceptance Test Plan/Results |

The **shared executable implementation** remains in [`../Coursework/hospital-pathway/`](../Coursework/hospital-pathway/): one Camunda 8 BPMN, eleven editable forms, Java workers, Maven/configuration files and shared automated-test logs. These files are linked from both course folders rather than copied into two versions.

These local documents were prepared against source commit `fc6293e`; the submission additions still need a final Git revision and repository-access check. A live Camunda run of one final-model self-pay route reached `COMPLETED` and is recorded in the shared [G07 JSON](../Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json). Other routes and the failed role-permission criterion remain identified in the course-specific test plans.
