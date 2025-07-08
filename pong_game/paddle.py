from turtle import Turtle

RIGHT_PADDLE_POSITION = [(380, 0)]  # , (380, -20), (380, 20)]
LEFT_PADDLE_POSITION = [(-380, 0)]  # , (-380, -20), (-380, 20)]

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = self.create_paddle(position)

    def create_paddle(self, goto):
        for position in goto:
            self.add_segments(position)

    def add_segments(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
