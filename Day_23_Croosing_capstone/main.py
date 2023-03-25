import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from grid import GridField

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
score = Scoreboard()
car_manager = CarManager()
grid_field = GridField()

screen.listen()
screen.onkeypress(turtle_player.step, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            score.game_over()
            game_is_on = False

    if turtle_player.finish():
        score.level += 1
        score.write_score()
        car_manager.axelerate()

screen.exitonclick()
