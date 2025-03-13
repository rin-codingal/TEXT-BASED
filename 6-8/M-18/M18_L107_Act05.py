rows = int(input("enter number of rows: "))
column = int(input("enter number of columns: "))
for i in range(1, rows, 2): #iterate for loop
    print((i * ".|.").center(column,"-")) #display output

print("WELCOME".center(column, "-"))

for i in range(rows-2, -1, -2):
    print((i * ".|.").center(column, "-"))    