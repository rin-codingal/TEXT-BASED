# Function to create list of square of numbers
def SquaredValues(beg, end):
	original_list = []
	# store all the values of square of numbers 
	# between given range in a list
	for i in range(beg, end):
		original_list.append(i**2)

	lst_even = []
	lst_odd = []

	# check and store odd and even squares in seperate lists
	for i in original_list:
		if i%2==0:
			lst_even.append(i)
		else:
			lst_odd.append(i)
	
	print("Here's a list of even squares within specified range", lst_even)
	print("Here's a list of odd squares within specified range", lst_odd)
	
beg = int(input("Enter starting range : "))
end = int(input("Enter end range : "))
SquaredValues(beg, end)


