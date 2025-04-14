L = [4, 5, 1, 2, 9, 7, 10, 8]

print("Original List :", L)
print()
  
count = 0
  
for i in L:
    count = count + i
      
avg = count/len(L)
  
print("sum = ", count)
print("average = ", avg)
print()

# Sorting the elements of the list
L.sort()
print("sorted array in ascending order: ",L)
print()

# printing the first element
print("Smallest element is:", L[0])
print()

# printing the last element
print("Largest element is:", L[-1])