from turtle import Turtle, Screen
from random import randint


def init_turtle(x, y, color):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

all_turtles = [
    init_turtle(-230, 150, "red"),
    init_turtle(-230, 100, "green"),
    init_turtle(-230, 50, "purple"),
    init_turtle(-230, 0, "grey"),
    init_turtle(-230, -50, "yellow"),
    init_turtle(-230, -100, "blue"),
    init_turtle(-230, -150, "pink")]

finished = False
while not finished:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            finished = True
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You've won!")
            else:
                print(f"You've lost! Winner was {winner}")
        turtle.forward(randint(0, 10))

screen.exitonclick()
