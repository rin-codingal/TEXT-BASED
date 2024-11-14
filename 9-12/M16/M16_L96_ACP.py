import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\StudentsPerformance.csv")

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

#Descriptive statistics
print("Descriptive statistics")
print(df.describe())
print()

#countplot gender
sns.countplot(x=df["gender"], data=df, palette="winter", hue=df["gender"])
plt.show()

#countplot ethnicity
sns.countplot(x=df["race/ethnicity"], data=df, palette="winter", hue=df["race/ethnicity"])
plt.show()

#countplot lunch
sns.countplot(x=df["lunch"], data=df, palette="winter", hue=df["lunch"])
plt.show()

#countplot parental level of education
sns.countplot(x=df["parental level of education"], data=df, palette="winter", hue=df["parental level of education"])
plt.xticks(rotation=45)
plt.show()

#pie chart of ethnicity
df.groupby("race/ethnicity").size().plot(kind="pie", autopct="%.2f")
plt.title("Ethnicity")
plt.show()

#pie chart of parental level of education
df.groupby("parental level of education").size().plot(kind="pie", autopct="%.2f")
plt.title("Parental Level of Education")
plt.show()

#countplot ethnicity on each gender
sns.countplot(data=df, x="gender", hue="race/ethnicity", palette="winter")
plt.show()

#countplot gender on each lunch
sns.countplot(data=df, x="lunch", hue="gender", palette="winter")
plt.show()

#displot
sns.displot(df["math score"], kde=True)
plt.title("Math Score")
plt.show()
print("Skewness :", df["math score"].skew())
print()

sns.displot(df["reading score"], kde=True)
plt.title("Reading Score")
plt.show()
print("Skewness :", df["reading score"].skew())
print()

sns.displot(df["writing score"], kde=True)
plt.title("Writing Score")
plt.show()
print("Skewness :", df["writing score"].skew())
print()

#boxplot math score on each gender
sns.boxplot(x=df["gender"],y=df["math score"], hue=df["gender"])
plt.show()

#heatmap
sns.heatmap(df.corr(numeric_only=True))
plt.show()