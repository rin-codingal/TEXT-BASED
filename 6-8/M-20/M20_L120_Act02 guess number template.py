import random 
import time

number=random.randint() 

def intro():
	print("")
	
	# declaring name variable global so it can be accessed outside the function
	global name
	name = input() #asks for the name
	print(f"{}, ")
	
	if(number%2==0):
		x = 
	else:
		x = 
		
	print()
	print(f" {} ")
	time.sleep(.5)
	
	print("")

def pick():
	guessesTaken = 

	#if the number of guesses is less than 6
	while guessesTaken < :
		time.sleep()

		#inserts the place to enter guess
		enter=input("") 

		#check if a number was entered
		try: 
			guess =     

			if guess<= and guess>=: 
				guessesTaken =  #adds one guess each time the player is wrong

				if guessesTaken<:
					if guess :
						print("The guess of the number that you have entered is too low")

					if guess :
						print("The guess of the number that you have entered is too high")

					if guess :
						time.sleep(.5)
						print("Try Again!")	

					if guess == number:
						break 
			
			if guess > or guess < : 
				print("")
				time.sleep(.25)
				print("Please enter a number between 1 and 100")

		except: #if a number wasn't entered
			print(f"I don't think that {enter} is a number. Sorry")
			
	if guess == number:
		guessesTaken = str(guessesTaken)
		print(f"")

	if guess != number:
		print(f"")

playagain="yes"

while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("")
	playagain=input()