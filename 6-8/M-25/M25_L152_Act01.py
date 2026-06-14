####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np

# Import dataset
data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\Weather Dataset.csv")

#display the first 5 rows of data
print("First 5 rows of data:")
print(data.head(5))
print()

#info
print("Info:")
data.info()
print()

#check the null value
print("Total null value in the data:")
print(data.isnull().sum())
print()

# Mean, Variance and Standard Deviation of Temperature (C)

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)
print()

var_temp = np.var(data['Temperature (C)'])
print("Variation of Temperature is :", var_temp)
print()

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)
print()

# Mean, Variance and Standard Deviation of Temperature (C) for every month

for i in range(1, 13):
    month = data.loc[data["month"] == i]["Temperature (C)"]
    print(f"For month {i}")
    print(f"Mean temperature is {np.mean(month)}")
    print(f"Standard deviation is {np.std(month)}")
    print()