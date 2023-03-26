from turtle import Turtle
FONT = ("Calibri", 10, "normal")


class Inscription(Turtle):
    def __init__(self):
        super().__init__()
        self.state = None
        self.penup()
        self.color("black")
        self.hideturtle()

    def write_on_map(self, result):
        self.state = result["state"]
        self.goto(result["x"], result["y"])
        self.write(self.state, align="center", font=FONT)



