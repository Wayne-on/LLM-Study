# roadmap.md — LLM-Study Skill Matrix (Evidence-Gated)

This roadmap is a **Skill Matrix**, not a simple to-do list.
Progress is gated by **Levels (L0–L5)** and must be backed by **evidence links** (sessions + lab results + track notes).

**Primary SSOT for learning history:** `/sessions/`  
**Stable knowledge:** `/tracks/`  
**Reproducible proof:** `/lab/` (with `README.md` + env spec + `RESULTS.md`)  
**Progress dashboard:** `/progress/`

---

## Levels (Ground Truth)

- **L0** — Heard of it (can’t explain reliably)
- **L1** — Can explain correctly (conceptual clarity, key terms, boundaries)
- **L2** — Working demo (runnable in `/lab/`, minimal but correct)
- **L3** — Comparative benchmarks + debugging (A/B comparison, failure analysis, fixes)
- **L4** — Production-ready (latency/memory/cost considered, monitoring/eval hooks, robust IO)
- **L5** — Design-level authority (can architect, teach, and lead delivery)

**Promotion rule:** No level upgrade without evidence links.

---

## Quarter Focus (Update Weekly)

- **Q1 focus:** LangChain v1.0 (LCEL) + DeepSpeed (ZeRO)
- **Q2 focus:** LangGraph + RAG evaluation harness
- **Q3 focus:** vLLM + quantization + serving benchmarks
- **Q4 focus:** fine-tuning mini-study + portfolio pack

---

## Track 01 — Frameworks & Application Orchestration

Focus: production design patterns, reliability, agentic workflows.

| Module | Topic | Level | Evidence (Links) | Status |
|---|---|---:|---|---|
| **LangChain v1.0** | LCEL primitives (Runnable, pipe, config) | L0 | - | Planned |
|  | Composition patterns (map, branch, parallel, retry) | L0 | - | Planned |
|  | Streaming (token streaming, callbacks) | L0 | - | Planned |
|  | Tool binding (schema, validation, retries) | L0 | - | Planned |
|  | Prompt & message modeling (roles, system constraints) | L0 | - | Planned |
| **LangGraph** | State modeling (MessagesState, reducers) | L0 | - | Planned |
|  | Cyclic graphs (loops, stop conditions) | L0 | - | Planned |
|  | Persistence (checkpointing, replay) | L0 | - | Planned |
|  | Error handling (timeouts, retries, fallbacks) | L0 | - | Planned |
| **RAG (Applied)** | Chunking strategy & metadata (why it matters) | L0 | - | Planned |
|  | Retrieval baseline (BM25 vs vector, top-k tuning) | L0 | - | Planned |
|  | Re-ranking (cross-encoder / LLM rerank) | L0 | - | Planned |
|  | Query rewrite (HyDE / sub-queries) | L0 | - | Planned |
| **Evaluation** | Offline eval set design (golden set, leakage) | L0 | - | Planned |
|  | RAG eval metrics (retrieval + generation) | L0 | - | Planned |
|  | Regression testing for prompts/workflows | L0 | - | Planned |

---

## Track 02 — Systems, Training & Performance (Infra)

Focus: GPU efficiency, distributed training, serving, benchmarking.

| Module | Topic | Level | Evidence (Links) | Status |
|---|---|---:|---|---|
| **DeepSpeed** | ZeRO-1/2/3: what is partitioned and why | L0 | - | Planned |
|  | Memory math (params/grads/optim/activations) | L0 | - | Planned |
|  | Offload (CPU/NVMe) trade-offs | L0 | - | Planned |
|  | Activation checkpointing (when it helps) | L0 | - | Planned |
|  | Throughput tuning (batch, seq, grad accum) | L0 | - | Planned |
| **Serving (Inference)** | KV cache scaling (batch/seq/heads) | L0 | - | Planned |
|  | vLLM concepts (PagedAttention, scheduling) | L0 | - | Planned |
|  | Throughput vs latency curves (p50/p95) | L0 | - | Planned |
| **Quantization** | INT8/FP8/4-bit: constraints & trade-offs | L0 | - | Planned |
|  | AWQ/GPTQ/GGUF (when to use what) | L0 | - | Planned |
| **Parallelism** | DP/TP/PP/SP mental model | L0 | - | Planned |
|  | Communication bottlenecks (bandwidth vs compute) | L0 | - | Planned |

---

## Track 03 — Mechanisms & Research (Theory)

Focus: deep understanding of “why it works”, boundaries, failure modes.

| Module | Topic | Level | Evidence (Links) | Status |
|---|---|---:|---|---|
| **Transformer Core** | Attention, FFN, residuals, normalization | L0 | - | Planned |
| **Attention Variants** | MQA/GQA intuition and impact | L0 | - | Planned |
|  | FlashAttention intuition (IO-aware view) | L0 | - | Planned |
| **Positioning** | RoPE: what it changes and why | L0 | - | Planned |
| **Caching** | KV cache: what it stores + scaling law | L0 | - | Planned |
| **MoE** | Gating + expert parallelism mental model | L0 | - | Planned |
| **Optimization** | Loss/optimizer basics for LLM training | L0 | - | Planned |
| **Scaling Laws** | Chinchilla compute-optimal idea (intuition) | L0 | - | Planned |
| **Alignment** | SFT vs DPO: objectives and behavior | L0 | - | Planned |
|  | PPO/RLHF: what is optimized and why it’s hard | L0 | - | Planned |

---

## Track 04 — Coding & System Design (Interview/Pro)

Focus: algorithmic sharpness + production LLM system design narratives.

| Module | Topic | Level | Evidence (Links) | Status |
|---|---|---:|---|---|
| **Data Structures** | Hashing, heaps, graphs (core patterns) | L0 | - | Planned |
| **Algorithms** | BFS/DFS, shortest path, greedy, DP essentials | L0 | - | Planned |
| **LLM System Design** | LLM gateway + rate limiting + caching | L0 | - | Planned |
|  | Retrieval system design (indexes, freshness, costs) | L0 | - | Planned |
|  | Training cluster design (cost + throughput) | L0 | - | Planned |
| **Debug Stories** | Incident-style writeups (symptom→hypothesis→test→fix) | L0 | - | Planned |

---

## Milestones (Evidence-Gated)

### Milestone 1 — Orchestrator (Framework L3)
- [ ] LangChain v1.0 core topics reach **L3**
- [ ] Build a minimal “production-like RAG” demo in `/lab/`
- [ ] Includes offline eval + regression tests
- Evidence required: session links + lab `RESULTS.md` + track notes

### Milestone 2 — Performance Tuner (Infra L3)
- [ ] DeepSpeed ZeRO memory math reaches **L3**
- [ ] vLLM throughput/latency benchmark reaches **L3**
- Evidence required: benchmark scripts + env + `RESULTS.md`

### Milestone 3 — Full-Stack LLM Algo Engineer (Multi-Track L4)
- [ ] At least **3 Infra topics** reach **L4**
- [ ] One end-to-end system writeup (trade-offs + eval + perf)
- Evidence required: design note + lab + regression/eval artifacts

---

## How to Update This File (Rules)

1. After each learning session:
   - Update the corresponding row’s **Level** (e.g., L0 → L1).
   - Add a link to the **session file** in Evidence.

2. When a lab demo is runnable:
   - Promote to **L2** and link the lab folder + README.

3. When you run A/B comparisons and debug failures:
   - Promote to **L3** and link `RESULTS.md` + failure analysis.

4. To claim **L4/L5**:
   - Must include explicit constraints (latency/memory/cost), monitoring/eval hooks, and robust IO.
   - Evidence must include design note + lab results + session(s).
