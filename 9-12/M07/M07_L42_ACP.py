import turtle

turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()

#equilateral triangle
board.pendown()
for i in range(3):
    board.forward(150)
    board.left(120)

board.right(90)
board.penup()
board.forward(100)
board.left(90)

#rectangle
board.pendown()
for i in range(2):
    board.forward(150)
    board.right(90)
    board.forward(75)
    board.right(90)

board.right(180)
board.penup()
board.forward(100)
board.left(90)

#hexagon
board.pendown()
board.color("red")
for i in range(6):
    board.forward(100)
    board.right(60)

turtle.done()