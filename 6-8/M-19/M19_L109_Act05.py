def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


print("Binary of 5:", end=' ')
DecimalToBinary(5)
print()  

print("Binary of 23:", end=' ')
DecimalToBinary(23)
print()  

print("Binary of 5:", end=' ')
DecimalToBinary(5)
print()  
