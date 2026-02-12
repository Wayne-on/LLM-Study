# Statistical Significance in Model Evaluation

When evaluating LLMs, comparing raw metrics (like "Model A is 2% more accurate than Model B") can be misleading due to noise, sample size, or randomness. Statistical significance helps distinguish a **real improvement** from **chance**.

## Why Statistical Significance Matters in Evaluation
Evaluation is not just a one-time measurement; it is a **decision-making process**. We can divide it into two core layers:

### Layer 1: Descriptive Statistics —— "The Measurement"
It tells you **what** happened in your test set.
- **Metrics**: Accuracy, F1-Score, RAGAS (0.74), BLEU, etc.
- **Role**: Provides a snapshot of performance on specific data.
- **Limitation**: It doesn't tell you if the result will hold true for the next 1,000 users.

### Layer 2: Inferential Statistics —— "The Decision"
It answers: **Is this difference real or just random noise?**
- **Tools**: McNemar, Paired T-test, Wilcoxon, Bootstrap CI, p-values.
- **Role**: Bridges the gap between "numbers" and "conclusions." It tells you whether to deploy Model B or keep iterating.

---

### Core Value in the LLM Cycle:
- **Cost vs. Reliability**: Knowing your **Confidence Interval (CI)** helps you decide if you've tested enough (e.g., 50 prompts might be enough, saving 500 unnecessary API calls).
- **Filtering Noise**: Parallel tests ensure that the "difficulty bias" of your prompts doesn't swamp the actual model performance signal.
- **Scientific Justification**: In production, "it feels better" is subjective; $p < 0.05$ is an objective, defensible justification for system changes.

## 1. McNemar's Test (Paired Binary Data)
Best for: **Paired comparisons** (the same test set) where outcomes are **binary** (Correct/Wrong, Win/Loss).

### The Intuition
Focus only on the **discordant pairs** (cases where the models disagree). If Model A fix a lot of errors Model B made, but Model B doesn't fix many of Model A's, the improvement is likely significant.

### 2x2 Contingency Table
| | Model B Correct | Model B Wrong |
|---|---|---|
| **Model A Correct** | Both Correct ($a$) | A Correct / B Wrong ($b$) |
| **Model A Wrong** | A Wrong / B Correct ($c$) | Both Wrong ($d$) |

- **Null Hypothesis ($H_0$):** Model A and Model B have the same error rate ($P(b) = P(c)$).
- **Test Statistic / Chi-squared Statistical Constant ($\chi^2$):** 
  $$\chi^2 = \frac{(|b - c| - 1)^2}{b + c}$$
  *(Note: This is the **卡方统计常量**. The $-1$ is Yates's continuity correction, used when $b+c$ is small).*

### Decision Rule
We compare the calculated $\chi^2$ against a **critical value** (typically **3.84** for a 95% confidence level):
- If $\chi^2 > 3.84$ (or $p\text{-value} < 0.05$), we reject $H_0$. 
- Result: The difference is **Statistically Significant**.

---

## 2. Bootstrap Method (Confidence Intervals)
Best for: Estimating the **reliability** of any metric (Accuracy, BLEU, ROUGE) and handling **small datasets**.

### The Intuition
"What would happen if we ran this experiment 1,000 times?" Instead of collecting more data, we **resample with replacement** from our original set.

### What is a Confidence Interval (CI)?
- **CI (Confidence Interval)**: The **range itself** (e.g., `[75%, 85%]`). It is the "safety range" for your metric.
- **CL (Confidence Level)**: Your **degree of certainty** (e.g., 95%). A 95% CL means if you repeat the experiment 100 times, the true value will fall within the CI 95 times.

> [!IMPORTANT]
> **Strictness vs. Precision**:
> - **95% CL** (Scientific standard): Wider range, more "conservative" and reliable.
> - **75% CL** (Quick internal check): Narrower range, more "aggressive" but higher risk of being wrong.

### Calculation Logic: The Percentile Method
When we run 1,000 Bootstrap iterations, we get 1,000 different accuracy scores. We sort them from smallest to largest:
1. **Find the 2.5th Percentile**: The 25th smallest score ($1000 \times 0.025$).
2. **Find the 97.5th Percentile**: The 975th score ($1000 \times 0.975$).
3. **The Result**: The range between these two points captures the **middle 95%** of outcomes.

---

## 3. Paired Bootstrap (The "Golden Standard" for A/B Testing)
While single-model Bootstrap tells you if your *data* is enough, **Paired Bootstrap** tells you if Model B is actually better than Model A.

### The Intuition: "Bootstrap of Differences"
Instead of looking at raw accuracies, we look at the **score difference** ($Score_B - Score_A$) on every single sample.

1. **Calculate Delta**: For each sample, $D = 1$ if B is better, $-1$ if A is better, $0$ if same.
2. **Resample Delta**: Do 1,000 Bootstrap iterations on this Delta array.
3. **Check the 95% CI of the Mean Delta**:
   - If the entire interval is **strictly above 0** (e.g., `[0.5%, 4.2%]`), Model B is **statistically significantly better** than Model A.
   - If the interval contains 0 (e.g., `[-1.2%, 2.5%]`), the improvement might just be noise.

---

## 4. Paired T-Test (Continuous Metrics)
Best for: Comparing **continuous scores** (e.g., GPT-4 judge scores 1-10, RAGAS scores 0-1) across the same set of prompts.

### The Intuition: "Is the Mean Difference Zero?"
The goal is to determine if the observed average improvement $\bar{d}$ is a "real signal" or just random "vibration" (noise) in the data.
- **The Signal**: The average of the differences ($\bar{d} = \frac{1}{n}\sum D_i$).
- **The Noise (SE)**: The Standard Error represents how much the mean might fluctuate across different prompt sets.
- **The Question**: Is the observed $\bar{d}$ just a random fluctuation, or is it a statistically significant "signal"?

### Requirement: Paired Data Check
- **1-to-1 Mapping**: Every score from Model A must have a corresponding score from Model B for the **exact same input**.
- **Shared Context**: By using the same prompts, we cancel out the "shared variance" (difficulty bias) between prompts.

### Deep Dive into Assumptions
To trust the p-value of a Paired T-test, evaluate these four pillars:

1.  **Independence of Pairs**: The output for Prompt #1 must not influence Prompt #2.
    - *The LLM Trap*: Using 100 prompts that are variations of the same template leads to **Autocorrelation**, which can artificially deflate your $p\text{-value}$.
2.  **Normality of Differences ($d_i$)**: The distribution of $(Score_B - Score_A)$ should be roughly bell-shaped.
    - **Robustness (The CLT Savior)**: LLM scores (1, 5, 10) are rarely normal. However, the T-test is **robust** due to the **Central Limit Theorem (CLT)**.
    - **Rule of Thumb**: If $N \ge 30$, the *sampling distribution of the mean* becomes normal even if the raw scores aren't.
3.  **No Extreme Outliers**: The T-test relies on the **Mean**, which is sensitive to extreme values. One catastrophic hallucination (Score 0 vs 10) can blow up the variance and kill your significance.
4.  **Continuous Data**: The metric should be interval-based (like 1-10 scores) where the distance between 2 and 4 is the same as 6 and 8.

### Visual Diagnostic Checklist
- **Histogram of Differences**: Is it roughly centered and symmetric?
- **Q-Q Plot**: If points follow the diagonal line, Normality is safe.
- **Boxplot**: Use this to hunt for **Outliers** (points outside the whiskers).

### Calculation & Metric
$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$
- **Effect Size (Cohen's $d$)**: $d = \bar{d} / s_d$. (0.2=Small, 0.5=Medium, 0.8=Large).

> [!TIP]
> **Confidence Interval**: Reporting the 95% CI of the difference (e.g., `Mean diff is 0.5 [0.2, 0.8]`) is more informative than a p-value. If the range includes 0, your improvement is not statistically significant.

---

## 5. Wilcoxon Signed-Rank Test (Non-Parametric Paired)
Best for: Comparing **paired scores** when data is **non-normal**, "dirty," or the sample size is **small** ($N < 30$).

### The Intuition: "Ranks, Not Values"
The Paired T-test is sensitive to the *exact distance* between scores. Wilcoxon is more relaxed—it only cares about the **rank** of the differences.
1.  Calculate differences ($d_i$).
2.  Rank them by their **absolute magnitude** (ignoring the sign).
3.  Add back the signs to the ranks.
4.  Sum the positive ranks. If Model B is truly better, the sum of its positive ranks will be significantly higher than expected by chance.

### Why use it in LLM Evaluation?
- **Robust to Outliers**: If one prompt has a score difference of -9.0 (a catastrophic failure), the T-test standard deviation explodes. Wilcoxon just gives it the "highest rank," limiting its destructive power on your statistics.
- **Ordinal Data**: Ideal if you are using Likert scales (e.g., 1-5 "helpfulness" ratings) where the "distance" between 4 and 5 might not be mathematically identical to 1 and 2.
- **Small Test Sets**: When testing on only 15-20 prompts, the normality assumption of the T-test is hard to prove. Wilcoxon is your safest bet.

> [!CAUTION]
> **Power Loss**: If your data *actually is* normally distributed, the Wilcoxon test is slightly less powerful than the T-test, meaning it might fail to detect a very small real improvement that a T-test would catch.

---

## 6. Summary Guide: Which to use?

| Scenario | Model Output | Metric Type | Recommended Test |
|---|---|---|---|
| **A/B Performance** | Correct / Wrong | Binary (0/1) | **McNemar's Test** |
| **Safety Margin** | Single Metric | Any (Acc, BLEU) | **Bootstrap CI** |
| **Quality Score ($N \ge 30$)** | GPT-4 (1-10) | Continuous | **Paired T-test** |
| **Small/Dirty Data ($N < 30$)**| Continuous | Non-normal | **Wilcoxon Signed-Rank** |
