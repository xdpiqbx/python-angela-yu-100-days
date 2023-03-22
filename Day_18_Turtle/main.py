import random
from turtle import Turtle, Screen
import colorgram

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange")

screen = Screen()
screen.colormode(255)


# def draw_square():
#     for _ in range(4):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.left(90)
#
# draw_square()

# def draw_dashed_line():
#     for _ in range(20):
#         timmy_the_turtle.pendown()
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(10)
# draw_dashed_line()

# def draw_figures():
#     sides = 3
#     while True:
#         timmy_the_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         for _ in range(sides):
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(360/sides)
#         sides += 1
# draw_figures()

# def random_walk():
#     directions = {
#         "forward": 0,
#         "left": 90,
#         "right": 270,
#         "back": 180
#     }
#     timmy_the_turtle.speed("fast")
#     timmy_the_turtle.pensize(15)
#     while True:
#         timmy_the_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         timmy_the_turtle.setheading(directions[random.choice(list(directions.keys()))])
#         timmy_the_turtle.forward(30)
# random_walk()

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors
#
# def draw_spirograph():
#     gap = 2
#     timmy_the_turtle.speed("fastest")
#     size = 200
#     for _ in range(int(360 / gap)):
#         timmy_the_turtle.pencolor(random_color())
#         timmy_the_turtle.circle(size)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap)
#         # size += 5
# draw_spirograph()

colors = colorgram.extract('spots.jpg', 42)
extracted_colors = []
for color in colors:
    extracted_colors.append(
        (color.rgb.r, color.rgb.g, color.rgb.b)
    )


def draw_spots():
    timmy_the_turtle.speed("fastest")
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.penup()
    x = -250
    y = -250
    timmy_the_turtle.goto(x, y)

    for _ in range(10):
        for _ in range(10):
            timmy_the_turtle.dot(20, random.choice(extracted_colors))
            timmy_the_turtle.forward(50)
        y += 50
        timmy_the_turtle.goto(x, y)


draw_spots()

screen.exitonclick()
