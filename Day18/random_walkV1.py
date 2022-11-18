from turtle import *
import turtle as t
import random

t.colormode(255)  # generating color from 0 to 255
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuples = (r,g,b)
    return tuples


turt = Turtle()
turt.pensize(15)
turt.speed("fastest")
for _ in range(200):
    turt.color(random_color())
    turt.forward(30)
    # get random orientation
    turt.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
