from turtle import Turtle

FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.penup()
        self.hideturtle()
        self.goto(x=-260, y=250)
        self.write(arg=f"Level {self.level}", font=FONT)
