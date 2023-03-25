import time
from grid import GridField
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
width = 900
height = 700
screen.setup(width, height)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong game")

g = GridField()
score = ScoreBoard()

rightPaddle = Paddle("right")
leftPaddle = Paddle("left")

screen.listen()
screen.onkey(rightPaddle.go_up, "Up")
screen.onkeypress(rightPaddle.go_up, "Up")

screen.onkey(rightPaddle.go_down, "Down")
screen.onkeypress(rightPaddle.go_down, "Down")

screen.onkey(leftPaddle.go_up, "w")
screen.onkeypress(leftPaddle.go_up, "w")

screen.onkey(leftPaddle.go_down, "s")
screen.onkeypress(leftPaddle.go_down, "s")

ball = Ball()

while True:
    screen.update()
    time.sleep(ball.ball_speed)
    print(ball.ball_speed)
    ball.move()

    is_left_paddle_collision = ball.distance(rightPaddle) < 50 and ball.xcor() > 390
    is_right_paddle_collision = ball.distance(leftPaddle) < 50 and ball.xcor() < -390

    ball.paddle_collision(is_left_paddle_collision, is_right_paddle_collision)

    if ball.goes_out():
        score.set_score(ball.get_score())

screen.exitonclick()
