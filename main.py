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
screen.onkey(key="Up", fun=turtle.move_up)
screen.onkey(key="Down", fun=turtle.move_down)

cars = CarManager()

counter_for_car = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter_for_car == 5:  # add new car every 6th loop
        cars.make_a_car()
        counter_for_car = 0
    cars.start_move()

    # Detect when turtle(player) reach the finish.
    if turtle.ycor() >= 280:
        turtle.reset_finish()
        cars.increase_cars_speed()

    counter_for_car += 1
