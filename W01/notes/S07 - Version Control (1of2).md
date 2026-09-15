# S07 · Version Control (½) ／ 版本控制（上）

> 来源：`W01/S07 - Version Control.pptx`（9 页）
> 讲者：Rumali Sirimanne
> 主题：版本控制的概念、用途、系统类型与基本功能

---

## Slide 1 · Title ／ 封面

**EN**

Business Process Modelling and Enterprise Architecture — Version Control (½)
Rumali Sirimanne

**中文**

业务流程建模与企业架构 —— 版本控制（上）
Rumali Sirimanne

---

## Slide 2 · Session Plan ／ 本节安排

**EN**

- What is Version Control?
- Uses of Version Control
- Version Control System (VCS)
- Centralised Version Control
- Distributed Version Control
- Features of VCS

**中文**

- 什么是版本控制？
- 版本控制的用途
- 版本控制系统（VCS）
- 集中式版本控制
- 分布式版本控制
- VCS 的功能特性

---

## Slide 3 · What is Version Control? ／ 什么是版本控制？

**EN**

- Version control
  - a.k.a. revision control or source control
  - managing multiple versions of documents, programs, web sites, etc.
  - Allows programmers to keep track of every revision
- How different is version control from back-up?
  - Back-up is usually **time based** (Mac Time Machine)
  - Version control is about **line of work**

**中文**

- 版本控制
  - 又称修订控制（revision control）或源码控制（source control）
  - 管理文档、程序、网站等的多个版本
  - 让程序员能够追踪每一次修订
- 版本控制与备份有何不同？
  - 备份通常以**时间**为轴（如 Mac 的 Time Machine）
  - 版本控制关注的是**工作的演变脉络**（line of work）

> 这是本页的核心区分：备份回答"三天前这个文件长什么样"，版本控制回答"这个功能是在哪个分支、由谁、为了什么改出来的"。

*[图片：示意图]*

---

## Slide 4 · Uses of Version Control ／ 版本控制的用途

**EN**

- Version control is not just useful for collaborative working, it is essential for quality source code development
- Often want to undo changes to a file
  - start work, realize it's the wrong approach, want to get back to starting point
  - like "undo" in an editor…
  - keep the whole history of every file and a changelog
- Also want to be able to see who changed what, when
- The best way to find out how something works is often to ask the person who wrote it

**中文**

- 版本控制不只是协作时的便利工具，更是高质量源码开发的**必需条件**
- 我们常常需要撤销对文件的修改
  - 开工之后发现思路不对，想回到起点
  - 就像编辑器里的"撤销"……
  - 但它保留每个文件的完整历史和变更日志
- 还希望能看到**谁在什么时候改了什么**
- 想弄明白某段代码为什么这样写，最好的办法往往是去问写它的人

---

## Slide 5 · Version Control System (VCS) ／ 版本控制系统

**EN**

- A system which allows for the management of a code base
- Files are kept in a **repository**
- Repositories can be local or remote to the user
- The user edits a copy called the **working copy**
- Changes are **committed** to the repository when the user is finished making changes
- Other people can then access the repository to get the new code
- Types of VCS
  - Centralised Version Control System
  - Distributed Version Control System

**中文**

- 一种用于管理代码库的系统
- 文件保存在**仓库（repository）**中
- 仓库对用户而言可以是本地的，也可以是远程的
- 用户编辑的副本称为**工作副本（working copy）**
- 修改完成后，把变更**提交（commit）**到仓库
- 其他人随后即可访问仓库取得新代码
- VCS 的类型
  - 集中式版本控制系统
  - 分布式版本控制系统

*[图片：Repo]*

---

## Slide 6 · Centralised Version Control ／ 集中式版本控制

**EN**

- A single server holds the code base
- Clients access the server by means of check-in / check-outs
- Examples include CVS, Subversion, Visual Source Safe.
- **Advantages**: Easier to maintain a single server.
- **Disadvantages**: Single point of failure.

**中文**

- 由**单一服务器**保存整个代码库
- 客户端通过签入/签出（check-in / check-out）访问服务器
- 典型例子：CVS、Subversion（SVN）、Visual Source Safe
- **优点**：只需维护一台服务器，较为简单。
- **缺点**：存在单点故障（服务器挂了，所有人都无法工作）。

*[图片：集中式版本控制示意图]*

---

## Slide 7 · Distributed Version Control ／ 分布式版本控制

**EN**

- Each client (essentially) holds a complete copy of the code base.
- Code is shared between clients by push / pulls
- **Advantages**: Many operations cheaper. No single point of failure
- **Disadvantages**: A bit more complicated!

**中文**

- 每个客户端（基本上）都持有一份完整的代码库副本。
- 代码通过 push / pull 在各客户端之间共享。
- **优点**：许多操作开销更小；不存在单点故障。
- **缺点**：相对更复杂一些！

> Git 属于分布式版本控制；这也是本课程会用到的方式。

*[图片：分布式版本控制示意图]*

---

## Slide 8 · Features of VCS ／ VCS 的功能特性

**EN**

**Essential Features**
- Check-in and check-out of items to repository
- Creation of baselines (labels / tags)
  - Version 1.0 released!
- Control and manipulation of branching
  - management of multiple versions
- Overview of version history

**Additional Features**
- Code Responsibility and Code Audits
- Forking (Common with Open Source)
- Metrics

**中文**

**核心功能**
- 向仓库签入（check-in）与从仓库签出（check-out）条目
- 创建基线（baseline，即标签 label / tag）
  - 例如：1.0 版发布！
- 分支（branching）的控制与操作
  - 管理多个版本
- 版本历史总览

**附加功能**
- 代码责任归属与代码审计（Code Responsibility / Code Audits）
- 派生（Forking，开源项目中很常见）
- 度量指标（Metrics）

> **基线（tag）**就是给某个 commit 起一个固定名字（如 `v1.0`），之后无论代码怎么演进，都能随时回到这个发布点。

*[图片：示意图]*

---

## Slide 9 · Closing Title ／ 结束页

**EN**

Business Process Modelling and Enterprise Architecture — Version Control (½)
Rumali Sirimanne

**中文**

业务流程建模与企业架构 —— 版本控制（上）
Rumali Sirimanne
