
number = int(input("Enter any number to be check :  "))

# Store the number for comparison later
original_number = number
reverse = 0

while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

print(f"Reverse number = {reverse}")
print()

if reverse == original_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")