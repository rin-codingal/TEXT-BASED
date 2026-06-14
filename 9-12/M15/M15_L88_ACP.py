import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M15\Penguins Data.csv")

type =[df["Culmen Length (mm)"], df["Culmen Depth (mm)"], df["Flipper Length (mm)"], df["Body Mass (g)"]]
colors = ["g", "y", "b", "r"]
label = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"]

plt.hist(type, rwidth=0.95, color=colors,label=label)
plt.legend()

#df.hist(figsize=(12,8))
plt.show()