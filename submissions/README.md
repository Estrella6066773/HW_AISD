# Course-specific submission documents

The project uses one shared case study and one authoritative implementation. Course-specific written deliverables are kept separately:

| Course | Folder | Main document |
| --- | --- | --- |
| Business Process Modelling and Enterprise Architecture (BPM&EA / UFCEP4-0-3) | [`BPMEA/`](BPMEA/README.md) | Group Project and Test Plan |
| Advanced Information Systems Development (AISD / UFCEP6-0-3) | [`AISD/`](AISD/README.md) | Design Decisions and Acceptance Test Plan/Results |

The **shared executable package** is [`Week3 Coursework/hospital-pathway/`](<../Week3 Coursework/hospital-pathway/>): one Camunda 8 BPMN, eleven editable forms, Java workers, Maven/configuration files and shared automated-test logs. These files are linked from both course folders rather than copied into two versions. `Coursework/` was renamed to `Week3 Coursework/` in `03180bb`, so any link that still spells the old `Coursework/hospital-pathway/` points at nothing.

The recorded executable tests use the initial-release source, which is tagged `submission-2026-09-29` (commit `f6fec99`, 29 September). That state is the baseline for the Java result logs, the four BPMN structural checks and the live Camunda run of one final-model self-pay route, which reached `COMPLETED` and is stored in the shared [G07 JSON](<../Week3 Coursework/hospital-pathway/evidence/Group_Final_E2E_20260929-135729.json>). The submission pack was first uploaded to `main` in `e8a6861`; `7be65b4` added the strategic BPMN and the i\* SD/SR models. The executable BPMN, the forms and the worker source have all changed since that tag, so the recorded results describe that baseline and not the current `main`. Other routes and the failed role-permission criterion remain identified in the course-specific test plans. Group second-owner review is still pending. The local c8run environment is not available for a repeat run. The second-release working set is in [`Week6 Coursework/`](<../Week6 Coursework/>).
