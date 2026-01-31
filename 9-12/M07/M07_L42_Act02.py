import turtle

turtle.Screen().bgcolor("Orange") #paper
pen = turtle.Turtle() #pen

angle = 360 / 3 #triangle has 3 sides
 
# first triangle for star
for i in range(3):
    pen.forward(100) # draw base 
    pen.left(angle)
 
#pen.penup()
pen.right(30)
pen.forward(50)
 
# second triangle for star
pen.pendown()
pen.left(90)
for i in range(3):
    pen.forward(100) # draw base 
    pen.left(angle)
 
turtle.done()