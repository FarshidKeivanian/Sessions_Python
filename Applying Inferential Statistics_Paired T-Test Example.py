import scipy.stats as stats

# Hypothetical average user engagement times in seconds before and after new app feature
before = [120, 130, 125, 140, 135]
after = [150, 160, 158, 162, 155]

# Performing a t-test on the sample data
t_stat, p_val = stats.ttest_rel(after, before)

print(f'T-statistic: {t_stat:.2f}')
print(f'P-value: {p_val:.3f}')
if p_val < 0.05:
    print("Result is statistically significant - we can roll out the new feature.")
else:
    print("Result is not statistically significant - further review required.")
