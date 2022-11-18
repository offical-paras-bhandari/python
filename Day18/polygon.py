from turtle import Turtle, Screen

turt = Turtle()
turt.shape("turtle")
turt.color("DarkOrchid2", "cyan")
loop = 0

for _ in range(0,3):
    turt.color("red")
    turt.forward(100)
    turt.right(120)
turt.forward(100)

for _ in range(0,4):
    turt.color("grey")
    turt.right(90)
    turt.forward(100)

for _ in range(0,5):
    turt.color("brown")
    turt.right(72)
    turt.forward(100)

for _ in range(0,6):
    turt.color("purple")
    turt.right(60)
    turt.forward(100)

for _ in range(0,7):
    turt.color("green")
    turt.right(51.42)
    turt.forward(100)


for _ in range(0,8):
    turt.color("cyan3")
    turt.right(45)
    turt.forward(100)

for _ in range(0,9):
    turt.color("cyan")
    turt.right(40)
    turt.forward(100)

for _ in range(0,10):
    turt.color("DarkOrange")
    turt.right(36)
    turt.forward(100)



hold_screen = Screen()
hold_screen.exitonclick()
