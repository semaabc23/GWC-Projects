from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(300,300)
x_pos = 300
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

# repeat 4 amount of times for a shape with 4 sides
for i in [0,1,2,3]:
    t.left(90)
    t.forward(300)

num_sides=input("How many sides?")
int_num_sides=int(num_sides)

#choose color of shape
color[1,5]
color_choice("red","blue","yellow","green","blue")

# Close window on click.
exitonclick()
