num = int(input("Enter any number and we'll count how many digits are there: "))

count = 0

while num != 0:
  count+=1
  num=num//10

print(count)
