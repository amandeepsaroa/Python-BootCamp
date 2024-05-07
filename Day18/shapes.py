import turtle
import random

turtle.colormode(255)
# creating turtle object mention module.className
turtle_obj = turtle.Turtle()


def change_color():

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle_obj.color((r, g, b))


dim = 3

# we want total of 8 shapes octagon
for j in range(0, 8):

    # each new shape new color
    change_color()

    # number of sides we want start with 3 triangle
    for i in range(0, dim):

        turtle_obj.forward(100)
        # so this is the logic 360/no.ofDirection angle for each corner based on no.of dimensions
        turtle_obj.right(360/dim)

    dim += 1


screen_obj = turtle.Screen()
screen_obj.exitonclick()
