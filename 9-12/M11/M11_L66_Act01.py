import math
 
def printPowerSet(set,SetSize):    
    PowerSetSize = (int) (math.pow(2, SetSize)) # Find total elements possible in the power set
    outer = 0
    inner = 0
        
    for outer in range(0, PowerSetSize):
        for inner in range(0, SetSize):
            # Check if inner bit in the outer is set If set then print inner element from set
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")

        print()
 

size = int(input("Enter array size: "))
 
set = []
for i in range(0,size):
    n = int(input("Enter element of the array: "))
    set.append(n)

print()

printPowerSet(set, len(set))