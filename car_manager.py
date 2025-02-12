import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.starting_speed = 5

    def make_a_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        x_pos = 320
        y_pos = random.randint(-250, 250)
        new_car.goto(x_pos, y_pos)
        self.cars.append(new_car)

    def start_move(self):
        for car in self.cars:
            car.forward(self.starting_speed)

    def increase_cars_speed(self):
        self.starting_speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.cars:
            if player.distance(car) <= 25:
                return True
        return False
