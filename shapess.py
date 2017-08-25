from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(300,300)
x_pos = 200
y_pos = 0
t.setposition(x_pos, y_pos)

for x in range(s):

    t.left(360/s)
    t.forward(200)

    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)

    t.circle(50,360,5)
