# Program to copy odd lines of one file to another

file1 = open('test3.txt', 'r') # open file in read mode

file2 = open('test5.txt', 'w') # open other file in write mode

# read the content of the file line by line
cont = file1.readlines()
type(cont)

for i in range(1, len(cont)+1):
	if(i % 2 != 0):
		file2.write(cont[i-1])
	else:
		pass

# close the file
file2.close()

# open file in read mode
file2 = open('test5.txt', 'r')

# read the content of the file
cont1 = file2.read()

# print the content of the file
print(cont1)

# close all files
file1.close()
file2.close()