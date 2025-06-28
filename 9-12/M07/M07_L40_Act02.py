n = int(input("enter number of rows: "))

for i in range(0, n): #outer loops for row
	for j in range(0, i+1): #inner loops for column
		print("*", end=" ")

	print()

	