# write in file using with()function
with open('test6.txt', 'w') as file:
  file.write("Hello, I am Nurinn and I'm from Indonesia.")
file.close()

# split file into words
with open('test6.txt', 'r') as file:
  data = file.readlines()

  print("Words in this file are:")

  for line in data:
    word = line.split()
    print (word)
file.close()

#create a new file
new_file = open("New_File.txt", "x")
new_file.close()

#check if a file exists 
import os
print("=== Checking if my_file exists or not ===")

if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("The file does not exist")

#create a new if it doesn't exist
my_file = open("my_file.txt", "w")
my_file.write("Hello, I am Nurinn and I'm from Indonesia.")
my_file.close()

#delete file named test7 if it exist
if os.path.exists("test7.txt"):
   os.remove("test7.txt")