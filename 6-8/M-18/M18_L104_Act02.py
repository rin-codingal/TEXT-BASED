#Input a word or sentence
string = input("Please enter your own String : ")

reverse = ""

#loop for printing in reverse 
for i in string:
    reverse = i + reverse

print() 

print("The Original String = ", string)
print("The Reversed String = ", reverse)