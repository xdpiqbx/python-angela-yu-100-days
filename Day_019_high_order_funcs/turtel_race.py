import random
from turtle import Turtle, Screen

screen = Screen()
screen_width = 800
screen_height = 640
screen.setup(screen_width, screen_height)


turtles = []
colors = ["green", "red", "orange", "dark violet", "blue", "black"]


def colors_to_string():
    return " | ".join(colors)


bet = screen.textinput(title="Make your bet", prompt="Whitch turtle will win the race?\n" + colors_to_string() + "\n Enter a color: ")


def create_turtles():
    for c in colors:
        t = Turtle("turtle")
        t.color(c)
        turtles.append(t)


def set_on_start():
    distance_between = 50
    turtles_row = distance_between * (len(turtles) - 1)
    x_coord = 0 - (screen_width / 2 - 25)
    y_coord = turtles_row / 2
    for t in turtles:
        t.penup()
        t.goto(x_coord, y_coord)
        t.pendown()
        y_coord -= distance_between


def start_the_race():
    while True:
        for t in turtles:
            t.forward(random.randint(0, 10))
            if t.position()[0] > screen_width / 2 - 25:
                return t.color()[0]


def evaluation_of_the_result(res):
    if bet == res:
        print("You WIN !")
    else:
        print(f"You Lose =( {res.capitalize()} turtle is won!")


create_turtles()
set_on_start()
result = start_the_race()
evaluation_of_the_result(result)

screen.exitonclick()
