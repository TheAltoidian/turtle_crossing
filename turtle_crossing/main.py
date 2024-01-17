import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_list = []
car_list.append(CarManager())
screen.listen()

screen.onkey(key="w", fun=player.move)
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    for car in car_list:
        car.go()
    # randomly decide to generate car
    time.sleep(0.1)
    screen.update()
    if player.at_finish():
        scoreboard.update_scoreboard()
#       increase car speed
#     elif collision:
#         game_is_on = False
#       display game over

screen.exitonclick()
