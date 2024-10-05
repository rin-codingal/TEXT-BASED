def powerOf4(n):     
    count = 0
     
    # If only 1 set bit exists
    if (n & (~(n & (n - 1)))):         
        # Count 0 bits before set bit
        while(n > 1):
            n >>= 1
            count += 1
         
        # If count is even return true else false
        if(count % 2 == 0):
            return True
        else:
            return False
 
 
numb = int(input("Enter your number : "))

if(powerOf4(numb)):
    print(f"{numb} is a power of 4")
else:
    print(f"{numb} is not a power of 4")
