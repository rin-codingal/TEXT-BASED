#open file and read its contents
file = open("4-5/M-23/sample.txt",'r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open("4-5/M-23/sample.txt",'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open("4-5/M-23/sample.txt",'a')
file.write(" Hello.. my name is Amazing.")
file.close()

