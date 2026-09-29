# Course-specific submission documents

The project uses one shared case study and one authoritative implementation. Course-specific written deliverables are kept separately:

| Course | Folder | Main document |
| --- | --- | --- |
| Business Process Modelling and Enterprise Architecture (BPM&EA / UFCEP4-0-3) | [`BPMEA/`](BPMEA/README.md) | Group Project and Test Plan |
| Advanced Information Systems Development (AISD / UFCEP6-0-3) | [`AISD/`](AISD/README.md) | Design Decisions and Acceptance Test Plan/Results |

The **shared executable implementation** remains in [`../Coursework/hospital-pathway/`](../Coursework/hospital-pathway/): one Camunda 8 BPMN, eleven editable forms, Java workers, Maven/configuration files and shared automated-test logs. These files are linked from both course folders rather than copied into two versions.

The identifiable submission version is git tag `submission-2026-09-29` on `main`. The recorded executable tests use implementation source commit `fc6293e`. That commit is the baseline for the Java results and for the live Camunda run of one final-model self-pay route, which reached `COMPLETED` and is stored in the shared [G07 JSON](../Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json). The submission pack was first uploaded to `main` in `e8a6861`. Commit `7be65b4` added the strategic BPMN and the i\* SD/SR models. Those later commits do not change the executable BPMN or the worker source that G07 ran. Other routes and the failed role-permission criterion remain identified in the course-specific test plans. Group second-owner review is still pending. The local c8run environment is not available for a repeat run.
