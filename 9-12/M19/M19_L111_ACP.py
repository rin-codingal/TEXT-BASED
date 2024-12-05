import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

dataset = load_breast_cancer()

sns.set_style("dark")
mpl.style.use(["https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle"])
mpl.rcParams.update({"figure.figsize": (8,6), "axes.titlepad": 22.0})

print(f"Target variables  : {dataset['target_names']}")
print()

(unique, counts) = np.unique(dataset['target'], return_counts=True)

print(f"Unique values of the target variable: {unique}")
print(f"Counts of the target variable : {counts}")
print()

# barplot
sns.barplot(x=dataset['target_names'], y=counts, hue=dataset['target_names'])
plt.title("Target variable counts in dataset")
plt.show()

# Define explonatory variables and target variable
X = dataset['data']
y = dataset['target']

# Apply normalization operation for numerical stability
standardizer = StandardScaler()
X = standardizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.25, random_state=0)

# Fit a Logistic Regression Model to the train data
model = LogisticRegression()
print(model.fit(X_train, y_train))
print()

# prediction on the testing data
predictions = model.predict(X_test)

cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()

print(f"True Positive(TP)  = {TP}")
print(f"False Positive(FP) = {FP}")
print(f"True Negative(TN)  = {TN}")
print(f"False Negative(FN) = {FN}")
print()

accuracy =  (TP+TN) /(TP+FP+TN+FN)

print(f"Accuracy of the binary classification = {round(accuracy, 3)}")
print()