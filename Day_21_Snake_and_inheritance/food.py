import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.8)
        self.color("orange")
        self.shape("circle")
        self.speed("fastest")
        self.draw_food()

    def draw_food(self):
        x = random.randrange(-26, 26, 2) * 10
        y = random.randrange(-26, 26, 2) * 10
        self.goto(x, y)
