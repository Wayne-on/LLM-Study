# Tool Calling Fundamentals (L1)

Tool calling (or Function Calling) is the mechanism by which an LLM requests the execution of external code.

## 1. The Workflow
1. **Definition**: Define a tool with a name, description, and JSON Schema.
2. **Binding**: Provide these definitions to the LLM (e.g., via `llm.bind_tools(tools)`).
3. **Inference**: LLM decides to use a tool and provides the arguments.
4. **Execution**: Your code runs the tool with the provided arguments.
5. **Feedback**: The tool result is passed back to the LLM as a `ToolMessage`.

## 2. Schema Design (JSON Schema)
The quality of the tool description is the single most important factor for accuracy.
- **Be Explicit**: "Get weather" is bad; "Get the current weather for a specific city and state" is better.
- **Type Safety**: Use `enum` where possible to restrict LLM hallucination.

## 3. Error Handling
LLMs often make mistakes in tool arguments (invalid JSON, missing fields).
- **Output Parsing**: Validate the LLM output against the schema.
- **Refinement**: If invalid, send the error message back to the LLM to "fix" the call.

## 4. Tool Choice
- **Force Call**: Forcing the LLM to use a specific tool.
- **Auto**: Letting the LLM decide.
- **None**: Forcing a text-only response.
