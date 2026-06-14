# open the file in read mode
file_read = open("9-12/M09/test2.txt", "r")
print("File in Read Mode -")
print(file_read.read())
file_read.close()

print()

# open the file in write mode to replace the original content with new sentence
file_write = open("9-12/M09/test2.txt", "w")

# write in the file 
file_write.write("File in write mode ....")
file_write.write("\nHello, sunshine ")
file_write.close()

# open the file in append mode to combine original sentence
# with new sentence
file_append = open("9-12/M09/test2.txt", "a")

# append in the file 
file_append.write("\n\nFile in append mode ....")
file_append.write("\nToday is a fine day")
file_append.close()
