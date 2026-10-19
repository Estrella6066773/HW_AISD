# Submission Index — second release

AISD (UFCEP6-0-3) · BPM&EA (UFCEP4-0-3) · Group hospital pathway
Repository `https://github.com/Estrella6066773/HW_AISD` · prepared 19 October 2026 · describes the revised release, tagged `submission-2026-10-20`; read its SHA from the tag

This file is the entry point to the pack. It names the releases, gives every artefact's repository path and format, and marks what is not yet in place.

## Releases

| Tag | Commit | Date | What it identifies |
|-----|--------|------|--------------------|
| `submission-2026-09-29` | `f6fec99` | 29 Sep 2026 | **Initial release.** Model `Hospital_All_Processes_Simple_C8` (`Week3 Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn`); baseline for the 29 September logs. |
| `submission-2026-10-20` | the tag target | 19 Oct 2026 | **Revised release and current state.** Model `Hospital_All_Processes_V3_C8` (`Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`); carries the 19 October acceptance run. Read its SHA from the tag. |

`standup-1-2026-09-16` and `sr3-2026-10-14` are not releases: they mark the first standup and the Sprint Review 3 snapshot. Read the revised release first.

## AISD artefacts

| ID | Artefact | Repository path | Format and status |
|----|----------|-----------------|-------------------|
| `A-1` | Second-release deck | `submissions/AISD/AISD_Presentation_2026-10-19.pptx` and `.pdf` | `.pptx` + PDF, 13 slides. In place. |
| `A-2` | Submission index and repository link | `submissions/Submission_Index.pdf` and `.md` | PDF, 2 pages. In place — this file. |
| `A-3` | Feedback response record | Record only: `Week6 Coursework/feedback/feedback-response_2026-10-16.md` | PDF (no format set by the brief). **Not in place.** `F-01`–`F-10` recorded; `F-11` not implemented; mentor column empty; `F-08` split undecided. |
| `A-4` | Planning evidence | Draft only: `Week6 Coursework/plan/sprint3-4-plan_2026-10-16.md` | PDF (no format set by the brief). **Not in place.** Risk record has six rows for the revised plan; none for the initial plan. |

The initial-release documents are retained as the 29 September baseline, not as second-release slots: `submissions/AISD/Group_Design_Decisions_2026-09-29.pdf`, `Group_Acceptance_Test_Plan_and_Results_2026-09-29.pdf` and `Hospital_All_Processes_Camunda8_Export_2026-09-29.pdf`.

## BPM&EA artefacts

| ID | Artefact | Repository path | Format and status |
|----|----------|-----------------|-------------------|
| `B-1` | Strategic model, readable PDF, abstraction note | `docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn`; `submissions/BPMEA/BPMEA_Strategic_Process_Readable_2026-10-19.pdf`; `submissions/BPMEA/BPMEA_Abstraction_Note.pdf` | `.bpmn` + PDF 8 pp + PDF 6 pp. In place; second-owner review signed 19 October. |
| `B-2` | i\* SD and three service SR views | `Week6 Coursework/istar/`: `V1_SD_diagram.txt`/`.png`; `PB-16_V1_Admin_SR_reviewed_2026-10-19.txt`/`.png`; `PB-16_V1_Clinical_SR_reviewed_2026-10-13.txt`/`.png`; `PB-16_V1_Finance_SR_reviewed_2026-10-13.txt` and `PB-16_V1_Finance_SR_reviewed.png` | piStar `.txt` + PNG, four models and four figures. In place; `PB-16` review **unsigned**. |
| `B-3` | Written evaluation, Part 1: requirements alignment | `submissions/BPMEA/BPMEA_Written_Evaluation.docx` and `.pdf` | `.docx` + PDF, 23 pp. In place; Part 1 final. |
| `B-4` | Written evaluation, Part 2: acceptance evaluation | Same file | `.docx` + PDF. **Draft**, awaiting Ryan (`PB-31`). |
| `B-5` | Editable operational model, deployment configuration, two readable exports | `Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn`; `Week3 Coursework/hospital-pathway/src/main/resources/application.yaml`, `config/application.example.yaml`; `submissions/BPMEA/BPMEA_Operational_Process_Readable_2026-10-19.pdf`, `BPMEA_Strategic_Process_Readable_2026-10-19.pdf` | `.bpmn` + YAML + PDF 16 pp + PDF 8 pp. In place. |

Carried by the repository, no separate slot: `B-6` worker source, `pom.xml` and configuration (`Week3 Coursework/hospital-pathway/`, 17 Java files, 19 tests); `B-7` the twelve forms in `Week6 Coursework/forms/`. `B-8`, the second-release Project and Test Plan, is **not in place**: only `submissions/BPMEA/Group_Project_and_Test_Plan_2026-09-29.pdf` exists.

## Acceptance evidence and result

Master record: `Week3 Coursework/hospital-pathway/evidence/Camunda_V3_Acceptance_2026-10-19.txt`.

The revised model ran on Camunda 8.10.0-alpha5. G07 reached `COMPLETED` (nine human tasks, no active incident); `AT-01`, `AT-02`, `AT-04`, `AT-05` and `AT-06` pass; **`AT-03` fails** because the model has no candidate groups, so a Medical Secretary can still complete the Consultant decision. A clean `mvn -B clean test` passes 19 tests. Without `--disable-connectors` the bundled Connectors health check shut c8run down mid-run; the cases were re-run after the restart.

## Run instructions

Full sequence: `Week3 Coursework/hospital-pathway/README.md`.

1. From `D:\OneDrive\MyProjects\AISD_Toolbox\tools\c8run-8.10.0-alpha5`, run `c8run.exe start --disable-connectors`. REST, Operate and Tasklist answer on `http://localhost:8080` (`demo` / `demo`); gRPC on `127.0.0.1:26500`.
2. From `Week3 Coursework/hospital-pathway`, run `mvn -B spring-boot:run`. It deploys the V3 model and the twelve forms from `Week6 Coursework/`; sources target Java 21, the recorded run used JDK 23.0.1.
3. Start `Hospital_All_Processes_V3_C8` in Tasklist, or run `python scripts/pb14_acceptance.py`, `pb18_acceptance.py` or `g07_e2e_acceptance.py`; `CAMUNDA_PROCESS_ID` defaults to `Hospital_All_Processes_V3_C8`.

`Week6 Coursework/code/` is a second copy of the Java module, with its `pom.xml` pointing at `../bpmn` and `../forms`; run one copy at a time.

## Limits recorded, not hidden

- `AT-03` fails on both releases; `BR-37` is unsupported — no role-based access control, every user task assigned to `demo`.
- `PB-16` i\* SD/SR second-owner review is unsigned.
- `B-8` does not exist in second-release form; `A-3` and `A-4` are not yet submittable files.
- `B-4` is drafted but not yet adopted by Ryan, its designated author.
- The formal change path, DNA to Finance, urgent authorisation, refund adjustment and letter escalation are modelled but no acceptance case drives them.
- The contribution record is a blank template and the Definition of Done is unsigned.
