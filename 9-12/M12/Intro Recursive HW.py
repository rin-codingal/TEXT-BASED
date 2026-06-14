# Function 1

def fac(n):
    if (n == 1 or n == 0):
        return 1
    print()
    return n * fac(n-1)

# Function 2

def print1to10(n):
    if (n > 10):
        return
    print(n)
    print1to10(n + 1)

number = int(input("Enter any Number to be Check : "))

func1 = fac(number)
func2 = print1to10(number)

print()
print(f"--> fac({number}) has a time complexity of 0({number})")
print(f"--> print1to10({number}) has a time complexity of 0(1), assuming n = {number} starts in the range 1 < n < 10")
print()