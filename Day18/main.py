from turtle import Turtle, Screen

# creating turtle object
timmy_the_turtle = Turtle()

# changing the shape of the timmy_the_turtle using the function shape
timmy_the_turtle.shape("turtle")

# changing the color of the turtle using the color method
timmy_the_turtle.color("DarkCyan")

# moving the turtle forward 100 spaces using the function forward
timmy_the_turtle.forward(100)

# to turn it in certain direction you can use function right left and specify the angle
timmy_the_turtle.right(90) # turn right at 90 deg angle

# now move forward 100 spaces
timmy_the_turtle.forward(100)

# in order for the window to stay
# we need to create a screen object which is also inside turtle module
# only exit when we click on window
screen = Screen()
screen.exitonclick()