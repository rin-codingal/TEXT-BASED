Base = int(input("Enter base : "))
Power = int(input("Enter power : "))
n = 1
for i in range(1, Power+1):
   n = n * Base
   print(n)