from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.goto(STARTING_POSITION)

    def up(self):
        self.setposition(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def has_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(STARTING_POSITION)