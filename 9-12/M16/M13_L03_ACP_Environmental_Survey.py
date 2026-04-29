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

avg_data = data.groupby(data['FUELTYPE']).mean(numeric_only=True)

avg_data = avg_data.reset_index()

print(avg_data)

plt.bar(avg_data['FUELTYPE'], avg_data['CO2EMISSIONS'], color='teal')
plt.xlabel('FUEL TYPE')
plt.ylabel('CO2 EMISSIONS')
plt.show()

sns.countplot(x=data['VEHICLECLASS'], palette='winter')
plt.show()

#mean for vehicle class
avg_data2 = data.groupby(data['VEHICLECLASS']).mean(numeric_only=True)

# numerical x
x = np.arange(0, len(avg_data2.index))

avg_data2 = avg_data2.reset_index()



print(avg_data2)

plt.bar(avg_data2['VEHICLECLASS'], avg_data2['CO2EMISSIONS'], color='teal')
plt.xlabel('VEHICLE CLASS')
plt.ylabel('CO2 EMISSIONS')
plt.show()

plt.bar(x, avg_data2['FUELCONSUMPTION_COMB'], bottom=avg_data2['FUELCONSUMPTION_COMB'], 
        color = '#6EAF46')
plt.ylabel('Fuel Consumption')
plt.xticks(x, avg_data2.index, rotation=90)
plt.legend(['City','Highway','Combined'])
plt.title('Average Fuel Consumption for Different Vehicle Type')
plt.show()