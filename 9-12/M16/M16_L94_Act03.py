import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

# Create new dataset with only Numerical Features
num_data = df.drop(["Name", "Ticket", "Cabin", "Embarked", "Gender"], axis=1)
labels = ["PassengerId","Survived","Pclass","Age","SibSp","Parch","Fare"]

# boxplot for all the features
for label in labels:
  plt.boxplot(num_data[label])
  #print("Distribution of", label)
  plt.title(f"Distribution of {label}")
  plt.show()

#scaling dataset
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)
print("After scaling dataset:")
print(num_data)