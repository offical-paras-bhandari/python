import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkey(fun=player.move_up, key="Up")
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # refreshing every 0.1 second
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect when player finish the line
    if player.is_finish_the_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.score_increase()
screen.exitonclick()
