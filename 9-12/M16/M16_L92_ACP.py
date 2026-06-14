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

# Variance and Standard Deviation of User Rating
rating_std = np.std(df["User Rating"])
print(f"Standard Deviation of User Rating is : {rating_std}")
print()

rating_var = np.var(df["User Rating"])
print(f"Variation of User Rating is : {rating_var}")
print()

# Variance and Standard Deviation of Price
price_std = np.std(df["Price"])
print(f"Standard Deviation of Price is : {price_std}")
print()

price_var = np.var(df["Price"])
print(f"Variation of Price is : {price_var}")
print()

#histogram
plt.hist(df["User Rating"])
plt.xlabel("User Rating")
plt.ylabel("Number of Books")
plt.show()

#value counts
print(df["User Rating"].value_counts())
print()

#histogram
bins_rating = np.arange(3,5,0.1)
plt.hist(df["User Rating"], edgecolor="black", color="lime", bins=bins_rating)
plt.xlabel("User Rating")
plt.ylabel("Number of Books")
plt.show()

plt.hist(df["Price"])
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()

print(df["Price"].value_counts())
print()

#histogram
bins_price = np.arange(0,110,5)
plt.hist(df["Price"], edgecolor="black", color="orange", bins=bins_price)
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()

