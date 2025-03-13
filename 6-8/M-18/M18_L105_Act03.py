# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num

while temp > 0:
   digit = temp % 10 # getting the remainder of the division
   sum = sum + digit ** 3 #calculate each digit to the power of 3 and then add it to the sum
   temp = temp // 10 # floor division (the result is rounded down without decimal value)

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")