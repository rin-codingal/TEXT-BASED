import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M14\IMDB_Dataset.csv")

print(sns.get_dataset_names())

print()

#the first 3 data
print(df.head(3))
print()

#the last 3 data
print(df.tail(3))
print()

#info
df.info()
print()

#check any null value
print(df.isnull().sum())
print()

#subset from row 41-75
print(df.loc[40:74,"Poster_Link":"No_of_Votes"])
print()

#display data with the highest number of votes
print(df.max())
print()

#boxplot
sns.boxplot(x="IMDB_Rating", y="Runtime", data=df)
plt.show()

x = df["IMDB_Rating"]
y = df["Runtime"]
plt.plot(x, y)
plt.show()

#joint plot
sns.jointplot(x="IMDB_Rating", y="Runtime",data=df)
plt.show()

#count plot
sns.countplot(x="IMDB_Rating", data=df)
plt.show()