def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print(f"when n is {n}, iteration = {iteration}")

OnTime(5)
OnTime(35)
OnTime(57)

print()

print("With every 'n' the time taken and iterations will increase linearly")