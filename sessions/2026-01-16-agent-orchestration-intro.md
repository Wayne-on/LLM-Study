# Session Record: Agent Systems & Orchestration Intro (L1)

- **Date**: 2026-01-16
- **Status**: Completed (L1)
- **Topic**: Agent Orchestration Patterns & Tool Calling Fundamentals

## Summary
In this session, we transitioned from evaluation to the construction of Agent systems. We focused on the conceptual landscape of how large language models are orchestrated to perform complex, multi-step tasks.

## Key Learnings
- **Orchestration Patterns**:
    - **Linear/Sequential**: Simple chain of steps.
    - **Router**: Dynamically selecting the next step based on LLM decision.
    - **Cyclic (Graph)**: Allowing for loops, refinement, and state persistence (e.g., LangGraph).
- **Tool Calling**:
    - The bridge between text and action via JSON Schema.
    - Importance of schema precision and error handling (retries/fallbacks).
- **State Management**:
    - Moving from stateless prompting to stateful orchestration where the graph "remembers" the path taken.

## Evidence & Artifacts
- Concepts Note: [orchestration-concepts.md](file:///d:/个人项目/LLM-Study/tracks/01-Frameworks/orchestration-concepts.md)
- Tool Calling Note: [tool-calling-basics.md](file:///d:/个人项目/LLM-Study/tracks/01-Frameworks/LangChain-v1.0/tool-calling-basics.md)

## Next Steps
- Implement a minimal ReAct agent in LangChain v1.0.
- Explore LangGraph state reducers and checklist persistence.
