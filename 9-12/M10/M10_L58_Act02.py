# calculate factors of a number
def print_factors(n):
   print(f"The factors of {n} are:")

   for i in range(1, n + 1):
       if n % i == 0:
           print(i)
 
number = int(input("Enter your number to find it's factors: ")) 
print_factors(number)