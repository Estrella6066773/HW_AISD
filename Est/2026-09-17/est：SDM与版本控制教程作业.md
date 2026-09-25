# Compare and Contrast Software Development Methodologies & Version Controlling

**课程**：Business Process Modelling and Enterprise Architecture & Advanced Information System Development
**Tutorial**：`W01/SDM Tutorial.docx`（正文标题为 Compare and Contrast Software Development Methodologies）；`W01/Version Controlling 1.docx`
**小组**：Ruby / Estrella / Ender / Ryan
**日期**：2026-09-17
**主笔**：Estrella（Geping Chen，23084393）
**依据**：两份 tutorial 表格；`W01/UFCEP6-0-3_Portfolio_Assessment_Specification V2.docx`；Simão（2011）；SWEBOK v3

> 用法：第一节是「要干啥」，从第二节起是填好的答案。上传小组仓库时交英文正文；中文是给组内讲和答辩用的。
> 标记 ⚠ 的行，需要对照论文第 4 章原表再核一遍数字，理由见 1.4.6。

---

## 0. 你要干啥

这两份 Word 都不是 Agile Workshop 的 Part 1–8，而是 BPM&EA 课的 tutorial 表格。

### 第一份：`SDM Tutorial.docx`

文件名写的是 SDM Tutorial，正文标题是 **Compare and Contrast Software Development Methodologies**。目标是把四种开发方法论按给定标准逐格标 low / medium / high / N/A，各写一份优缺点，最后讲给不技术的管理层听。

| 题 | 要交什么 |
|----|----------|
| Pros and Cons | Waterfall、Spiral Model、RAD Model、Agile 各一份优点与缺点 |
| Comparison Table | 11 项标准 × 4 种方法，每格标 low / medium / high / N/A |
| Follow-on Task | 用 SWEBOK 指南与 Simão 论文第 4 章（Results）为上面的判断补证据，并把本组结论与论文结果对应起来 |

题面自带的约束：这是一份要讲给管理层做决策依据的对比，读者不是工程师；题面也预设了本组第一版结论会被批评为「主观、缺严谨性、缺科学证据」，所以续做任务不是可选项，而是对这份表的合法性补证。

### 第二份：`Version Controlling 1.docx`

| 题 | 要交什么 |
|----|----------|
| Task 1 | 登录 UWE GitLab |
| Task 2 | 新建项目：命名、项目标识、可见性、勾选 README |
| Task 3 | 邀请组员并按角色授权 |
| Task 4 | 克隆、暂存、提交、推送 |
| Task 5（选做） | Merge Request 与 Issue 跟踪 |

### 两份的共同要求

答案都要上传到小组仓库。第一份题面写明必须小组一起做。

---

## Tutorial 1 · Compare and Contrast Software Development Methodologies

### 1.1 评分口径（必须先声明，否则表没法读）

题面只要求标 low / medium / high / N/A，没说「高」是指好还是指多。这三类标准方向并不一致，先定义清楚，正是续做任务所说的「补严谨性」的第一步。

| 类别 | 涉及标准 | 标「高」的含义 |
|------|----------|----------------|
| 能力类 | Flexibility、Simplicity、Phase Containment of Error、Client Interaction、Success to failure ratio | 该项能力达成程度高，越高越好 |
| 代价类 | Cost、Risk Factor、Expertise Required、Time Required、Resource Required | 需要投入或承担的量更大，越低越好 |
| 节奏类 | Development Time | 从开工到首个可用交付耗时更长 |

三点补充说明：

1. **N/A 的用法**：本题的 N/A 只用于「该标准预设了阶段式生命周期、而该方法本身没有阶段」的情形。全表只有 Agile 的 Phase Containment of Error 标 N/A。
2. **Agile 取哪一支**：题面写 Agile (any variant of your choice)，本组取 **Scrum**。理由很实际：Simão 的论文同时评了 Scrum 与 XP，取 Scrum 可以让续做任务的映射逐条对应；XP 作为对照在 1.4 里出现。
3. **Success to failure ratio 的口径**：指该方法在业界实践中交付成功的相对比例，不是本组项目的成败预测。

### 1.2 Pros and Cons

| Methodology | Pros | Cons |
|-------------|------|------|
| **Waterfall** | 阶段与交付物定义清楚，进度和预算容易向管理层汇报；每阶段有评审关口，错误容易在阶段内被发现；文档齐全，人员更替时交接成本低；合同与验收边界清晰，适合固定价项目 | 需求在早期就要冻结，后期变更代价很高；客户要到末期才看到可运行的软件，风险集中在收尾阶段；几乎没有过程自我调整的空间；测试长期被排在末段，缺陷暴露晚 |
| **Spiral Model** | 以风险为驱动的迭代，每一圈都先做风险分析再动工，高风险项被优先处理；原型让客户在早期就能评估方向；设计、测试与配置管理在同一条循环里被反复覆盖，质量活动不靠末段补 | 风险分析本身要求专业判断，门槛高；每一圈都要维护原型、评审与文档，投入和周期都大；若项目风险不高，这套机制的性价比明显偏低；圈数多了以后，整体进度反而难向管理层说明白 |
| **RAD Model** | 交付节奏快，把「先做出来再看」变成正式流程；时间盒管住迭代长度，客户预期容易对齐；借助工具生成与应用复用，能显著压缩编码与测试量；焦点小组持续在场，需求偏差能早纠正 | 高度依赖可复用组件与自动化工具，工具链不到位就退化成赶工的瀑布；测试与维护在方法论里关注不足；设计缺少统一的记号与规范，长期可维护性差；只适合范围清楚、模块化、工期紧的中小型系统 |
| **Agile (Scrum)** | 用待办列表与燃尽图把进度变成可见的日常信息；增量在每个冲刺末交付，客户随时可以看到真东西；冲刺目标、角色与仪式清楚，团队自组织；拥抱需求变更，风险被摊到每个短冲刺里 | 需要团队有较强自律与工程实践打底，否则「迭代」会变成没有文档的赶工；对过程度量与文档的要求低，交付到合规或长周期维护场景时补账成本高；规模一大人与人之间的协调开销迅速上升；冲刺不产出的代价被时间盒放大 |

### 1.3 Comparison Table

图例：**H** = high，**M** = medium，**L** = low，**N/A** = 该标准不适用。

| Criterion | Waterfall | Spiral Model | RAD Model | Agile (Scrum) |
|-----------|-----------|--------------|-----------|---------------|
| **Flexibility**<br>改变方向的能力 | **L** — 需求在早期冻结，变更要走正式的变更流程，越晚越贵 | **M** — 每一圈结束可以重新定向，但圈内不轻易改 | **H** — 时间盒加焦点小组反馈，方向随时可调 | **H** — 每个冲刺结束都可重排待办列表的优先级 |
| **Cost**<br>总投入（越低越好） | **M** — 需求稳定时很便宜，一旦变更就变成高代价返工 | **H** — 每圈都要重做风险分析、原型与评审 | **M** — 工具与人员投入高，但编码和测试量被压缩 | **M** — 短迭代带来额外的协调与集成开销 |
| **Risk Factor**<br>风险敞口（越低越好） | **H** — 风险堆在后期集成与验收，最后一次见面才暴露 | **L** — 风险分析是每一圈的起点，高风险项先做 | **M** — 早期可见原型压低了方向风险，但测试与维护风险被留下 | **L** — 短冲刺把风险切碎，每个增量都经过验证 |
| **Simplicity**<br>概念与管理上的简明程度 | **H** — 只有顺序阶段，团队和客户都容易理解 | **L** — 螺旋、圈次、风险等级、原型并行推进，管理复杂度高 | **M** — 时间盒好理解，但工具链与角色配合有额外复杂度 | **M** — 仪式简单，真正难的是自组织与工程纪律 |
| **Development Time**<br>到首个可用交付的耗时（越低越好） | **H** — 首个可运行版本通常到末期才出现 | **H** — 首个交付晚，但每一圈都有可评估的原型 | **L** — 时间盒天生为快速交付设计 | **L** — 每个冲刺末就有可用增量 |
| **Phase Containment of Error**<br>缺陷在阶段内被拦住的程度 | **H** — 阶段关口与阶段评审就是为此设计的，缺陷不易流向下一阶段 | **M** — 每圈都验证，但迭代反复会掩盖「缺陷属于哪一圈」 | **L** — 追求速度，正式的阶段检查被弱化，缺陷容易流到测试或上线 | **N/A** — 该标准预设阶段式生命周期；Agile 靠持续测试与增量验证控制缺陷，而非阶段关口 |
| **Expertise Required**<br>对团队能力的要求（越低越好） | **M** — 懂流程与文档规范即可，主要靠纪律 | **H** — 风险识别与原型设计都需要有经验的人 | **M** — 需要熟悉工具链与快速建模的人 | **H** — 自组织、持续重构与测试优先都要求成熟工程师 |
| **Success to failure ratio**<br>业界实践中的相对成功率 | **M** — 需求真正稳定的项目成功率高，需求会变的项目失败率高 | **M** — 机制有效但采用面窄，重投入也带来新的失败点 | **L** — 工具链与人员不到位时会退化成失控的赶工 | **H** — 增量交付与持续反馈使成功率在多数场景下更稳 |
| **Client Interaction**<br>客户参与程度 | **L** — 主要在需求确认与最终验收两次深度参与 | **H** — 每一圈结束都要评审原型并确认方向 | **H** — 焦点小组在设计到交付全程参与 | **H** — 每个冲刺评审都要客户到场并对增量提意见 |
| **Time Required**<br>全流程总工期（越低越好） | **H** — 阶段串行，返工会把工期整体拉长 | **H** — 圈数与风险等级决定工期，很难压缩 | **L** — 时间盒加复用把总工期压到最短 | **L** — 增量交付让首个版本很早可用，总工期相对可控 |
| **Resource Required**<br>所需资源（越低越好） | **M** — 主要是文档与评审的人力 | **H** — 原型、风险分析与反复评审都要人 | **H** — 强依赖自动化工具、复用组件与专职协调 | **M** — 团队规模小但要求每人多能 |

### 1.4 Follow-on Task · 把本组结论对到论文的证据上

#### 1.4.1 题目为什么这么出

题面已经替我们写出了批评意见：这份对比「主观、缺严谨性、缺科学证据」。这句话说得对。1.3 的每一格都是本组凭经验下的判断，没有任何可复核的依据。要回应这个批评，不能把话说得更响，只能换一种做法：把每种方法拿去和一份公开的、公认的知识体系逐条对照，让评分有出处。这就是续做任务要求做的两件事——读 SWEBOK 指南，读 Simão 论文第 4 章的结果，再把本组的判断和论文的结果对应起来。

#### 1.4.2 两份来源是什么

**SWEBOK** 是 IEEE Computer Society 出版的《软件工程知识体系指南》。它把软件工程划成若干知识领域（Knowledge Area，简称 KA），逐个说明该领域的共识议题与最佳实践。它的价值在于：KA 是公开的、有编号的、可以逐条引用的，因此「这个方法在需求领域做得如何」就变成了一个有对照物的提问，而不是感觉。

**Simão 的论文**正是拿这套 KA 去评方法论的。要点如下：

- 完整引用：Simão, E.M. (2011) *Comparison of Software Development Methodologies Based on the SWEBOK*. 硕士学位论文（master's dissertation），Universidade do Minho，导师 João M. Fernandes。
- 论文提出一个比较框架：先为每种方法论定义「理想用法」，再把它逐条对照 SWEBOK 的 KA，判定其符合程度。
- 判定用三级满意度量表：**0 = 完全不满足（no satisfaction）**，**1 = 部分满足（partial satisfaction）**，**2 = 完全满足（full satisfaction）**。
- 研究覆盖 5 种方法论：**Waterfall、Spiral、RAD、Scrum、XP**——本题要求的四种正好落在其中（Agile 取 Scrum）。
- 结果按九个 KA 给出，论文把它们三三分组呈现：① Software Requirements、Software Design、Software Construction；② Software Testing、Software Maintenance、Software Configuration Management；③ Software Engineering Management、Software Engineering Process、Software Quality。
- 每组 KA 都有结果表（第 4 章 Table 4.1 起），并配每种方法一张满意度柱状图（Figure 4.1 至 4.5）。柱高按「实际满意度 ÷ 最大可能满意度」换算成百分比。

**一处事实更正**：题面把 Simão 的论文称作 PhD thesis，它实际是硕士学位论文。答辩或引用时按「master's dissertation, 2011」写。

**一处口径提醒**：Simão 论文依据的 SWEBOK 是较早版本，只覆盖九个 KA；现行 SWEBOK v3 共 15 个 KA。引用时应写明论文评的是哪九个，不要把论文的结论说成覆盖了整个 SWEBOK。

#### 1.4.3 论文第 4 章对各方法的结论

以下取自论文第 4 章 Results 的正文论述：

| Methodology | 论文报告的主要结果 |
|-------------|--------------------|
| **Waterfall** | 整体呈「单线推进」，没有为变更、过程评估与过程调整留出空间，因此工程过程类 KA 的满意度偏低；设计高度依赖文档而不是能落到各设计层次的实务做法；**需求分析与质量保证的满意度很高**；**软件构建被扣分**，原因是既不承诺简洁性，也不承诺「为验证而编码」 |
| **Spiral** | 由于采用原型技术，并在每一圈引入迭代与复审，**设计与测试两个 KA 的满意度很高**；配置管理、工程过程与工程管理属于合理水平；缺乏度量与量化（风险分析之外），也不承诺简洁性与代码验证，因此**软件构建与工程管理偏低**；没有定义专门的维护阶段或维护活动，**维护 KA 因此偏低** |
| **RAD** | 借助工具体系与管理方式，**软件构建达到完全满足**；借助模拟手段，**需求 KA 达到完全满足**；对测试与维护关注不足，**这两项是该方法最低的**；设计缺少记号与规范定义，整体也缺少度量与可量化的评审 |
| **Scrum** | 凭借角色分工与待办列表、燃尽图等工件，**是唯一在工程管理与工程过程两个 KA 上达到完全满足的方法**；把维护当作下一轮迭代处理，且未着力降低复杂度，**软件构建与维护两个 KA 是该方法最低的** |
| **XP**（对照） | 设有专门的维护阶段，并以简洁性、细致复审与对应角色为抓手，**是唯一在维护与软件构建两个 KA 上完全满足的方法**；引入测试者与跟踪者角色后，**也是唯一在软件配置管理上完全满足的方法**；设计过程与工程管理／工程过程是该方法最低的 KA，但绝对值仍然很高 |

#### 1.4.4 映射：本组的标准对到论文的 KA

本表的读法是：左列是本组表格里的标准，中列是它最接近的论文 KA，右列是论文是否真的为这条标准提供了证据。

| 本组标准 | 对应的论文 KA | 论文是否提供证据 | 对照结果 |
|----------|---------------|------------------|----------|
| Flexibility | Software Engineering Process、Software Requirements | 是 | **支持本组判断**。论文指出 Waterfall 的单线结构没有为变更与过程调整留空间，与本组给 Flexibility 的 L 一致；Scrum 在工程过程上达完全满足，与本组给 Agile 的 H 一致 |
| Cost | 无直接对应 KA（属工程经济学范围，不在论文覆盖的九个 KA 内） | 否 | **本组判断无外部证据**。论文不比较成本 |
| Risk Factor | Software Engineering Management | 部分 | **方向一致但口径不同**。论文承认 Spiral 以风险分析为核心并因此得分，但未把「风险敞口」量化，无法直接验证本组的 L／H |
| Simplicity | Software Construction | 是 | **支持本组判断**。论文明确因「不承诺简洁性」扣减 Waterfall 的构建得分，又把简洁性列为 XP 在构建上完全满足的原因；与本组把简洁性归为方法属性、并把 Waterfall 记为 H（概念简明）需要区分：论文说的是**代码层面的简洁**，本组说的是**管理层面的简明**，两者不是同一件事，表中已按管理层面定级，此处需在答辩时说明 |
| Development Time / Time Required | Software Engineering Management | 否 | **本组判断无外部证据**。论文自陈缺乏度量与量化，工期类结论无法从该研究得出 |
| Phase Containment of Error | Software Testing、Software Quality | 部分 | **仅得到间接支持**。论文对 Waterfall 的测试评价不低（阶段关口的作用），对 RAD 的测试评价最低；但论文不以「缺陷是否在阶段内被拦截」为评分口径，本行保留为本组判断 |
| Expertise Required | 无直接对应 KA | 否 | **本组判断无外部证据**。论文提到 Waterfall 与 Spiral 的「理想方法论」是作者从模型外推出来的，这提示能力门槛确实存在，但未评分 |
| Success to failure ratio | Software Quality | 否 | **本组判断无外部证据**，且论文主动回避了这条。论文在后记中说明，要判断某种方法如何影响软件质量，必须分析该方法产出的实际结果，而这就把项目情境的主观性带了回来，与该研究「尽量去主观化」的目标冲突，因此被列为后续工作 |
| Client Interaction | Software Requirements、Software Engineering Management | 是 | **支持本组判断**。论文把 RAD 的需求满意度列为完全满足，原因正是模拟与客户反馈机制；Scrum 凭待办列表与产品负责人角色在工程管理上达完全满足 |
| Resource Required | Software Engineering Management | 部分 | **方向一致**。RAD 依赖工具与协调、Spiral 依赖每圈的风险分析，论文都提到，但同样没有量化资源投入 |

#### 1.4.5 对照之后的三个结论

**第一，本组表格里能被论文证实的是「能力」这一侧，不能被证实的是「代价」这一侧。** 需求、设计、构建、测试、维护、配置管理、工程管理与工程过程这八个 KA 描述的是「这套方法在做什么、做得多好」；而成本、资源、工期、成功率属于「要花多少、值不值」。论文只回答了前者。因此 1.3 的 11 行标准应分成两半看待：Flexibility、Simplicity、Client Interaction 三条得到论文直接支持，Phase Containment of Error 得到间接支持；Cost、Risk Factor、Expertise Required、Success to failure ratio、Time Required、Resource Required 这六条目前仍只是一组排过序的主观判断，需要在答辩时如实说明。

**第二，本组有一处判断被论文纠正。** 本组原以为 Spiral 在管理与进度上会因反复迭代而吃亏，论文给出了更细的区分：Spiral 在**配置管理、工程过程与工程管理**上属于合理水平，真正低的是**软件构建、工程管理与维护**，其中维护低的原因是该方法根本没有定义维护阶段。这条修正说明「迭代多」并不自动等于「管理差」，真正决定分数的是有没有把某个 KA 当作必须处理的活动。

**第三，论文本身也有它自己的边界，引用时要一并说明。** 论文的实现方式是：由作者定义每种方法的「理想用法」，再逐条对照 KA 打分。打分动作仍然由人完成，作者自己在方法一节承认，评估者读过这些方法的优缺点材料，因此仍可能带着这套阅读印象去评分。论文的应对是要求评分时「直接对着事实判定是否符合」，以此压低主观性，但这不等于消除。所以论文提供的是一条**可复核的对照路径**，不是一组实验数据。

#### 1.4.6 ⚠ 需要核对的两处

1. 论文第 4 章的结果表和 Figure 4.1 至 4.5 的具体百分比，本次未逐格抄录。上表 1.4.3 的结论取自第 4 章的正文论述，1.4.4 的「是否提供证据」判断据此得出。若要把百分比写进正式提交版，需对照论文原表（第 4 章 Table 4.1 起）逐项填入。
2. 论文的 SWEBOK 版本与九个 KA 的划分，需按论文原文的表述再核一次，避免与 SWEBOK v3 的 15 个 KA 混用。

### 1.5 给管理层看的两段话

题面要求把结论讲给不技术的读者。以下是本组的正式口径，可直接用于汇报。

**一，四种方法没有绝对的好坏，只有与项目条件是否匹配。** 需求在开工前就能定死、验收标准写进合同的工程，选 Waterfall 最省事，它的阶段关口能把缺陷挡在阶段内；需要在做之前先确认方向对不对、且风险集中在少数关键技术点的项目，选 Spiral，它每一圈先做风险分析；范围清楚、模块化、必须在很短时间内出成果的系统，选 RAD；需求会变、需要在过程中不断拿真实产出与客户对齐的项目，选 Agile。

**二，本组的判断哪些站得住，哪些还需要补。** 在「这套方法做得好不好」这一类问题上，本组结论与公开发表的研究结论一致，例如 Spiral 强在设计与测试、弱在维护，RAD 强在需求与构建、弱在测试与维护，Scrum 强在管理过程。但在「要花多少钱、要多少人、要多久、成功概率多高」这一类问题上，目前没有公开研究可以直接支持，本组给出的评价属于有依据的经验判断，用于初步筛选，不应当作决策的唯一依据。如果只能记住一句：这份对比能帮你排除明显不合适的选项，不能替你算出回报率。

---

## Tutorial 2 · Version Controlling

### 2.1 Task 1–5 的完成情况

| Task | 要求 | 本组实际做法 | 状态 |
|------|------|--------------|------|
| Task 1 | 登录 UWE GitLab | 协作改在 GitHub 进行，未使用 GitLab | 未按其平台执行，差异见 2.2 |
| Task 2 | 新建项目（Repository／Project） | 已在 GitHub 建立小组仓库并生成 README | 已完成，平台改换 |
| Task 3 | 邀请组员并授权 | 四位成员均能推送，提交历史中四人齐备 | 已完成，平台改换 |
| Task 4 | 克隆、提交、推送 | 按「暂存 → 提交 → 推送」循环协作，累计 54 次提交 | 已完成 |
| Task 5（选做） | Merge Request 与 Issue | 已使用分支与合并；Issue 跟踪未启用 | 部分完成 |

Task 2 与 Task 3 是在 GitHub 上完成的等价动作，Task 1 的登录环节在 GitHub 上没有对应要求。平台不同不是形式问题，需要在提交时讲清楚，原因见下一节。

### 2.2 本组实际使用的平台，以及需要说明的差异

本组协作实际使用的仓库是 **GitHub**：

```
https://github.com/Estrella6066773/HW_AISD.git
```

这是一个必须主动说明的差异，不能含糊带过：

- **教程表格写的登录地址是 `https://gitlab.com`**，即公网 GitLab。
- **考核规范给出的资源链接是 `https://gitlab.uwe.ac.uk/users/sign_in`**，即 UWE 自建实例。两者不是同一个站点，教程表格里的地址应视为笔误。
- **本组实际使用的是 GitHub。** 考核规范正文的要求措辞是「把产物、代码与工作笔记保存在共享仓库或项目工作区」，提交方式是「通过 Blackboard 提交，并附上可访问的仓库链接」——规范本身并未指定 GitLab 为唯一平台。

因此需要做两件事：

1. 向 tutor 确认 GitHub 仓库是否被接受。若不接受，按 Task 2 在 UWE GitLab 重建仓库并迁移，本文件 2.1 至 2.3 的记录随之更新。
2. 无论最终落在哪个平台，都要确认 tutor 能打开链接。若仓库为私有，必须把 tutor 账号加为成员，否则「可访问的仓库链接」这条不成立。

### 2.3 角色对照

教程按 GitLab 的角色体系说明权限，GitHub 的对应关系如下，迁移时按此对齐：

| 教程中的角色 | 权限说明 | GitHub 对应角色 | 本组实际对应情况 |
|--------------|----------|-----------------|------------------|
| Guest | 只能查看，不能修改 | Read | 未使用 |
| Reporter | 可查看、克隆、拉取，不能推送 | Triage | 未使用 |
| Developer | 可以贡献代码，教程推荐给组员 | Write | 由提交历史可见四位成员均可推送，对应此级 |
| Maintainer | 可以贡献、合并并管理项目 | Maintain（或 Admin） | 由建仓人持有，负责合并与成员管理 |

其中「四位成员均可推送」是从提交历史推出的，没有逐人核对过仓库的成员设置页面。登记证据时若被追问，需回仓库设置页确认一次。

### 2.4 证据清单

以下取自本仓库实际历史，可直接登记进 `est：PB-17贡献记录表` 的视图 A。

| 证据项 | 内容 | 位置 |
|--------|------|------|
| 仓库地址 | `https://github.com/Estrella6066773/HW_AISD.git` | 远端 `origin` |
| 建仓首个提交 | `c8036f4`，2026-09-14，Estrella6066，Initial commit | `git log --reverse` |
| 项目骨架提交 | `c8da046`，2026-09-15，郑好，含 README 与 `.gitignore` | 提交历史 |
| 成员加入情况 | 四位成员均在提交历史中出现：Estrella6066、郑好、ENTONG-Ryan、DLuffy | `git shortlog -sne --all` |
| 分支使用 | `main` 之外存在远端分支 `ryan/workshop-2026-09-15` | `git branch -a` |
| 提交总量与跨度 | 54 次提交，2026-09-14 至 2026-09-17 | `git rev-list --count HEAD` |
| 教程文档入库 | `746f9df`，2026-09-17，导入 BPMN、业务流程建模、软件开发方法论与版本控制四份教程文档 | 提交历史 |

有两处与贡献记录相关的问题，顺带记在这里：

1. **提交信息未带条目编号。** 产品待办 PB-17 的验收条件要求提交记录类证据带条目编号，现有提交信息多为描述性文字。建议此后按 `PB-xx：说明` 的格式写，可省掉事后逐条对账。
2. **同一人存在两个提交身份。** 提交历史里 `郑好` 分别以 Gitee 邮箱与 GitHub 匿名邮箱出现，`git shortlog` 会把他算成两条记录。这一点已列在 `est：PB-17贡献记录表` 第六节待确认项第 5 条，本次证据再次印证：若不统一邮箱，按人汇总贡献时会出错。

### 2.5 命令对照（Task 4 用）

```bash
git clone https://github.com/Estrella6066773/HW_AISD.git
git add .
git commit -m "PB-xx：说明本次改动"
git push
```

与教程 Task 4 给出的三条命令一致，未作改动。

---

## 交之前检查

- [ ] 1.2 的优缺点四条齐全，无空单元格
- [ ] 1.3 的 11 行 × 4 列全部填了，N/A 只有一处且有说明
- [ ] 1.1 的评分口径已随表提交，评分类别（能力类／代价类／节奏类）写明
- [ ] 1.4 已引用 Simão（2011）全文信息，并更正「博士学位论文」为硕士学位论文
- [ ] 1.4.6 标注的两处 ⚠ 已对照论文原表核对，或已在提交版中保留说明
- [ ] 1.5 的两段话可直接用于汇报，未使用工程术语
- [ ] 2.2 的平台差异已向 tutor 确认，结论已回写
- [ ] 2.4 的证据在仓库中均可打开
- [ ] 本文件已上传小组仓库（对应 BPMN 表格 Task D 的同一要求）

---

## 附录 · 与仓库现有产物的对照

| 本文件的哪一部分 | 仓库里已有的承接 |
|------------------|------------------|
| 小组仓库与提交证据 | `est：PB-17贡献记录表` 视图 A |
| 人员用名与身份 | `est：PB-17贡献记录表` 第二节人名对照；第六节第 5 条 |
| 提交信息规范 | 产品待办 PB-17 验收条件 |
| 另一份 BPMN 教程的 Task D | `Ruby/2026-09-17/ruby：BPM与BPMN教程作业.md`，同一句「上传到小组仓库」 |
| 教程文档本身 | `W01/SDM Tutorial.docx`、`W01/Version Controlling 1.docx`，提交 `746f9df` |

本文件与 `ruby：BPM与BPMN教程作业.md` 是同一批 tutorial 的两份作业，上传时建议一并提交，避免老师只收到其中一份。

---

## 参考

- Simão, E.M. (2011) *Comparison of Software Development Methodologies Based on the SWEBOK*. Master's dissertation. Universidade do Minho. Available at: https://hdl.handle.net/1822/28562
- IEEE Computer Society (2014) *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide), Version 3.0*. Available at: https://ieeecs-media.computer.org/media/education/swebok/swebok-v3.pdf
- UWE Bristol (2026) *UFCEP6-0-3 Portfolio Assessment Specification V2*.
- Boehm, B. (1988) 'A spiral model of software development and enhancement', *IEEE Computer*, 21(5), pp. 61–72.
- Martin, J. (1991) *Rapid Application Development*. Englewood Cliffs, NJ: Prentice-Hall.
- Schwaber, K. and Beedle, M. (2001) *Agile Software Development with Scrum*. Upper Saddle River, NJ: Prentice Hall.
- Tutorialspoint (no date) *SDLC*. Available at: https://www.tutorialspoint.com/sdlc/index.htm
