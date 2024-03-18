from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))
