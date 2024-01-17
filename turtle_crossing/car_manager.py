from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        color = COLORS[randint(0,len(COLORS)-1)]
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.goto(x=300, y=randint(30,260))
        self.speed("fastest")
        self.left(180)
        self.current_speed = STARTING_MOVE_DISTANCE

    def go(self):
        self.forward(self.current_speed)
    #     check if at end of screen, if so, delete car

    def speed_up(self):
        self.current_speed += MOVE_INCREMENT

