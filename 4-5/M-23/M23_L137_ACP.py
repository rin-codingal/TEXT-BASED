import time

score = 0

print("Hello there, welcome to the General Knowledge Quiz!")
time.sleep(1.5)

print("Their are 10 questions, try to answer them all correctly")
time.sleep(1.5)

print("Choose A, B, C, or D to answer!")
time.sleep(1.5)

print("Your all set. Good luck!")

question_1 = input("1. Which direction does the sunrise from?\nA. West\nB. South\nC. East\nD. West:  ")

question_2 = input("2. Which is the largest ocean in the world\nA. Atlantic Ocean\nB. Pacific Ocean\nC. Indian Ocean\nD. Arctic Ocean:  ")

question_3 = input("3. How much players does a cricket team have?\nA. 8\nB. 14\nC. 10\nD. 11:  ")

question_4 = input("4. How many equal sides does an isosceles triangle have?\nA. 1\nB. 3\nC. 0\nD. 4  ")

question_5 = input("5. A Dodo is an endangered bird.\nA. True\nB. False:  ")

question_6 = input("6. An ostrich’s eye is bigger than its brain.\nA. True\nB. False:  ")

question_7 = input("7. Can you name the closest star to Earth?\nA. Moon\nB. Sun\nC. Mars\nD. Venus:  ")

question_8 = input("8. How many bones do sharks have?\nA. 0\nB. 1\nC. 2\nD. 3:  ")

question_9 = input("9. What kind of tree do acorns come from?\nA. Maple tree\nB. Palm tree\nC. Oak tree\nD. Cedar tree:  ")

question_10 = input("10. Which bird is the universal symbol of Peace?\nA. Pigeon\nB. Peacock\nC. Dove\nD. Pelican:  ")

print("This is a bonus question!!!")
time.sleep(0.5)

question_11 = input("What is the “Fear of Darkness” called?\nA. Nyctophobia\nB. Ablutophobia\nC. Ophidiophobia\nD. Arachnophobia:  ")

print("You are all done with the quiz.")
time.sleep(1)
print("Checking your score...")
time.sleep(1)


if question_1.lower() == "c":
  score = score + 1
if question_2.lower() == "b":
  score = score + 1
if question_3.lower() == "d":
    score = score + 1
if question_4.lower() == "d":
    score = score + 1
if question_5.lower() == "b":
    score = score + 1
if question_6.lower() == "a":
    score = score + 1
if question_7.lower() == "b":
    score = score + 1
if question_8.lower() == "a":
    score = score + 1
if question_9.lower() == "c":
    score = score + 1
if question_10.lower() == "c":
    score = score + 1
if question_11.lower() == "a":
    score = score + 1

print("Your score has been calculated.")
print(score, "/11 is your final score.")