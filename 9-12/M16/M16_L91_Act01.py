import pandas as pd

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#types
print("Types:")
print(df.dtypes)
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()