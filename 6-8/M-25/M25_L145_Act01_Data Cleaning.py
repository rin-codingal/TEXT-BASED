# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file
df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\country_vaccinations.csv")

# Display first 10 rows
print("First 10 rows:")
print(df.head(10))
print()

# Check for any null values in each column
print("Any null value:")
print(df.isnull().any())
print()

# Visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]  # Taking the first 100 rows for better performance
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

# Display first 10 rows
print("First 10 rows:")
print(df.head(10))
print()

# Drop rows where all values are NaN
print("remove null values:")
print(df.dropna(how="all"))
print()

# Fill missing values using backward fill method
print("fill null value (backward fill)")
#print(df.fillna(method="bfill"))
print(df.bfill())
print()

# Interpolate missing values
print("interpolate")
#print(df.interpolate(numeric_only=True))
print(df.select_dtypes(include="number").interpolate())
print()

# Drop all rows with any NaN values
print("remove null values:")
df_dropped = df.dropna()
print(df_dropped)