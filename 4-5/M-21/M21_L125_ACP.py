Powered_By = int(input("Enter a number to get the power series of it: "))

user = int(input("Till where do you want it? "))

for i in range(1, user+1):
   print(Powered_By**i)

print()

Base = int(input("Enter base : "))
Power = int(input("Enter power : "))
n = 1
for i in range(1, Power+1):
    n = Base*n
    print(n)