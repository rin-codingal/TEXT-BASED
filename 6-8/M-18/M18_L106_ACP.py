"""def converttobinary(n):
  if n > 1:
    converttobinary(n//2 ) #floor division to get result without decimal value
    
  print(n%2 , end=" " ) # printing the remainder of division by 2

print()
dec = int(input("enter a number to find it's binary value: "))

converttobinary(dec)
print()
print()"""

dec = int(input("enter a number to find it's binary value: "))

#using loop
binary_result = ""
while dec > 0:
  remainder = dec % 2
  dec = dec // 2 
  binary_result = str(remainder) + binary_result

print(binary_result)
  