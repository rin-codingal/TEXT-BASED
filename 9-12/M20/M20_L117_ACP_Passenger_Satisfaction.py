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

#1. load the data
data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M20\Airline Data.csv")
print("First 5 rows of data:")
print(data.head())
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

# 4. Logistic Regression Model
LogReg = LogisticRegression(max_iter=1000) # Increased max_iter to help model converge
LogReg.fit(X_train, y_train)
ypred1 = LogReg.predict(X_test)
print("Logistic Regression accuracy score: ", accuracy_score(y_test, ypred1))
print()

# 5. Find optimal K Value for KNN
error_rates = []

for a in range(1, 40):
    k = a
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    
    # FIX: Use inequality comparison instead of subtraction
    error_rates.append(np.mean(preds != y_test))

plt.figure(figsize=(10, 7))
plt.plot(range(1, 40), error_rates, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

# 6. Evaluate KNN with K=8
knn_model = KNeighborsClassifier(n_neighbors=8)
knn_model.fit(X_train, y_train)
y_predict_knn = knn_model.predict(X_test)
print("KNN (K=8) accuracy score: ", accuracy_score(y_test, y_predict_knn))
print()

# 7. Decision Tree Model
clf_model = DecisionTreeClassifier()
clf_model.fit(X_train, y_train)
y_predict_dt = clf_model.predict(X_test)
print("Decision Tree accuracy score: ", accuracy_score(y_test, y_predict_dt))