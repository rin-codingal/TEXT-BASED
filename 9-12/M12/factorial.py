def factorial(n):
  if n == 0 or n == 1:  
      return 1
  else:
      return n * factorial(n - 1)  

num = int(input("enter number: "))
result = factorial(num)

print(f"factorial of {num} is {result}")  
