import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# set plot style
sns.set_style("whitegrid")

# Countplot for feature Survived
sns.countplot(x="Survived", data=df, hue="Survived")
plt.show()

# Barchart for showing passengers belonging to different gender who survived or not
sns.countplot(x="Gender", hue="Survived", data=df)
plt.show()

# Customize Plots
sns.countplot(x="Survived", data=df, palette="winter", hue="Survived")
plt.show()

sns.countplot(x="Gender", hue="Survived", data=df, palette="winter")
plt.show()

# Countplot for Embarked
sns.countplot(x="Embarked", data=df, hue="Embarked")
plt.show()

# Rotate the value labels and modify their font size
sns.countplot(x="Embarked", data=df, hue="Embarked")
plt.xticks(rotation=30, fontsize=20)
plt.show()