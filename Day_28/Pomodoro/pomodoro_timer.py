import math
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MINUTE = 0.1

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class PomodoroTimer:
    def __init__(self, canvas, window, timer_text, timer_label, check_mark):
        self.canvas = canvas
        self.window = window
        self.timer_text = timer_text
        self.timer_label = timer_label
        self.check_mark = check_mark
        self.is_timer_started = False
        self.reps = 0
        self.marks = 0
        self.timer = None

    def count_down(self, count):
        minutes = str(math.floor(count / 60))
        seconds = str(math.floor(count % 60))
        if len(seconds) == 1:
            seconds = "0" + seconds
        self.canvas.itemconfig(self.timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.is_timer_started = False
            self.start_timer()

    def start_timer(self):
        if self.is_timer_started:
            return
        self.is_timer_started = True

        self.reps += 1
        count_time = MINUTE

        if self.reps % 8 == 0:
            count_time *= LONG_BREAK_MIN
            self.timer_label.config(text="Long Break", fg=RED)
        elif self.reps % 2 == 0:
            count_time *= SHORT_BREAK_MIN
            self.timer_label.config(text="Break", fg=PINK)
        else:
            self.marks += 1
            count_time *= WORK_MIN
            self.timer_label.config(text="To Work", fg=GREEN)
            self.check_mark.config(text="✓" * self.marks)

        self.is_timer_started = True
        self.count_down(count_time)

    def reset_timer(self):
        if self.timer is not None:
            self.reps = 0
            self.marks = 0
            self.window.after_cancel(self.timer)
            self.timer_label.config(text="Timer")
            self.check_mark.config(text="")
            self.canvas.itemconfig(self.timer_text, text="00:00")

