def power2(n):
    if n <= 0:
        return False
    
    return (n & (n - 1)) == 0

num = int(input("Enter a number: "))

if power2(num):
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")