def find_prob(a,b):
	if a==1:
		prob_a = 0.2
		if b==1:
			prob_bga = 0.85
		elif b==2:
			prob_bga = 0.15
		else:
			print("Invalid Choice")
			
		prob_a_and_b = prob_a * prob_bga
		
		print(f"Probability of b given a: {prob_bga}")
		print(f"Probability of both the events occuring: {prob_a_and_b}")

	elif a==2:
		prob_a = 0.8
		if b==1:
			prob_bga = 0.02
		elif b==2:
			prob_bga = 0.98
		else:
			print("Invalid Choice")
			
		prob_a_and_b = prob_a * prob_bga
		
		print(f"Probability of b given a: {prob_bga}")
		print(f"Probability of both the events occuring: {prob_a_and_b}")

	else:
		print("Invalid Choice")

print("Let's calculate probability.")

print("Person has step throat?")
print("1. Yes")
print("2. No")
print()

a = int(input("Enter your choice (1/2): "))

print("Person has tested positive?")
print("1. Yes")
print("2. No")
print()

b = int(input("Enter your choice (1/2): "))
print()

print("Probabilities for event a and b:")
find_prob(a,b)
print()
