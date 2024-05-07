import turtle

tim = turtle.Turtle()
tim.shape("arrow")

for i in range(0, 10):

    # draw 10 spaces line using forward function
    tim.forward(10)
    # pull pen up
    tim.penup()
    # now draw a line again this will not showup because pen is up
    tim.forward(10)
    # now pendown so that line shows up when drawn
    tim.pendown()


screen_obj = turtle.Screen()
screen_obj.exitonclick()
