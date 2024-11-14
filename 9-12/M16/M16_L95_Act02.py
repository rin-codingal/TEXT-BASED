import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#boxplot embarked vs age
sns.boxplot(data = df, x = "Embarked", y = "Age", hue="Embarked")
plt.show()

# scatterplot Survived vs Fare
plt.scatter(x = df["Fare"], y = df["Survived"])
plt.ylabel("Survived")
plt.xlabel("Fare")
plt.show()

# scatterplot Survived vs Parch
plt.scatter(x = df["Parch"], y = df["Survived"])
plt.ylabel("Survived")
plt.xlabel("Parch")
plt.show()

# scatterplot Survived vs SibSp
plt.scatter(x = df["SibSp"], y = df["Survived"])
plt.ylabel("Survived")
plt.xlabel("SibSp")
plt.show()

# Check association between Gender and Embarked
association_categorical = pd.crosstab(df["Gender"], df["Embarked"])
print("Association between Gender and Embarked:")
print(association_categorical)
print()

