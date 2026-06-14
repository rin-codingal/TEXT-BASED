import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\titanic.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#shape
print("Shape:")
print(df.shape)
print()

#heatmap
sns.heatmap(df.isnull(), cmap="spring")
plt.show()


#drop Fare column
df.drop("Fare", axis=1, inplace=True)

#display the first 5 rows of df after dropping the Fare column
print("First 5 rows of data after removing 'Fare' column:")
print(df.head())
print()

#drop null value
df.dropna(inplace=True)

#heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.show()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

#get dummies of Gender column
print(pd.get_dummies(df["Gender"]).head())
print()

gender = pd.get_dummies(df["Gender"], drop_first=True)

#display first 5 rows of gender
print("First 5 rows of Gender after removing the first column")
print(gender.head())
print()

print(pd.get_dummies(df["Embarked"]).head(4))
print()

arked = pd.get_dummies(df["Embarked"], drop_first=True)
pclass = pd.get_dummies(df["Pclass"], drop_first=True)

print(pclass.head(4))
print()

Titanic = pd.concat([df, gender, pclass], axis=1)

#displaying the Updated Dataset
print("Updated dataset")
print(Titanic.head())
print()

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\titanic.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()