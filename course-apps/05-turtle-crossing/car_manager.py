from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_inc = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(260, random.randint(-250, 250))
        car.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(car)

    def update(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_inc
            if new_x > -350:
                car.goto(new_x, car.ycor())
            else:
                self.cars.remove(car)
        if random.randint(0, 4) == 1:
            self.add_car()


