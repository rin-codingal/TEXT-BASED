#Roman to Integer
def roman_to_int(a):
    #dictionary of roman unit towith integer equivalent values
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    res=0 #result integer

    for i in range(len(a)):
        if i+1<len(a) and (roman[a[i]] < roman[a[i+1]]):
            res-=roman[a[i]]
        else:
            res+=roman[a[i]]

    return res

a=input("enter a roman numeral: ")
print(f"integer form of {a} is = {roman_to_int(a)}")