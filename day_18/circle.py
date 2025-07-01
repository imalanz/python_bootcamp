import turtle as t
import random

turt = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


turt.pensize(1)
turt.speed("fastest")


def draw(size):
    for _ in range(int(360 / size)):
        turt.color(random_color())
        turt.circle(200)
        turt.setheading(turt.heading() + size)


draw(5)
screen = t.Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
