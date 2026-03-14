# OpenClaw 集中学习清单

## 一、学习目标

这次学习 OpenClaw，不要把目标定成“会配置渠道、会接飞书、会聊天”。

更好的目标是这 4 个：

1. 我能说清 **OpenClaw 到底是什么架构**
2. 我能说清 **消息进来后是怎么变成一次 agent 执行的**
3. 我能说清 **workspace / session / tools / plugins 各自负责什么**
4. 我能判断 **哪些设计值得我以后自己做企业级 Agent 时借鉴**

---

## 二、OpenClaw 的核心定位

OpenClaw 不只是一个聊天机器人项目，更适合理解为一个 **self-hosted gateway / agent runtime**。

学习时要先抓住它的几个核心抽象：

- **Gateway**：整个系统入口，负责渠道接入、会话路由、状态管理
- **Agent**：一个独立“脑子”，有自己的 workspace、配置、身份、记忆
- **Session**：上下文和记忆的分桶机制
- **Tools**：给模型调用的能力
- **Plugins**：给整个系统加扩展能力
- **Workspace**：agent 的工作目录，也是很多上下文工程的显式载体

---

## 三、推荐学习顺序

不要一上来就看源码，也不要一开始就折腾多 agent 和复杂插件。

推荐顺序：

**最小闭环 → workspace → session → memory → tools/browser → multi-agent → plugins → 源码**

这个顺序的核心原因是：

> OpenClaw 最值得学的，不是“接了哪些渠道”，而是它如何把 agent runtime、workspace、session、memory、tools、plugins 这几层拆开。

---

# 模块 1：先跑通“最小闭环”

## 目标

只做最小闭环，不碰多 agent，不碰插件开发，不碰复杂渠道。

## 要做的事

先确认以下能力已经可用：

- `openclaw gateway status`
- `openclaw dashboard`
- 浏览器里能够正常聊天

## 这一模块要回答的问题

- 一句消息是怎么进入 Gateway 的？
- 回复出来之前，中间经过了哪些层？
- 现在看到的“能聊天”，本质是 Gateway 在跑，还是某个前端在跑？

## 建议产出

写一页自己的笔记，标题可以叫：

**OpenClaw 最小运行闭环**

只写一句总链路：

> 用户消息 → Gateway → agent runtime → tools / memory / workspace context → 回复

---

# 模块 2：重点研究 workspace，而不是聊天界面

这是 OpenClaw 最值得学的部分之一。

## 核心理解

OpenClaw 把很多“上下文工程”显式文件化了。  
也就是说，很多能力不是藏在某个巨大 prompt 里，而是写在 workspace 文件里。

常见文件包括：

- `AGENTS.md`
- `SOUL.md`
- `TOOLS.md`
- `BOOTSTRAP.md`
- `IDENTITY.md`
- `USER.md`
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`

## 你要做的实验

每次只改一个文件，然后观察行为变化：

### 1. 只改 `SOUL.md`
观察：

- 语气是否变化
- 边界是否变化
- 人格是否变化

### 2. 只改 `USER.md`
观察：

- 它对“你是谁”的理解是否变化
- 是否更容易带入用户背景

### 3. 只改 `AGENTS.md`
观察：

- 执行偏好是否变化
- 操作约束是否变化
- 是否更像“系统规则”

### 4. 手动写 `MEMORY.md` 和 `memory/当天日期.md`
观察：

- 聊天时是否引用这些内容
- 长期记忆和当天记忆是否有区别

## 这一模块最终要理解的结论

OpenClaw 的一个关键设计思想是：

> 把人格、规则、用户画像、记忆等上下文工程显式写进文件系统，而不是全部藏在黑盒 prompt 里。

这对你以后做企业级 Agent 非常有借鉴意义。

---

# 模块 3：把 session 吃透

这一块比 multi-agent 更重要。

## 你要搞懂的核心问题

- 什么叫 main session？
- 什么叫按用户分桶？
- 什么叫按渠道分桶？
- 一条消息到底是怎么映射到某个 session key 的？

## 你要做的实验

重点测试下面 4 种情况：

### 1. 同一窗口连续聊天
看是否进入同一个上下文桶。

### 2. 换一个窗口聊天
看 session 是否变化。

### 3. 换一个渠道聊天
看上下文是否还连续。

### 4. 群聊 / 私聊
如果你后面接了渠道，要测试：

- 群聊和私聊是否共享上下文
- 不同人是否进入不同 session

## 这一模块的核心结论

以后做企业级助手时，所谓“上下文工程”有一大部分其实就是：

> 用户消息如何映射到 session key，进而决定上下文连续性和记忆边界。

---

# 模块 4：理解 memory 机制

## 核心理解

OpenClaw 的 memory 更像是一种 **文件化外置记忆**，而不是“模型自己神秘地记住了什么”。

也就是说：

- 记忆最终是落到文件里的
- 文件才是真正的 source of truth
- 模型是否“记住”，本质上取决于写没写进去、读没读出来

## 你要做的实验

### 1. 手动写 `memory/YYYY-MM-DD.md`
观察当天对话是否引用。

### 2. 手动写 `MEMORY.md`
观察长期偏好和设定是否会持续影响行为。

### 3. 在聊天中明确说“记住这件事”
观察：

- 它是否真的写入了 memory
- 写到了 daily memory 还是 long-term memory

### 4. 看 memory 状态
观察系统是否有相关状态、索引或读取机制。

## 你要想明白的问题

- OpenClaw 的记忆到底是不是黑盒？
- 为什么用 Markdown 文件存 memory？
- 这种方式对可解释性、可维护性有什么优势？

## 结论

这类“文件化记忆”的思路非常适合企业场景，因为它：

- 可查看
- 可编辑
- 可审计
- 可迁移

---

# 模块 5：再看 tools，尤其是 browser

这一块要重点理解“受控工具”的设计思想。

## 核心理解

Tool 是给 agent 调用的动作接口，不等于系统插件。

要先理解：

- 哪些能力适合做 tool
- 哪些能力不应该直接暴露给 agent
- tool 调用和普通聊天的边界是什么

## 你要做的事

### 1. 看当前有哪些 tools
不要先开发，先观察现成能力。

### 2. 重点体验 browser
观察：

- browser 能做到哪些自动化动作
- 是否使用独立 profile
- 是否和你自己的真实浏览器环境隔离

### 3. 对比普通聊天和 tool 调用
重点看：

- 什么时候是纯生成
- 什么时候会触发执行
- 工具能力的边界怎么控制

## 这一模块要输出的结论

你需要能回答：

- 什么能力适合定义成 tool？
- 什么能力不适合？
- OpenClaw 的 tools 和你理解的 skills / function calling / MCP 有什么异同？

---

# 模块 6：再看 multi-agent

等前面模块理解得差不多了，再看 multi-agent 才不会乱。

## 核心理解

multi-agent 不是简单“多几个 prompt”，而是：

- 多套 workspace
- 多套身份
- 多套 sessions
- 多套路由绑定关系

## 你要做的实验

自己创建两个 agent，例如：

- `work`
- `personal`

然后测试：

### 1. 不同 agent 的 `SOUL.md`
看人格和行为是否明显隔离。

### 2. 不同 agent 的 workspace
看上下文和记忆是否独立。

### 3. 不同 agent 的绑定关系
看某个入口是否可以固定走某个 agent。

## 你要搞懂的问题

- multi-agent 到底是不是“多 prompt”？
- agent 的隔离边界在哪里？
- channel / routing / binding 是怎么和 agent 关联起来的？

## 最终结论

OpenClaw 的 multi-agent 更接近：

> 多个独立工作空间下的多实例 runtime，而不是简单多角色提示词。

---

# 模块 7：最后才看 plugins

插件不是最先学的，因为它是“扩展 OpenClaw 系统”，不是“理解 OpenClaw 本体”。

## 先要搞懂的分工

### Tool
给 agent 调用的能力。

### Plugin
给 OpenClaw 系统本身扩展命令、工具、RPC、服务等能力。

## 你这一模块的目标

先不要急着写插件，先搞清：

- plugin 和 tool 的区别
- plugin 和 workspace skill 的关系
- plugin 在系统架构里属于哪一层
- 什么功能应该做成 plugin
- 什么功能只需要 tool / skill 就够了

## 你可以做的最小实验

- 查看当前已加载插件
- 安装一个最简单的官方插件
- 观察它给系统增加的到底是什么：
  - 命令
  - 工具
  - RPC
  - 还是后台服务

## 这一模块的最终结论

插件是系统扩展层，不是学习 OpenClaw 的起点。

---

# 模块 8：最后回头读源码

等前面都过完，再读源码才不会迷路。

## 推荐顺序

1. CLI 入口
2. Gateway 配置与启动
3. agent runtime
4. session 管理
5. tools 注册
6. plugins 注册

## 为什么不能一开始就看源码

因为一开始没有“运行时地图”，你看到的只会是一堆目录和模块名，理解会非常散。

而当你已经知道：

- 消息怎么进来
- session 怎么分桶
- workspace 怎么注入上下文
- tools 和 plugins 怎么分层

这时再读代码，就会非常顺。

---

# 四、这几天集中学习时，一定要写的 3 份笔记

## 1. OpenClaw 架构图

至少包含以下节点：

- Gateway
- Channel
- Agent
- Workspace
- Session
- Memory
- Tools
- Plugins

目标是让你自己能画出一张图，解释整条消息链路。

---

## 2. OpenClaw 与你现有体系的映射表

建议写成这种形式：

- OpenClaw Gateway ≈ 模型网关 / 运行时入口
- Workspace 文件 ≈ 显式上下文工程
- Session ≈ 对话上下文分桶
- Memory ≈ 文件化外置记忆
- Tools ≈ 工具调用层
- Plugins ≈ 系统扩展层

这一步很关键，因为它能帮助你把“学会 OpenClaw”转化为“借鉴 OpenClaw 的设计”。

---

## 3. 值得借鉴 / 不值得直接照搬

建议分成两栏。

### 值得借鉴

- 把上下文工程显式文件化
- 把 session 边界设计清楚
- 把工具层和系统扩展层分开
- 把记忆落到可读写文件中
- 让 agent 以 workspace 为核心组织运行

### 需要谨慎

- 安全边界不能想当然
- 工具权限不能默认全开
- 个人助手信任模型不一定适合企业多人场景
- 插件与宿主环境隔离问题要特别注意

---

# 五、学习完成后的最终标准

如果你学完后，能够清楚回答下面这些问题，就说明你真的学进去了：

1. OpenClaw 为什么不是单纯聊天机器人，而更像一个 gateway / agent runtime？
2. 一条消息从进入系统到输出回复，中间经历了哪些层？
3. workspace 为什么是 OpenClaw 的核心？
4. session 为什么比 multi-agent 更值得先学？
5. memory 为什么做成文件化外置记忆？
6. tools 和 plugins 的边界是什么？
7. multi-agent 为什么不是简单“多 prompt”？
8. OpenClaw 哪些设计适合借鉴到企业级 Agent 系统里？

---

# 六、最推荐的整体学习顺序（最终版）

直接照这个顺序冲：

**最小闭环 → workspace → session → memory → tools/browser → multi-agent → plugins → 源码**

这是最省时间、也最不容易学乱的路径。

---

# 七、一句话总结

OpenClaw 最值得学习的，不是“它帮你自动干活”，而是它把 Agent 系统拆成了：

- Gateway
- Agent
- Workspace
- Session
- Memory
- Tools
- Plugins

并且把大量上下文工程显式文件化了。

这套思路对以后自己做企业级助手、运行时框架、Skills / MCP / Tool 系统设计，都非常有启发。