import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Matches
df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\matches.csv")

#display the first 5 rows of df
print("First 5 rows of matches data:")
print(df.head())
print()

#shape
print("Shape:")
print(df.shape)
print()

#check the null value
print("Total null value in the matches data:")
print(df.isnull().sum())
print()

#heatmap
sns.heatmap(df.isnull(), cmap="spring")
plt.show()

#display the original Dataset again
print("First 5 rows of matches data:")
print(df.head())
print()

#Dropping the umpire 3 coloumn
df.drop("umpire3", axis=1, inplace=True)

#display the  Dataset after dropping umpire3 column
print("First 5 rows of matches data after dropping 'umpire3' column:")
print(df.head())
print()

#drop null value
df.dropna(inplace=True)

#heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.show()

#check the null value
print("Total null value in the matches data:")
print(df.isnull().sum())
print()

#dropping the coloumn season since in the date coloumn that year ha salready been mentioned so dropping it
df.drop("season", axis=1, inplace=True)

#display the  Dataset after dropping season column
print("First 5 rows of matches data after dropping 'season' column:")
print(df.head())
print()

#Deliveries
df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M18\deliveries.csv")

#display the first 5 rows of df
print("First 5 rows of deliveries data:")
print(df.head())
print()

#shape
print("Shape:")
print(df.shape)
print()

#check the null value
print("Total null value in the deliveries data:")
print(df.isnull().sum())
print()

#heatmap
sns.heatmap(df.isnull(), cmap="spring")
plt.show()

#drop null value
df.dropna(inplace=True)

#heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.show()

#check the null value
print("Total null value in the deliveries data:")
print(df.isnull().sum())
print()

#display the new dataset
print("First 5 rows of deliveries data:")
print(df.head())
print()

