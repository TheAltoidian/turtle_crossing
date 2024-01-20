from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.up()
            color = COLORS[randint(0, len(COLORS)-1)]
            new_car.color(color)
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.goto(x=300, y=randint(-240, 240))
            new_car.speed("fastest")
            new_car.left(180)
            new_car.finished = False
            self.car_list.append(new_car)

    def go(self):
        for car in self.car_list:
            car.forward(self.speed)
            car.finished = self.check_end_of_screen(car.xcor())
        self.clear_cars()

    def clear_cars(self):
        reversed_list = self.car_list[::-1]
        i = len(self.car_list)-1
        for car in reversed_list:
            if car.finished:
                self.car_list[i].reset()
                self.car_list[i].hideturtle()
                self.car_list.pop(i)
            else:
                i -= 1


    def collision(self, turtle_location):
        splat = False
        for car in self.car_list:
            if -20 < car.xcor() < 20:
                distance = abs(car.ycor() - turtle_location)
                if distance < 15:
                    splat = True
        return splat

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def check_end_of_screen(self, position):
        if position < -310:
            return True
        else:
            return False
