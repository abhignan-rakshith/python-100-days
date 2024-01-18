import turtle
import pandas

# Setting up the screen
screen = turtle.Screen()
screen.title("Indian States and Capitals Game")
screen.setup(width=800, height=900)
image = "blank_Indian_states.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# Importing states data
state_data = pandas.read_csv("28_states.csv")
number_of_states = len(state_data.state)

# Game Logic...goes on until 'exit' command
state_guesses = []
capital_guesses = []
while len(state_guesses) < number_of_states:
    answer_state = screen.textinput(f"{len(state_guesses)}/{number_of_states} States Correct",
                                    "What's another state's name?").title()
    if answer_state == 'Exit':
        break

    # Check if the state is in the data
    current_state = state_data[state_data.state == answer_state]

    if not current_state.empty:
        state_guesses.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(current_state.iat[0, 1], current_state.iat[0, 2])
        state_turtle.write(answer_state, align="center", font=("Arial", 10, "normal"))

        # Guess the capital
        answer_capital = screen.textinput(f"Guess the capital of {answer_state}",
                                          "What's the capital?").title()
        if answer_capital == current_state.iat[0, 3]:
            capital_guesses.append(answer_capital)
            state_turtle.setheading(270)
            state_turtle.forward(15)
            state_turtle.color("green")
            state_turtle.write(answer_capital, align="center", font=("Arial", 8, "normal"))
        else:
            state_turtle.setheading(270)
            state_turtle.forward(15)
            state_turtle.color("red")
            state_turtle.write(current_state.iat[0, 3], align="center", font=("Arial", 8, "normal"))

        screen.update()

# States to learn extracted into csv:
states_to_learn_df = state_data[~state_data.state.isin(state_guesses)]
states_to_learn_df.state.to_csv("states_to_learn.csv", index=False, header=False)

# Capitals to learn extracted into csv:
capitals_to_learn_df = state_data[~state_data.capital.isin(capital_guesses)]
capitals_to_learn_df.capital.to_csv("capitals_to_learn.csv", index=False, header=False)


