fruit_List = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(fruit_List))
print("First Element:", fruit_List[0])
print("Last Element:", fruit_List[-1])

fruit_List.append('Papaya')
print("Updated List :", fruit_List)
print()

fruit_List.remove('Guava')
print("Updated List :", fruit_List)
print()

fruit_List.sort()
print("Sorted List:", fruit_List)
print()

fruit_List.pop(1)
print("Updated List :", fruit_List)
print()

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