test_list = [1, 4, 5, 6, 4, 5, 6, 5, 4]
 
print("The original list : " + str(test_list))
 
particular_value = 5
result = []
temp_list = []

for i in test_list:
    if i == particular_value:
        temp_list.append(i)
        result.append(temp_list)
        temp_list = []
    else:
        temp_list.append(i)

result.append(temp_list)
print("The list after splitting by a value : " + str(result))