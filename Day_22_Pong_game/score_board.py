from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def set_score(self, left_right_scores):
        self.left_score = left_right_scores[0]
        self.right_score = left_right_scores[1]
        self.write_score()

    def write_score(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))


