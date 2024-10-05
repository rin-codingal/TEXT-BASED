def reverseBits(number) :
    reversed = 0
    
    while (number > 0) :         
        # Shift reversed number to left
        reversed = reversed << 1
         
        # Check if last bit is 0 or 1
		# If 1 add it using OR operator else leave 
        if (number & 1 == 1) :
            reversed = reversed ^ 1
         
        # Right shift the orignal number
        number = number >> 1
         
    return reversed
     
numb = int(input("Enter your number : "))
print(f"Number of reversed bits : {reverseBits(numb)}")