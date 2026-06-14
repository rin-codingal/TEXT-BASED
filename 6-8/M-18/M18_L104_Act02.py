#Input a word or sentence
word = input("Please enter your own word or sentence : ")

reverse = ""

#loop for printing in reverse 
for i in word:
    reverse = i + reverse

print() 

print("The Original String = ", word)
print("The Reversed String = ", reverse)