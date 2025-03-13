def numberOfBits(n):
    ones = 0
    zeroes= 0
    
    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeroes += 1

        n >>= 1

    print(f"Number of ones = {ones}")
    print(f"Number of zeroes = {zeroes}")


numb = int(input("Enter your number: "))
numberOfBits(numb)