import math

print("The Floor value of 23.56 is: ",math.floor(23.56))
print("The Ceiling value of 23.56 is: ",math.ceil(23.56))
print()

print("sin, cos, tan of 45:")
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print()
print("Factorial of 5: ",math.factorial(5))

print()
x = 5
y = -7
z = math.copysign(x,y)
print("the copysign result = ",z)