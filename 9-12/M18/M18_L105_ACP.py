import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\titanic.csv")

# Drop some columns which is not relevant to the analysis (they are not numeric)
cols_to_drop = ["Name", "Ticket", "Cabin"]
df = df.drop(cols_to_drop, axis=1)
#df = df.pop(cols_to_drop)

print("info:")
print(df.info())
print()

#heatmap
sns.heatmap(df.isnull())
plt.show()

# To replace missing values with interpolated values, for example Age
df["Age"] = df["Age"].interpolate()

# Drop all rows with missing data
df = df.dropna()

#display the first 5 rows of df
print("First 5 rows of titanic data:")
print(df.head())
print()

#countplot
sns.countplot(x="Survived", data = df, hue="Survived")
plt.show()

#countplot which gender survived the most
sns.countplot(x="Survived", data=df, hue="Gender", palette="winter")
plt.show()

# countplot which PClass survived the most and the least
sns.countplot(x="Survived", hue="Pclass",  data = df, palette="PuBu")
plt.show()

#histogram
df["Age"].plot.hist()
plt.show()
