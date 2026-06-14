
import turtle

sc = turtle.Screen()
sc.bgcolor("light pink")
sc.setup(1500, 700)
sc.title("Welcome to Turtle Window")

pen = turtle.Turtle()
pen.speed(3)

# rectangle
angle = 360 / 4
for i in range(4):
    pen.forward(150)
    pen.left(angle) 

pen.penup()
pen.forward(200)
pen.pendown()

# square
for i in range(4):
    pen.forward(100)
    pen.left(angle)

pen.penup()
pen.forward(150)
pen.pendown()

# triangle
pen.pencolor("blue")
angle = 360 / 3
for i in range(3):
    pen.forward(100)
    pen.left(angle)

pen.penup()
pen.forward(200)
pen.pendown()

# circle
pen.pencolor("black")
for i in range(360):
    pen.forward(1)
    pen.left(1)

pen.penup()
pen.right(90)
pen.forward(150)
pen.left(90)
pen.pendown()

# pentagon
angle = 360 / 5
for i in range(5):
    pen.forward(100)
    pen.left(angle)

pen.penup()
pen.backward(700)
pen.pendown()

# hexagon
angle = 360 / 6
for i in range(6):
    pen.forward(100)
    pen.left(angle)
 
turtle.done()
