fruits = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(fruits))
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

fruits.append('Papaya')
print("Updated List :", fruits)

fruits.remove('Guava')
print("Updated List :", fruits)

fruits.sort()
print("Sorted List:", fruits)

fruits.pop(1)
print("Updated List :", fruits)

fruits.reverse()
print("Reversed List :", fruits)

print("Multiplication on List :", fruits*2)

fruits = fruits[:4]
print("Sliced List :", fruits)

fruits.clear()
print("Updated List :", fruits)