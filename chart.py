import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate synthetic customer engagement data
np.random.seed(42)

metrics = [
    "Email Opens",
    "Website Visits",
    "App Sessions",
    "Purchases",
    "Social Media Likes",
    "Customer Support Calls"
]

data = pd.DataFrame({
    metric: np.random.randint(0, 100, 200)
    for metric in metrics
})

# Step 2: Compute correlation matrix
corr_matrix = data.corr()

# Step 3: Create Seaborn heatmap
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 8x8 inches for 512x512 pixels

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1, vmax=1,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Save exactly 512x512 pixels without bbox_inches='tight'
plt.savefig("chart.png", dpi=64)  
plt.close()
