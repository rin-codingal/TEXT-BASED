import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#countplot which gender survived the most
sns.countplot(x=df["Gender"], data=df, hue=df["Survived"])
#sns.countplot(df["Gender"], hue=df["Survived"])
plt.show()

# countplot which PClass survived the most and the least
#sns.countplot(df["Pclass"], hue=df["Survived"])
sns.countplot(x=df["Pclass"], data=df, hue=df["Survived"])
plt.show()

# displot Highest number of passengers belong to which Age
sns.displot(df["Age"],kde=False,bins=40)
plt.show()

#countplot Highest number of passengers belong to which Gender
#sns.countplot(data["Gender"])
sns.countplot(x=df["Gender"], data=df, hue=df["Gender"])
plt.show()

#countplot Is SibSp correlated/associated with Survived feature
sns.countplot(x="Survived", hue="SibSp", data=df, palette="mako")
plt.show()

#countplot Is Parch correlated/associated with Survived feature
sns.countplot(x="Survived", hue="Parch", data=df, palette="mako")
plt.show()

#displot Is the feature Fare having normal distribution/spread of data
sns.displot(df["Fare"], kde=True)
plt.show()

#boxplot age group of majority of people belonging to PClass=1
sns.boxplot(x="Pclass",y="Age",data=df,palette="winter")
plt.show()

# heatmap of all the features with target variable Survived
sns.heatmap(df.corr(numeric_only=True))
plt.show()

