# Session: Mastering Statistical Significance in LLM Evaluation
**Date:** 2026-02-11  
**Track:** [Evaluation](file:///d:/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/LLM-Study/tracks/04-LLM-Agent/Evaluation/06-statistical-significance.md)

## Context
Goal: Transition from simple accuracy reporting to rigorous statistical evaluation to ensure model improvements are not just noise.

## Key Learnings
1. **McNemar's Method**: 
   - Powerful for "Head-to-Head" comparisons.
   - It doesn't care about where both models were right or both wrong. It only cares about the **swaps** ($b$ and $c$).
   - Used extensively in NLP papers to prove a new architecture is better.
2. **Bootstrap CI**:
   - The "Poor man's" way to get statistical power.
   - Very useful when you have a small "Golden Set" (e.g., 50-100 items) and want to know how much to trust the 80% accuracy score.
3. **Paired T-test**:
   - Essential for the "LLM-as-a-Judge" era where we get 0-1 or 1-10 scores instead of just True/False.

## Q&A Highlights
**Q: My model accuracy went from 72% to 74% on 100 samples. Is it better?**  
**A:** Use McNemar. If the p-value is > 0.05, those 2 extra correct answers might be luck. You'd need a larger sample or a more consistent performance gap to be sure.

## Next Steps
- Implement these tests in the `lab/eval_stats_demo.py`.
- Apply McNemar to the next prompt tuning session.
