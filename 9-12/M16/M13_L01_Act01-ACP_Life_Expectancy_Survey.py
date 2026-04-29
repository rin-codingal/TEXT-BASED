#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import data
data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\gapminder(2007).csv")

print("First 5 rows of data:")
print(data.head())

#Data Information
print("Data Information:")
print(data.info())

#Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

#Plotting Relationships
sns.scatterplot(data=data, x='gdp_cap', y='life_exp')
plt.show()

sns.scatterplot(data=data, x='gdp_cap', y='life_exp', hue='continent')
plt.show()

fig, ax = plt.subplots(figsize=(8,8))
sns.scatterplot(data=data, x="gdp_cap", y="life_exp", size="population", alpha=0.7, hue="continent", sizes=(20,1000),palette='bright')
plt.show()

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()

sns.relplot(data=data, y='life_exp',x='gdp_cap', col='continent', col_wrap=3, height=3)
plt.show()

sns.pairplot(data, hue='continent')
plt.show()