from turtle import Turtle
import os

SCOREBOARD_FONT = ('Arial', 14, 'normal')
SCOREBOARD_FONT_COLOR = "orange"
SCOREBOARD_ALIGNMENT = "center"
SCORE_FILE_NAME = "score.txt"

GAME_OVER_FONT = ('Arial', 28, 'normal')

SCOREBOARD_Y_POSITION = 260


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.create_score_file_if_not_exists_return_high_score()
        self.color(SCOREBOARD_FONT_COLOR)
        self.sety(SCOREBOARD_Y_POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, SCOREBOARD_ALIGNMENT, SCOREBOARD_FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.save_high_score_to_file()
        self.score = 0
        self.update_scoreboard()

    def save_high_score_to_file(self):
        mode = "w"
        with open(SCORE_FILE_NAME, mode) as file:
            file.write(str(self.high_score))

    def get_high_score_from_file(self):
        with open(SCORE_FILE_NAME) as file:
            score = file.read()
            return int(score)

    def create_score_file(self):
        mode = "w"
        with open(SCORE_FILE_NAME, mode) as file:
            file.write(str(0))

    def create_score_file_if_not_exists_return_high_score(self):
        if os.path.exists(SCORE_FILE_NAME):
            return self.get_high_score_from_file()
        else:
            self.create_score_file()
            return 0


    # def game_over_prompt(self):
    #     self.sety(0)
    #     self.write(f"GAME OVER", False, SCOREBOARD_ALIGNMENT, GAME_OVER_FONT)




