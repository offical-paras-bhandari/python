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
    color = (r, g, b)
    return color


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        turt.color(random_color())
        turt.circle(200)
        current_heading = turt.heading()  # getting Current Heading
        turt.setheading(current_heading + size_of_graph)


draw_spirograph(5)

hold_screen = Screen()
hold_screen.exitonclick()
