def sym_difference(set1, set2):
	print("Original sets:")
	print(set1)
	print(set2)
	print()
	
	result = set1.symmetric_difference(set2)
	print("Symmetric difference of setc1 - setc2:")
	return result

seta1 = set(["green", "blue"])
seta2 = set(["blue", "yellow"])
resulta = sym_difference(seta1, seta2)

print("Result of A Sets:")
print(resulta)
print()