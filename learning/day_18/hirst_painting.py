import colorgram
import random
import turtle as t


def select_colors(image: str, number: int):
    colors = colorgram.extract(f"/home/imanol/Downloads/{image}", number)

    colores = []
    for i in colors:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        new_color = (r, g, b)
        colores.append(new_color)

    return colores


colores = select_colors("colori_pastello.jpg", 30)

t.colormode(255)
tim = t.Turtle()

tim.speed("fast")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(500)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colores))
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
