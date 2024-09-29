# Binary to decimal conversion
def binaryToDecimal(binary):
    decimal = 0
    i = 0

    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        
        i += 1

    print("Decimal number of",binary,":",decimal)   
     

binary = int(input("Enter your Binary: "))

binaryToDecimal(binary)
