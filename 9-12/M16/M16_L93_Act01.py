import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Quartiles of Feature Age
age_q1 = np.quantile(df["Age"], 0.25)
age_q2 = np.quantile(df["Age"], 0.50)
age_q3 = np.quantile(df["Age"], 0.75)

print("Age Quartiles:")
print(f"Q1 = {age_q1}")
print(f"Q2 = {age_q2}")
print(f"Q3 = {age_q3}")
print()

# Interquartile Range of Feature Age
IQR_age = age_q3 - age_q1
print(f"Interquartile Range = {IQR_age}")
print()

#histogram feature age
plt.hist(df["Age"])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")
plt.show()

# Quartiles of Feature Fare
fare_q1 = np.quantile(df["Fare"], 0.25)
fare_q2 = np.quantile(df["Fare"], 0.50)
fare_q3 = np.quantile(df["Fare"], 0.75)

print("Age Fare:")
print(f"Q1 = {fare_q1}")
print(f"Q2 = {fare_q2}")
print(f"Q3 = {fare_q3}")
print()

# Interquartile Range of Feature Fare
IQR_fare = fare_q3 - fare_q1
print(f"Interquartile Range = {IQR_fare}")
print()

#histogram feature Fare
bins =np.arange(0,250,20)
plt.hist(df["Fare"], bins=np.arange(1,250, 20))
plt.ylabel("Count of Passengers")
plt.xlabel("Fare")
plt.xticks(bins)
plt.show()

