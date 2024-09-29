import turtle

turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()
 
# first triangle for star
for i in range(3):
    board.forward(100) # draw base
 
    board.left(120)
'''
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
'''
 
board.penup()
board.right(30)
board.forward(50)
 
# second triangle for star
board.pendown()
board.left(90)
for i in range(3):
    board.forward(100) # draw base
 
    board.left(120)
'''
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
'''
 
turtle.done()