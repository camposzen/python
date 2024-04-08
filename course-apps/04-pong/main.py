from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(365, 0, "white")
l_paddle = Paddle(-375, 0, "white")
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # collision with top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with r_paddle
    if ball.xcor() > 340 and ball.distance(r_paddle.position()) < 50 or \
            ball.xcor() < -350 and ball.distance(l_paddle.position()) < 50:
        ball.bounce_x()

    # r_paddle misses
    if ball.xcor() > 370:
        ball.reset()
        scoreboard.l_point()

    # l_paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
