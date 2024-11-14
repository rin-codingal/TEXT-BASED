import numpy as np  
import matplotlib.pyplot as plt

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
july = [12, 15, 11, 9, 1, 9, 21]
august = [17, 5, 2, 11, 1, 8, 29]

#Bar plot for july
plt.bar(day, july, width=0.5, color="lime", edgecolor="red")

plt.title("Birth Rate For July")
plt.xlabel("Day")
plt.ylabel("Birth Rate")

plt.ylim(1,30)

plt.legend()
plt.show()

#Bar plot for August
plt.bar(day, august, width=0.5, color="blue", edgecolor="red")

plt.title("Birth Rate For August")
plt.xlabel("Day")
plt.ylabel("Birth Rate")

plt.ylim(1,30)

plt.legend()
plt.show()

#Bar plot for both months
X_axis = np.arange(len(day))

plt.bar(X_axis - 0.25, july, width=0.5, label = "July", color="lime", edgecolor="red") 
plt.bar(X_axis + 0.25, august, width=0.5, label = "August", color="blue", edgecolor="red") 

plt.xticks(X_axis, day) 
plt.title("Birth Rate on July and August")
plt.xlabel("Day")
plt.ylabel("Birth Rate")

plt.ylim(1,30)

plt.legend()
plt.show()