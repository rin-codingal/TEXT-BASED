def find_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i, n):
            substrings.append(s[i:j+1])
    
    return substrings

# Taking input from the user
string = input("Enter string: ")

# Getting all substrings
result = find_substrings(string)

# Printing each substring
for sub in result:
    print(sub)