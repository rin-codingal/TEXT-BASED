# write in file using with()function
with open("4-5/M-23/sample-2.txt", 'w') as file:
  file.write("Hi! I am Lucian and I'm 3 years old.")
file.close()

# split file into words
with open("4-5/M-23/sample-2.txt", 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

