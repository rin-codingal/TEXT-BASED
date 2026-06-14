import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Bestsellers with categories.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#info
print("Info:")
print(df.info())
print()

#check if there's null value present
print("Check which data contains null value:")
print(df.isnull().any())
print()

# 10 percentile price
ten_percentile_price = np.quantile(df["Price"], 0.1)
print("Value that divides 10 Percent of Data :", ten_percentile_price)
print()

# Quartiles of Feature Price
price_q1 = np.quantile(df["Price"], 0.25)
price_q2 = np.quantile(df["Price"], 0.50)
price_q3 = np.quantile(df["Price"], 0.75)

print("Quartiles for Price:")
print(f"Q1 = {price_q1}")
print(f"Q2 = {price_q2}")
print(f"Q3 = {price_q3}")
print()

# Interquartile Range of Feature Price
IQR_price = price_q3 - price_q1
print(f"Interquartile Range for Price= {IQR_price}")
print()

# Quartiles of Feature User Rating
rating_q1 = np.quantile(df["User Rating"], 0.25)
rating_q2 = np.quantile(df["User Rating"], 0.50)
rating_q3 = np.quantile(df["User Rating"], 0.75)

print("Quartiles for User Rating:")
print(f"Q1 = {rating_q1}")
print(f"Q2 = {rating_q2}")
print(f"Q3 = {rating_q3}")
print()

# Interquartile Range of Feature User Rating
IQR_rating = rating_q3 - rating_q1
print(f"Interquartile Range for User Rating = {IQR_rating}")
print()

# Boxplot of feature Price
plt.boxplot(df["Price"])
plt.ylabel("Price")
plt.title("Distribution of Price")
plt.show()

# Boxplot of user rating
plt.boxplot(df["User Rating"])
plt.ylabel("User Rating")
plt.title("Distribution of User Rating")
plt.show()

