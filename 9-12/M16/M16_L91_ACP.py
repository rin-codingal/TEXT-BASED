import pandas as pd
import numpy as np
import statistics as stats

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

# Mean Value of user rating
mean_rating = np.mean(df["User Rating"])
print(f"Mean value User Rating is = {mean_rating}")
print()

# Median Value of user rating
median_rating = np.median(df["User Rating"])
print(f"Median value User Rating is = {median_rating}")
print()

# Mode Value of user rating
mode_rating = stats.mode(df["User Rating"])
print(f"Mode value User Rating is = {mode_rating}")
print()

# Mean Value of Reviews
mean_reviews = np.mean(df["Reviews"])
print(f"Mean value Reviews is = {mean_reviews}")
print()

# Median Value of Reviews
median_reviews = np.median(df["Reviews"])
print(f"Median value Reviews is = {median_reviews}")
print()

# Mode Value of Reviews
mode_reviews = stats.mode(df["Reviews"])
print(f"Mode value Reviews is = {mode_reviews}")
print()

# Mean Value of Price
mean_price = np.mean(df["Price"])
print(f"Mean value Price is = {mean_price}")
print()

# Median Value of Price
median_price = np.median(df["Price"])
print(f"Median value Price is = {median_price}")
print()

# Mode Value of Price
mode_price = stats.mode(df["Price"])
print(f"Mode value Price is = {mode_price}")
print()