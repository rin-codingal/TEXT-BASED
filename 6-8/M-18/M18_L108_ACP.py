import turtle #importing library  

paper = turtle.Screen() # make the paper or the screen
paper.bgcolor("light blue") # set the 'paper' background color
paper.title("Homework: Customise Square")

pen = turtle.Turtle() #make the pen

s = int(input("Enter the length of the side of the Square: ")) 
num_of_sides = 4 #number sides of square
angle = 360/num_of_sides 

for i in range(num_of_sides):
  pen.forward(s) 
  pen.left(angle) 

turtle.done()