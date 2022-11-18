from turtle import Turtle, Screen

turtle = Turtle()
for _ in range(0, 50):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
hold_screen = Screen()
hold_screen.exitonclick()
# for _ in range(0,3):
#     print("Paras")
