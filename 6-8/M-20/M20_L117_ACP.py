test_dict = {'Codingal' : 3, 
             'is' : 2, 
             'best' : 2, 
             'for' : 2, 
             'Coding' : 1}
  
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
  
# Initialize value 
K = int(input("Enter the number to check frequency in Test dictionary : "))
  
# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
      
# printing result 
print("Frequency of ",K," is : ",res)