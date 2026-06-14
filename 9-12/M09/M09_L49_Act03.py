# Program to count number of lines in this file
# Opening a file
file = open("9-12/M09/test2.txt","r")
Counter = 0

# Reading from file
content = file.read()

# splitting content into lines
# and storing them in a list
content_list = content.split("\n")

for i in content_list:
	if i:
		Counter += 1
		
print("This is the number of lines in the file:", Counter)
