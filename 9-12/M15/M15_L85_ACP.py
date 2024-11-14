import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\Penguins_Data.csv")

#display the first 3 rows of df
print("First 3 rows of data:")
print(df.head(3))
print()

#check if there's null value present
print("Check which data contains null value:")
print(df.isnull().any())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Visualize missing values using a heatmap
sns.heatmap(df.isnull())
plt.show()

#fill up numerical null value
#df["Culmen Depth (mm)"] = df.fillna(df["Culmen Depth (mm)"].mean())
df["Culmen Depth (mm)"].fillna(df["Culmen Depth (mm)"].mean())

#df["Culmen Length (mm)"] = df.fillna(df["Culmen Length (mm)"].mean())
df["Culmen Length (mm)"].fillna(df["Culmen Length (mm)"].mean())

#df["Flipper Length (mm)"] = df.fillna(df["Flipper Length (mm)"].mean())
df["Flipper Length (mm)"].fillna(df["Flipper Length (mm)"].mean())

#df["Body Mass (g)"] = df.fillna(df["Body Mass (g)"].mean())
df["Body Mass (g)"].fillna(df["Body Mass (g)"].mean())

#df["Delta 13 C (o/oo)"] = df.fillna(df["Delta 13 C (o/oo)"].mean())
df["Delta 13 C (o/oo)"].fillna(df["Delta 13 C (o/oo)"].mean())

#df["Delta 15 N (o/oo)"] = df.fillna(df["Delta 15 N (o/oo)"].mean())
df["Delta 15 N (o/oo)"].fillna(df["Delta 15 N (o/oo)"].mean())

#fill up categorical null value
#df["Gender"] = df.fillna(df["Gender"].value_counts().index[0])
df["Gender"].fillna(df["Gender"].value_counts().index[0])


#remove null data
null_data = df.drop("Comments", axis=1)

#re-check total null value after removing them
print("updated null value in the data:")
print(null_data.isnull().sum())
print()