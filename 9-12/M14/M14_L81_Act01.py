import matplotlib.pyplot as plt

#line chart
def line_chart_of_students_and_marks():
  plt.plot(students_names,students_marks)
  plt.title("Students Marks Graph")
  plt.xlabel("Students Names")
  plt.ylabel("Students Marks")
  plt.show()

# bar chart 
def percentage_bar_chart():
  plt.bar(students_names,marks_perc)
  plt.title("Students Percentage Graph")
  plt.xlabel("Student Names")
  plt.ylabel("Student Percentage")
  plt.show()

students_names=["Jimmy","Santoso","Bambang","Emil","Jack","Amber","Ratna","Sinta"]
students_marks=[37,50,25,45,30,40,25,30]

marks_perc = []

for x in students_marks:
	res = (x/50)*100
	marks_perc.append(res)

print("mark percentage:")
print(marks_perc)
print()

line_chart_of_students_and_marks()
percentage_bar_chart()