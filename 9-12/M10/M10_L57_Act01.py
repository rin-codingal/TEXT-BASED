#calculate time complexity of the recursive function
def timeComplexRecur(n):
    if n < 0:
        return
    
    print("test")

    if n >= 2:
        timeComplexRecur(n/2)
        timeComplexRecur(n/2)

timeComplexRecur(8)