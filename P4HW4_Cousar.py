# This program will use turtle graphics to draw a
# shape using a nested loop.
# 3/19/2019
# CTI-110 P4HW4 - Nested Loops
# Tavius Cousar

# Import turtle
import turtle

# Set up window and turtle (tut)
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Tri-Force')
tut = turtle.Turtle()
tut.shape("turtle")
tut.color('yellow')
tut.pensize(5)

for a in range(3):
    for b in range(5):
        tut.left(120)
        tut.forward(80)
    tut.forward(4)
    tut.right(120)

# Allow user to click window to exit
wn.exitonclick()

