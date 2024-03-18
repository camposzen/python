from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.h_direction = 10
        self.v_direction = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.h_direction, self.ycor() + self.v_direction)

    def bounce_y(self):
        self.v_direction *= -1

    def bounce_x(self):
        self.h_direction *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1


