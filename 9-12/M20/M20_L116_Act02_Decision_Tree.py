import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\sample_data.csv")  
print(data.head())
print()

y = data.pop('TARGET CLASS')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


clf_model = DecisionTreeClassifier()
clf_model.fit(X_train, y_train)


y_predict = clf_model.predict(X_test)
print("accuracy : ", accuracy_score(y_test, y_predict))