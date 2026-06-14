# Program to append contents of file in another file

# entering the file names
firstfile = input("Enter the name of first file: ")
secondfile = input("Enter the name of second file: ")

# opening both files in read only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

# printing the contens of the file before appending
print("CONTENT OF THE FIRST FILE BEFORE APPENDING: -\n", f1.read())
print()

print("CONTENT OF THE SECOND FILE BEFORE APPENDING: -\n", f2.read())

# closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# appending the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

print()
print("=======================================")
print()

# printing the contents of the files after appendng
print("CONTENT OF THE FIRST FILE AFTER APPENDING: -\n", f1.read())
print()

print("CONTENT OF THE SECOND FILE AFTER APPENDING: -\n", f2.read())

# closing the files
f1.close()
f2.close()
