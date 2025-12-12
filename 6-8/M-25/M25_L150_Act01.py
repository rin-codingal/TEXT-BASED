import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\heart.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#shape
print("Shape:")
print(df.shape)
print()

#columns
print("Columns:")
print(df.columns)
print()

#Descriptive statistics
print("Descriptive statistics:")
print(df.describe())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

#info
print("Info:")
df.info()
print()

#heatmap
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="terrain")
plt.show()

#pairplot
sns.pairplot(data=df)
plt.show()

#histogram
df.hist(figsize=(12,12), layout=(5,3))
plt.show()

#box and whiskers plot
df.plot(kind = "box", subplots=True, layout=(5, 3), figsize=(12,12))
plt.show()

#barplot
sns.barplot(data=df, x="sex", y="chol", hue="target", palette="spring")
plt.show()

#count value
print("Total sex:")
print(df["sex"].value_counts())
print()

print("Total target:")
print(df["target"].value_counts())

#countplot
sns.countplot(x='sex', data= df, palette='husl', hue='target')
plt.show()

sns.countplot(x='target', palette='BuGn', data=df)
plt.show()

sns.countplot(x='ca', hue='target', data= df)
plt.show()