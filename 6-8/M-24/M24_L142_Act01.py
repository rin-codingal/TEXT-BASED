import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-24\USA_Housing.csv")

#print the first 10 data
print(df.head(10))

print()

df.info()
print()

print(df.describe())
print()

#print the columns
print(df.columns)
print()

sns.pairplot(df)
plt.show()