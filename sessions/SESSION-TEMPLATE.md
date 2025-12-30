# SESSION-TEMPLATE.md — LLM-Study

> **Purpose:** Capture the raw learning history (SSOT) for one session.
> This file should be copied into `/sessions/` as:
>
> - `/sessions/YYYY-MM-DD__track__module__topic.md` (preferred)
> - or `/sessions/YYYY-MM-DD-topic.md` (fallback)

---

## YAML Metadata (Required)

```yaml
---
date: YYYY-MM-DD
start_time: "HH:MM"          # optional
duration_min: 0              # estimate is fine
track: 01-Frameworks | 02-Infra-System | 03-Theory-Paper | 04-Interview
module: LangChain-v1.0 | DeepSpeed | vLLM | Attention | ...
topic: Short, specific title
goal_type: production | research | interview
status: weak | ok | mastered
level_before: L0 | L1 | L2 | L3 | L4 | L5
level_after: L0 | L1 | L2 | L3 | L4 | L5
evidence_targets:
  sessions: []               # keep this file path after saving
  tracks: []                 # add if you distilled anything today
  lab: []                    # add if you wrote/ran code
refs:                        # primary sources only if possible
  - title: ""
    link: ""
tags: [tag1, tag2]
---
````

---

## 1) Session Summary (10 lines max)

* **Why today (context):**
* **What I wanted (success definition):**
* **What we actually did:**
* **Outcome (pass/fail vs goal):**
* **One sentence takeaway:**

---

## 2) Baseline (Before Teaching)

### 2.1 What I thought I knew

* …

### 2.2 What I was confused about

* …

### 2.3 Constraints / assumptions

* Hardware:
* Latency/throughput target:
* Cost target:
* Data/eval availability:
* Other:

---

## 3) Dialogue Log (Socratic Record)

> Keep this section faithful and concrete.
> Prefer short bullets over long prose.

### Q1 — [Question / Topic]

* **My question (verbatim):**
* **My initial answer / mental model:**
* **Mentor’s key guidance (concepts + reasoning):**
* **Common pitfalls / failure modes mentioned:**

**Comprehension check**

* **Check question:**
* **My answer:**
* **Verdict:** Strong / Partial / Weak
* **Fix / clarification (if needed):**

**Micro-experiment or exercise (if any)**

* What we tested:
* Inputs:
* Expected outcome:
* Actual outcome:
* Notes:

---

### Q2 — [Question / Topic]

*(repeat the same structure as Q1)*

---

## 4) Key Concepts (Distilled, Evidence-Friendly)

> Write “stable” statements only. If it’s uncertain, mark it.

### 4.1 Facts (with sources)

* **Fact:** …

  * Source: …

### 4.2 Inferences (based on facts above)

* **Inference:** …

  * Depends on: …

### 4.3 Hypotheses (need verification)

* **Hypothesis:** …

  * Verification plan: …

---

## 5) Verification (MANDATORY)

### 5.1 Verification task

* **Task:**
* **Pass criteria:**
* **Expected failure cases:**

### 5.2 Result

* **Status:** Not started / Passed / Failed
* **If failed, why:**
* **Next fix:**

---

## 6) Lab Artifacts (If Any)

> If code was written or run, record it here.

* **Lab path(s):**
* **How to run (one-liner):**
* **Environment notes (GPU/driver/libs):**
* **Metrics collected:** (tokens/sec, p50/p95 latency, peak VRAM, etc.)
* **RESULTS.md updated?** Yes / No

---

## 7) Knowledge Gaps & Risk Register

> Keep this brutally honest. These drive future review sessions.

| Gap / Risk | Severity (H/M/L) | Symptom | Likely cause | Fix plan | Evidence link |
| ---------- | ---------------- | ------- | ------------ | -------- | ------------- |
|            |                  |         |              |          |               |

---

## 8) What I Can Now Do (Evidence-Based)

> Use capability statements, not vague confidence.

| Capability | Level reached | Proof (links)              |
| ---------- | ------------: | -------------------------- |
| I can …    |            L? | session / lab / track link |

---

## 9) Updates Required (SSOT Workflow)

### 9.1 Progress updates (must do after session)

* [ ] Update `/progress/tech-stack.md` (levels + evidence)
* [ ] Update `/progress/tracker.md` (checklist items)

### 9.2 Distillation targets (optional but recommended)

* [ ] Create/update track note: `tracks/.../...md`
* [ ] Update module index: `tracks/.../INDEX.md`

---

## 10) Next Session Plan (Max 3 items)

* [ ] **Next #1:** …
* [ ] **Next #2:** …
* [ ] **Next #3:** …

---

## 11) Meta Notes (Optional)

* What teaching style worked best today:
* My recurring mistake pattern:
* What to change in my approach next time:

