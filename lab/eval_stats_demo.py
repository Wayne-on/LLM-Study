import numpy as np
from scipy import stats

def demo_mcnemar():
    print("--- McNemar's Test Demo ---")
    # Sample outcomes for 100 test cases
    # a: both correct = 70
    # b: A correct, B wrong = 15
    # c: A wrong, B correct = 5
    # d: both wrong = 10
    b = 15
    c = 5
    
    # Simple McNemar Statistic with Yates Correction
    chi2 = (abs(b - c) - 1)**2 / (b + c)
    p_value = 1 - stats.chi2.cdf(chi2, df=1)
    
    print(f"A_corr/B_wrong (b): {b}, A_wrong/B_corr (c): {c}")
    print(f"Chi-squared: {chi2:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Result: Statistically Significant improvement!\n")
    else:
        print("Result: Not significant. Difference might be noise.\n")

def demo_bootstrap(data, n_iterations=1000):
    print("--- Bootstrap Confidence Interval Demo ---")
    stats_list = []
    n_samples = len(data)
    
    for _ in range(n_iterations):
        # Resample with replacement
        resample = np.random.choice(data, size=n_samples, replace=True)
        stats_list.append(np.mean(resample))
    
    lower = np.percentile(stats_list, 2.5)
    upper = np.percentile(stats_list, 97.5)
    
    print(f"Original Accuracy: {np.mean(data):.2f}")
    print(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]\n")

def demo_paired_ttest():
    print("--- Paired T-test Demo ---")
    # Model A scores (GPT-4 judge 1-10)
    scores_a = np.array([8, 7, 9, 6, 8, 10, 7, 8, 9, 5])
    # Model B scores (GPT-4 judge 1-10)
    scores_b = np.array([9, 8, 9, 7, 9, 10, 8, 9, 10, 6])
    
    # 1. Scipy calculation
    t_stat, p_val = stats.ttest_rel(scores_b, scores_a)
    
    # 2. Manual calculation for learning
    diffs = scores_b - scores_a
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs, ddof=1)
    n = len(diffs)
    se = std_diff / np.sqrt(n)
    t_manual = mean_diff / se
    
    # Cohen's d (Effect Size)
    cohen_d = mean_diff / std_diff
    
    print(f"Model A Mean: {np.mean(scores_a):.2f}, Model B Mean: {np.mean(scores_b):.2f}")
    print(f"Mean Difference: {mean_diff:.2f}")
    print(f"T-statistic (Manual): {t_manual:.4f}")
    print(f"P-value: {p_val:.4f}")
    print(f"Effect Size (Cohen's d): {cohen_d:.4f}")
    
    if p_val < 0.05:
        print("Result: Significant improvement!\n")
    else:
        print("Result: Not significant.\n")

def demo_wilcoxon():
    print("--- Wilcoxon Signed-Rank Test Demo ---")
    # Small dataset with an outlier
    # Model A wins one big with a lucky 10, but B is consistently slightly better elsewhere
    a = np.array([10, 2, 2, 2, 2, 2, 2, 2, 2, 2]) 
    b = np.array([2,  3, 3, 3, 3, 3, 3, 3, 3, 3]) 
    
    # Wilcoxon focuses on the fact that B won 9/10 times
    stat, p_val = stats.wilcoxon(b, a, alternative='greater')
    
    # For comparison, a T-test would be crushed by the 10 vs 2 difference
    t_stat, t_p = stats.ttest_rel(b, a, alternative='greater')
    
    print(f"Model A scores: {a}")
    print(f"Model B scores: {b}")
    print(f"Wilcoxon P-value: {p_val:.4f}")
    print(f"Paired T-test P-value: {t_p:.4f}")
    
    if p_val < 0.05:
        print("Result: Wilcoxon detected B is significantly better (more consistent win)!\n")
    else:
        print("Result: Not significant.\n")

if __name__ == "__main__":
    # 1. McNemar
    demo_mcnemar()
    
    # 2. Bootstrap
    sample_data = [1]*75 + [0]*25
    demo_bootstrap(sample_data)
    
    # 3. Paired T-test
    demo_paired_ttest()
    
    # 4. Wilcoxon
    demo_wilcoxon()
