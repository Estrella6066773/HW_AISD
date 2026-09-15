# ruby：Part 6 Sprint Backlog（Sprint 1）

**主笔**：Ruby（23084382）
**复核**：Dluffy（Ender）

| Sprint | Goal |
|--------|------|
| Sprint 1 | Finish and upload the Product Backlog and this Sprint 1 Backlog by 16 Sep. Then specify the first slice: referral check → doctor decision → first clinic booking (scheduling may be mocked). Payment, clinic letters and enquiry routing are out of this sprint. |

| Sprint | Task ID | Task Description | First Owner | Second Owner | Estimate | Acceptance Conditions | Evidence | Status |
|--------|---------|------------------|-------------|--------------|----------|-----------------------|----------|--------|
| Sprint 1 | T01 | List roles and permissions for referral check: secretaries may request missing papers; they must not accept a referral | Hao Zheng | Geping Chen | 2h | Matches case study rules on secretaries vs doctor | Permission notes | Done |
| Sprint 1 | T02 | Write the main referral path: receive → check papers → send to doctor | Hao Zheng | Guanyan He | 3h | Steps match the case study | Path notes (diagram later) | In progress |
| Sprint 1 | T03 | Write the four doctor outcomes: accept / reject / ask for more papers / send to another service; reason and decision-maker required | Hao Zheng | Geping Chen | 3h | Cannot continue without reason and who decided | Decision fields and rules | Not started |
| Sprint 1 | T04 | Write the reject / redirect path: no first clinic booking after reject | Guanyan He | Hao Zheng | 2h | Rejected referrals do not enter new-patient booking | Exception path notes | Not started |
| Sprint 1 | T05 | First clinic booking request only after accept (speciality, priority, time window, patient needs) | Hao Zheng | Minghao Qin | 3h | Admin cannot book before accept | Gate rule | Not started |
| Sprint 1 | T06 | Agree outside scheduling (may mock): confirm if a slot exists; if not, pending and flag to pathway team; do not book outside the requested window | Minghao Qin | Guanyan He | 5h | No slot = pending or escalated | Mock agreement and fail rules | Not started |
| Sprint 1 | T07 | Notification rules: letter as normal; also phone if the visit is within two weeks; log every call result | Geping Chen | Hao Zheng | 3h | Visits within 14 days must have a phone-attempt record | Notification rules | Not started |
| Sprint 1 | T20 | First standup: Product Backlog and this table uploaded; all members on GitHub; plan only, no diagram or code yet | Hao Zheng | Geping Chen | 2h | Repo has PB and Sprint Backlog; four members added | GitHub link and files | In progress |
