# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

#total digit
pow = len(str(num))

# find the sum of the cube of each digit
temp = num

while temp > 0:
   digit = temp % 10 # getting the remainder of the division
   sum = sum + digit ** pow #calculate each digit to the power of total digit and then add it to the sum
   temp = temp // 10 # floor division (the result is rounded down without decimal value)

# display the result
if num == sum:
   print(f"{num} is an Armstrong number")
else:
   print(f"{num} is not an Armstrong number")