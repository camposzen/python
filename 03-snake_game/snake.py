from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = -20
        for _ in range(3):
            self.add_segment((x, 0));
            x += 20

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.setposition(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            self.segments[s].setx(self.segments[s - 1].xcor())
            self.segments[s].sety(self.segments[s - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
