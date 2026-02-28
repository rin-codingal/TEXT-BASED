# program to send if the number is power of 2 or not 


def checkifpower(n):
  # if n is less than equal to 0 just say no 
  if(n<=0):
    return False 
  # if we reach lowest power of n just return true
  if(n==1):
    return True
  if(n%2==0):
    return checkifpower(n//2)
  
  return False

# take input
n = int(input("enter your number : "))

if(checkifpower(n)):
  print("power of 2")
else:
  print("not power of 2")