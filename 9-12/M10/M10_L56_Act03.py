def onSquareTime(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1
        print()
        
    print(f"when n is {n}, iteration = {iteration}")
    print()

onSquareTime(5)
onSquareTime(4)
onSquareTime(3)

print()
print("with every 'n', the time taken = n^2")
print("O(n^2)")