#create a new file
new_file = open("9-12/M09/drinks.txt", "x")
new_file.close()

#check if a file exists 
import os
print("=== Checking if my_file exists or not ===")

if os.path.exists("9-12/M09/my_file.txt"):
  os.remove("9-12/M09/my_file.txt")
else:
  print("The file does not exist")

#create a new if it doesn't exist
my_file = open("9-12/M09/fileku.txt", "w")
my_file.write("Hi! I am Nurinn and I'm from Indonesia.")
my_file.close()

#delete file named test7 if it exist
if os.path.exists("9-12/M09/test7.txt"):
   os.remove("9-12/M09/test7.txt")

#delete the folder 'L100' if it exist
if os.path.exists("9-12/M09/L100"):
   os.rmdir("9-12/M09/L100")