import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M14\Tips_Dataset.csv")

#print the first 10 data
print(df.head(10))
print()

#print the last 10 data
print(df.tail(10))
print()

sns.displot(df["size"], kde=True)
plt.show()

sns.displot(df["tip"], kde=True)
plt.show()

sns.displot(df["total_bill"], kde=True)
plt.show()

sns.displot(df["total_bill"], kde=False)
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="time")
plt.show()

sns.pairplot(df, hue ="gender")
plt.show()

