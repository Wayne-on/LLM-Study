---
date: 2026-01-05
track: 01-Frameworks
module: Evaluation
topic: LLM Evaluation Basics & RAG Triad
status: ok
links:
  notes: tracks/04-LLM-Agent/Evaluation/01-standard-methods.md
refs:
  - https://www.trulens.org/trulens_eval/core_concepts_rag_triad/
tags: [evaluation, rag, metrics, basics]
---

## Goal + context
学习 LLM Evaluation 的标准方法，目标是达到 L1 级别（口头解释概念），为后续构建生产级评估 Harness 打下基础。

## Prior understanding
- 对 RAGAS, DeepEval, BLEU/ROUGE 等概念不清楚。
- 目标明确：生产级评估。

## What we covered
1. **LLM 评估的本质跳变**：从“字面对齐”到“语义对齐”。
2. **评估三轴 (Three Axes)**：Traditional, Human, LLM-as-a-Judge。
3. **RAG Triad (三元组)**：Context Relevance, Groundedness, Answer Relevance。
4. **Ragas vs 其他框架**：Ragas (RAG 专项), DeepEval (工程化), Promptfoo (矩阵测试), Custom Rubric (灵活度)。
5. **Meta-Evaluation (元评估)**：如何通过人工打标来评估 Judge 的对齐率 (Cohen's Kappa)。
6. **Online vs Offline 哲学**：离线看 Benchmark/回归，线上看风险管控/可观测性。

## Knowledge gaps + mistakes
- 用户最初不了解主流框架的设计偏好（如 Ragas 强调的参考答案无关性）。
- 虽然识别出了幻觉，但对如何通过优化 Prompt 或检索来量化解决仍需后续探讨。

## What I can now do
- 能够口头解释 RAG Triad 的三个维度及其对应的失效场景。
- 理解为什么生产环境不能只依赖 BLEU/ROUGE。
- 理解 Meta-Evaluation 的闭环逻辑。
- 能够根据业务场景选择合适的评估框架或自定义 Prompt。

## Verification task outcome
- **Pass 1**: 准确识别出 Groundedness 导致的幻觉。
- **Pass 2**: 准确识别出回归测试中 FN 的含义及其修复方向。

## What to distill into /tracks
- `tracks/04-LLM-Agent/Evaluation/01-standard-methods.md`
- `tracks/04-LLM-Agent/Evaluation/02-ragas-vs-others.md`
- `tracks/04-LLM-Agent/Evaluation/03-general-llm-metrics.md`
- `tracks/04-LLM-Agent/Evaluation/04-meta-evaluation.md`
- `tracks/04-LLM-Agent/Evaluation/05-online-evaluation-monitoring.md`
