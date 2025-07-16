from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_turtles = []

move_y = -150
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()

    new_turtle.goto(x=-230, y=move_y)
    move_y += 30
    list_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won!!, winner turtle: {winning_color}")
            else:
                print(f"youve lost!!, winner turtle: {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
