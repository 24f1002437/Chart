import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame({
    'Customer_Visits': np.random.randint(50, 300, 58),
    'Time_On_Site': np.random.rand(58) * 10,
    'Purchase_Frequency': np.random.rand(58) * 5,
    'Satisfaction_Score': np.random.rand(58) * 100,
    'Engagement_Score': np.random.rand(58) * 100
})

# Correlation matrix
corr = data.corr()

# Ensure consistent Seaborn theme
sns.set(style="white", context="talk")

# Create figure with EXACT 512x512 px
plt.figure(figsize=(8, 8), dpi=64)

# REQUIRED: seaborn heatmap with annot
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    cbar=True
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16)

# Save EXACT 512x512
plt.savefig("chart.png", dpi=64)
plt.close()
