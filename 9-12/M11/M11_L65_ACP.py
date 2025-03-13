# Find the longest consecutive 1's in binary representation of a number
def max1(n):
    count = 0

    # Count the number of iterations to reach number = 0.
    while (n!=0):  
        n = (n & (n << 1)) # This operation reduces length of every sequence of 1s by one
        count=count+1
        
    return count

numb = int(input("Enter your number : "))
print(f"Longest consecutive 1's length : {max1(numb)}")
