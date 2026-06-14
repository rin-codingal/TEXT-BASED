RB = int(input("Enter number of red balls: "))
BB = int(input("Enter number of blue balls: "))
WB = int(input("Enter number of white balls: "))
print()

total = RB + BB + WB

prob_a = WB/total
prob_b = (WB-1)/(total-1)

prob_a_and_b = round(prob_a*prob_b, 3)

print(f"Probability that the second ball is white and the first shirt is also white: {prob_a_and_b}")
print()