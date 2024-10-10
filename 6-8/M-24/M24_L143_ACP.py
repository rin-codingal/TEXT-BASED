import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-24\Iris_Dataset.csv")

#print the first 10 data
print(iris.head(10))
print()

sns.barplot(x="Species", y="SepalLengthCm", data=iris, palette=["blue", "orange", "green"])
plt.show()

sns.countplot(x="Species", data=iris, palette=["blue", "orange", "green"])
plt.show()

sns.boxplot(x="Species", y="SepalWidthCm", data=iris, palette=["blue", "orange", "green"])
plt.show()

sns.swarmplot(x="Species", y="SepalWidthCm", data=iris, palette=["blue", "orange", "green"])
plt.show()

sns.displot(iris["SepalWidthCm"])
plt.show()

sns.jointplot(x="SepalWidthCm", data=iris)
plt.show()

sns.pairplot(data=iris, hue="Species")
plt.show()