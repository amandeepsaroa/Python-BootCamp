# below is the code to extract rgb tuple color code from the image
# import colorgram
#
# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)

colors_extracted = [(0, 0, 0), (240, 225, 232), (202, 165, 109), (38, 99, 134), (128, 164, 189), (126, 84, 55), (234, 206, 108),
       (174, 149, 43), (198, 74, 110), (223, 126, 144), (134, 56, 76), (115, 40, 73), (87, 169, 116), (219, 67, 55),
       (107, 197, 190), (247, 159, 168), (41, 157, 206), (69, 108, 75), (1, 61, 85), (212, 183, 178), (87, 50, 44),
       (61, 58, 59), (154, 212, 203), (159, 206, 214), (122, 122, 158), (10, 85, 105), (187, 186, 205)]


turtle_obj = turtle.Turtle()
turtle_obj.setheading(225)
turtle_obj.penup()

turtle_obj.hideturtle()
turtle_obj.forward(300)
turtle_obj.setheading(0)

screen_obj = turtle.Screen()


def get_random_color():

    random_color_tuple = random.choice(colors_extracted)
    return random_color_tuple


def draw_painting():

    number_of_dots = 100

    for dot_count in range(1 , number_of_dots+1):

        turtle_obj.dot(20, get_random_color())
        turtle_obj.forward(50)

        if dot_count % 10 == 0:

            turtle_obj.setheading(90)
            turtle_obj.forward(50)
            turtle_obj.setheading(180)
            turtle_obj.forward(500)
            turtle_obj.setheading(0)


def main():

    draw_painting()

    screen_obj.exitonclick()


if __name__ == "__main__":
    main()