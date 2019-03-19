# This program wil use turtle graphics to draw my initals.
# 3/18/2019
# CTI-110 P4T1b - Initials
# Tavius Cousar

# Import turtle
import turtle

# Set up window and turtle (tut)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title('My Initials')
tut = turtle.Turtle()
tut.color("white")
tut.pensize(10)

# Set up movements for first initital (T)
tut.forward(100)
tut.backward(50)
tut.right(90)
tut.forward(100)

# Reposition the turtle for second initial (C)
tut.penup()
tut.goto(0, 0)
tut.goto(125,0)
tut.pendown()

# Set up movements for second initial (C)
tut.left(90)
tut.forward(100)
tut.backward(100)
tut.right(90)
tut.forward(100)
tut.left(90)
tut.forward(100)

# Allow user to click window to exit
wn.exitonclick()
