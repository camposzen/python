import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()
total = len(states)
# print(states)
# print(total)

screen = turtle.Screen()
screen.title("Guess U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def update_map(state):
    s = states_data[states_data.state == state.title()]
    turtle_state = turtle.Turtle()
    turtle_state.penup()
    turtle_state.hideturtle()
    turtle_state.goto(int(s["x"]), int(s["y"]))
    turtle_state.pencolor("green")
    turtle_state.write(arg=state, font=("Helvetica", 11, "bold"))


answer = screen.textinput(title="Guess State", prompt="State name?")
correct_answers = 0
game_over = False
while not game_over:
    if answer in states:
        correct_answers += 1
        update_map(answer)

    answer = screen.textinput(title=f"{correct_answers}/{total}", prompt="State name?")
    if correct_answers == len(states):
        game_over = True

screen.exitonclick()
