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

# grid = Grid()
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

score.write_scoreboard()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 5:
        food.draw_food()
        snake.extend()
        score.set_score(score.get_score() + 1)
        score.write_scoreboard()

    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        score.game_over_prompt()
        break

    if snake.tail_collision():
        score.game_over_prompt()
        break

screen.exitonclick()
