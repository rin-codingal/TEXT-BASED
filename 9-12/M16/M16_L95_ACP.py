import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

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

#frequency category genre
print("Frequency of Categories of Genre :")
print(df["Genre"].value_counts())
print()

# Minimum and Maximum values of User Rating
min = df["User Rating"].min()
max = df["User Rating"].max()
print(f"Minimum Rating: {min}")
print(f"Maximum rating: {max}")
print()

# creating binned rating
bins = [3,4,5]
df["binned_rating"] = pd.cut(df["User Rating"], bins)
print("First 5 rows of Binned User Rating:")
print(df.head())
print()

# Giving label to binned rating
rating_labels = ["Good","Excellent"]
df["binned_rating"] = pd.cut(df["User Rating"], bins, labels = rating_labels)
print("First 5 rows of Binned User Rating with Label:")
print(df.head())
print()

#displot
labels = ["User Rating","Reviews","Price","Year"]

for i in labels:
  sns.displot(df[i], kde=True)
  plt.title(i)
  plt.show()
  print("Skewness -", df[i].skew())
  print()

#boxplot
sns.boxplot(data=df, x="Genre", y="User Rating", hue="Genre")
plt.show()

#scatterplot user rating vs price
plt.scatter(x=df["User Rating"], y=df["Price"])
plt.show()

