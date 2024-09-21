# open the file in read mode
file_read = open('test2.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('test2.txt', 'w')

# write in the file 
file_write.write("\nFile in write mode ....")
file_write.write("Hello, sunshine ")
file_write.close()

# open the file in append mode
file_append = open('test2.txt', 'a')
# append in the file 
file_append.write("\nFile in append mode ....")
file_append.write("Hello, sunshine")
file_append.close()

