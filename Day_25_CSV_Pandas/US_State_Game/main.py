import turtle
import pandas

from inscription import Inscription

CSV_FILE = "50_states.csv"
FONT = ("Courier", 20, "bold")

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. Status Game")
screen.setup(725, 491)

screen.addshape(IMAGE)
turtle.shape(IMAGE)

inscription = Inscription()


def get_state_from_csv(answer):
    data = pandas.read_csv(CSV_FILE)
    result = data[data["state"] == answer]
    if not result.empty:
        return {
            # "state": result.state.to_string(index=False),
            "state": result.state.item(),
            "x": int(result.x),
            "y": int(result.y),
        }
    else:
        return {}


def save_states_to_learn(answers):
    data = pandas.read_csv(CSV_FILE)
    csv_states = data.state.to_list()
    difference = [state for state in csv_states if (state not in answers)]
    data = pandas.DataFrame({"states": difference})
    data.to_csv("states_to_learn.csv")


title = "Guess the state"
right_answers = []
while True:
    answer_state = screen.textinput(title=title, prompt="What's another state name?").capitalize()
    if answer_state == "Q":
        save_states_to_learn(right_answers)
        break
    if not (answer_state in right_answers):
        data_from_csv = get_state_from_csv(answer_state)
        if data_from_csv:
            inscription.write_on_map(data_from_csv)
            right_answers.append(answer_state)
            title = f"{len(right_answers)}/50 States Correct"

# def get_mouse_click_coords(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coords)
# turtle.mainloop()
