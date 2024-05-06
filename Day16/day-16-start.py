from turtle import Turtle , Screen


# creating turtle object named timmy
# turtle is the module
# Turtle is the class
timmy = Turtle()
print(timmy)


timmy.shape('turtle')
timmy.color('Coral')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()