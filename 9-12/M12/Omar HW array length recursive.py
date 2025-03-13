def recursive_length(my_list):
    if not my_list:
        return 0
    return 1 + recursive_length(my_list[1:])

my_array = [1, 2, 234, 234, 745, 3, 6, 653]
print("Length of array:", recursive_length(my_array))