#read first line of file
file = open("test2.txt","r")
print("=== Reading first line ===")
print(file.readline())
file.close()

print()

#read first 2 lines of file
file = open("test2.txt","r")
print("=== Reading multiple lines ===")
print(file.readline())
print(file.readline())
file.close()

print()

#looping through all the lines of the file
file = open("test2.txt","r")
print("=== Looping through the lines ===")

for line in file:
  print(line)
file.close()