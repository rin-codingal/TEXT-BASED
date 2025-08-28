# set of integers
my_set = {1, 2, 3}
print(my_set)
print()

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
print()

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
print()

# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)
print()

#remove a number from a set
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
print()

num_set.pop()
print("After removing the last element from the said set:")
print(num_set)