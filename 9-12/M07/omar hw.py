number = int(input("Enter a number : "))

if number < 0:
    print("Please enter a positive number.")
else:
    num = str(number)
    order = len(num)
    sum = 0

    for digit in num:
        sum += int(digit) ** order

    # Check if the sum of powers equals the original number
    if sum == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")