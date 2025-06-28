rows = int(input("Please Enter the total Number of Rows  : "))
number = 1 #initialise by 1

print("Floyd's Triangle") 

for i in range(1, rows + 1): # representing rows
    for j in range(1, i + 1): # representing columns
        print(number, end='  ')
        number = number + 1

    print()