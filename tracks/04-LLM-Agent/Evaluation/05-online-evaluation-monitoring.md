# Online Evaluation & Monitoring Strategies

## 1. The Offline vs. Online Gap
- **Offline (Development)**: High cost, high accuracy, Golden Data available. Goal: **Regression & Benchmarking**.
- **Online (Production)**: Low-latency, high volume, No labels. Goal: **Risk Control & Observability**.

## 2. Online Strategies

### A. Real-time Guardrails
- Lightweight checks (regex, small classifiers) performed *during* inference to block toxicity or PII.

### B. Scaled AI-as-a-Judge (The Sieve)
- Instead of humans sampling randomly, use a cheap LLM Judge to score 100% of traffic.
- **AI-driven Sampling**: Human experts only audit the 5% of cases where the AI score is low or "uncertain".

### C. Observability & Drift
- **Semantic Drift**: Noticing when user topics change (new prompts being asked that weren't in your offline test set).
- **Confidence Calibration**: Monitoring the confidence of the LLM Judge itself.

## 3. Data Flywheel
Online evaluation identifies the most "ambiguous" or "difficult" cases, which should be added to the **Offline Golden Set** to make the next version of the model and judge more robust.
