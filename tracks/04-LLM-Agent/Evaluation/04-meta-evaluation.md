# Meta-Evaluation: Evaluating the Evaluator

## 1. What is Meta-Evaluation?
The process of measuring how well your LLM-as-a-Judge aligns with human reasoning (Ground Truth).

## 2. Statistical Alignment
- **Agreement Rate**: % of cases where LLM score matches Human score.
- **Cohen’s Kappa**: Statistical coefficient measuring agreement above chance (Target > 0.6).
- **Precision/Recall (for binary labels)**:
  - **False Positives (FP)**: Judge is too strict.
  - **False Negatives (FN)**: Judge is too lenient (missing hallucinations/errors).

### 2.1 Cohen's Kappa Deep Dive
Cohen's Kappa is preferred over raw Accuracy because it accounts for the possibility of agreement occurring by chance.

**Formula:**
$$\kappa = \frac{p_o - p_e}{1 - p_e}$$
- $p_o$: Observed agreement rate.
- $p_e$: Expected agreement rate by chance.

**How to calculate $p_e$:**
$p_e$ is the sum of probabilities that both raters choose the same category by chance. For each category $i$:
$$P(\text{chance}_i) = P(\text{human chooses } i) \times P(\text{llm chooses } i)$$
$$p_e = \sum P(\text{chance}_i)$$

*Example (N=100):*
- Human says "Good" 75 times, LLM says "Good" 80 times. $P(\text{chance}_{\text{good}}) = 0.75 \times 0.80 = 0.60$
- Human says "Bad" 25 times, LLM says "Bad" 20 times. $P(\text{chance}_{\text{bad}}) = 0.25 \times 0.20 = 0.05$
- $p_e = 0.60 + 0.05 = 0.65$

**Interpretation Table (Landis & Koch):**
| Kappa Value | Strength of Agreement | Conclusion |
|---|---|---|
| < 0 | Poor | Worse than chance |
| 0.0 - 0.2 | Slight | Barely usable |
| 0.2 - 0.4 | Fair | Needs prompt overhaul |
| 0.4 - 0.6 | Moderate | Needs human oversight |
| 0.6 - 0.8 | Substantial | **Ready for Production** |
| 0.8 - 1.0 | Almost Perfect | **Ready for Automation** |

## 3. The Feedback Loop
Meta-eval is not a one-time event; it drives **Prompt Engineering**:
1. **Compare**: Find LLM vs. Human mismatches.
2. **Analyze**: Why did the LLM disagree? Missing context? Vague rubric?
3. **Refine**: Update the Rubric with a "Few-shot" example of that specific failed case.
4. **Repeat**: Until the LLM Judge consistently represents the human expert.
