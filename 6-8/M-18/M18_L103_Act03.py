print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int( input("Enter your choice (1 or 2): ") )

if( choice == 1 ): #condition 1 outer if statement
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")

  #Condition for selecting the type of bike
  choice2=int(input("Enter you choice2 (1 or 2): "))

  if choice2==1: #inner if statement
    print("you have selected scooty")
  else:
    print("you have selected scooter")


elif( choice == 2 ): #outer elif statement
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  
  choice3=int(input("enter your choice3 (1 or 2): "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected sedan")
  else:
    print("you have selected XUV")

else: #outer else statement
  print("Wrong choice!")