#create a new file
new_file = open("4-5/M-23/new-sample.txt", 'x')
new_file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("4-5/M-23/sample.txt"):
  os.remove("4-5/M-23/sample.txt")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("4-5/M-23/sample.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()

#delete file named sample
os.remove("4-5/M-23/sample.txt")

#delete the folder
os.rmdir('Folder')

