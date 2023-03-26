from turtle import Screen

from scoreboard import ScoreBoard
from grid import Grid
from food import Food
from snake import Snake
import time

screen = Screen()
width = 600
height = 600
screen.setup(width, height)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake game")

grid = Grid()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

score_board.update_scoreboard()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 5:
        food.draw_food()
        snake.extend()
        score_board.set_score(score_board.get_score() + 1)
        score_board.update_scoreboard()

    is_left_or_right_wall_collision = snake.head.xcor() > 260 or snake.head.xcor() < -260
    is_top_or_bottom_wall_collision = snake.head.ycor() > 260 or snake.head.ycor() < -260

    if is_left_or_right_wall_collision or is_top_or_bottom_wall_collision:
        score_board.reset()
        snake.reset()

    if snake.tail_collision():
        score_board.reset()
        snake.reset()

screen.exitonclick()
