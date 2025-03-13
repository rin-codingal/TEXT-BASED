def take_input():
    number = int(input("Enter any number to be check : "))
    if number >= 0:
        print("Number +ve")
        take_input()
    else:
        print("Number -ve")


take_input()