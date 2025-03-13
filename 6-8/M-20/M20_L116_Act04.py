test_list = [(1, 4, 5), (7, 8), (2, 4, 10)] 
 
# printing original list 
print("The original list is : ",test_list) 
 
# Average of tuple list 
# Using loops 
sum = 0
for sub in test_list: 
    for i in sub: 
        sum = sum + i 
res = sum / len(test_list) 
 
# printing result 
print("The mean of tuple list is : ",res) 