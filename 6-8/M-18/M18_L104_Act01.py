n = int(input("enter the number whose sum you want to find: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i    
    print(f"Sum of {i} = {sum}")