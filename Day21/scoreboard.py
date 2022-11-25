from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.pensize(100)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"ScoreBoard {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GameOver", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
