import numpy as np
import pandas as pd

d1 = {"Name": ["Layla", "Hinata", "Jack", "Omar"], "ID": [1, 2, 3, 4], "Salary": [200, 250, np.nan, pd.NaT],
      "Role": ["CEO", None, pd.NaT, pd.NaT]}

df = pd.DataFrame(d1)

print(df)
print()

#the first 2 data
print(df.head(2))
print()

#the last 2 data
print(df.tail(2))
print()

print(df.isnull().sum())
print()

df.info()
print()

df1 = df.dropna()
print(df1)

print()

df1 = df.dropna(axis=1)
print(df1)
print()

#df["Salary"].fillna("300",inplace=True)
df.fillna({"Salary":"300"}, inplace=True)
print(df)

print()

#df["Role"].fillna("CEO",inplace=True)
df.fillna({"Role":"CEO"}, inplace=True)
print(df)