def  checkIfSame(n1,n2):
    if((n1 ^ n2)!= 0):
        print("numbers are not equal")
    else:
        print("both numbers are equal")

fnum = int(input("Enter first number to compare: "))
snum = int(input("Enter second number to compare: "))

checkIfSame(fnum,snum)
