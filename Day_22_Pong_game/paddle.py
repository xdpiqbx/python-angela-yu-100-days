from turtle import Turtle

TOP_BORDER = 250
BOTTOM_BORDER = -250
PADDLE_STEP = 20


class Paddle(Turtle):
    def __init__(self, paddle_side):
        super().__init__()
        self.paddle_side = paddle_side
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x = self.get_x_direction()
        self.y = 0
        self.goto(self.x, self.y)

    def go_up(self):
        if self.y >= TOP_BORDER:
            return
        self.y += PADDLE_STEP
        self.goto(self.x, self.y)

    def go_down(self):
        if self.y <= BOTTOM_BORDER:
            return
        self.y -= PADDLE_STEP
        self.goto(self.x, self.y)

    def get_x_direction(self):
        if self.paddle_side == "right":
            return 410
        else:
            return -410
