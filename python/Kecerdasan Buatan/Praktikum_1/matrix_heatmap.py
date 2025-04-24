# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# Load California Housing dataset
california_dataset = fetch_california_housing()

# Create a DataFrame
california = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)

# Plot the heatmap for correlation
plt.figure(figsize=(10, 8))  # Mengatur ukuran heatmap
ax = sns.heatmap(california.corr().round(2), annot=True, cmap="coolwarm")

# Show plot
plt.show()
