# Program to print the time complexity of the given function
def timeComplex(n):   
    for i in range(0,n+1): # first loop
        print("First Loop")
    
    print()

    j=1
    while(j<=n+1): # second loop
        print("Second Loop ",j)
        j=j*2

    print()
    
    for i in range(0,100): # third loop
        print("Third loop")

print("Function above will take time :")
print(" O(N) +  O(log N) + O(1)")
print()

timeComplex(5)