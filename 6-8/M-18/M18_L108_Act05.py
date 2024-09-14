import turtle 

my_wn = turtle.Screen()
my_wn.bgcolor("light blue") 
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

while True: #iterate loop
  for i in range(4): 
    my_pen.color(colors[i%6])
    my_pen.fd(size + 1)
    my_pen.left(90)
    size = size - 5
  size = size + 1
  