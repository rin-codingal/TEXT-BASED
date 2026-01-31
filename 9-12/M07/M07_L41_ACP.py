def recur_fibo(pos):
   if pos <= 1:
       return pos
   else:
       return(recur_fibo(pos-1) + recur_fibo(pos-2))

nterms = int(input("Enter Number of Terms : "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       result = recur_fibo(i)
       print(result)