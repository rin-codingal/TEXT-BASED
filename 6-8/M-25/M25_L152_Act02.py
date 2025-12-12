# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Import dataset
data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\IMDB Dataset.csv")

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

# Plot Histogram for feature Runtime
plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Plot Histogram for feature IMDB_Rating
plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.show()

# Define parameter bins_runtime for feature Runtime and plot histogram for it
data['Runtime'].unique()

bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Define parameter bins_rating for feature IMDB_Rating and plot histogram for it
data['IMDB_Rating'].unique()

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)
plt.show()