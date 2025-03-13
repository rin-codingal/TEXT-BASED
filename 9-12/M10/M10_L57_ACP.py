# Program to print he Recurrence relation of the below 2 recursive functions 
def func1(n):
  if n > 0 :
      return
  
  for i in range (0,n+1):
      print("tes1")

  func1(n/2)
  func1(n/3)
  

def func2(n):
  if n <= 1 :
      return
  
  print("test2")

  func2(n-1)

# Printing the recurrence relations
print("For first function : ")
print("T(n) = T(n/2) + T(n/3) + N")
print(func1(5))

print()
print()

print("For second function : ")
print("T(n) = T(n-1) + 1")
print(func2(5))