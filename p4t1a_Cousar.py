# This program wil use turtle graphics to draw both a square and a triangle.
# 3/18/2019
# CTI-110 P4T1a - Shapes
# Tavius Cousar

# Import turtle
import turtle

# Set up window and turtle (tut)
wn = turtle.Screen()
wn.title('Square and Triangle Drawing')
tut = turtle.Turtle()

# Set up turtle movement for square to repeat four times
for x in range(4):
    tut.forward(50)
    tut.left(90)

# Move turtle to create space for triangle
for x in [1]:
    tut.right(90)
    tut.forward(100)
    
# Set up turtle movement for triangle to repeat three times
for x in range(3):
    tut.right(120)
    tut.forward(80)

# Allow user to click window to exit
wn.exitonclick()
