# Factorial of a number using recursion
def recur_factorial(n):
   if n == 1:
      return n
   else:
      return n*recur_factorial(n-1)

num = int(input("Enter a number: "))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   result = recur_factorial(num) #calling function and save the value into a variable
   print("The factorial of", num, "is", result)