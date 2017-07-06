from turtle import *
import math

# Name your Turtle.
jimbo = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
square_count = input(5)
count_int = int(square_ct)

if count_int > 1:
    jimbo.pendown()
    jimbo.begin_fill()
    jimbo.forward(100)
    jimbo.right(90)
    jimbo.forward(100)
    jimbo.right(90)
    jimbo.forward(100)
    jimbo.right(90)
    jimbo.forward(100)
    jimbo.end_fill()

    jimbo.up()
    jimbo.forward(20)
    jimbo.color(random.random(),random.random(), random.random())
    jimbo.penup()

# Close window on click.
exitonclick()
