def divide(ourdividend, ourDivisor):
    sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1);
    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourdividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i

    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber

x = int(input("Enter x (dividend) for x/y: "))
y = int(input("Enter y (divisor) for x/y: "))

print(f"Result of {x}/{y} is {divide(x, y)}")