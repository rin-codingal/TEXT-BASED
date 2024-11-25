import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\petrol_consumption.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#Descriptive statistics
print("Descriptive statistics")
print(df.describe())
print()

X = df[["Petrol_tax", "Average_income", "Paved_Highways",
       "Population_Driver_licence(%)"]]
y = df["Petrol_Consumption"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=["Coefficient"])
print(coeff_df)
print()

y_pred = regressor.predict(X_test)
df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(df)
print()

print(f"Mean Absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}")
print(f"Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred)}")
print(f"Root Mean Squared Error: {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}")