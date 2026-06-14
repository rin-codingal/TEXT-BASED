import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

#1. load the data
data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\Airline Data.csv")
print("First 5 rows of data:")
print(data.head())
print()

print("information: ")
print(data.info())
print()

data['satisfaction'].value_counts().plot.bar()
plt.title('Satisfaction Distribution')
plt.ylabel('Count')
plt.show()

# 2. Data Preprocessing & Cleaning
# Drop unnecessary identifier columns
data = data.drop(columns=['Unnamed: 0', 'id'])

# Handle missing values in 'Arrival Delay in Minutes' by filling with the median
data['Arrival Delay in Minutes'] = data['Arrival Delay in Minutes'].fillna(data['Arrival Delay in Minutes'].median())

# Encode ALL categorical object columns into numerical values
lb = LabelEncoder()
categorical_cols = ['Gender', 'Customer Type', 'Type of Travel', 'Class', 'satisfaction']

for col in categorical_cols:
    data[col] = lb.fit_transform(data[col])

print("Data after preprocessing and encoding:")
print(data.head())
print()

# 3. Split data into Features (X) and Target (y)
y = data.pop('satisfaction')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

ypred1 = LogReg.predict(X_test)
print("accuracy : ", accuracy_score(y_test,ypred1))