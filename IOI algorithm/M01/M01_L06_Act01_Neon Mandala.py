# ================================================
#  ACTIVITY - NEON MANDALA

# PART 1 - IMPORT AND SCREEN SETUP
# turtle.Screen() creates the canvas we draw on.
# bgcolor("black") sets the background -- neon colors pop on black!
# title() sets the text that appears in the window's title bar.
import turtle

paper = turtle.Screen()
paper.bgcolor("black")
paper.title("Neon Mandala")

# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates our drawing pen.
# speed("fastest") skips the slow animation so it draws instantly.
# hideturtle() hides the arrow shape -- only the art is visible.
pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle()

# PART 3 - OUTER COLOR SPIRAL (MOVEMENT + LOOPS + COLOR)
# forward(n) moves the turtle forward n pixels.
# right(91) turns it 91 degrees -- 1 degree extra creates the spiral drift!
# The for loop repeats 80 times, growing the distance each round.
# colors[i % len(colors)] cycles through the color list endlessly.
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]

for i in range(80):
    pen.color(colors[i % len(colors)])
    pen.width(2)
    pen.forward(i * 2)
    pen.right(91)

# PART 4 - PEN CONTROL: MOVE TO CENTER AND DRAW A FILLED STAR
# penup() lifts the pen so moving doesn't draw a line.
# goto(0, 0) teleports the turtle to the exact center of the canvas.
# pendown() puts the pen back on the canvas -- drawing starts again.
# begin_fill() + end_fill() fills the shape with the chosen color.
# A 5-pointed star turns 144 degrees at each point.
pen.penup()
pen.goto(0, -60)
pen.setheading(90)
pen.pendown()
pen.color("gold", "yellow")
pen.begin_fill()

for i in range(5):
    pen.forward(130)
    pen.right(144)

pen.end_fill()

# PART 5 - INNER PETAL RING (NESTED LOOP + FILL)
# The outer loop spins around 360 degrees (36 petals x 10 degrees each).
# The inner loop draws one square petal each rotation.
# Nesting loops inside loops is how complex patterns are built!
pen.penup()
pen.goto(0, 0)
pen.pendown()
petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]

for i in range(36):
    pen.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i + 2) % len(petal_colors)])
    
    pen.begin_fill()

    for j in range(4):
        pen.forward(55)
        pen.right(90)
    pen.end_fill()
    pen.right(10)

# KEEP WINDOW OPEN
turtle.done()
