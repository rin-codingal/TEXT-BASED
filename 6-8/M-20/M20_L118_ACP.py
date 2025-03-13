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
setb1 = set([1, 1, 2, 3, 4, 5])
setb2 = set([1, 5, 6, 7, 8, 9])

print("Result of A Sets")
print(sym_difference(seta1, seta2))
print()
print()

print("Result of B Sets")
print(sym_difference(setb1, setb2))