from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(STARTING_POSITION)
        self.speed("fastest")
        self.showturtle()

    def at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.level_start()
            return True
        else:
            return False

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_start(self):
        self.goto(STARTING_POSITION)