import matplotlib.pyplot as plt

blood_sugar_men = [117, 75, 90, 159, 149, 88, 93, 115, 135, 87, 77, 82, 131]
blood_sugar_women = [75, 97, 89, 120, 133, 150, 84, 79, 89, 79, 120, 112, 99]

'''
 Diabetic blood_sugar range

 80 - 100 = normal
 100 - 125 = pre-diabetic
 above 125 = diabetic
 '''

type = [blood_sugar_men, blood_sugar_women]
colors = ["g", "b"]
label = ["men", "women"]
bins = [75, 100, 125, 150]


plt.xlabel("Blood Sugar Range")
plt.ylabel("Total no. of patients")

plt.hist(type, bins=bins, rwidth=0.95, color=colors,
            label=label, orientation="horizontal")

plt.title("Blood Sugar Level Chart")
plt.legend()
plt.show()