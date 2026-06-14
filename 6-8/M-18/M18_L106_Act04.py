#Ask user to enter a number
Number = int(input(" Please Enter any Number: "))
Sum = 0 #initialise
Temp = Number 

while(Temp > 0): #using while loop
    Factorial = 1   # fact variable with 1  
    #intialize with 1  
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i # Find factorial of each number  
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print() 
print("Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)