import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M16\Titanic Dataset.csv")

#display the first 5 rows of df
print("First 5 rows of data:")
print(df.head())
print()

#check the null value
print("Total null value in the data:")
print(df.isnull().sum())
print()

# Boxplot of Feature Age
plt.boxplot(df["Age"])
plt.title("Age distribution")
plt.show()

# Boxplot of Feature Pclass
plt.boxplot(df["Pclass"])
plt.title("Passenger Class distribution")
plt.show()