# Palindrome checker
number = int(input("Enter your Number : "))

# Store the number for comparison later 
temp  = number
reverse=int(0)


# while number is not 0 all last digit to reverse number
while number>0:
  rem = (number%10)
  reverse = reverse*10 + rem
  number//=10

print("Reversed number : ",reverse)
print()

if(temp==reverse):
  print(f"{temp} is a Palindrome")
else:
  print(f"{temp} is Not a palindrome")
