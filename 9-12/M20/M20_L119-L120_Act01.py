import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\Churn_Modelling.csv")

#display the first 5 rows of data
print("First 5 rows of data:")
print(df.head())
print()

#info
print(df.info())
print()

#describe
print(df.describe())
print()

#label encoding
lb = LabelEncoder()

df["Geography"] = lb.fit_transform(df["Geography"])
df["Gender"] = lb.fit_transform(df["Gender"])

#print data
print("data after label encoding:")
print(df)
print()

#info
print(df.info())
print()

#feature selection
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

#shape
print(f"shape : {df.shape}")
print()

#train test split
y = df.pop('Exited')
X = df

#x shape
print(f"x shape : {X.shape}")
print()

#y shape
print(f"y shape : {y.shape}")
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#display x train
print("x train:")
print(X_train)
print()

#model building