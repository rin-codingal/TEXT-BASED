# Find the longest consecutive 1's in binary representation of a number

def max1(number):
    count = 0

    # Count the number of iterations to reach number = 0.
    while (number!=0):  
        number = (number & (number << 1)) # This operation reduces length of every sequence of 1s by one
        count=count+1
        
    return count

number = int(input("Enter your number : "))
print("Longest consecutive 1's length : ",max1(number))
