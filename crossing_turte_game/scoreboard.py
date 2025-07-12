from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 230)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def points(self):
        self.score += 1
        self.update_score()
