import turtle

# Function to draw an equilateral triangle
def draw_triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Function to draw a hexagon
def draw_hexagon(side_length):
    for i in range(6):
        turtle.forward(side_length)
        turtle.left(60)

# Set up the turtle
turtle.speed(1)

# Draw an equilateral triangle
turtle.penup()
turtle.goto(-100, 0)  # Move to starting position
turtle.pendown()
draw_triangle(100)

# Draw a rectangle
turtle.penup()
turtle.goto(50, 0)  # Move to starting position
turtle.pendown()
draw_rectangle(150, 75)

# Draw a hexagon
turtle.penup()
turtle.goto(-50, -150)  # Move to starting position
turtle.pendown()
draw_hexagon(50)

# Finish drawing
turtle.done()