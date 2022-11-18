from turtle import Turtle, Screen

paras_the_turtle = Turtle()
paras_the_turtle.shape("turtle")
paras_the_turtle.color("DarkOrchid2", "cyan")
loop = 0

for i in range(0, 4):
    paras_the_turtle.right(90)
    paras_the_turtle.forward(150)

hold_screen = Screen()
hold_screen.exitonclick()
