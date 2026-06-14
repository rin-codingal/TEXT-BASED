import random

def dice_roll_exp():
	numbers = [1,2,3,4,5,6]

	result = random.choice(numbers)

	prob = numbers.count(6)/len(numbers)
	print(f"Probability of getting a 6 is: {prob}")

	if result == 6:
		return "Yeay! You got 6!"
	else:
		return "Oh, No! You didn't get a 6. Please, Roll Again."
		
res = dice_roll_exp()
print(res)	