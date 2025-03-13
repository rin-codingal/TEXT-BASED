#First approach
def fun1(n):
    print("iteration for first approach = 1")
    return n*(n+1)/2

print(fun1(5))
print()

#second approach
def fun2(n):
    sum = 0
    iteration = 0
    for i in range(1,n+1):
        iteration += 1
        sum+=i

    print("iteration for second approach = ",iteration)

    return sum

print(fun2(5))
print()

#third approach
def fun3(n):
    sum=0
    iteration = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            iteration += 1
            sum+=1
            
    print("iteration for third approach = ",iteration)

    return sum

print(fun3(5))