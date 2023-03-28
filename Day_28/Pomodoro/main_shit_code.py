from tkinter import Tk, PhotoImage, Canvas, Label, Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CANVAS_CENTER = {"x": int(CANVAS_WIDTH / 2), "y": int(CANVAS_HEIGHT / 2)}

timer = None
reps = 0
marks = 0
is_timer_started = False
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global is_timer_started
    global reps
    global marks
    if is_timer_started:
        return
    is_timer_started = True
    reps += 1
    count_time = 60

    if reps % 8 == 0:
        count_time *= LONG_BREAK_MIN
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_time *= SHORT_BREAK_MIN
        timer_label.config(text="Break", fg=PINK)
    else:
        marks += 1
        count_time *= WORK_MIN
        timer_label.config(text="To Work", fg=GREEN)
        check_mark.config(text="✓"*marks)

    count_down(count_time)

def reset_timer():
    global timer
    if timer is not None:
        global is_timer_started
        global reps
        global marks
        is_timer_started = False
        reps = 0
        marks = 0
        window.after_cancel(timer)
        timer_label.config(text="Timer")
        check_mark.config(text="")
        canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    minutes = str(math.floor(count / 60))
    seconds = str(math.floor(count % 60))
    if len(seconds) == 1:
        seconds = "0"+seconds
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

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

# ----- Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
