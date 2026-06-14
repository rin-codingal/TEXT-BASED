import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Weather Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#info
print("Info:")
print(df.info())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Mean, Variance and Standard Deviation of Temperature (C)
mean_temp = np.mean(df["Temperature (C)"])
print(f"Mean Temperature is : {mean_temp}")
print()

var_temp = np.var(df["Temperature (C)"])
print(f"Variation of Temperature is : {var_temp}")
print()

standard_deviation_temp = np.std(df["Temperature (C)"])
print(f"Standard Deviation of Temperature is : {standard_deviation_temp}")
print()

# Mean, Variance and Standard Deviation of Temperature (C) for every month
for i in range(1, 13):
  month = df.loc[df["month"] == i]["Temperature (C)"]
  print(f"For month {i}")
  print(f"Mean temperature is {np.mean(month)}")
  print(f"Standard deviation is {np.std(month)}")
  print()

print()