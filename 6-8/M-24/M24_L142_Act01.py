import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-24\USA_Housing.csv")

#print the first 10 data
print("first 10 rows:")
print(df.head(10))

print()

#print the last 10 data
print("last 10 rows:")
print(df.tail(10))

print()

df.info()
print()

print(df.describe())
print()

#print the columns
print(df.columns)
print()

#pairplot
sns.pairplot(df)
plt.show()

# Drop the 'Address' column before calculating correlation
df_numerical = df.drop('Address', axis=1)

#heatmap
sns.heatmap(df_numerical.corr(), annot=True)
plt.show()