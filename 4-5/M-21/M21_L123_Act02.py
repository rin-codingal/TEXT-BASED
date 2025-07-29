import turtle

turtle.Screen().bgcolor("Cyan")

board = turtle.Turtle()
 
# Triangle
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)

#move position
board.penup()
board.left(120)
board.forward(200)
board.pendown()


# Square
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

turtle.done()