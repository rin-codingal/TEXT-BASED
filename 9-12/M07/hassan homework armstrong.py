def is_armstrong_number(num):
  digits = str(num)
  # Calculate the number of digits
  n = len(digits)

  # Calculate the sum of each digit raised to the power of n
  sum_of_powers = sum(int(digit)**n for digit in digits)

  # Return whether the sum equals the original number
  return sum_of_powers == num


# Example usage
number = int(input("Enter a number: "))
if is_armstrong_number(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")