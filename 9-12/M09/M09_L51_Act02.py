#create a new file
new_file = open("drinks.txt", "x")
new_file.close()

#check if a file exists 
import os
print("=== Checking if my_file exists or not ===")

if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("The file does not exist")

#create a new if it doesn't exist
my_file = open("fileku.txt", "w")
my_file.write("Hi! I am Nurinn and I'm from Indonesia.")
my_file.close()

#delete file named test7 if it exist
if os.path.exists("test7.txt"):
   os.remove("test7.txt")

#delete the folder if it exist
if os.path.exists("Folder"):
   os.rmdir("Folder")