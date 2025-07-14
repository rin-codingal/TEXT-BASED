import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
pen = turtle.Turtle()

# creating a square
for i in range(4):
	pen.forward(100)
	pen.left(90)

turtle.done()