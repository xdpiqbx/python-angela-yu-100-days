from tkinter import Tk, PhotoImage, Canvas, Label, Button
from pomodoro_timer import PomodoroTimer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CANVAS_CENTER = {"x": int(CANVAS_WIDTH / 2), "y": int(CANVAS_HEIGHT / 2)}

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

TOMATO_IMAGE = PhotoImage(file="tomato.png")

canvas = Canvas(
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    highlightthickness=0,
    bg=YELLOW
)
canvas.create_image(
    CANVAS_CENTER["x"],
    CANVAS_CENTER["y"],
    image=TOMATO_IMAGE
)
timer_text = canvas.create_text(
    CANVAS_CENTER["x"],
    CANVAS_CENTER["y"] + 20,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# ----- Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "normal"))
check_mark.grid(column=1, row=3)

# ----- PomodoroTimer
pomodoro = PomodoroTimer(canvas, window, timer_text, timer_label, check_mark)

# ----- Button
start_button = Button(text="Start", command=pomodoro.start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=pomodoro.reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
