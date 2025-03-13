import random

Dependence= "We pick out two cards from a standard deck of 52 cards without replacement. Event A is that we pick an Ace on the first draw. Event B is that we pick an Ace on the second draw."

mutually_exclusive= "Suppose we flip a coin ten times. Event A is that we flip all heads on the first five flips. Event B is that we flip all heads on the second five flips." 

notmutuallyexclusive= "We roll a dice once. Event A is rolling an odd number. Event B is rolling a number greater than four."

independent = "We have a bag of five marbles: three are green and two are blue. Suppose that we pick one marble from the bag. Event A is that the marble is green. Event B is that the marble is blue."

event_lst = [Dependence, mutually_exclusive,notmutuallyexclusive,independent]

def guess_the_type(event):  
    print(event)
    print()
    
    print("Guess whether this is a:")
    print("1. dependent")
    print("2. independent")
    print("3. mutually exclusive")
    print("4. not mutually exclusive event")
    print()

    

    answer = int(input("Enter your answer : "))
    if event == Dependence:
        if answer == 1:
            print("You guessed it right!")
            print()
            print()
            return "correct"
        else:
            print("Your answer is wrong")
            print()
            print()
            return "wrong"
        
    if event == mutually_exclusive:
        if answer == 3:
            print("You guessed it right!")
            print()
            print()
            return "correct"
        else:
            print("Your answer is wrong")
            print()
            print()
            return "wrong"
        
    if event == notmutuallyexclusive:
        if answer == 4:
            print("You guessed it right!")
            print()
            print()
            return "correct"
        else:
            print("Your answer is wrong")
            print()
            print()
            return "wrong"
        
    if event == independent:
        if answer == 2:
            print("You guessed it right!")
            print()
            print()
            return "correct"

        else:
            print("Your answer is wrong")
            print()
            print()
            return "wrong"
        
firstanswer=guess_the_type(Dependence)
secondanswer=guess_the_type(mutually_exclusive)
thirdanswer=guess_the_type(notmutuallyexclusive)
fourthanswer=guess_the_type(independent)

if firstanswer=="correct" and secondanswer=="correct" and thirdanswer=="correct" and fourthanswer=="correct":
      print("You have guessed all the events correctly!")