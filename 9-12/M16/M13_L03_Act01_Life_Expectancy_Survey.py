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

avg_data = data.groupby(data['continent']).mean(numeric_only=True)

avg_data = avg_data.reset_index()

print(avg_data)

plt.bar(avg_data['continent'], avg_data['life_exp'], color='teal')
plt.xlabel('Continent')
plt.ylabel('Average Life Expectancy')
plt.show()

plt.bar(avg_data['continent'], avg_data['gdp_cap'], color='darkred')
plt.xlabel('Continent')
plt.ylabel('Average GDP per capita')
plt.show()

sns.countplot(x=data['continent'], palette='winter')
plt.show()