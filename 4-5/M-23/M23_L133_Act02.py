# open the file in read mode
file_read = open("4-5/M-23/hello.txt",'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open("4-5/M-23/hello.txt", 'w')

# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am replacing the content ")
file_write.close()

# open the file in append mode
file_append = open("4-5/M-23/hello.txt", 'a')

# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("\nHello tralala")
file_append.close()