from turtle import Turtle


class GridField(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.penup()
        self.color("dark slate gray")
        self.speed("fastest")
        self.goto(-400, -300)
        self.field()
        self.hideturtle()

    def field(self):
        self.pendown()
        forward_distances = [800, 600, 800, 600, 400, 600]
        for distance in forward_distances:
            self.forward(distance)
            self.left(90)
