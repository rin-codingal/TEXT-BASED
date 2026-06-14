import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\water_potability.csv")
print("First 5 rows of data:")
print(df.head())
print()

print("shape:")
print(df.shape)
print()

print("total null data:")
print(df.isnull().sum())
print()

print("info:")
print(df.info())
print()

print("description:")
print(df.describe())
print()

print("total null data after filling them:")
df.fillna(df.mean(), inplace=True)
print(df.isnull().sum())
print()

print("total potability")
print(df.Potability.value_counts())
print()

sns.countplot(df['Potability'])
plt.show()

sns.distplot(df['ph'])
plt.show()

df.hist(figsize=(14,14))
plt.show()

plt.figure(figsize=(13,8))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.show()

df.boxplot(figsize=(14,7))
plt.show()

X = df.drop('Potability', axis=1)
Y = df['Potability']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=101, shuffle=True)

dt=DecisionTreeClassifier(criterion='gini', min_samples_split=10, splitter='best')
dt.fit(X_train,Y_train)

prediction=dt.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test,prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test,prediction)}")
print(f"Classification Report =\n {classification_report(Y_test,prediction)}")

knn = KNeighborsClassifier(n_neighbors = 10)
print(knn.fit(X_train, Y_train))

prediction=knn.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test, prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test, prediction)}")
print(f"Classification Report =\n {classification_report(Y_test, prediction)}")


log = LogisticRegression(random_state = 0)
print(log.fit(X_train, Y_train))

prediction=log.predict(X_test)
print(f"Accuracy Score = {accuracy_score(Y_test,prediction)*100}")
print(f"Confusion Matrix =\n {confusion_matrix(Y_test,prediction)}")
print(f"Classification Report =\n {classification_report(Y_test,prediction)}")