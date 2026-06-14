import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Mean Value of age
mean_age = np.mean(df["Age"])
print(f"Mean Age of Passengers is = {mean_age}")
print()
      
# Mean Value of Fare
mean_fare = np.mean(df["Fare"])
print(f"Mean Fare is = {mean_fare}")

