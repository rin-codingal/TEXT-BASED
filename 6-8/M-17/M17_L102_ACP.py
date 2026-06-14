c = input("Enter a Character: ")

if len(c) == 0:
    print("Invalid Input!")
else:
    if c >= 'a' and c <= 'z':
        print(f"{c} is an alphabet.")
    elif c >= 'A' and c <= 'Z':
        print(f"{c} is an alphabet.")
    else:
        print(f"{c} is not an alphabet!")