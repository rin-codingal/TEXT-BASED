try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    result = num1 /num2
    print("The result of the division is",result)
    print("The second result is",result2)

except ZeroDivisionError:
    print("No number can be divided by zero.")

except SyntaxError:
    print("The numbers must be seperated by a comma:")

except ValueError:
    print("Only numeric values are allowed to be entered.")

except NameError as ex:
    print("A name error occured as:",ex)

except:
    print("An unexpected error occured.")

else:
    print("No error occured!")

finally:
    print("I would be executed no matter what.")