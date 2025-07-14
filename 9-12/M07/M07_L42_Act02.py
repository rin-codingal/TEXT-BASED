import turtle

turtle.Screen().bgcolor("Orange")
pen = turtle.Turtle()
 
# first triangle for star
for i in range(3):
    pen.forward(100) # draw base 
    pen.left(120)
 
pen.penup()
pen.right(30)
pen.forward(50)
 
# second triangle for star
pen.pendown()
pen.left(90)
for i in range(3):
    pen.forward(100) # draw base 
    pen.left(120)
 
turtle.done()