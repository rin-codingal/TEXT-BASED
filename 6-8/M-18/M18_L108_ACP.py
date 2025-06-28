import turtle #importing library  

paper = turtle.Screen() # make the paper or the screen
paper.bgcolor("light blue") # set the 'paper' background color
paper.title("Homework: Customise Square")

pen = turtle.Turtle() #make the pen

s = int(input("Enter the length of the side of the Square: "))  

for i in range(4):
  pen.forward(s) 
  pen.left(90) 

turtle.done()