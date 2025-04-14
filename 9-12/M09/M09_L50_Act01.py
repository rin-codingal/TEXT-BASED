#open file and read its contents
file = open("9-12/M09/test2.txt","r")
print(file.read())
print()

file.close()

#open file and read its beginning 8 characters
file = open("9-12/M09/test2.txt","r")

print("Read in parts")
print(file.read(8))
file.close()

print()












#append your name and age in the file
file = open("test2.txt","a")
file.write(" \nHi! I am Nurinn and I am from Indonesia.")
file.close()

