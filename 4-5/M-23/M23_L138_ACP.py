import random
import time
import sys

print("Welcome to the dice simulator.")

roll = True

def dice():
  dice_val = random.randint(1, 6)
  print("The dice value is ",dice_val)

while roll == True:
  roll_dice = input("Do you want to roll the dice? (Yes/No): ")

  if roll_dice.lower() == "yes":
    print("The dice is rolling...")
    time.sleep(2)
    dice()

  elif roll_dice.lower() == "no":
    roll = False
    sys.exit("Thank you for visiting\nSee you next time\nExiting simulator... ")