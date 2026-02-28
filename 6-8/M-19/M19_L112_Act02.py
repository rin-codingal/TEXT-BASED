try:
  num1, num2 = eval(input("Enter two numbers separated by comma: "))
  result = num1/num2

  #code = "if True print('Yes')"
  #exec(code)
  
  print("Result is : ", result)
  print("Result is : ", result2) # this is name error

except ZeroDivisionError:
  print("Division by zero is not allowed")

except SyntaxError:
  print("syntax error")

except ValueError:
  print("Please enter numerical value")

except NameError as ex:
  print("The name error exception is ",ex)
  
except:
  print("Some error occurred")

else:
  print("no exception or no error")

finally:
  print("I will execute no matter what happens")