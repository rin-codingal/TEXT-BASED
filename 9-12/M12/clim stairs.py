# Program to Print the number of ways to climb n stairs when you can jump 1,2,3 stair at a time

def ways(stairs):

  # check corner case
  if stairs<0:
    return 0

  # if no stair left, just return one as we reach the top
  if stairs==0:
    return 1
    
  twosteps=0
  onestep=0

# we can jump 2 only 2 or more stairs are left
  if (stairs>=2):
    twosteps = ways(stairs-2)
# jump 1 if 1 or more stairs remains 
  onestep = ways(stairs-1)
  
# return total ways 
  return twosteps+onestep

stairs = int(input("enter number of steps :"))

print("number to ways to climb :",ways(stairs))
