import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

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

# Median value of feature Genre
categories = ["Fiction","Non-Fiction"]
df["genre_num"] = pd.Categorical(df["Genre"], categories, ordered=True)
median_value = np.median(df["genre_num"].cat.codes)
median_cat = categories[int(median_value)]
print(f"Median Value of Genre is : {median_cat}")
print()

#countplot genre
sns.countplot(x=df["Genre"], data=df, palette="winter")
plt.title("Genre")
plt.show()

#pie chart genre
df.groupby("Genre").size().plot(kind="pie", autopct="%.2f")
plt.title("Genre")
plt.show()

#boxplot of User Rating
labels = ["User Rating","Reviews","Price","Year"]
for i in labels:
  plt.boxplot(df[i])
  plt.title(i)
  plt.show()

#data shape
num_data = df.drop(["Name","Author","Genre","genre_num"], axis=1)
print(f"data shape: {num_data.shape}")

#first 5 rows of num_data
print("First 5 rows of num_data:")
print(num_data.head())
print()

#scaling dataset
scaler = StandardScaler()
scaled_num_data = scaler.fit_transform(num_data)
print("After scaling dataset:")
print(scaled_num_data)