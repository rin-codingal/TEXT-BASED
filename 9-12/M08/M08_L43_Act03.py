def convert(my_list):
	result = {}
	for item in my_list:
		result[item[0]] = item[1:]
	return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("Original list of Students:")
print(students)
print()

print("Converted  lists to a dictionary:")
print(convert(students))