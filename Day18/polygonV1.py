import turtle as t
import random

turt = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turt.forward(100)
        turt.right(angle)
        num_sides += 1


for shapes_sides in range(3, 11):
    turt.color(random.choice(colours))
    draw_shapes(shapes_sides)
