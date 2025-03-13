try : 
  num = int(input("Enter your number : "))
  print("the number entered is: ",num)
except ValueError as ex:
  print("Exception: ",ex)


print("I am outside the try block")