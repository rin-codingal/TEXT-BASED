# Program to find multiple with 1 and n iterations

# For 1 iteration simply multiply 
def f1(n,m):
  total = n*m
  print("1 iteration: ",total) 



# For n iteration run a for loop
def fn(n,m):
  total = 0
  for i in range(1,n+1):
    total += m
  print("n iteration: ",total) 

m = int(input("Enter 'a' (first number) for a*b : "))
n = int(input("Enter 'b' (second number) for a*b : "))

f1(m,n)
print()
fn(m,n)
