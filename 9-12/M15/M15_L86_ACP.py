import matplotlib.pyplot as plt

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
july = [12, 15, 11, 9, 1, 9, 21]
august = [17, 5, 2, 11, 1, 8, 29]

plt.plot(day,july,"g", linestyle="dotted",marker="o", linewidth=3,label="July")
plt.plot(day,august,"r", linestyle="dashed",marker="D", linewidth=3,label="August")

plt.title("Birth Rate")
plt.xlabel("Day")
plt.ylabel("Birth Rate")


plt.ylim(1,30)

plt.legend()
plt.show()