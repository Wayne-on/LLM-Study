# Standard LLM Evaluation Methods

## 1. Paradigm Shift: Word-Overlap to Semantic-Judge
Traditional metrics (BLEU/ROUGE) are no longer sufficient for production LLMs because they fail to capture meaning. Production harnesses now rely on **LLM-as-a-Judge**.

### Comparison Table
| Type | Main Metrics | Target | Best For |
|---|---|---|---|
| **Deterministic** | BLEU, ROUGE | Character/Word overlap | Summarization (baseline), Translation |
| **Model-based** | BERTScore | Vector similarity | Semantic consistency |
| **Logic/Judge** | GPT-4o Scoring | Reasoning & Quality | Production RAG, Complex Chat |

## 2. The RAG Triad
The standard framework for evaluating RAG systems without a full reference answer set.

1. **Context Relevance**: Is the retrieved text useful for answering the query?
2. **Groundedness (Faithfulness)**: Is the response derived *purely* from the context? (The "Anti-Hallucination" check)
3. **Answer Relevance**: Does the final response actually satisfy the user's intent?

## 3. High-Signal Harness Components
- **Golden Set**: A curated dataset of (Question, Reference, [Context]) used for regression testing.
- **Synthesizers**: Tools (like RAGAS) that use LLMs to generate Golden Sets from raw documents.
- **Latency/Cost Benchmarking**: Measuring the performance of the evaluation itself.

## 4. Key Pitfalls
- **Self-Correction Bias**: A model scoring its own output tends to be overly optimistic.
- **Reference Answer Dependency**: Over-reliance on "perfect" standard answers that may not be available in many domains.
