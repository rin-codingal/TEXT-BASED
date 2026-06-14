import turtle

turtle.Screen().bgcolor("Cyan")
paper = turtle.Screen()
paper.setup(700, 500)

pen = turtle.Turtle()
 
# Triangle
angle3 = 360/3
pen.forward(100)
 
pen.left(angle3)
pen.forward(100)
 
pen.left(angle3)
pen.forward(100)

#move position
pen.penup()
pen.left(120)
pen.forward(200)

#start to draw
pen.pendown()

# Square
angle4 = 360/4
pen.forward(100)
pen.left(angle4)

pen.forward(100)
pen.left(angle4)

pen.forward(100)
pen.left(angle4)

pen.forward(100)
pen.left(angle4)

turtle.done()