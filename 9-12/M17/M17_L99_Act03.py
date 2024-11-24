RS = int(input("Enter number of red shirts: "))
BS = int(input("Enter number of blue shirts: "))
WS = int(input("Enter number of white shirts: "))
print()

total = RS + BS + WS

prob_a = BS/total
prob_b = RS/total

prob_bga = round(prob_b, 3)
prob_a_and_b = round(prob_a * prob_b, 3)

print(f"Probability that the second shirt is red given that the first shirt is blue: {prob_bga}")

print(f"Probability that the second shirt is red and the first shirt is blue: {prob_a_and_b}")
print()