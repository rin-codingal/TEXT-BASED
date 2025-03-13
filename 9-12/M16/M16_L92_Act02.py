import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\IMDB Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Plot Histogram for feature Runtime
plt.hist(df["Runtime"])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Plot Histogram for feature IMDB_Rating
plt.hist(df["IMDB_Rating"])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.show()

# Define parameter bins_runtime for feature Runtime and plot histogram for it
print(df["Runtime"].unique())
print()

bins_time = np.arange(80, 230, 10)
plt.hist(df["Runtime"], edgecolor="black", bins=bins_time, color="g")
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Define parameter bins_rating for feature IMDB_Rating and plot histogram for it
print(df["IMDB_Rating"].unique())
print()

bins_rating = np.arange(8, 10, 0.20)
plt.hist(df["IMDB_Rating"], edgecolor="black", bins=bins_rating, color="g")
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)
plt.show()