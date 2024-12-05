import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import math

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M19\insurance_data.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#scatterplot
plt.scatter(df.age, df.bought_insurance, marker="+", color="red")
plt.show()

#Defining the Training and Testing Variables
X_train, X_test, y_train, y_test = train_test_split(df[["age"]],df.bought_insurance,train_size=0.8)

#display X_test
print(X_test)
print()

# Using Logistic Regression Algorithm
model = LogisticRegression()
print(model.fit(X_train, y_train))
print()

#display X_test
print(X_test)
print()

# predicting the y
y_predicted = model.predict(X_test)

print("prediction probability:")
print(model.predict_proba(X_test))
print()

#test model
print(f"test model score: {model.score(X_test,y_test)}")
print()

print(f"y_predicted: {y_predicted}")
print()

print(X_test)

#coeficient
print(f"coefficient: {model.coef_}")
print()

#intercept
print(f"intercept: {model.intercept_}")
print()

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)

    return y

age = 35
print(prediction_function(age))
print()