def prob_a_and_b(a, b, total):
	# probability of event 1st orange ball
	prob_a = a/total

	# probability of event 2nd blue ball
	prob_b = b/(total-1)

	# probability of intersection of events a and b
	prob_A_and_B = prob_a * prob_b

	# add return statement here
	return round(prob_A_and_B, 3)
  

# taking input for total number of orange and blue balls
orange = int(input("Enter number of orange balls: "))
blue = int(input("Enter number of blue balls: "))

total = orange + blue


prob = prob_a_and_b(orange, blue, total)
print(f"Probability of Getting 1st orange and 2nd blue ball: {prob}")
print()