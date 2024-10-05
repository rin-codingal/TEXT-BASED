def swap(a,b):
    a = a^b
    b = a^b
    a = a^b

    print(f"After swapping with first method: a ={a} and b = {b}")

def swap2(a,b):
    a = (a&b)+(a|b)
    b = a+(~b)+1
    a = a+(~b)+1

    print(f"After swapping with second method: a ={a} and b = {b}")

a =10
b = 20
print("original number:")
print(f"a = {a}")
print(f"b = {b}")
print()

swap(a, b)
swap2(a, b)