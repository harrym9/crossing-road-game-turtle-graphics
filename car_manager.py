import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car = None
        self.x_pos = None
        self.y_pos = None
        self.starting_move = 5
        self.make_a_car()

    def make_a_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.color(random.choice(COLORS))
        self.car.setheading(180)
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.x_pos = 320
        self.y_pos = random.randint(-250, 250)
        self.car.goto(self.x_pos, self.y_pos)
        self.cars.append(self.car)

    def start_move(self):
        for car in self.cars:
            car.forward(self.starting_move)

    def increase_cars_speed(self):
        self.starting_move += MOVE_INCREMENT
