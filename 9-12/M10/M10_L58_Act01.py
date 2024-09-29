#armstrong number
number = int(input("Enter a number: "))

result = 0
temp = number

while temp > 0:
    digit = temp % 10 
    result = result + digit ** 3 #exponentiation
    temp = temp//10

print("result = ",result)

if number == result:
  print(number, "is an armstrong number ")
else:
  print(number, "is not an armstrong number ")