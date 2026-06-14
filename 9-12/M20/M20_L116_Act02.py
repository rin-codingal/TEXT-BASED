def q1():
    print("What do we call the first layer of this neural network?")
    a1 = input("Enter your answer : ")
    a1 = a1.lower()

    if a1=='input layer':
        s = 1
    else:
        s=0
    return s

def q2():
    print("How many number of neurons can be there in the first layer of this neural network?")
    a2 = int(input("Enter your answer : "))

    if a2==8:
        s = 1
    else:
        s=0
    return s

def q3():
    print("How many hidden layers are present in this neural network?")
    a3 = int(input("Enter your answer : "))

    if a3==3:
        s = 1
    else:
        s=0
    return s

def q4():
    print("There can be any number of neurons in the hidden layer of this neural network. True or False?")
    a4 = input("Enter your answer : ")
    a4 = a4.lower()

    if a4=="true":
        s = 1
    else:
        s=0
    return s

def q5():
    print("What do we call the last layer of this neural network?")
    a5 = input("Enter your answer : ")
    a5 = a5.lower()

    if a5=="output layer":
        s = 1
    else:
        s=0
    return s

def q6():
    print("How many number of neurons can be there in the last layer of this neural network?")
    a6 = int(input("Enter your answer : "))

    if a6==1:
        s = 1
    else:
        s=0
    return s

score = 0
score = score + q1()
print()

score = score + q2()
print()

score = score + q3()
print()

score = score + q4()
print()

score = score + q5()
print()

score = score + q6()
print()

print(f"your score is {score}")
print()