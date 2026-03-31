import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 🔵 Cluster 1 (positive correlation)
x1 = np.random.normal(2, 0.5, 30)
y1 = 2 * x1 + np.random.normal(0, 0.5, 30)

# 🟢 Cluster 2 (another group)
x2 = np.random.normal(6, 0.5, 30)
y2 = 2 * x2 + np.random.normal(0, 0.5, 30)

# 🔴 Outlier
x_outlier = [8]
y_outlier = [20]

# Combine all data
x = np.concatenate([x1, x2, x_outlier])
y = np.concatenate([y1, y2, y_outlier])

# Plot
plt.figure(figsize=(8,6))
plt.scatter(x1, y1, color='blue', label='Cluster 1')
plt.scatter(x2, y2, color='green', label='Cluster 2')
plt.scatter(x_outlier, y_outlier, color='red', s=100, label='Outlier')

# Labels
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Clusters, Outlier, and Positive Correlation")

plt.legend()
plt.grid(True)

plt.show()