from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.x_move = 10
        self.y_move = 10
        self.left_score = 0
        self.right_score = 0
        self.ball_speed = 0.1

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)
        self.wall_collision()

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.wall_bounce()

    def paddle_collision(self, is_left_paddle, is_right_paddle):
        if is_right_paddle or is_left_paddle:
            self.paddle_bounce()
            self.acceleration()

    def goes_out(self):
        if self.is_left_miss() or self.is_right_miss():
            self.reset_position()
            return True

    def reset_position(self):
        self.setx(0)
        self.sety(0)
        self.paddle_bounce()

    def is_right_miss(self):
        if self.xcor() > 410:
            self.left_score += 1
            return True

    def is_left_miss(self):
        if self.xcor() < -410:
            self.right_score += 1
            return True

    def get_score(self):
        return self.left_score, self.right_score

    def acceleration(self):
        self.ball_speed *= 0.9



