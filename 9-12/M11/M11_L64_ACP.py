def powerOf8(n):
	bitPosition = 0
	mask = 1
	
	while (bitPosition <= 63):
		mask <<= bitPosition

		# If only set bit in n
		# is at position i
		if (mask == n):
			return True
		
		bitPosition += 3
		mask = 1

	return False

numb = int(input("Enter your number : "))

if (powerOf8(numb)):
	print(f"Yes {numb} is power of 8")
else:
	print(f"No {numb} is not power of 8")


