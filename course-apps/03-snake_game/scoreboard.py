from turtle import Turtle


class Scoreboard:

    def __init__(self):
        super().__init__()
        self.score = -1

        with open("score.txt", "r") as file:
            self.highest_score = int(file.read())

        self.highest_score = 0
        self.board = Turtle()
        self.board.penup()
        self.board.hideturtle()
        self.board.color("grey")
        self.board.goto(0, -280)
        self.increase()

    def increase(self):
        self.score += 1
        self.board.clear()
        self.board.write(arg=f"Score: {self.score}, Highest Score: {self.highest_score}", align="center", font=("Helvetica", 15, "bold"))

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write(arg=f"GAME OVER", align="center", font=("Helvetica", 15, "bold"))

    def reset(self):
        if self.score > self.highest_score:
            with open("score.txt", "w") as file:
                file.write(f"{self.highest_score}")
            self.highest_score = self.score
        self.score = -1
        self.increase()
