from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fordward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    new = tim.heading() + 10
    tim.setheading(new)


def turn_left():
    new = tim.heading() - 10
    tim.setheading(new)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fordward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
