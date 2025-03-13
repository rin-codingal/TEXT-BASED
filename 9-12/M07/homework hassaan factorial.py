def factorial(n):
    if n==1:
        return n
    else :
        return n*factorial(n-1) #recursive funcation which calls it's self repetivli

num=int(input("enter a number to find it's factorial= "))

#check if the number is negative
if num<0:
    print("sorry factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print(f"the factorial of {num} is {factorial(num)}")
    