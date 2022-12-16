import pandas
import turtle
from turtle import *

screen = Screen()
gif = Turtle()
name_of_state = Turtle()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)

gif.shape(image)

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()# alternative to exit onclick

score = 0
total = 50
df = pandas.read_csv("50_states.csv")
# searching data based on answer
game_is_on = True
while game_is_on:
    answer = ""
    answer = screen.textinput(title=f"{score}/{total} Guess the Name", prompt="What's another states name")
    data = df.state.to_list()
    answer_title_case = answer.title()

    if answer_title_case in data:
        state_data = df[df.state == answer_title_case]
        x_cord = int(state_data.x)
        y_cord = int(state_data.y)
        name_of_state.penup()
        name_of_state.hideturtle()
        name_of_state.goto(x_cord, y_cord)
        name_of_state.write(f"{answer_title_case}")
        score += 1

    if score == len(data):
        game_is_on = False

turtle.mainloop()
