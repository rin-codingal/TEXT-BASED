import random

# The program generates a secret number
secret_number = random.randint(1, 10) 

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")

# Get the user's single guess
guess = int(input("Enter your guess: "))

# Check the guess using conditional statements
if guess == secret_number:
    print("Congratulations! You guessed it correctly!")
else:
    print(f"Sorry, it's wrong. The secret number was {secret_number}.")