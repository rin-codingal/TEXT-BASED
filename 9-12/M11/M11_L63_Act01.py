def  checkIfSame(number1,number2):
    if((number1 ^ number2)!= 0):
        print("numbers are not equal")
    else:
        print("both numbers are equal")

fnum = int(input("Enter first number to compare: "))
snum = int(input("Enter second number to compare: "))
checkIfSame(fnum,snum)
