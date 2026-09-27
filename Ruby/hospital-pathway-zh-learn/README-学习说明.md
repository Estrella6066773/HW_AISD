# 医院路径 — 中文学习副本（可删）

正式工程在 `Coursework/hospital-pathway`。本目录仅供自己看懂流程，交作业请用英文版。

## 每次怎么开（与英文版相同顺序）

1. **先开 Camunda**（c8run / starter），确认：
   - Operate：http://localhost:8080/operate （demo / demo）
   - Tasklist：http://localhost:8080/tasklist （demo / demo）
2. **再开 Java**（二选一，窗口不要关）：

```bash
cd "Ruby/hospital-pathway-zh-learn"
mvn spring-boot:run
```

或在 IDE 打开 `HospitalPathwayApplication.java` → Run（Java 21）。

3. **不要**与正式版 `hospital-pathway` 同时跑。

若本机 Camunda 是 8090，把 `src/main/resources/application.yaml` 的 `rest-address` 改成 `8090`。

## 完整路线

见同目录 `完整体验路线.md`。
