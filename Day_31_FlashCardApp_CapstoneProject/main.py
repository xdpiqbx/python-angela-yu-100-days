import random
from tkinter import Tk, PhotoImage, Canvas, Button, Label
import pandas

CANVAS_IMAGE_WIDTH = 800
CANVAS_IMAGE_HEIGHT = 526
CARD_FRONT_IMAGE = "images/card_front.png"
CARD_BACK_IMAGE = "images/card_back.png"
YES_IMAGE = "images/right.png"  # ✅
NO_IMAGE = "images/wrong.png"   # ❌
CSV_FILE = "data/french_words.csv"
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"
FONT_LANGUAGE = (FONT_NAME, 40, "italic")
FONT_WORD = (FONT_NAME, 60, "bold")
WINDOW_PADDING = 50
LABEL_LANGUAGE_POSITION = {
    "x": CANVAS_IMAGE_WIDTH / 2,
    "y": 150
}
LABEL_WORD_POSITION = {
    "x": CANVAS_IMAGE_WIDTH / 2,
    "y": 263
}

data = pandas.read_csv(CSV_FILE)
words_list_with_translate = data.to_dict(orient="records")


# ---------- NEXT WORD ----------
def next_word():
    word_item = random.choice(words_list_with_translate)
    canvas.itemconfig(language_text_canvas, text="French")
    canvas.itemconfig(word_text_canvas, text=word_item["French"])


window = Tk()
window.title("Flash Cards")
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

CARD_IMAGE = PhotoImage(file=CARD_FRONT_IMAGE)

canvas = Canvas(
    width=CANVAS_IMAGE_WIDTH,
    height=CANVAS_IMAGE_HEIGHT,
    highlightthickness=0,
    bg=BACKGROUND_COLOR
)

canvas.create_image(
    CANVAS_IMAGE_WIDTH/2,
    CANVAS_IMAGE_HEIGHT/2,
    image=CARD_IMAGE
)

language_text_canvas = canvas.create_text(400, 150, text="Placeholder", font=FONT_LANGUAGE)
word_text_canvas = canvas.create_text(400, 263, text="Placeholder", font=FONT_WORD)

canvas.grid(row=0, column=0, columnspan=2)

# ----- Button
YES = PhotoImage(file=YES_IMAGE)
yes_button = Button(image=YES, command=next_word, highlightthickness=0)
yes_button.grid(row=1, column=0)

NO = PhotoImage(file=NO_IMAGE)
no_button = Button(image=NO, command=next_word, highlightthickness=0)
no_button.grid(row=1, column=1)

next_word()

window.mainloop()
