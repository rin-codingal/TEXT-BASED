import pandas as pd
import numpy as np
import statistics as stats

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Median Value of age
median_age = np.median(df["Age"])
print(f"Median Age of Passengers is = {median_age}")
print()
      
# Median Value of Fare
median_fare = np.median(df["Fare"])
print(f"Median Fare is = {median_fare}")
print()

# Mode value of age
mode_age = stats.mode(df["Age"])
print(f"Mode value of Age = {mode_age}")
print()

# Mode value of PClass
mode_pclass = stats.mode(df["Pclass"])
print(f"Mode value of Pclass = {mode_pclass}")
print()

# Mode Value of Categorical Feature - Gender
mode_gender = df["Gender"].value_counts().index[0]
print(f"Mode feature of Gender = {mode_gender}")
print()