# write in file using with()function
with open('test6.txt', 'w') as file:
  file.write("Hi! I am Nurinn and I'm from Indonesia.")
file.close()

# split file into words
with open('test6.txt', 'r') as file:
  data = file.readlines()

  print("Words in this file are:")

  for line in data:
    word = line.split()
    print (word)
file.close()