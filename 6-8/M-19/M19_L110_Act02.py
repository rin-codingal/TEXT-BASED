#define function to calculate cube
def cube(number):
	return number * number * number
  
#define a function which will execute cube function if the user entered number is divisible by 3
def by_three(num):
	if num % 3 ==0:
		return cube(num) #calling function cube()
	else:
		return False

x = 9
y = 4

#display result
result1 = by_three(x) #passing argument x
result2 = by_three(y) #passing argument y

print(result1)
print(result2)