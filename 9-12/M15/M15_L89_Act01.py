import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\USA_Housing.csv")

#display the first 5 rows
print("The first 5 rows")
print(df.head())
print()

#info
print("Information")
df.info()
print()

#Descriptive statistics
print("Descriptive statistics")
print(df.describe())
print()

#columns
print("Columns")
print(df.columns)
print()

#pairplot
sns.pairplot(df)
plt.show()

#heatmap
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()

#machine learning data modeling
from sklearn.model_selection import train_test_split

x=df[["Avg. Area Income", "Avg. Area House Age", "Avg. Area Number of Rooms",
       "Avg. Area Number of Bedrooms", "Area Population"]]

y=df["Price"]



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.40,random_state=101)

print(x_train)
print()

#linear regression
from sklearn.linear_model import LinearRegression

lm=LinearRegression()
lm.fit(x_train,y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1)
coeff_df=pd.DataFrame(lm.coef_,x.columns,columns=["Coefficient"])

print("Linear Regression")
print(coeff_df)
print()

#scatterplot
predictions=lm.predict(x_test)
plt.scatter(y_test,predictions)
plt.show()

#displot
sns.displot((y_test-predictions),bins=50)
plt.show()

#metrics
from sklearn import metrics

print("Metrics:")
print("MAE:", metrics.mean_absolute_error(y_test, predictions))
print("MSE:", metrics.mean_squared_error(y_test, predictions))
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, predictions)))