import turtle
import random

# to use (r,g,b)  tuple for coloring 0..255
turtle.colormode(255)

# turtle object
turtle_obj = turtle.Turtle()
# turtle speed
turtle_obj.speed(0)
# turtle width
turtle_obj.width(2)

# screen object so that we can exit only when we click on screen
screen_obj = turtle.Screen()


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # this will return the tuple
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):

    for i in range(0, int(360 / size_of_gap)):
        # get the random r,b,g tuple from the function
        produced_color = random_color()
        # set the object color
        turtle_obj.color(produced_color)
        # draw a circle of radius 100
        turtle_obj.circle(100, extent=None, steps=None)
        # get the current heading add 5 degree to it to set new heading
        current_heading = turtle_obj.heading()
        # set new heading by adding 5 degree to current heading
        turtle_obj.setheading(current_heading + size_of_gap)


def main():

    draw_spirograph(5)

    screen_obj.exitonclick()


if __name__ == "__main__":
    main()