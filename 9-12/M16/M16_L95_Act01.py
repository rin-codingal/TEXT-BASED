import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Minimum and Maximum Values of Age
minimum_age = df["Age"].min()
print("Minimum Age :", minimum_age)
print()

maximum_age = df["Age"].max()
print("Maximum Age :", maximum_age)
print()

# Creating binned age and giving it a label
bins = [0, 15, 30, 45, 60, 75]
df["binned_age"] = pd.cut(df["Age"], bins)
print("Binned age:")
print(df[["binned_age", "Age"]].head())
print()

age_labels = ["Young", "Young - Adult", "Middle Aged", "Middle-Older Age", "Senior"]
 
# Bin the values of the "Age" column and specify the labels 
df["binned_age"] = pd.cut(df["Age"], bins, labels = age_labels)
print("Binned age with label:")
print(df[["binned_age", "Age"]].head())
print()

# Barplot for binned age
df["binned_age"].value_counts().plot(kind="bar")
 
# Label the bar graph
plt.title("Dance Class Age Distribution")
plt.xlabel("Ages")
plt.ylabel("Count") 
plt.show()

# Check distribution and skewness of all the features
labels = ["PassengerId","Survived","Pclass","Age","SibSp","Parch","Fare"]
for i in labels:
  print("Distribution of", i)
  sns.displot(df[i], kde=True)
  plt.title(i)
  plt.show()
  print(f"Skewness : {df[i].skew()}")
  print()

# Log Transform Skewed Features
df["log_SibSp"] = np.log(df["SibSp"])
df["log_Parch"] = np.log(df["Parch"])
df["log_Fare"] = np.log(df["Fare"])