#Least Common Multiple
# Using Eucliden Algorithms 
def hcf(smallNum,largeNum): 
  while(smallNum):
    numberStore = smallNum
    smallNum = largeNum % smallNum
    largeNum = numberStore

  return largeNum

# Enter 2 numbers
largeNum = int(input("Enter the Largest number : "))
smallNum = int(input("Enter the Smallest number : "))

# LCM is the smallest number that two or more numbers can divide into evenly
lcm = int((smallNum / hcf(smallNum,largeNum))* largeNum)
print("LCM is : ",lcm)


