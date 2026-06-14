import turtle

s = turtle.Turtle()

Guess = int(input("What is 8 X 5?"))

if Guess == 8*5:
    s.write(str(Guess) + ' is correct!')
    s.penup()
    s.backward(10)
else:
    s.write('You said ' + str(Guess) + '. I got ' + str(8*5))
    s.penup()
    s.backward(10)

turtle.done()