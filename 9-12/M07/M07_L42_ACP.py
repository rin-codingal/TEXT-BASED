import turtle

turtle.Screen().bgcolor("Orange")
pen = turtle.Turtle()

#equilateral triangle
pen.pendown()
for i in range(3):
    pen.forward(150)
    pen.left(120)

pen.right(90)
pen.penup()
pen.forward(100)
pen.left(90)

#rectangle
pen.pendown()
for i in range(2):
    pen.forward(150)
    pen.right(90)
    pen.forward(75)
    pen.right(90)

pen.right(180)
pen.penup()
pen.forward(100)
pen.left(90)

#hexagon
pen.pendown()
pen.color("red")
for i in range(6):
    pen.forward(100)
    pen.right(60)

turtle.done()