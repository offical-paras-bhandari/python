from turtle import *
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
turt = Turtle()
turt.pensize(10)
turt.speed(5)
for _ in range(50):
    random_color = random.choice(colours)
    turt.color(random_color)
    random_walk = random.randrange(0, 360, 90)
    turt.forward(20)
    turt.right(random_walk)

screen = Screen()
screen.exitonclick()
