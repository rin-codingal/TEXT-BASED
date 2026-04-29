import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\gapminder(2007).csv")

print("First 5 rows of data:")
print(data.head())

#Data Information
print("Data Information:")
print(data.info())

#Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

labels = ['population','life_exp','gdp_cap']

# Plotting boxplots
for l in labels:
  sns.boxplot(y=data[l], palette='winter')
  plt.show()

sns.boxplot(y='gdp_cap', x='continent',data=data, palette='viridis')
plt.show()

sns.boxplot(y='life_exp', x='continent',data=data, palette='viridis')
plt.show()

# Plotting violin plots
sns.violinplot(y='gdp_cap', x='continent',data=data, palette='bright')
plt.show()

sns.violinplot(y='life_exp', x='continent',data=data, palette='bright')
plt.show()

#Plotting Density Plot
for l in labels:
  sns.kdeplot(data[l])
  plt.show()

# Plotting histogram
for l in labels:
  plt.hist(data[l])
  plt.xlabel(l)
  plt.show()

# Plotting Distplot
for l in labels:
  sns.distplot(data[l])
  plt.show()
  print("Skewness is :", data[l].skew())