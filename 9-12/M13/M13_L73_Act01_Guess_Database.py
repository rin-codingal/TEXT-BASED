print("What is the type of above given database")
print("1) Relational Database")
print("2) Non-Relational Database")

answer = int(input("Enter your guess here..."))

if answer == 2:
    print("You guessed it right!")
else:
    print("Unfortunately your guess was wrong.")

print()
print("Please tell your mentor why you guessed this?")