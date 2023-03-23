from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def move_forwards():
#     tim.forward(10)
# screen.listen()
# screen.onkey(fun=move_forwards, key="space")

def move_forwards():
    tim.forward(10)


def move_back():
    tim.back(10)


def turn_left():
    # tim.left(15)
    tim.setheading(tim.heading() + 15)


def turn_right():
    # tim.right(15)
    tim.setheading(tim.heading() - 15)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")




screen.exitonclick()