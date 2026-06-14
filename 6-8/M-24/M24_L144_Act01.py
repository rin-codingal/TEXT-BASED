import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-24\penguins_size.csv")

print(sns.get_dataset_names())

print()

df = sns.load_dataset("penguins")
print(df.head(10))
print()

print(df.shape)
print()

print(df.tail())
print()

print(df.isnull().sum())
print()

print(df.describe().T)
print()

print(df.describe())
print()

print(df.dtypes)
print()

df.info()
print()

print(df.isnull().sum())
print()

print(df.describe(include="all"))
print()

print(df.corr(numeric_only=True))
print()

#heatmap
plt.figure("Heatmap") # Set the window title
sns.heatmap(df.corr(numeric_only=True), cmap= "Wistia", annot=True)
plt.show()

#histogram
df.hist(figsize=(12,8))
plt.show()

df.plot(kind= "box", subplots=True, layout=(3,2), sharex=False, sharey= False , figsize=(8,12))
plt.show()

print(df.sex.value_counts())
print()

print(df.island.value_counts())
print()

print(df.species.value_counts())
print()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data=df, x="sex", palette="summer")
plt.show()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data=df, x="island", palette="RdPu")
plt.show()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data=df, x="species", palette="YlOrRd")
plt.show()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data= df, x="sex", palette="rocket", hue="species")
plt.show()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data= df, x= "island", hue="species", palette="husl")
plt.show()

#countplot
plt.figure("Countplot") # Set the window title
sns.countplot(data= df, x= "island", hue="sex", palette="spring")
plt.show()

#pairplot
sns.pairplot(data=df, hue="species",palette="mako")
plt.show()