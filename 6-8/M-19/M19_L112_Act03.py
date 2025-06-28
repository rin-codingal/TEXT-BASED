valid = False

while not valid: #outer loop
  try:
    n = int(input("Enter a number: "))

    #enter a even number
    while n%2 == 0: #inner loop
      print("bye")
      valid = True
      break

  except ValueError:
    print("Invalid")