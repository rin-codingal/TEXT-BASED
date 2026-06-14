def incdec(n,num):
    # Base case to return value when we reach our limit
    if(n<1 or n>num):
        return
    
    # Print decreasing first
    print(f"decreasing number = {n}")

    incdec(n-1,num)
    print()

    # Print increasing order 
    print(f"increasing number = {n}")
    
 
n = int(input("Enter any number n : "))
incdec(n,n)