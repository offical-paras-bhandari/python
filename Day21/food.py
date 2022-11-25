from turtle import Turtle
import random


# inheritance from Superclass which is Turtle
# self is object or instance of Food class which is able to access parent class (Turtle)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)