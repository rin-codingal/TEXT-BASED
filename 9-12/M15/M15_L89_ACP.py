import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\Penguins Data.csv")

#scatterplot Culmen Length vs Body Mass
x = df["Culmen Length (mm)"]
y = df["Body Mass (g)"]
plt.scatter(x, y, c="orange")
plt.title("Culmen Length and Body Mass")
plt.show()

#scatterplot Culmen Depth vs Body Mass
x = df["Culmen Depth (mm)"]
y = df["Body Mass (g)"]
plt.scatter(x, y, c="red")
plt.title("Culmen Depth and Body Mass")
plt.show()

#pairplot all feaatures
sns.pairplot(df)
plt.show()

#area graph
df.plot.area()
plt.show()