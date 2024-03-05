import turtle
import pandas as pd

# Setting up turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv('./50_states.csv')
all_states = states_data.state.to_list()

game_is_over = 0
correct_guesses = []

while len(correct_guesses) != 50:

    # Getting the state name from user
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Exit condition
    if answer_state == 'Exit':
        break

    # Checking the guess is in the list
    if answer_state in all_states:
        correct_guesses.append(answer_state)

        state = states_data[states_data['state'] == answer_state]

        # Creating a new turtle for the state name
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state.x), int(state.y))
        new_turtle.write(answer_state, align="center", font=('Arial', 8, 'normal'))

states_to_learn = list(set(all_states) - set(correct_guesses))
states_to_learn.sort()

states_data = {
    'state': states_to_learn,
}
states_df = pd.DataFrame(states_data)
states_df.to_csv('states_to_learn.csv')
