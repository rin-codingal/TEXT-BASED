a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

lcm = max(a, b)
while lcm % a != 0 or lcm % b != 0:
    lcm += 1

print(f"LCM is: {lcm}")