# Basic Star Pattern
print("Star Pattern")
for i in range(1,6):
  for j in range(i):
    print("*", end="")
  print()

print()

#Inverted Star Pattern
print("Inverted Star Pattern")
for i in range(6,1,-1):
  for j in range(i, 1, -1):
    print("*", end="")
  print()

