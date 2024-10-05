def FirstSetBit(number): # function to find the rightmost set bit 
    # Position and mask variable
    position = 1
    mask = 1
 
    while (not(number & mask)) : 
        # left shift mask to check next bit
        mask = mask << 1
        position += 1
     
    return position
 
number = int(input("Enter a number : "))

print(f"Position of the first set bit : {FirstSetBit(number)}")
