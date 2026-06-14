import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\Pokemon Data.csv")
print("First 5 rows of data:")
print(data.head())
print()

data['Type 2'].fillna(value='None',inplace=True)
print("Total null data:")
print(data.isnull().sum())
print()

data['Type 1'].value_counts().plot.bar()
plt.show()

data['Type 2'].value_counts().plot.bar()
plt.show()

data['Legendary'].value_counts().plot.bar()
plt.show()

data['Type 1'].unique()
data['Type 2'].unique()


lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

print(data.head())
print()

data.drop('Name', axis=1, inplace=True)

data = pd.get_dummies(data)

print(data.shape)
print()

y = data.pop('Legendary')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

ypred1 = LogReg.predict(X_test)
accuracy_score(y_test,ypred1)


error_rates = []

for a in range(1, 40):
    k = a
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(y_test - preds))

plt.figure(figsize=(10, 7))
plt.plot(range(1,40),error_rates,color='blue', linestyle='dashed', marker='o',
markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

knn_model = KNeighborsClassifier(n_neighbors=8)
print(knn_model.fit(X_train, y_train))
print()

y_predict = knn_model.predict(X_test)
print("accuracy score: ", accuracy_score(y_test, y_predict))
print()

clf_model = DecisionTreeClassifier()
print(clf_model.fit(X_train, y_train))
print()

y_predict = clf_model.predict(X_test)
print("accuracy score: ", accuracy_score(y_test, y_predict))