import random 
import time

number=random.randint(1, 100) 

def intro():
	print("May I ask you for your name?")
	
	# declaring name variable global so it can be accessed outside the function
	global name
	name = input() #asks for the name
	print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 100")
	
	if(number%2==0):
		x = "even"
	else:
		x = "odd"
		
	print()
	print(f"This is an {x} number")
	time.sleep(.5)
	
	print("Go ahead. Guess!")

def pick():
	guessesTaken = 0

	#if the number of guesses is less than 6
	while guessesTaken < 6:
		time.sleep(.25)

		#inserts the place to enter guess
		enter=input("Guess: ") 

		#check if a number was entered
		try: 
			guess = int(enter)    

			if guess<=100 and guess>=1: 
				guessesTaken = guessesTaken + 1 #adds one guess each time the player is wrong

				if guessesTaken<6:
					if guess < number:
						print("The guess of the number that you have entered is too low")

					if guess > number:
						print("The guess of the number that you have entered is too high")

					if guess != number:
						time.sleep(.5)
						print("Try Again!")

					if guess == number:
						break 
			
			if guess > 100 or guess < 1: 
				print("That number isn't in the range!")
				time.sleep(.25)
				print("Please enter a number between 1 and 100")

		except: #if a number wasn't entered
			print(f"I don't think that {enter} is a number. Sorry")
			
	if guess == number:
		guessesTaken = str(guessesTaken)
		print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")

	if guess != number:
		print(f"Nope. The number I was thinking of was {number}")

playagain="yes"

while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("Do you want to play again?")
	playagain=input()