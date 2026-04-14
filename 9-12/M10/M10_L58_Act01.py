#armstrong number
x = input("Enter a number: ")
number_of_digit = len(x)

number = int(x)

result = 0
temp = number

while temp > 0:
    digit = temp % 10 
    result = result + digit ** number_of_digit #exponentiation
    temp = temp//10

print("result = ",result)

if number == result:
  print(number, "is an armstrong number ")
else:
  print(number, "is not an armstrong number ")