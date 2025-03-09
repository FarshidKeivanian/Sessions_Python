import math

# Given values
Z = 1.96  # Z-score for 95% confidence
p = 0.5   # Estimated proportion
ME = 0.05  # Margin of error

# Sample size formula
n = (Z**2 * p * (1 - p)) / (ME**2)

# Print result
print(f"Required sample size: {math.ceil(n)}")
