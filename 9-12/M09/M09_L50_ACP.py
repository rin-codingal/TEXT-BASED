#open file and read its contents
file = open("test3.txt","r")
print("=== Read all of file's content ===")
print(file.read())
print()

file.close()

#open file and read its beginning 8 characters
file = open("test3.txt","r")

print("=== Read in parts=== ")
print(file.read(8))
file.close()

print()

#read first line of file
file = open("test3.txt","r")
print("=== Reading first line ===")

print(file.readline())
file.close()

print()

#read first 2 lines of file
file = open("test3.txt","r")
print("=== Reading multiple lines ===")
print(file.readline())
print(file.readline())
file.close()

print()

#looping through all the lines of the file
file = open("test3.txt","r")
print("=== Looping through the lines ===")

for line in file:
  print(line)
file.close()