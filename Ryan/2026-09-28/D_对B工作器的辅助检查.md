# D 对 B 工作器的辅助检查记录

2026-09-28，基于同步基线 `98fad83`。由 Codex 帮助 Ryan 阅读，**待 Ryan 与 B 核对，不视为二责签字**。未改 B 的工作器实现。

检查对象：[MemberBPathwayWorkers.java](../../Coursework/hospital-pathway/src/main/java/io/camunda/demo/hospital/MemberBPathwayWorkers.java)。

| 观察 | 影响／建议 |
|---|---|
| `upsertBooking` 复用已有行时，仅在目标状态为 PENDING 时修改状态；目标为 CONFIRMED 时沿用旧值 | 同一 occupancy key 先 unavailable 再 reserve，会保留 PENDING，尽管任务名已经是 reserve-appointment；建议 B 补 pending → confirmed 测试和状态转换 |
| `checkSlot` 调用时固定请求 CONFIRMED | 当前表示课堂模拟可用号源；若要覆盖“没有合适时间窗”的验收条件，需要 B 说明输入契约和 pending 分支，不能只用成功演示证明完整号源校验 |
| 四参数 `append` 每次调用都会追加审计 | B 的重复领取会保留多条尝试日志；占用行仍受唯一键约束。需明确这些行是“尝试日志”还是“一次成功占用的唯一回执” |

D 本次保留原四参数审计 API，并有集成测试验证旧调用仍正常写入。路线 14 实测经过 B 的 `check-slot` 后进入 D 变更通知并结束。它只验证了这条成功联调路线，没有覆盖上述 pending → confirmed 情况。
