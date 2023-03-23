from turtle import Turtle

SCOREBOARD_FONT = ('Arial', 14, 'normal')
SCOREBOARD_FONT_COLOR = "orange"
SCOREBOARD_ALIGNMENT = "center"

GAME_OVER_FONT = ('Arial', 28, 'normal')

SCOREBOARD_Y_POSITION = 260


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCOREBOARD_FONT_COLOR)
        self.sety(SCOREBOARD_Y_POSITION)
        self.write_scoreboard()
        self.hideturtle()

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, SCOREBOARD_ALIGNMENT, SCOREBOARD_FONT)

    def game_over_prompt(self):
        self.sety(0)
        self.write(f"GAME OVER", False, SCOREBOARD_ALIGNMENT, GAME_OVER_FONT)




