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

# Countplot for feature Continent
# Setting different themes
sns.set_style('white')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('dark')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('ticks')
sns.countplot(x=data['continent'])
plt.show()

# Despining
sns.set_style('white')
sns.countplot(x=data['continent'])
sns.despine()
plt.show()

# Trying different palettes
sns.set_style('whitegrid')
sns.countplot(x=data['continent'], palette='winter')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'], color='Purple')
plt.show()

# Scaling figures
sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['continent'], color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)
plt.show()

# Scaling font size of figure
sns.set_style('whitegrid')
sns.set_context("poster", font_scale=0.8)
sns.countplot(x=data['continent'], color='Purple')
plt.xticks(rotation=45)
plt.show()