from turtle import Turtle, Screen

# turtle object
turtle_obj = Turtle()

for i in range(0, 4):

    turtle_obj.forward(100)
    turtle_obj.right(90)

# create screen object
screen_obj = Screen()
screen_obj.exitonclick()