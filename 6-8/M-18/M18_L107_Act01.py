print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))

for i in range(n): #outer loop to handle number of rows  
    for j in range(i+1): #inner loop to handle number of columns      
        print("* ", end="") #display result
        
    print()