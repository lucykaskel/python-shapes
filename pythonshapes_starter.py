from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.

sides = int(input("Enter the number of sides you want "))
print('You entered', sides)
color = input("Enter a color.")
print("You entered", color)
t.pencolor(color)
setup(500,500)

for i in range(sides):
    t.left(360/sides)
    t.forward(90)







# Close window on click.
exitonclick()
