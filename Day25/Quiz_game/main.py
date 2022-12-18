import pandas
import turtle

screen = turtle.Screen()

screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_stated = []

while len(guessed_stated) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_stated)}/50 Guess the State",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_list = [state for state in all_states if state not in guessed_stated]
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_stated.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  # grab first index .item()

turtle.exitonclick()
