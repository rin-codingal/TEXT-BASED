class Area:
  radius= 0
    
  def AreaOfCircle(self,radius):
    AreaCircle=3.14*radius*radius
    return AreaCircle
  
  def PerimeterOfCircle(self,radius):
    PerimeterCircle=2*3.14*radius
    return PerimeterCircle

AreaPerimeterOBJ=Area()

Question=(input("Which of the following do you want to calculate? \n A)Area Of Circle \n B)Perimeter Of Circle \n"))

if Question.upper()=="A":
  radius=(int(input("Please enter the radius of the circle: \n")))
  print("Area of the circle is :",AreaPerimeterOBJ.AreaOfCircle(radius))

elif Question.upper()=="B":
  radius=(int(input("Please enter the radius of the circle: \n")))
  print("Perimeter of the circle is :",AreaPerimeterOBJ.PerimeterOfCircle(radius))

else:
  print("Please choose the correct option")