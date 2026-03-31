import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("finance_dataset_cleaned.csv")   

# Select columns similar to your example style
cols = ['Revenue', 'Expenses', 'Profit', 'ROI', 'ROE', 'StockPrice']

# Create boxplot
plt.figure(figsize=(10,6))
plt.boxplot([df[col] for col in cols], labels=cols)

# Labels and title
plt.xlabel("Financial Features")
plt.ylabel("Values")
plt.title("Boxplot of Financial Dataset")

plt.grid(True)
plt.show()