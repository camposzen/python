from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Da Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()

    # collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
