import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Iris Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

#Descriptive statistics
print("Descriptive statistics")
print(df.describe())
print()

# Boxplot of all the features 
labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
for i in labels:
  print("Distribution of", i)
  sns.boxplot(df[i])
  plt.title(i)
  plt.show()

#heatmap of all features
sns.heatmap(df.corr(numeric_only=True))
plt.show()

#displot
labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
for i in labels:
  #print("Distribution of", i)
  sns.displot(df[i], kde=True)
  plt.title(f"Distribution of {i}")
  plt.show()

#Skewness
labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
for i in labels:
  print("skewness of ", i)
  print(df[i].skew())
  print()