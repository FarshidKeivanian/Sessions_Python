import numpy as np
from scipy import stats

# Given data from pilot study
pilot_data = [45, 50, 55, 48, 60, 53, 52, 49, 47, 51]  # Example health outcomes

# Mean and standard deviation of the pilot study
mean_pilot = np.mean(pilot_data)
std_pilot = np.std(pilot_data, ddof=1)  # ddof=1 for sample standard deviation
n_pilot = len(pilot_data)

# Population parameters (Assumed)
population_mean = 50  # Null hypothesis: no improvement, so mean is 50

# Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(pilot_data, population_mean)

# Results
alpha = 0.05  # Significance level

print(f"t-statistic: {t_stat}, p-value: {p_value}")

# Decision
if p_value < alpha:
    print("Reject the null hypothesis, the program shows significant improvement.")
else:
    print("Fail to reject the null hypothesis, the program does not show significant improvement.")
