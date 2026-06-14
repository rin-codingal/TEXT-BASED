import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\Pokemon Data.csv")
print("First 5 rows of data:")
print(data.head())
print()

print("information: ")
print(data.info())
print()

data['Type 2'].fillna(value='None',inplace=True)
print("Total null data for type 2:")
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

print("First 5 rows of data:")
print(data.head())
print()

data.drop('Name', axis=1, inplace=True)

data = pd.get_dummies(data)

print("data shape:")
print(data.shape)
print()


y = data.pop('Legendary')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

ypred1 = LogReg.predict(X_test)
print("accuracy : ", accuracy_score(y_test,ypred1))