import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(key="Up", fun=turtle.move_up)

    # Detect when turtle(player) reach the finish.
    if turtle.ycor() >= 280:
        turtle.reset_finish()
