import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
all_cars = CarManager()
screen.listen()

screen.onkey(key="w", fun=player.move)
screen.onkey(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    all_cars.create_car()
    all_cars.go()
    time.sleep(0.1)
    screen.update()
    if player.at_finish():
        scoreboard.update_scoreboard()
        all_cars.speed_up()
    elif all_cars.collision(player.ycor()):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
