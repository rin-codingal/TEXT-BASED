import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Weather Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

df_group = df.groupby('month').mean(numeric_only=True)
df_group = df_group.reset_index()

df_group.plot.area(x='month',y='Humidity', alpha=0.6)
plt.show()

plt.plot(df['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading Number over Time')
plt.show()