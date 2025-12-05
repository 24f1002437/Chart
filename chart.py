import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(0)
data = pd.DataFrame({
    'Customer_Visits': np.random.randint(50, 300, 50),
    'Time_On_Site': np.random.rand(50) * 10,
    'Purchase_Frequency': np.random.rand(50) * 5,
    'Satisfaction_Score': np.random.rand(50) * 100,
    'Engagement_Score': np.random.rand(50) * 100
})

# Correlation matrix
corr = data.corr()

# Styling
sns.set_style("white")
sns.set_context("talk")

# --- THE IMPORTANT PART ---
# EXACT 512x512 px output
plt.figure(figsize=(8, 8), dpi=64)   # 8 in × 64 dpi = EXACT 512 px

ax = sns.heatmap(corr, annot=True, cmap="YlGnBu", square=True)

# Save WITHOUT bbox_inches='tight' (this breaks pixel size)
plt.savefig("chart.png", dpi=64)

# Close the figure
plt.close()
