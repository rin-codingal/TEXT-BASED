import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

X_train = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1, 1)
y_train = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5])
X_test =  np.array([10,11,12,13,14]).reshape(-1, 1)
y_test =  np.array([5,5.5,7,6.5,7])

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# The coefficients
print(f"Coefficients: {regr.coef_}")
print()

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))

print()

# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f"
      % r2_score(y_test, y_pred))
print()

# Plot outputs
plt.figure(figsize=(12, 8))
plt.scatter(X_test, y_test,  color="black", alpha = 0.5)
plt.plot(X_test, y_pred, color="red", linewidth=3, alpha = 0.8)

plt.show()

# mean square error 
print(np.square(y_test - y_pred).mean())
print()

print(1-(np.square(y_test - y_pred).sum())/np.square(y_test - y_test.mean()).sum())
