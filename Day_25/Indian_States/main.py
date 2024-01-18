import turtle
import pandas

# Code to get states coords
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Setting up the screen
screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(width=800, height=900)
image = "blank_Indian_states.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# Importing states data
state_data = pandas.read_csv("28_states.csv")
number_of_states = len(state_data.state)

# Game Logic...goes on until 'exit' command
correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{len(correct_guesses)}/{number_of_states} States Correct",
                                    "What's another state's name?").title()
    if answer_state == 'Exit':
        break
    mask = state_data.state.isin([answer_state])
    current_state = state_data[mask]

    if not current_state.empty:
        correct_guesses.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(current_state.iat[0, 1], current_state.iat[0, 2])
        state_turtle.write(answer_state, align="center", font=("Arial", 10, "normal"))
        screen.update()

# States to learn extracted into csv:
mask2 = state_data.state.isin(correct_guesses)
states_to_learn_df = state_data[~mask2]
states_to_learn = states_to_learn_df.state.to_csv("states_to_learn.csv", index=False, header=False)
