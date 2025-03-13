import pandas as pd
import numpy as np
from sklearn import linear_model

#loading the datafile from the given location
file = "https://aegis4048.github.io/downloads/notebooks/sample_data/unconv_MV_v5.csv"
df = pd.read_csv(file)

#marking the features required and the target data
features = ["Por", "Brittle", "Perm", "TOC"]
target = "Prod"

#Reshaping X and Y values
X = df[features].values.reshape(-1, len(features))
y = df[target].values

#fiting the models
ols = linear_model.LinearRegression()
model = ols.fit(X, y)

#checking the values in the array from the given data
print(f"model coeficient: {model.coef_}")
print()

#intercept
print(f"required intercept from the data: {model.intercept_}")
print()

#accuracy
print(f"accuracy assessment: {model.score(X, y)}")
print()

#future prediction
x_pred = np.array([12, 81, 2.31, 2.8])
x_pred = x_pred.reshape(-1, len(features))

print(f"future predicted model: {model.predict(x_pred)}")
print()

# prediction of 2 gases production rate
x_pred = np.array([[12, 81, 2.31, 2.8], [15, 60, 2.5, 1]])
x_pred = x_pred.reshape(-1, len(features))

print(f"future predicted model of 2 gases production rate: {model.predict(x_pred)}")
print()