import turtle
from turtle import Turtle, Screen

roy = Turtle()
screen = Screen()

roy.shape("turtle")


def moveforward():
    roy.forward(20)
    roy.color("green", "blue")


def movebackward():
    roy.backward(20)
    roy.color("blue")


def turnright():
    current_heading = roy.heading() - 10
    roy.setheading(current_heading)


def turnleft():
    current_heading = roy.heading() + 10
    roy.setheading(current_heading)


def clear():
    roy.clear()
    roy.penup()
    roy.home()


screen.listen()
screen.onkey(key="w", fun=moveforward)
screen.onkey(key="s", fun=movebackward)
screen.onkey(key="d", fun=turnright)
screen.onkey(key="a", fun=turnleft)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
