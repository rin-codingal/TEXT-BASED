a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print(f"{avg} is higher than {a}, {b}, {c}")
elif avg > a and avg > b:
    print(f"{avg} is higher than {a}, {b}")
elif avg > a and avg > c:
    print(f"{avg} is higher than {a}, {c}")
elif avg > b and avg > c:
    print(f"{avg} is higher than {b}, {c}")
elif avg > a:
    print(f"{avg} is just higher than {a}")
elif avg > b:
    print(f"{avg} is just higher than {b}")
elif avg > c:
    print(f"{avg} is just higher than {c}")
else:
  print("invalid input")