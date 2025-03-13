def a_and_b(a, b):

	if a==1:
		prob_student = 0.3
		if b ==1:
			prob_dining = 0.75
		else:
			prob_dining = 0.25
		print(f"Probability of freshman eating in the dining hall: {prob_dining}")

	if a==2:
		prob_student=0.7
		if b==1:
			prob_dining = 0.6
		else:
			prob_dining = 0.4
		print(f"Probability of getting a freshman eating in the dining hall: {prob_dining}")
	
	prob_a_and_b = prob_student * prob_dining
	
	return round(prob_a_and_b, 3)

print("Check the probability of any event occuring.")
print("Is the student a Freshman?")
print("1. Yes")
print("2. No")
print()

a = int(input("Enter your choice (1/2): "))

print("Is student eating in dining hall?")

print("1. Yes")
print("2. No")
print()

b = int(input("Enter your choice (1/2): "))

print(f"Here is the probability of both the events occuring : {a_and_b(a, b)}")