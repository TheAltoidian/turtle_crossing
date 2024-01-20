from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.teleport(-280, 260)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        (self.write(f"Level {self.level}", font=FONT))

    def game_over(self):
        end_text = Turtle()
        end_text.up()
        end_text.write("GAME OVER", align="center", font=FONT)
