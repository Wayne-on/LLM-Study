# LLM Algorithm Expert — Study & Skill Tracker

**Last Updated**: YYYY-MM-DD  
**Start Date**: YYYY-MM-DD  
**Target Milestone**: YYYY-MM-DD (e.g., “LLM Expert v1”)  
**Time Budget**: __ hrs/week  
**Primary Focus**: Applied LLM systems for enterprise deployment (RAG / Agents / Serving / Evaluation)

This single document tracks ALL progress toward becoming an LLM Algorithm Expert:
- Topic coverage (checklist + mastery level)
- Practice projects + deliverables
- Knowledge gaps + next actions
- Reading/materials inventory
- Weekly plan + execution log

---

## Quick Stats

- **Overall Coverage**: 0 / ___ topics = **0%**
- **Projects Shipped**: 0 / ___
- **Eval Suites Built**: 0 / ___
- **Serving Benchmarks Completed**: 0 / ___
- **Current Priority**: (fill)

---

## Skill Map Overview (Domains)

| Domain | Weight | Topics Covered | Status | Priority |
|---|---:|---:|---|---|
| **A. LLM Foundations & Math** | 10% | 0/___ | ⚪ Not Started | High |
| **B. Pretraining & Data Engineering** | 10% | 0/___ | ⚪ Not Started | Medium |
| **C. Fine-tuning & Alignment (SFT/LoRA/DPO/RL)** | 15% | 0/___ | ⚪ Not Started | High |
| **D. Inference, Serving & Optimization (vLLM/TRT/Triton)** | 15% | 0/___ | ⚪ Not Started | High |
| **E. RAG & Knowledge Systems** | 15% | 0/___ | ⚪ Not Started | High |
| **F. Agent Systems & Orchestration (LangGraph/MCP/Tools)** | 10% | 3/___ | 🟡 Learning | High |
| **G. Evaluation, Monitoring & Iteration Loops** | 10% | 0/___ | ⚪ Not Started | High |
| **H. Multimodal & Speech (ASR + SpeechLM + MLLM)** | 10% | 0/___ | ⚪ Not Started | Medium |
| **I. MLOps, Reliability & Security/Compliance** | 5% | 0/___ | ⚪ Not Started | Medium |

> **Mastery legend**: ⚪ not started · 🟡 learning · 🟢 solid · 🔵 advanced · 🟣 expert  
> **Evidence rule**: mark 🟢+ only if you have (1) notes, (2) code/demo, (3) evaluation result.

---

## A. LLM Foundations & Math (10%)

### A1. Transformer fundamentals
- [ ] Attention (scaled dot-product, multi-head, masking)
- [ ] Positional encoding (absolute/relative/rotary)
- [ ] LayerNorm/RMSNorm, residuals, MLP blocks
- [ ] KV cache: concept + memory/latency trade-offs
- [ ] Tokenization (BPE/Unigram), vocab design basics

### A2. Training objective & basics
- [ ] Causal LM vs seq2seq objective
- [ ] Cross-entropy, label smoothing, perplexity
- [ ] Exposure bias, length bias

### A3. System-level intuition
- [ ] Compute/memory/IO bottlenecks (what dominates when)
- [ ] Batch/seq length effects on throughput/latency
- [ ] Numerical precision (FP16/BF16/FP8/INT8/INT4) — conceptual map

### Notes / Links
- Notes: `progress/notes/A_foundations.md` (create)
- Key references: (fill)

---

## B. Pretraining & Data Engineering (10%)

### B1. Data pipelines
- [ ] Data collection, filtering, dedup, quality scoring
- [ ] Mixture design (domain balancing, curriculum)
- [ ] Token budget accounting; contamination checks

### B2. Distributed training fundamentals
- [ ] Data parallel / tensor parallel / pipeline parallel
- [ ] ZeRO stages; activation checkpointing
- [ ] Gradient accumulation; optimizer states

### B3. Efficiency & stability
- [ ] LR schedules; warmup; weight decay
- [ ] Gradient clipping; loss spikes; NaN debugging
- [ ] Checkpointing strategy; resuming correctly

### Notes / Links
- Notes: `progress/notes/B_pretraining.md` (create)

---

## C. Fine-tuning & Alignment (15%)

### C1. SFT (Supervised Fine-tuning)
- [ ] Dataset design for instruction following (schema, prompts, templates)
- [ ] Train/val splits; leakage prevention
- [ ] Hyperparameters; early stopping; overfitting patterns

### C2. LoRA / QLoRA
- [ ] Low-rank idea; where to insert adapters (qkv/o/proj/mlp)
- [ ] Rank/alpha/dropout trade-offs
- [ ] QLoRA quantization + adapter training constraints
- [ ] Merge vs keep adapters; deployment considerations

### C3. Preference optimization / alignment
- [ ] DPO: objective intuition; data requirements; failure modes
- [ ] RLHF overview (PPO-style), reward model basics
- [ ] Safety-alignment trade-offs in enterprise settings

### C4. Practical recipes
- [ ] LlamaFactory-style pipelines (data → train → eval → export)
- [ ] Multi-lingual fine-tuning strategy (Thai/Arabic/Spanish/Chinese)
- [ ] Task-specific tuning: intent classification, policy compliance, QC reasoning

### Notes / Links
- Notes: `progress/notes/C_finetune.md` (create)

---

## D. Inference, Serving & Optimization (15%)

### D1. Serving fundamentals
- [ ] Latency vs throughput; batching strategies
- [ ] Streaming generation; token-level latency
- [ ] Concurrency, backpressure, timeouts/retries

### D2. KV cache & memory optimization
- [ ] Paged attention; cache eviction policies
- [ ] Prefix caching; speculative decoding (overview)
- [ ] Quantized KV cache (pros/cons)

### D3. Frameworks & runtimes
- [ ] vLLM architecture & scheduling
- [ ] TensorRT-LLM build/deploy basics
- [ ] Triton Inference Server: model repo, ensemble, metrics

### D4. Quantization & acceleration
- [ ] INT8/INT4 weight-only; GPTQ/AWQ (conceptual)
- [ ] FP8 serving constraints; calibration basics
- [ ] FlashAttention (what it improves and why)

### D5. Benchmarking & profiling
- [ ] Standard benchmark protocol (hardware, batch, seq, concurrency)
- [ ] GPU profiling basics; identifying bottlenecks
- [ ] Cost model: $/1M tokens, utilization, SLOs

### Notes / Links
- Notes: `progress/notes/D_serving.md` (create)

---

## E. RAG & Knowledge Systems (15%)

### E1. Document processing
- [ ] Parsing: PDF/HTML/Markdown/Excel
- [ ] Chunking strategies (structure-aware, size limits, overlap)
- [ ] Table handling (structure extraction; tool-augmented retrieval)
- [ ] Metadata schema design (title/section/path/source/lang)

### E2. Retrieval
- [ ] Dense embeddings; multilingual embeddings
- [ ] Hybrid retrieval (BM25 + dense)
- [ ] Reranking (cross-encoder, API-based rerank)
- [ ] Query rewriting; multi-query; self-query routing

### E3. Grounding & generation
- [ ] Context packing; citations/attribution strategy
- [ ] Hallucination controls; refusal policies
- [ ] Answer synthesis patterns (map-reduce, refine)

### E4. RAG evaluation
- [ ] Retrieval metrics: recall@k, MRR, nDCG
- [ ] End-to-end metrics: faithfulness, answer correctness, usefulness
- [ ] Offline test set construction + regression harness

### Notes / Links
- Notes: `progress/notes/E_rag.md` (create)

---

## F. Agent Systems & Orchestration (10%)

### F1. Tool calling & schemas
- [x] Function/tool schema design (JSON schema, validation)
- [x] Tool routing and fallback policy
- [ ] Determinism: idempotency, retries, side-effect controls

### F2. Orchestration patterns
- [x] Prompt chaining; routing; orchestrator-workers
- [ ] Planner-executor; ReAct-style; guardrails
- [ ] State management (messages state, structured state)

### F3. LangGraph (or equivalent)
- [ ] Graph design: nodes/edges/state
- [ ] Human-in-the-loop checkpoints
- [ ] Production deployment patterns

### F4. Memory systems (applied)
- [ ] Session memory vs long-term memory
- [ ] CRUD memory store; summarization policy
- [ ] Retrieval-based memory; privacy constraints

### Notes / Links
- Notes: `tracks/01-Frameworks/orchestration-concepts.md`, `tracks/01-Frameworks/LangChain-v1.0/tool-calling-basics.md`
- Session: `sessions/2026-01-16-agent-orchestration-intro.md`

---

## G. Evaluation, Monitoring & Iteration Loops (10%)

### G1. Evaluation design
- [ ] Define success metrics per product use-case (accuracy, cost, UX)
- [ ] Golden set creation; labeling guidelines
- [ ] Error taxonomy (what to bucket and why)

### G2. Online monitoring
- [ ] Drift detection signals (traffic, intents, retrieval hit-rate)
- [ ] Feedback signals (thumbs up/down, escalation rate, recontact)
- [ ] Alerting: SLOs, thresholds, dashboards

### G3. Closed-loop improvement
- [ ] Data collection loop (hard cases, low-confidence, refusal)
- [ ] Weekly/monthly cadence: sample → label → train → eval → release
- [ ] A/B testing & rollout strategy

### Notes / Links
- Notes: `progress/notes/G_eval.md` (create)

---

## H. Multimodal & Speech (10%)

### H1. ASR systems
- [ ] ASR metrics (WER/CER), domain adaptation, VAD segmentation
- [ ] Diarization basics; channel handling
- [ ] Noise/music handling strategies

### H2. SpeechLM / audio-text
- [ ] Audio encoder + adaptor + LLM architectures (overview)
- [ ] Fine-tuning strategies for audio-text tasks
- [ ] Evaluation for voice QA / call QA

### H3. Vision-to-text grounding (for mixed docs)
- [ ] OCR vs vision captioning vs layout models (trade-offs)
- [ ] Chart/table understanding strategies
- [ ] “Unify modalities to text” pipeline validation

### Notes / Links
- Notes: `progress/notes/H_multimodal.md` (create)

---

## I. MLOps, Reliability & Security/Compliance (5%)

### I1. MLOps basics
- [ ] Model versioning; data versioning
- [ ] Reproducible runs; experiment tracking
- [ ] Release notes + rollback plan

### I2. Reliability engineering for LLM apps
- [ ] Rate limiting, caching, circuit breakers
- [ ] Timeout/retry policies; partial failures
- [ ] Graceful degradation strategy

### I3. Security & compliance
- [ ] Prompt injection threats; tool abuse risks
- [ ] PII handling; logging redaction
- [ ] Access control for tools/knowledge

### Notes / Links
- Notes: `progress/notes/I_ops_security.md` (create)

---

## Projects (Evidence-Backed Mastery)

> Rule: each project must produce **code**, **eval**, **writeup**, and **deployment notes**.

### P1. RAG Knowledge Factory (multi-format ingestion)
- [ ] Repo created
- [ ] Feishu/Markdown pipeline
- [ ] PDF pipeline
- [ ] Excel pipeline
- [ ] Table-to-DB tool linking
- [ ] Eval set + regression tests
- **Deliverables**:
  - [ ] `progress/projects/P1_writeup.md`
  - [ ] Benchmark report
  - [ ] Demo endpoint / Dify integration notes

### P2. Intent + Similar-Q + SOP Router (hybrid NLU)
- [ ] Intent classifier interface (top1/topk + thresholding)
- [ ] Similar question retrieval (within-intent vs global)
- [ ] SOP execution and fallback strategy
- [ ] Dashboard metrics + error analysis
- **Deliverables**:
  - [ ] `progress/projects/P2_writeup.md`

### P3. Serving Benchmark Suite (vLLM vs TRT vs Triton)
- [ ] Standard benchmark harness
- [ ] Throughput/latency curves at multiple concurrencies
- [ ] Memory footprint & cost estimate
- **Deliverables**:
  - [ ] `progress/projects/P3_report.md`

### P4. QC System Loop (rules → prompts → eval → iteration)
- [ ] Rule schema + template renderer
- [ ] Validation node + structured outputs
- [ ] Eval loop (ticket-level + rule-level)
- **Deliverables**:
  - [ ] `progress/projects/P4_report.md`

---

## Weekly Plan (Rolling)

### This Week (YYYY-WW)
**Focus**:
- [ ] (1)
- [ ] (2)
- [ ] (3)

**Outputs by end of week**:
- [ ] (code)
- [ ] (eval)
- [ ] (writeup)

### Next Week (YYYY-WW)
- [ ] (1)
- [ ] (2)

---

## Study Session Log (Lightweight)

| Date | Time Spent | Topic/Task | Output (link) | Result | Next Action |
|---|---:|---|---|---|---|
| YYYY-MM-DD | __h |  |  |  |  |

---

## Knowledge Gaps / Backlog (Always-On)

### Current Gaps (highest impact first)
- [ ] Gap #1 — why it matters + what “done” looks like
- [ ] Gap #2
- [ ] Gap #3

### Common Failure Modes to Watch (personal)
- [ ] “Understood but can’t re-implement from scratch”
- [ ] “Can run code but can’t explain design trade-offs”
- [ ] “No eval harness → regressions invisible”
- [ ] “Serving works but no cost/SLO story”

---

## Resource Inventory (What you have)

### Courses / Docs
- [ ] (name) — status: not started / in progress / done
- [ ] (name)

### Papers (must produce notes + 5-bullet takeaway)
- [ ] (paper)
- [ ] (paper)

### Codebases to Read (must produce architecture diagram)
- [ ] (repo)
- [ ] (repo)

---

## Competency Checklist (Graduation Criteria)

Mark “READY” only when ALL are done with evidence.

### Expert v1 Criteria
- [ ] I can design a production RAG system end-to-end with eval + monitoring
- [ ] I can fine-tune (LoRA/QLoRA) for a domain task and defend the choices
- [ ] I can benchmark and optimize serving for a target SLO and cost
- [ ] I can build a closed-loop iteration process (data → label → train → eval → release)
- [ ] I can explain trade-offs clearly (latency/throughput/quality/cost/risk)

**When all checked → Expert v1 achieved on**: YYYY-MM-DD
