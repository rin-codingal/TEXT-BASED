import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

weather = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-24\Weather_Dataset.csv")

#print first 5 data
print(weather.head())

print()

weather.info()

sns.barplot(x="wind_speed", y="temperature",data=weather, palette=["red", "blue", "green"])
plt.show()

sns.displot(weather["temperature"],kde=True)
plt.show()

sns.displot(weather["humidity"], rug=True, kde=True)
plt.show()

sns.jointplot(x="humidity", y="temperature",data=weather)
plt.show()

sns.jointplot(x="humidity", y="temperature",data=weather, kind="hex")
plt.show()

sns.jointplot(x="humidity", y="temperature",data=weather, kind="kde")
plt.show()

sns.pairplot(weather[["humidity", "temperature", "air_pollution_index"]])
plt.show()

sns.stripplot(x="weather_type", y="temperature", data=weather)
plt.show()

sns.stripplot(x="weather_type", y="temperature", data=weather, jitter=True)
plt.show()

sns.swarmplot(x="humidity", y="temperature", data=weather)
plt.show()

sns.boxplot(x="humidity", y="temperature", data=weather, hue=weather['weather_type'])
plt.show()

sns.barplot(x="wind_speed", y="temperature",data=weather, hue=weather['weather_type'])
plt.show()

sns.countplot(x="weather_type", data=weather)
plt.show()

sns.pointplot(x="humidity", y="temperature", data=weather, hue=weather['weather_type'])
plt.show()

sns.lmplot(x="humidity", y="temperature", data=weather)
plt.show()

sns.lmplot(x="humidity", y="temperature", data=weather, hue=weather['weather_type'])
plt.show()