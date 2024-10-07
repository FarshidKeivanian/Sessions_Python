import numpy as np
from scipy import stats

# Example Data
sample_size = 200
sample_mean = 7.5
sample_std = 1.2  # assumed standard deviation

# Z-score for 95% confidence level
z_score = stats.norm.ppf(0.975)

# Calculate margin of error
margin_of_error = z_score * (sample_std / np.sqrt(sample_size))

# Confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print(f"95% Confidence Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
