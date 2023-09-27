import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")


guessed_state = []
number_guessed = 0
unguessed_states = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{number_guessed}/50 States Correct", prompt="What's another state's name?").title()
    all_states = data.state.to_list()
    if answer_state == "Exit":
        for states in all_states:
            if states not in guessed_state:
                unguessed_states.append(states)
        df = pandas.DataFrame(unguessed_states)
        df.to_csv("States_To_Learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(f"{state_data.state.item()}", align="center")
        guessed_state.append(answer_state)
        number_guessed += 1









