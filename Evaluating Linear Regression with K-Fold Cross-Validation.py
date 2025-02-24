from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np

# Generate a synthetic dataset (100 samples, 1 feature)
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Initialize the model
model = LinearRegression()

# Define 5-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation and compute scores
scores = cross_val_score(model, X, y, cv=kf, scoring='r2')

# Print results
print(f"Cross-Validation Scores: {scores}")
print(f"Mean Score: {np.mean(scores):.4f}")
