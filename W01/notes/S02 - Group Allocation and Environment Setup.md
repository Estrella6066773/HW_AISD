# S02 · Group Allocation and Environment Setup ／ 分组与环境搭建

> 来源：`W01/S02 - Group Allocation and Environment Setup (c8).pptx`（15 页）
> 讲者：Dilshan Jayatilake & Rumali Sirimanne
> 主题：分组规则 + 本地搭建 Camunda 环境

---

## Slide 1 · Title ／ 封面

**EN**

Business Process Modelling and Enterprise Architecture & Advanced Information Systems Development
Dilshan Jayatilake & Rumali Sirimanne

**中文**

业务流程建模与企业架构 与 高级信息系统开发
Dilshan Jayatilake、Rumali Sirimanne

---

## Slide 2 · Session Plan ／ 本节安排

**EN**

- Group Formation
- Setting Up Camunda Environment
  - Install Camunda
  - Running the Camunda 7 cluster locally
  - Explore Camunda
  - Camunda Running!!!
- Group Task: Case Study Analysis
- Group Activities Checklist

**中文**

- 分组
- 搭建 Camunda 环境
  - 安装 Camunda
  - 在本地运行 Camunda 7 集群
  - 探索 Camunda
  - Camunda 跑起来了！
- 小组任务：案例分析
- 小组活动清单

> 注意：大纲第 3 点写的是 "Camunda 7"，但后面几页实际操作的是 **Camunda 8 Run**。以幻灯片正文为准，本课程用的是 Camunda 8。

---

## Slide 3 · Group Formation ／ 分组

**EN**

Group Formation

**中文**

分组（本页为分节标题页，具体规则见 Slide 12）

---

## Slide 4 · Setting Up Camunda Environment ／ 搭建 Camunda 环境

**EN**

Setting Up Camunda Environment

**中文**

搭建 Camunda 环境（分节标题页）

---

## Slide 5 · Setting Up Camunda Environment ／ 搭建 Camunda 环境

**EN**

Setting Up Camunda Environment

**中文**

搭建 Camunda 环境（分节标题页）

---

## Slide 6 · Launch Camunda 8 Run ／ 启动 Camunda 8 Run

**EN**

To start Camunda 8 Run, follow these simple steps:

1. Open a terminal (or command prompt) and navigate to the unzipped starter folder.
2. Run the start script:
   - Windows: `camunda-starter.bat`
   - Mac/Linux: `./camunda-starter.sh`
3. Watch the logs in the terminal.
4. You should see messages indicating that web interfaces are available at `http://localhost:8090` for various tools (Operate, Tasklist, etc.)

**中文**

启动 Camunda 8 Run，按以下步骤操作：

1. 打开终端（或命令提示符），进入解压后的 starter 文件夹。
2. 运行启动脚本：
   - Windows：`camunda-starter.bat`
   - Mac/Linux：`./camunda-starter.sh`
3. 观察终端里的日志输出。
4. 应当看到提示信息，说明各工具（Operate、Tasklist 等）的 Web 界面已在 `http://localhost:8090` 可用。

---

## Slide 7 · Running the Camunda 8 Cluster Locally ／ 本地运行 Camunda 8 集群

**EN**

Access each component using the following URLs:

- Operate: `http://localhost:8090/operate`
- Tasklist: `http://localhost:8090/tasklist`
- Admin: `http://localhost:8090/admin`

Login with:
- Username: `demo`
- Password: `demo`

**中文**

通过以下地址访问各个组件：

- Operate（流程运行监控）：`http://localhost:8090/operate`
- Tasklist（任务列表）：`http://localhost:8090/tasklist`
- Admin（管理后台）：`http://localhost:8090/admin`

登录凭据：
- 用户名：`demo`
- 密码：`demo`

---

## Slide 8 · You Should See… ／ 你应该看到……

**EN**

- Operate
- Task List
- Admin

**中文**

- Operate 界面
- 任务列表界面
- Admin 管理界面

（配图展示三个界面的样子）

---

## Slide 9 · Camunda Modeler ／ Camunda 建模器

**EN**

1. Go to: https://camunda.com/download/modeler/
2. Select and download the correct variant based on your operating system
3. Download and Install
4. Run

**中文**

1. 访问：https://camunda.com/download/modeler/
2. 根据操作系统选择并下载对应版本
3. 下载并安装
4. 运行

> Camunda Modeler 是画 BPMN 流程图的桌面工具，后续作业里的流程图都用它绘制。

---

## Slide 10 · Running Camunda — Configure the Connection ／ 运行 Camunda：配置连接

**EN**

1. First, launch the Camunda Modeler application.
2. Configure the connection:
   - Cluster endpoint: `http://localhost:8090/v2/`
   - or Zeebe API (gRPC): `http://localhost:26500`
   - You can find this on the console.
3. Select "Camunda connection" as the connection you just created.

*[images: Badge 1–4 outlines — deployment step badges]*

**中文**

1. 先启动 Camunda Modeler。
2. 配置连接：
   - 集群端点（Cluster endpoint）：`http://localhost:8090/v2/`
   - 或 Zeebe API（gRPC）：`http://localhost:26500`
   - 该地址可以在控制台输出中找到。
3. 选择你刚创建的 "Camunda connection" 作为连接。

*[图片：序号 1–4 的步骤徽章]*

---

## Slide 11 · Running Camunda — Deploy the Process ／ 运行 Camunda：部署流程

**EN**

1. First, launch the Camunda Modeler application.
2. Make sure your model is executable.
3. Deploying the process to the engine:
   - Click the Rocket icon on the bottom ribbon.
4. Go to: `http://localhost:8090/tasklist/processes`
   - You should see your process ready to start.
5. Go to: `http://localhost:8090/operate/`
   - Observe the process that you just started.

*[image: screenshot of the Modeler]*

**中文**

1. 先启动 Camunda Modeler。
2. 确认你的模型是可执行的（executable）。
3. 把流程部署到引擎：
   - 点击底部工具栏上的火箭图标。
4. 访问 `http://localhost:8090/tasklist/processes`
   - 应能看到你的流程已就绪、可以启动。
5. 访问 `http://localhost:8090/operate/`
   - 观察你刚启动的流程实例。

> 「可执行」指 BPMN 模型带有引擎可识别的技术属性（如任务类型、表单、变量绑定）；只画图不设这些属性，部署时不会真正生成可运行实例。

---

## Slide 12 · Find Your Group ／ 找到你的小组

**EN**

- Group Size: **5**
- Group stays throughout both units AISD & BPM&EA
- Once you set the groups you cannot change groups
- Individual contributions will be accounted for individual marks

*[image: Finding Your Group]*

**中文**

- 小组规模：**5 人**
- 小组在 AISD 与 BPM&EA 两个单元中保持不变
- 分组确定后不可更换
- 个人贡献将计入个人分数

> 最后一条很关键：小组作业里会区分个人贡献，不是"全组同分"。

---

## Slide 13 · Group Task: Case Study Analysis ／ 小组任务：案例分析

**EN**

Group Task: Case Study Analysis

**中文**

小组任务：案例分析（分节标题页，具体内容见课堂布置）

---

## Slide 14 · Group Activities Checklist ／ 小组活动清单

**EN**

Group Activities Checklist

**中文**

小组活动清单（分节标题页，具体清单见课堂布置）

---

## Slide 15 · Closing Title ／ 结束页

**EN**

Business Process Modelling and Enterprise Architecture & Advanced Information Systems Development — Group Allocation and Environment Setup
Dilshan Jayatilake & Rumali Sirimanne

**中文**

业务流程建模与企业架构 与 高级信息系统开发 —— 分组与环境搭建
Dilshan Jayatilake、Rumali Sirimanne
