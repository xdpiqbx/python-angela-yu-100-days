from turtle import Screen
from snake import Snake
import time

screen = Screen()
width = 600
height = 600
screen.setup(width, height)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake game")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.01)
    snake.move()

screen.exitonclick()
