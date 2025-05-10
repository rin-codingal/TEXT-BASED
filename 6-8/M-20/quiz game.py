username = input("please enter your name: ")
print(f"Welcome, {username}! Get ready for the quiz!")

score = 0

QUESTIONS = [
    ("What is the capital of UK?", "London"),
    ("Which built-in function can get information from the user", "input"),
    ("Which keyword do you use to loop over a given list of elements", "for")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print()
print(f"your score is: {score}")
print()