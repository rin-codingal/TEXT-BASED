import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\country_vaccinations.csv")

#display the first 10 rows of data
print("First 10 rows of data:")
print(df.head(10))
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

#considering "False" as NaN or Null value
missing_value=["N/a","na",np.nan]
df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\country_vaccinations.csv",na_values=False)

#re-check the null value
print("Total null value in the data with 'False' considered as null as well:")
print(df.isnull().sum())
print()

#check if there's null value present
print("Check which data contains null value:")
print(df.isnull().any())
print()

# Visualize missing values using a heatmap
subset = df.iloc[:5200, :]  # Taking the first 100 rows for better performance
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

#display the last 10 rows of data
print("Last 10 rows of data:")
print(df.tail(10))
print()

#remove data with Null/NaN value
print("After removing data which contains null value:")
print(df.dropna())
print()

#only removing data if all of the values are NaN
print("after removing data that all values are null")
print(df.dropna(how="all"))
print()

#replace NaN with 0
print("after replacing NaN with 0:")
print(df.fillna(0))
print()

#backward fill the missing value
print("Fill the missing value with backward fill method:")
#print(df.fillna(method="bfill"))
print(df.bfill())
print()

#fill the NA value
print("fill the NA value using interpolate:")
#print(df.interpolate())
print(df.infer_objects(copy=False))
print()

#get the clean data
print("Clean data after removing null value:")
df_dropped=df.dropna()
print(df_dropped)
print()

