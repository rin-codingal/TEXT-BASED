#Input the value of terms
n = int(input("Enter the value of terms: "))
print()

sum = 0  #initialize sum value
i = 1  #initialize i value

while i <= n: #loop will run from 1 to n
  sum = sum + i
  print(f"Sum of {i}= {sum}")
  i = i + 1

  