nd = int(input("Enter total number of attendance days: "))
na = int(input("Enter number of days absent: "))

result = (nd-na)/nd*100

print("Your attendance is ",result)

if result < 75 :
     print("You are not eligible for exams")
else:
     print("You are eligible for attending exam")