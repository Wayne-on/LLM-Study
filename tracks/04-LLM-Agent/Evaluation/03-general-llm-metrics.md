# General LLM Metrics & Task-Specific Evaluation

## 1. Core Performance Metrics
Beyond RAG, LLMs are evaluated on general linguistic and logic quality:
- **Coherence**: Does the output flow logically?
- **Conciseness**: Is it free of unnecessary filler?
- **Tone/Style**: Does it match the persona (e.g., professional, empathetic)?

## 2. Safety & Compliance
Critical for customer-facing production:
- **Toxicity Detection**: Hate speech, harassment.
- **PII Leakage**: Ensuring no personal identifiable information is in the output.
- **Fairness/Bias**: Checking for stereotypical or harmful predispositions.

## 3. Task-Specific Metrics (Applied)

### A. Function Calling (Agent Accuracy)
- **JSON Schema Validity**: Does it match the expected interface?
- **Parameter Hallucination**: Does it invent non-existent arguments?
- **Tool Selection Logic**: Did it pick the correct tool for the intent?

### B. Voice Quality Assurance (QA)
- **Compliance Adherence**: Did the agent say the required opening/closing?
- **Escalation Trigger**: Did it correctly identify when to call a human manager?
- **Instruction Following**: Did it respect service constraints (e.g., no discounts > 10%)?
