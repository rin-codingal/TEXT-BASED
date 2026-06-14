fruit_List = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']
list_size = len(fruit_List)

print("Length of list: ",list_size)
print("First Element: ",fruit_List[0])
print("Last Element: ",fruit_List[-1])

#add papaya on the last element
fruit_List.append('Papaya')
print("Updated List after adding papaya:", fruit_List)
print()

#add strawberry between guava and mango
fruit_List.insert(2,"strawberry") #number 2 is the index number (position)
print("Updated List after adding strawberry:", fruit_List)
print()

#remove guava
fruit_List.remove('Guava')
print("Updated List after removing guava:", fruit_List)
print()

#remove element index 1
fruit_List.pop(1)
print("Updated List after removing element on index 1:", fruit_List)
print()

#sorting list
fruit_List.sort()
print("Sorted List:", fruit_List)
print()

#reverse list
fruit_List.reverse()
print("Reversed List :", fruit_List)
print()

print("Multiplication on List :", fruit_List*2)
print()

fruit_List = fruit_List[:4]
print("Sliced List :", fruit_List)
print()

fruit_List.clear()
print("Updated List :", fruit_List)