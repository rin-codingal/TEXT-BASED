#calculate space complexity of the recursive function
def sum(n): 
    return n*(n+1)/2

def arraySum(a): #Space complexity: θ(1), Auxiliary space = θ(1)
    sum = 0
    for i in a:
        sum = sum + i

    return sum

def sumn(n): #Space complexity: θ(n), Auxiliary space = θ(1)
    if n <= 0:
        return
    
    x = n + sumn(n-1)
    
    return x

print(sum(5))
print()

myArray = [4, 7, 12, 23]
print(arraySum(myArray))
print()

print(sumn(5))