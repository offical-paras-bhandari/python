from turtle import Screen
import turtle as t
import random

turt = t.Turtle()
t.colormode(255)
turt.pensize(2)
turt.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


for _ in range(72):
    turt.color(random_color())
    turt.circle(200)
    turt.left(5)
turt.hideturtle()

hold_screen = Screen()
hold_screen.exitonclick()
