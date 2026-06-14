import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

#get data
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])

#create model and train
model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
print(model.fit(x, y))

print()

#evaluate the model
p_pred = model.predict_proba(x)
y_pred = model.predict(x)
score_ = model.score(x, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)

print("x: ", x, sep="\n")
print()

print("y: ", y, sep="\n")
print()

print(f"intercept: {model.intercept_}")
print()

print(f"coef: {model.coef_}")
print()

print("p_pred:", p_pred, sep="\n")
print()

print("y_pred:", y_pred)
print()