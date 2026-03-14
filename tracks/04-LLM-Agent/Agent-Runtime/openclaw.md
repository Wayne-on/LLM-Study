OpenClaw
Gateway / channels / sessions / tools / events

算法负责：

上下文管理

编排

Skills / Tools

路由与 fallback

输出结构化

必要的审批点

后端同事负责：

登录鉴权

权限/RBAC

会话存储

业务接口

审计

网关


Python + PydanticAI 开发 Agent 内核
用 MCP 组织 Skills / Tools
外面只包一层很薄的 FastAPI 适配层，供后端调用

所以你真正该用的，不是“完整助手框架”，而是“Agent 内核框架”

如果我替你把选型说死，就是这句：

你现在该用 PydanticAI 开发一个“Agent 内核服务”，而不是去找一个完整助手平台。

然后外面这样搭：

前端 / 飞书 / IM
   ↓
业务后端 / BFF
   ↓
Agent Runtime Service（你负责）
   ├─ context manager
   ├─ orchestration
   ├─ skills/tools
   ├─ route/fallback
   └─ structured output
        ↓
内部 API / MCP Tools（后端提供或你封装）

用 Python + PydanticAI 开发 Agent Runtime 内核，用 MCP 组织 Skills/Tools，再用一层很薄的 FastAPI 暴露给后端。