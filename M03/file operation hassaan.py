file =open("sample4.txt","r")
print(file.read()) #it is to read the entire content
file.close()

print()

#reading the first 10 chracters of sample4.txt
file =open("sample4.txt","r")
print("the first 10 chracters of sample4")
print(file.read(10))
file.close()

print()

#reading the first line of sample4
file =open("sample4.txt","r")
print("Reading the first line of sample4")
print(file.readline())
file.close()

print()

#reading the first three liness of sample4
file =open("sample4.txt","r")
print("Reading the first three lines of sample4")
print(file.readline())
print(file.readline())
print(file.readline())

print()

file =open("sample4.txt","r")
print(file.read()) #it is to read the entire content
file.close()

print()

#reading the first 10 chracters of sample4.txt
file =open("sample4.txt","r")
print("the first 10 chracters of sample4")
print(file.read(10))
file.close()

print()

#reading the first line of sample4
file =open("sample4.txt","r")
print("Reading the first line of sample4")
print(file.readline())
file.close()

print()

#reading the first three liness of sample4
file =open("sample4.txt","r")
print("Reading the first three lines of sample4")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#opening the file in the append mode
file =open("sample4.txt","a")
file.write("\ntoday is november the second ")
file.close()