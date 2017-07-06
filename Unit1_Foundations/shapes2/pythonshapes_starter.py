from turtle import *
import math

# Name your Turtle.
jimbo = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
jimbo.setposition(x_pos, y_pos)

### Write your code below:

jimbo.pendown()
jimbo.forward(100)
jimbo.right(90)
jimbo.forward(100)
jimbo.right(90)
jimbo.forward(100)
jimbo.right(90)
jimbo.forward(100)
jimbo.penup()

# Close window on click.
exitonclick()
