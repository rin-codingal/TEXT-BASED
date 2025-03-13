import numpy as np

# create n sided "dice"
dice_sides = int(input("enter number of sides for dice (6/12) : "))
dice = range(1, dice_sides)

# set number of rolls
num_rolls = int(input("Enter number of times you want to roll the dice : "))

# roll the "dice" the set amount of times
results = np.random.choice(dice, size = num_rolls, replace = True)
print(results)