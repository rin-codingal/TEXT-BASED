"""
A Disarium number is a number in which the sum of its digits, each raised to the power of its respective position, equals the number itself
"""

def is_disarium(number):
    """
    Checks if a given number is a Disarium number.

    Args:
        number: An integer to check.

    Returns:
        True if the number is a Disarium number, False otherwise.
    """
    num_str = str(number)
    length = len(num_str)
    sum_of_powers = 0

    for i, digit_char in enumerate(num_str):
        digit = int(digit_char)
        position = i + 1  # Positions are 1-indexed
        sum_of_powers += digit ** position

    return sum_of_powers == number

num = int(input("Enter any number: "))
result = is_disarium(num)

if result:
    print(f"{num} is a disarium number")
else:
    print(f"{num} is not disarium number")