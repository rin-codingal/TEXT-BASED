my_set = {1,2,2,3,4,4,4}
print("Set :", my_set)

print()
myset2 = {"mango", "strawberry", "mango"}
print(myset2)

my_set.add(5)
print("Updated Set:", my_set)
print()

set1 = my_set
set2 = {2,4,4,6}

print("Set 1", set1)
print("Set 2", set2)
print()

print("Difference")
print(set1.difference(set2))
print()

print("Symmeteric Difference")
print(set1.symmetric_difference(set2))