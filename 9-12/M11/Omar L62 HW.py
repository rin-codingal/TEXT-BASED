def FirstSetBit(n):
    if n == 0:
        return 0
    position = 1
    while n & 1 == 0:
        n >>= 1
        position += 1
    return position

number = int(input("Enter number: "))
position = FirstSetBit(number)

if position == 0:
    print("No set bits found.")
else:
    print(f"Position of the first set bit: {position}")