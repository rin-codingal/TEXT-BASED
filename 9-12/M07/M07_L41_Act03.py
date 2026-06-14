# Program make a simple calculator
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

a = add(num1, num2)
b = subtract(num1, num2)
c = multiply(num1, num2)
d = divide(num1, num2)

print("Sum :", a)
print("Difference :", b)
print("Product :", c)
print("Quotient :", d)