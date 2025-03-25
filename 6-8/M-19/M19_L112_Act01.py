try : 
  num = int(input("Enter your number : "))
  print("the number entered is: ",num)

except ValueError as e: #using value error
  print("Exception: ",e)

print("I am outside the try-except block") #always executed and displayed the message
print()