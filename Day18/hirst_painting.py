# TODO Extracted color form photos.
# import colorgram
# colors_collection = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuples = (r, g, b)
#     colors_collection.append(tuples)
# print(colors_collection)
# ------------This are Values-------------#
import turtle
from turtle import *
import random

colors = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124),
          (171, 153, 41),(136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148),
          (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89),
          (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209)]


def draw(x):
    turt.home()
    for _ in range(x):
        for _ in range(x):
            turt.dot(15,random.choice(colors))
            turt.penup()
            turt.forward(30)

        turt.setheading(90)
        turt.penup()
        turt.forward(30)
        turt.setheading(180)
        cordx = turt.xcor()
        (turt.setx(cordx - cordx))
        turt.setheading(360)
    turt.hideturtle()


turt = Turtle()
turt.speed("fastest")  # calls automatically because it is constructor
turtle.colormode(255)

draw(10)

hold_screen = Screen()
hold_screen.exitonclick()
