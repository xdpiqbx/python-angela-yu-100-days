from turtle import Turtle


class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("dark slate gray")
        self.speed("fastest")
        self.goto(-260, -240)
        self.draw_grid()
        self.hideturtle()

    def draw_grid(self):
        y = -260
        r = int(600 / 20) - 2
        for _ in range(r):
            self.pendown()
            self.forward(520)
            self.penup()
            self.goto(-260, y)
            y += 20

        self.right(90)

        x = 260
        r = int(600 / 20) - 3
        for _ in range(r):
            self.goto(x, 260)
            self.pendown()
            self.forward(520)
            self.penup()
            x -= 20

