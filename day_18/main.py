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


angles = [0, 90, 180, 270]
turt.pensize(15)
turt.speed("fastest")

for _ in range(300):
    turt.color(random_color())
    turt.forward(30)
    turt.setheading(random.choice(angles))

screen = t.Screen()
screen.screensize(2000, 1500)

turt.screen.mainloop()
