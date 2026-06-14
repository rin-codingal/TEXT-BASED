def print_numbers(n):
  if (n <= 10): 
      print(n)  
      print_numbers(n + 1) 
  else:
      return

# Start the recursion by calling the function with 1
print_numbers(1)