import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------------------
# Generate realistic synthetic customer metrics
# -----------------------------------------

np.random.seed(42)

data = pd.DataFrame({
    "Customer_Satisfaction": np.random.normal(75, 8, 200),
    "Engagement_Score": np.random.normal(65, 10, 200),
    "Purchase_Frequency": np.random.normal(12, 3, 200),
    "Avg_Session_Duration": np.random.normal(5, 1.2, 200),
    "Marketing_Response_Rate": np.random.normal(0.18, 0.04, 200),
})

corr = data.corr()

# -----------------------------------------
# Visualization Settings (Professional Styling)
# -----------------------------------------

sns.set_style("white")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 512x512 because dpi=64
ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="Blues",
    linewidths=1,
    linecolor="white",
    square=True,
    cbar=True
)

plt.title("Customer Engagement Correlation Matrix", pad=20)

# -----------------------------------------
# Save Output (Exactly 512 × 512)
# -----------------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches='tight')
