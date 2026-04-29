# take input from the user
x = input("Enter a number: ")
total_digit = len(x) # total digit of the number

num = int(x)

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum = sum + digit ** total_digit
   temp = temp // 10 # floor division to get the quotient

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")