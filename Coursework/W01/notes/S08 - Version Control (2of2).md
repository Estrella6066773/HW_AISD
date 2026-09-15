# S08 · Version Control (2/2) ／ 版本控制（下）

> 来源：`W01/S08 - Version Control.pptx`（20 页）
> 讲者：Rumali Sirimanne
> 主题：版本控制的核心概念、分支/合并的实际场景，以及 Git 基本命令

---

## Slide 1 · Title ／ 封面

**EN**

Business Process Modelling & Enterprise Architecture and Advanced Information Systems Development — Version Control
Rumali Sirimanne

**中文**

业务流程建模与企业架构 与 高级信息系统开发 —— 版本控制
Rumali Sirimanne

---

## Slide 2 · Session Plan ／ 本节安排

**EN**

- Versioning Tasks and Concepts
- Example Scenario and GitHub

**中文**

- 版本控制的任务与概念
- 示例场景与 GitHub

---

## Slide 3 · Basic Concepts of Versioning ／ 版本控制的基本概念

**EN**

- Projects
- Revisions
- Branches
- Merging
- Conflicts

*[image: 18. Git & Version Control – The Fun Way – YouTube]*

**中文**

- 项目（Projects）
- 修订（Revisions）
- 分支（Branches）
- 合并（Merging）
- 冲突（Conflicts）

*[图片：YouTube 视频《Git & Version Control – The Fun Way》]*

---

## Slide 4 · Projects ／ 项目

**EN**

- A project is a set of files in version control
  - Called a *module* in CVS
- Version control doesn't care what files
  - Not a build system
  - Or a test system
  - Though there are often hooks to these other systems
- Just manages versions of a collection of files

**中文**

- 一个"项目"就是纳入版本控制的一组文件
  - 在 CVS 中被称为 *module*（模块）
- 版本控制并不关心这些文件是什么
  - 它不是构建系统
  - 也不是测试系统
  - 不过通常会提供挂钩（hooks）与这些系统对接
- 它只负责管理一组文件的各个版本

> 要点：Git 本身不编译、不跑测试，它只关心"内容的版本"。构建和测试要靠 CI（如 GitHub Actions）另外接上。

---

## Slide 5 · Revisions ／ 修订

**EN**

- **Check Out**
  - If you want to make a change the file needs to be checked out from the repository
- **Check In**
  - When changes are completed the new code is checked-in.
- Consider:
  - Check out a file
  - Edit it
  - Check the file back in
  - This creates a new version of the file
  - Usually increment minor version number
  - E.g., 1.5 → 1.6

**中文**

- **签出（Check Out）**
  - 如果你想修改某个文件，需要先把它从仓库中签出
- **签入（Check In）**
  - 修改完成后，把新代码签入
- 设想这样一个流程：
  - 签出一个文件
  - 编辑它
  - 把它签回仓库
  - 这会创建该文件的一个新版本
  - 通常递增次版本号（minor version）
  - 例如：1.5 → 1.6

*[图片：Revisions]*

---

## Slide 6 · Revision (cont'd) ／ 修订（续）

**EN**

- A **commit** consists of a set of checked-in files and the **diff** between the new and parent versions of each file.
- Each check-in is accompanied by a user name and other meta data.

**中文**

- 一次**提交（commit）**由一组签入的文件构成，并记录每个文件新版本与父版本之间的**差异（diff）**。
- 每次签入都附带用户名及其他元数据（时间戳、提交说明等）。

> Git 存储的是"差异 + 快照"而非整个文件副本，这也是仓库体积小的原因。

*[图片：Basic Checkin]*
*[图片：Diff]*

---

## Slide 7 · Branches ／ 分支

**EN**

- A branch is just two revisions of a file
  - Two people check out 1.5
  - Check in 1.5.1
  - Check in 1.5.2
- Notes:
  - Normally checking in does **not** create a branch
  - Changes merged into main code line
  - Must **explicitly** ask to create a branch

**中文**

- 一个分支本质上就是同一文件的两个修订版本
  - 两个人各自签出 1.5
  - 一人签入 1.5.1
  - 另一人签入 1.5.2
- 说明：
  - 通常签入并不会创建分支
  - 变更会被合并进主干代码线
  - 必须**显式地**请求创建分支

*[图片：Branching]*

---

## Slide 8 · Merging ／ 合并

**EN**

- There are occasions when multiple versions of a file need to be collapsed into a single version.
  - E.g. A feature from one branch is required in another
- This process is known as a **merge**.
- Difficult and dangerous to do in CVS
- Easy and cheap to do in git

**中文**

- 有时需要把一个文件的多个版本归并成单一版本。
  - 例如：某个分支上的功能需要在另一个分支上使用
- 这个过程称为**合并（merge）**。
- 在 CVS 中做合并既困难又危险
- 在 Git 中做合并则轻松且代价很低

> 这也是 Git 逐渐取代 CVS/SVN 的重要原因之一——分支与合并的成本极低，可以放心地开分支做实验。

*[图片：Merging]*

---

## Slide 9 · Conflicts ／ 冲突

**EN**

- Arise when two programmers edit the same piece of code
- One change overwrites another
- The system doesn't know what should be done, and so complains of a conflict.
- Conflicts must be resolved by hand

**中文**

- 当两名程序员编辑了同一段代码时就会出现
- 一处修改覆盖了另一处
- 系统不知道该如何处理，于是报告冲突（conflict）。
- 冲突必须**手工**解决

*[图片：Conflict]*

---

## Slide 10 · Example Scenario and GitHub ／ 示例场景与 GitHub

**EN**

Example Scenario and GitHub

**中文**

示例场景与 GitHub（分节标题页）

---

> ### 关于 Slide 11–16：分支与合并场景
>
> 这 6 页在原 PPT 中是**同一张图逐步播放的动画**，讲一个"线上版本发现致命 bug"的故事。抽取出来是碎片化的，下面按叙事顺序重构成一个完整场景，并标注每一步。

### Slide 11 · Step 1 — 首次公开发布

**EN**

- Releases: **1.0**
- First public release of the hot new product

**中文**

- 版本线：**1.0**
- 这款热门新产品的首次公开发布

---

### Slide 12 · Step 2 — 内部继续开发

**EN**

- Internal development continues, progressing to version **1.3**

**中文**

- 内部开发继续进行，推进到 **1.3** 版

---

### Slide 13 · Step 3 — 发现致命 bug，开分支修复

**EN**

- A fatal bug is discovered in the product (1.0), but 1.3 is not stable enough to release.
- **Solution**: Create a version based on 1.0 with the bug fix.

**中文**

- 在产品 **1.0** 中发现了一个致命 bug，但 **1.3** 还不够稳定，无法发布。
- **解决方案**：基于 1.0 创建一个带 bug 修复的版本。

> 关键决策点：不能直接把 1.3 发出去（不稳定），也不能等 1.3 修好再修 bug（用户等不了），所以从 1.0 拉一条修复分支。

---

### Slide 14 · Step 4 — 这就是分支

**EN**

- Note that there are now **two lines of development** beginning at 1.0.
- This is **branching**.

**中文**

- 注意，现在从 1.0 开始有了**两条并行的开发线**。
- 这就是**分支（branching）**。

---

### Slide 15 · Step 5 — 修复也要回流到主线

**EN**

- The bug fix should also be applied to the main code line so that the next product release has the fix.
- Releases: 1.3 → **1.4**

**中文**

- 这个 bug 修复也应当应用到主线代码上，这样下一个产品版本才会包含该修复。
- 版本线：1.3 → **1.4**

---

### Slide 16 · Step 6 — 这就是合并

**EN**

- Note that two separate lines of development come back together in **1.4**.
- This is **merging** or updating.

**中文**

- 注意，两条独立的开发线在 **1.4** 处重新汇合。
- 这就是**合并（merging）**或更新（updating）。

---

## Slide 17 · Using a Git Repository ／ 使用 Git 仓库：工作流

**EN**

- Workflow: your local repository consists of three "trees" maintained by git.
  - The first one is your **Working Directory**, which holds the actual files.
  - The second one is the **Index**, which acts as a staging area.
  - The third one is the **HEAD**, which points to the last commit you've made.

**中文**

- 工作流：你的本地仓库由 Git 维护的三个"树（trees）"组成。
  - 第一个是**工作目录（Working Directory）**，存放实际的文件。
  - 第二个是**索引（Index）**，充当暂存区（staging area）。
  - 第三个是 **HEAD**，指向你最后一次提交。

> 数据流向：工作目录 →（`git add`）→ 暂存区 Index →（`git commit`）→ HEAD/版本库。理解这三层，"为什么 add 完还要 commit"就清楚了。

---

## Slide 18 · Using a Git Repository ／ 使用 Git 仓库：常用命令

**EN**

**Create a new (local) repository** — create a new directory and initialise
```bash
git init
```

**Check out a repository**
```bash
git clone /path/to/repository
git clone username@host:/path/to/repository
```

**Propose changes to Index**
```bash
git add <filename>
git add *
```

**Commit changes**
```bash
git commit -m "Commit message"
```

**Push changes (to master branch)**
```bash
git push origin master
```

**Update local repository to newest commit**
```bash
git pull
```

**中文**

**创建新的（本地）仓库** —— 新建目录并初始化
```bash
git init
```

**检出（克隆）仓库**
```bash
git clone /path/to/repository
git clone username@host:/path/to/repository
```

**把改动加入索引（暂存）**
```bash
git add <filename>
git add *
```

**提交改动**
```bash
git commit -m "提交说明"
```

**推送改动（到 master 分支）**
```bash
git push origin master
```

**把本地仓库更新到最新提交**
```bash
git pull
```

> 补充（幻灯片未提但实际常用）：`git status` 看当前状态、`git log` 看历史、`git branch` 看分支、`git checkout -b <name>` 新建并切换分支。

---

## Slide 19 · References and Further Reading ／ 参考与延伸阅读

**EN**

- https://betterexplained.com/articles/a-visual-guide-to-version-control/
- http://rogerdudler.github.io/git-guide/

**中文**

- https://betterexplained.com/articles/a-visual-guide-to-version-control/ —— 版本控制可视化指南
- http://rogerdudler.github.io/git-guide/ —— Git 简明指南（中文版可用：https://rogerdudler.github.io/git-guide/index.zh.html）

---

## Slide 20 · Closing Title ／ 结束页

**EN**

Business Process Modelling & Enterprise Architecture and Advanced Information Systems Development — Version Control
Rumali Sirimanne

**中文**

业务流程建模与企业架构 与 高级信息系统开发 —— 版本控制
Rumali Sirimanne
