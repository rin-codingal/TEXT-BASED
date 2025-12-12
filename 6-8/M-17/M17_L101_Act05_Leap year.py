year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year")

    if year % 100 == 0:
        print("and it's a century year too")
    else:
        print("and it's not century year")

else:
    print(f"{year} is not a leap year")