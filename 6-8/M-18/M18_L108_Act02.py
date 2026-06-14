import turtle #importing library

paper = turtle.Screen() # make the paper or the screen
paper.bgcolor("Aqua") # set the 'paper' background color
paper.setup(500,500) # width = 500, height = 500
paper.title("Star of David")

pen = turtle.Turtle() #make the pen
 
# first triangle for star
pen.pendown()
pen.forward(100) # draw base
 
pen.left(120)
pen.forward(100)
 
pen.left(120)
pen.forward(100)

#change the position of the pen
pen.penup()
pen.right(150)
pen.forward(50)
 
# second triangle for star
pen.pendown()
pen.right(90)
pen.forward(100)
 
pen.right(120)
pen.forward(100)
 
pen.right(120)
pen.forward(100)
 
turtle.done()