#2 digit primes
def prime2Dig(n):     
    prime = [True for i in range(n + 1)] #make list to store if number is prime or not    

    currentNumber = 2 #start from 2 as 1 and 0 are non prime

    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):            
            for i in range(currentNumber ** 2, n + 1, currentNumber): #mark all multiples of that number as non primes
                prime[i] = False

        currentNumber += 1

    #mark 0,1 as non primes
    prime[0]= False
    prime[1]= False

    #print all primes till n
    for p in range(n + 1):
        if prime[p]:
            print(p)


n = 99
print("All 2 digit prime numbers: ")
prime2Dig(n)