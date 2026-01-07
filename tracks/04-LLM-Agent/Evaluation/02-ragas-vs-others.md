# Evaluation Frameworks: Ragas vs. Others

## 1. Why use a Framework?
Frameworks provide standardized abstractions for:
- **Metric Definitions**: Pre-built logic for consistency (e.g., Faithfulness).
- **Integrations**: Easy connection to CI/CD and logs (LangSmith, Weights & Biases).
- **Synthetic Data**: Building test sets without manual effort.

## 2. Framework Comparison Matrix

| Framework | Strengths | Ideal For |
|---|---|---|
| **Ragas** | Premier RAG-specific metrics; Reference-free eval; Test set generator. | RAG systems without golden answers. |
| **DeepEval** | Best developer DX; `pytest`-like syntax; modular components. | Professional CI/CD integration and unit testing. |
| **TruLens** | Visualization dashboard; detailed observability of intermediate traces. | Tracking the reasoning path of complex agents. |
| **Promptfoo** | Matrix testing (Model A/B vs. Prompt 1/2). | Rapid prototyping and prompt optimization. |

## 3. The "Custom Prompt" Alternative
In many production cases, a **custom-written Rubric (scoring guide)** inside a Prompt is superior to framework defaults because:
- It understands business-specific context (e.g., "Empathy" defined for your specific customer base).
- It is easier to debug and tune than black-box framework code.

> [!TIP]
> Use frameworks for **infrastructure** (running the tests, logging results), but use custom **Rubrics** for the actual evaluation logic in sensitive business domains.
