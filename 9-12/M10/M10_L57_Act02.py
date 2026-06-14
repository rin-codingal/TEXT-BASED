#calculate space complexity of the recursive function
def sum(n): 
    return n*(n+1)//2

def arraySum(a): #Space complexity: θ(1), Auxiliary space = θ(1)
    sum = 0
    for i in a:
        sum = sum + i

    return sum

def sumn(n): #Space complexity: θ(n), Auxiliary space = θ(1)
    
    if n <= 0:
        result = 0
    else:    
        #print("executed")
        #print(f"number = {n}")
        #print()
        result = n + sumn(n-1)
    #print(f"result = {result}")

    return result
    
    
x = 5
print(f"the sum of the first {x} number is = {sum(x)}")
print()

myArray = [4, 7, 12, 23]
print(f"the sum of array elements is = {arraySum(myArray)}")
print()

y = sumn(x)
print(f"the sum of the first {x} number using recursive is = {y}")