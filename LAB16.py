import pandas as pd
data = {
    "Name": ["A","B","C","D"],
    "Marks": [90,100,34,None]
}
df = pd.DataFrame(data)
print("Original data: ")
print(df)
df["Marks"].fillna(df['Marks'].fillna(df['Marks'].mean()))
print("\nAfter handling missing values: ")
print(df)