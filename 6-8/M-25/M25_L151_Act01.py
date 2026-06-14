# Import Libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\Titanic Dataset.csv")

#display the first 5 rows of data
print("First 5 rows of data:")
print(data.head())
print()

#shape
print("Shape:")
print(data.shape)
print()

#heatmap
sns.heatmap(data.isnull(), cmap="spring")
plt.show()

#drop null value
data.dropna(inplace=True)

#heatmap
sns.heatmap(data.isnull(), cbar=False)
plt.show()

#check the null value
print("Total null value in the data:")
print(data.isnull().sum())
print()

# Median Value of Age and Fare
median_age = np.median(data['Age'])
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

# Mode Value of Age and PClass
mode_age = stats.mode(data['Age'])
print("Mode value of Age -", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass -", mode_class)

# Mode Value of Categorical Feature - Gender
mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)