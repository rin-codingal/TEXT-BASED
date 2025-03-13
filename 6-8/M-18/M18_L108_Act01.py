import turtle #importing library

paper = turtle.Screen() # make the paper or the screen
paper.bgcolor("orange") # set the 'paper' background color
paper.setup(300,400) # width = 300, height = 400
paper.title("Polygon")

pen = turtle.Turtle() #make the pen
 
num_sides = 6 # number of hexagon's side
side_length = 70

angle = 360 / num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)
     
turtle.done()