# Agent Orchestration Patterns

Understanding how to structure the flow of LLM applications is critical for reliability.

## 1. Linear Chaining (Sequential)
The simplest pattern where the output of one step is the input to the next.
- **Use Case**: Simple data transformation.
- **Constraint**: Rigid, cannot handle unexpected inputs or errors gracefully.

## 2. Routing
An LLM acts as a "classifier" or "dispatcher" to decide which path to take.
- **Use Case**: Intent detection in customer service (e.g., "Refund" vs. "Technical Support").
- **Constraint**: Usually one-way; hard to recover if the router makes a mistake initially.

## 3. Parallel Execution
Running multiple prompts in parallel and aggregating the results.
- **Use Case**: Multi-perspective analysis or independent sub-task processing.

## 4. Cyclic Graphs (Agentic Loops)
Allowing the system to revisit nodes, often used in **ReAct** (Reason + Act) patterns.
- **Use Case**: Complex research tasks where the agent needs to loop until a condition is met.
- **Framework**: Best implemented with **LangGraph** due to first-class support for cycles and state persistence.

## Summary Table

| Pattern | Complexity | Reliability | Flexibility |
|---|---|---|---|
| Sequential | Low | High | Low |
| Routing | Medium | Medium | Medium |
| Cyclic | High | Hard to control | High |
