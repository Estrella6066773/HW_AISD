# PB-17 贡献记录表

**主笔**：Estrella　**复核**：Ender　**起表日期**：2026-09-16　**对应条目**：PB-17 举证与贡献记录维护

**用途**：留存全组贡献证据，供 tutor 核查个人贡献。依据考核规范 Section 4 的要求：*Group-based marks are subject to individual contribution. Retain contribution evidence for tutor moderation.*

**验收条件**（取自产品待办 PB-17）：表内每条证据都能打开，且与条目负责人一致；缺证据的条目不标完成。

---

## 一、使用说明

1. 本表分两个视图。**视图 A** 按证据逐行登记，回答「有哪些证据」；**视图 B** 按条目对账，回答「证据够不够、能不能认定完成」。
2. 证据由**本人自交**，不代填；Estrella 汇总核对，Ender 复核。
3. 每行证据的位置必须是**真实可打开的路径或链接**，不写「说明」「见上文」「截图」这类占位内容。
4. 条目状态沿用产品待办的口径：In progress 表示已开工，Not started 表示尚未开工，Blocked 表示受阻，Done 表示完成。
5. 标 Done 必须有可打开的产物与证据位置；缺证据的条目在视图 B 中标为「不可认定完成」，并在备注写明缺什么。

---

## 二、人名对照（核对「负责人一致」时使用）

**统一用名**取仓库文件夹名，与 `README.md`、`docs/p3-product-backlog.md`、`Ruby/2026-09-14/分工表.md` 一致。

| 统一用名 | 仓库文件夹 | Blackboard 显示名 | GitHub 提交显示名 | UWE ID |
|----------|------------|-------------------|-------------------|--------|
| Ruby | `Ruby/` | Ruby Zheng | 郑好 | 23084382 |
| Estrella | `Est/` | Estrella Chen | Estrella6066 | 23084393 |
| Ender | `Ender/` | Ender Qin | DLuffy | 23084402 |
| Ryan | `Ryan/` | HeGuanYan He | ENTONG-Ryan | 23084395 |

**注意**：任务拆分 `docs/p4-work-breakdown.md` 里 C 组员写作 `Ender`，与产品待办里的 `Ender` 是同一人，登记时统一写 `Ender`。

---

## 三、证据类型代号（登记时选用其一）

| 代号 | 类型 | 具体形式 | 判定要点 |
|------|------|----------|----------|
| SCR | 截图 | png / jpg | 能看清界面或状态，非空白、非纯文字标题 |
| CMT | 提交记录 | commit 短哈希 + 仓库链接 | 提交信息带条目编号 |
| MTG | 会议记录 | md | 有日期、出席人、结论与待办分工 |
| ART | 文档或模型产物 | md / bpmn / json | 是被认可为交付物的成品，非过程草稿 |
| TAG | 版本快照 | git tag | 每次评审一个 |
| LOG | 运行记录 | txt / log | 含时间与结果，多为模拟服务或测试输出 |
| BRD | 看板状态 | 截图或链接 | 状态需与产品待办一致 |

---

## 四、视图 A · 证据明细表

登记规则：一条证据一行。同一条目下同一人有多份证据时分多行登记。

| 证据编号 | 条目编号 | 姓名 | 条目内角色 | 证据类型 | 证据位置 | 证据日期 | 条目当前状态 | 核对结果 | 核对人与日期 | 备注 |
|----------|----------|------|------------|----------|----------|----------|--------------|----------|--------------|------|
| E-001 | PB-15 | Estrella | 第一负责人 | ART | `docs/p3-product-backlog.md` | 2026-09-16 | In progress | 通过 | Estrella 2026-09-16 | 格式示例行，正式填写时替换为实际证据 |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

**字段说明**

| 列 | 填写要求 |
|----|----------|
| 证据编号 | 形如 `E-001`，顺序编，便于口头引用 |
| 条目编号 | `PB-xx`；有任务卡时并列写出，如 `PB-01 / T01` |
| 姓名 | 用第二节的「统一用名」 |
| 条目内角色 | 第一负责人 / 第二负责人 / 参与 |
| 证据类型 | 用第三节的代号 |
| 证据位置 | 仓库内可打开的路径或链接 |
| 证据日期 | 证据产生日期，非录入日期 |
| 条目当前状态 | 抄产品待办，录入时抄一次 |
| 核对结果 | 通过 / 缺件 / 待补 / 待核 |
| 核对人与日期 | 由 Estrella 核对，Ender 复核 |

---

## 五、视图 B · 条目覆盖检查表

负责人与状态栏取自 `docs/p3-product-backlog.md`（2026-09-16 版本）。右侧四列在汇总核对后填写。

| 条目编号 | 优先级 | 第一负责人 | 第二负责人 | 条目当前状态 | 已有证据条数 | 证据是否均可打开 | 负责人是否一致 | 可否认定完成 | 备注 |
|----------|--------|------------|------------|--------------|--------------|------------------|----------------|--------------|------|
| PB-01 | P0 | Ruby | Estrella | In progress |  |  |  |  |  |
| PB-02 | P0 | Ruby | Ryan | Not started |  |  |  |  |  |
| PB-03 | P0 | Ruby | Ender | Not started |  |  |  |  |  |
| PB-04 | P0 | Estrella | Ruby | Not started |  |  |  |  |  |
| PB-05 | P0 | Ruby | Estrella | Not started |  |  |  |  |  |
| PB-06 | P0 | Ender | Ryan | Not started |  |  |  |  |  |
| PB-07 | P0 | Ender | Estrella | Not started |  |  |  |  |  |
| PB-08 | P1 | Ryan | Ruby | Not started |  |  |  |  |  |
| PB-09 | P1 | Estrella | Ryan | Not started |  |  |  |  |  |
| PB-10 | P1 | Estrella | Ender | Not started |  |  |  |  |  |
| PB-11 | P0 | Ryan | Ruby | Not started |  |  |  |  |  |
| PB-12 | P0 | Ruby | Estrella | Not started |  |  |  |  |  |
| PB-13 | P1 | Estrella | Ruby | Not started |  |  |  |  |  |
| PB-14 | P1 | Ryan | Ender | Not started |  |  |  |  |  |
| PB-15 | P0 | Ruby | Estrella | In progress |  |  |  |  |  |
| PB-16 | P0 | Estrella | Ryan | Not started |  |  |  |  |  |
| PB-17 | P0 | Estrella | Ender | In progress |  |  |  |  |  |
| PB-18 | P1 | Ryan | Ender | Not started |  |  |  |  |  |
| PB-19 | P1 | Ender | Ryan | Not started |  |  |  |  |  |
| PB-20 | P1 | Ender | Estrella | Not started |  |  |  |  |  |
| PB-21 | P1 | Ryan | Ender | Not started |  |  |  |  |  |
| PB-22 | P0 | Ruby | Estrella | Not started |  |  |  |  |  |
| PB-23 | P2 | Ryan | Ruby | Not started |  |  |  |  |  |
| PB-24 | P2 | Ryan | Ender | Not started |  |  |  |  |  |
| PB-25 | P2 | Ryan | Ruby | Not started |  |  |  |  |  |
| PB-26 | P2 | Estrella | Ender | Not started |  |  |  |  |  |
| PB-27 | P2 | Estrella | Ryan | Not started |  |  |  |  |  |
| PB-28 | P0 | Ruby | Ryan | In progress |  |  |  |  |  |
| PB-29 | P0 | Ender | Estrella | In progress |  |  |  |  |  |

**首轮已知反例（须如实标出，不要掩盖）**

任务拆分 `docs/p4-work-breakdown.md` 的 **T01** 状态标 `Done`，但证据列只写「Part 1 摘要中的权限规则」，没有可打开的路径。按完成定义与 PB-17 的验收条件，此项**不可认定完成**。处理方式二选一，在备注写明：

- 由 Ruby 补齐权限表路径与截图后重新认定；或
- 状态改回 `In progress`，待补齐后再标完成。

---

## 六、待全组确认项（过会拍板后回写）

| # | 事项 | 建议 | 状态 |
|---|------|------|------|
| 1 | 存放位置 | 仓库根目录新建 `evidence/PB-xx/`，个人日期文件夹只放工作草稿 | 待确认 |
| 2 | 人名统一 | 统一用仓库文件夹名，按第二节对照表 | 待确认 |
| 3 | 表头列数 | 采用视图 A 的 11 列，或删减到已约定的 5 列加最少增补 | 待确认 |
| 4 | 视图 B 维护人 | Estrella 汇总，Ender 复核 | 待确认 |
| 5 | Ruby 的提交身份 | 现有两个身份，其中一个为 Gitee 邮箱；建议此后改用 GitHub 账号邮箱，历史提交不改写、如实说明 | 待确认 |

---

## 七、相邻记录

| 记录 | 说明 |
|------|------|
| 标记站会个人记录 | 每人一份，作为 `MTG` 类证据登记；两次站会共 10% 为个人分，必须逐人留档 |
| 反馈行动记录 | 考核规范 Section 6 要求留存，字段为提出点、回应、第一与第二负责人、完成证据；另表同模板，初稿可用 Part 8 评审准备里的 F01 至 F06 反馈表 |
| 版本快照 | 每次冲刺评审一个 git tag，作为该次评审的增量快照 |

---

## 八、完成自检

- [ ] 四个人都有证据，不存在一人多、一人空
- [ ] 每个位置都真实可打开，没有占位内容
- [ ] 每行姓名与产品待办登记的负责人一致
- [ ] 标完成的条目全部有可打开证据，反例如实标出
- [ ] 提交记录类证据带条目编号，显示名与邮箱能对应到人
- [ ] 每次评审有版本快照
- [ ] 站会个人记录逐人留档
- [ ] 全组对表头与存放位置无异议，核对结果经 Ender 复核
