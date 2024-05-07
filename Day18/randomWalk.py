import turtle
import random

turtle.colormode(255)
# creating turtle object mention module.className
turtle_obj = turtle.Turtle()

# setting width of the turtle object
turtle_obj.width(15)

# setting the speed of the turtle to fast
turtle_obj.speed(10)

# creating screenObject
screen_obj = turtle.Screen()


def change_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # tuple (a,b,c)
    # set the color of the turtle_object
    turtle_obj.color((r, g, b))


for i in range(0, 200):

    # change color after every turn
    change_color()
    turtle_obj.forward(20)

    # get random angle left, right, U-turn, same direction, that's why using step size of 90
    angle = random.randrange(0,361,90)
    turtle_obj.setheading(angle)
    # print(angle)

screen_obj.exitonclick()
