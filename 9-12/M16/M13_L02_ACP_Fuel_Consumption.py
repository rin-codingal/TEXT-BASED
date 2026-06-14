import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\FuelConsumption.csv")

print("First 5 rows of data:")
print(data.head())

#Data Information
print("Data Information:")
print(data.info())

#Check presence of null values
print("Check which data contains null value:")
print(data.isnull().any())

labels = ['FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB', 'FUELCONSUMPTION_COMB_MPG', 'CO2EMISSIONS']

# Plotting boxplots
for l in labels:
  sns.boxplot(y=data[l], palette='winter')
  plt.show()

sns.boxplot(y='CO2EMISSIONS', x='FUELTYPE',data=data, palette='viridis')
plt.show()

sns.boxplot(y='CO2EMISSIONS', x='VEHICLECLASS',data=data, palette='viridis')
plt.show()

# Plotting violin plots
sns.violinplot(y='CO2EMISSIONS', x='FUELTYPE',data=data, palette='bright')
plt.show()

sns.violinplot(y='CO2EMISSIONS', x='VEHICLECLASS',data=data, palette='bright')
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