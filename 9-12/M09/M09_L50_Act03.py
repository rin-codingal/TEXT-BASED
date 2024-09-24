# Program to remove lines starting with any prefix

file1 = open("test3.txt","r")
file2 = open("test4.txt","w")

# reading each line from original text file
for line in file1.readlines():		
	if not (line.startswith('Reading')):	# reading all lines that do not begin with "Reading"		
		print(line) # printing those lines
		file2.write(line) # storing only those lines that do not begin with "Reading"

# close and save the files
file2.close()
file1.close()