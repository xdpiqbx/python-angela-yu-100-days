from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        game_over = self
        game_over.goto(0, 0)
        game_over.write(f"GAME OVER", align="center", font=("Courier", 18, "bold"))

