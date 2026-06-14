import turtle 
pen = turtle.Turtle() #pen
paper = turtle.Screen() #paper
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
paper.bgcolor('black') 
pen.speed('fastest')
pen.hideturtle()

while True:
  for x in range(200): 
    pen.pencolor(colors[x%len(colors)])
    pen.width(x/100 + 1)
    pen.forward(x) 
    pen.left(59)
    
  pen.right(239)  

  for x in range(200, 0, -1): #sreenandan until this line
    pen.pencolor('black') 
    pen.width(x/100 + 7)
    pen.forward(x) 
    pen.right(59) 

turtle.done()