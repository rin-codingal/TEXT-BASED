import numpy as np
import pandas as pd

d1 = {"Name": ["Jeffrey", "Mary", "Meghan", "Audrey"], "ID": [1, 2, 3, 4], "Salary": [170, 230, np.nan, pd.NaT],
      "Role": ["CEO", None, pd.NaT, pd.NaT]}

df = pd.DataFrame(d1)

print("all of the data:")
print(df)
print()

#print the first 2 rows
print("the first 2 rows of data")
print(df.head(2))
print()

#print the last 2 rows
print("the last 2 rows of data:")
print(df.tail(2))
print()




#calculating data with null value
print("data with null value:")
print(df.isnull().sum())
print()

print("dataframe information:")
print(df.info())
print()

#removing data which contains null value
df1 = df.dropna()
print("updated dataframe after removing null value:")
print(df1)
print()

df1 = df.dropna(axis=1)
print(df1)
print()

#updating salary null value into 300
df["Salary"].fillna("300",inplace=True)
print("updated data after filling up null value in salary with 300:")
print(df)
print()

#updating role null value into CEO
df["Role"].fillna("CEO",inplace=True)
print("updated data after filling up null value in role with 'CEO':")
print(df)
