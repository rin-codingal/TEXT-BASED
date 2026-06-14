# take marks as input from user
print("Enter Marks Obtained in 3 Subjects: ")

math = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))

# Let's calculate the percentage of marks
sum = math + english + science
print("sum of math, english, and science: ",sum)

perc = (sum/300)*100

print(f"Percentage Mark = {perc}")
