my_tuple = () #empty tuple
print(my_tuple)
print()

# Tuple having integers
my_tuple = (1, 2, 3)
print("tuple with integers value : ",my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4) #integer, string, float
print("tuple with mixed datatype : ",my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) # tuple consisting of string, list, and another tuple
print("nested tuple : ",my_tuple)
print()

# Accessing tuple elements using indexing
my_tuple = ('b','e','a','u','t','y')
print(my_tuple[0])   
print(my_tuple[5]) 
print()  

# Iterating through tuple
for letter in (my_tuple):
    print("Hello", letter)