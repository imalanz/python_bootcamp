import time
from turtle import Screen
from player import Player

from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_new_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            turtle.start_again()
            score.score = 0
            print("GAME OVER!")

    if turtle.ycor() > 280:
        score.points()
        turtle.start_again()
        cars.level_up()


screen.exitonclick()
