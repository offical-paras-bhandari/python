import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet1 = screen.textinput(title="Make first bet", prompt="Which color of turtle will be a winner?")
user_bet2 = screen.textinput(title="Make second bet", prompt="Which color of turtle will be a winner?")
colors = ["red","blue"]
direction = [-100, -50]
all_turtles = []

for turtle_index in range(0, 2):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[0])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=direction[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet1 and user_bet2:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            print(turtle.color())#first Color is pencolor and second color is fill color.
            winning_color = turtle.pencolor()
            if winning_color == user_bet1:
                print(f"winner is {user_bet1} turtle")
            else:
                print(f"winner is {user_bet2} turtle")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
