import random
from tkinter import Tk, PhotoImage, Canvas, Button
import pandas

CANVAS_IMAGE_WIDTH = 800
CANVAS_IMAGE_HEIGHT = 526

CARD_FRONT_IMAGE = "images/card_front.png"
CARD_BACK_IMAGE = "images/card_back.png"
YES_IMAGE = "images/right.png"  # ✅
NO_IMAGE = "images/wrong.png"   # ❌

CSV_FILE = "data/french_words.csv"
CSV_WORDS_TO_LEARN = "data/words_to_learn.csv"

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"

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

words_list_to_learn = {}
word_item = {}

def create_words_to_learn():
    pandas.DataFrame(pandas.read_csv(CSV_FILE)).to_csv(CSV_WORDS_TO_LEARN, index=False)
    return pandas.read_csv(CSV_WORDS_TO_LEARN).to_dict(orient="records")

try:
    words_list_to_learn = pandas.read_csv(CSV_WORDS_TO_LEARN).to_dict(orient="records")
except FileNotFoundError:
    words_list_to_learn = create_words_to_learn()
except pandas.errors.EmptyDataError:
    words_list_to_learn = create_words_to_learn()


# ---------- words_to_learn.csv ----------
def known_word():
    try:
        words_list_to_learn.remove(word_item)
        pandas.DataFrame(words_list_to_learn).to_csv(CSV_WORDS_TO_LEARN, index=False)
        next_word()
    except IndexError:
        card_canvas.itemconfig(language_text_canvas, text="French / English", fill=BLACK)
        card_canvas.itemconfig(word_text_canvas, text="that's all!", fill=BLACK)
        card_canvas.itemconfig(card_on_bg, image=CARD_PHOTO_IMAGE_F)
    except ValueError:
        print("Value error")
    except AttributeError:
        print("Attribute Error")


# ---------- NEXT WORD ----------
def next_word():
    global word_item
    global flip_timer
    window.after_cancel(flip_timer)
    try:
        word_item = random.choice(words_list_to_learn)
        card_canvas.itemconfig(language_text_canvas, text="French", fill=BLACK)
        card_canvas.itemconfig(word_text_canvas, text=word_item["French"], fill=BLACK)
        card_canvas.itemconfig(card_on_bg, image=CARD_PHOTO_IMAGE_F)
        flip_timer = window.after(3000, func=flip_card)
    except KeyError:
        print("word_item does not exists")
    except IndexError:
        print("All Done =)")
        window.destroy()



# ---------- FLIP CARD ----------
def flip_card():
    global word_item
    card_canvas.itemconfig(language_text_canvas, text="English", fill=WHITE)
    card_canvas.itemconfig(word_text_canvas, text=word_item["English"], fill=WHITE)
    card_canvas.itemconfig(card_on_bg, image=CARD_PHOTO_IMAGE_B)


window = Tk()
window.title("Flash Cards")
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

CARD_PHOTO_IMAGE_F = PhotoImage(file=CARD_FRONT_IMAGE)
CARD_PHOTO_IMAGE_B = PhotoImage(file=CARD_BACK_IMAGE)

flip_timer = window.after(3000, func=flip_card)

card_canvas = Canvas(
    width=CANVAS_IMAGE_WIDTH,
    height=CANVAS_IMAGE_HEIGHT,
    highlightthickness=0,
    bg=BACKGROUND_COLOR
)

card_on_bg = card_canvas.create_image(
    CANVAS_IMAGE_WIDTH/2,
    CANVAS_IMAGE_HEIGHT/2,
    image=CARD_PHOTO_IMAGE_F
)

language_text_canvas = card_canvas.create_text(400, 150, text="Placeholder", font=FONT_LANGUAGE)
word_text_canvas = card_canvas.create_text(400, 263, text="Placeholder", font=FONT_WORD)

card_canvas.grid(row=0, column=0, columnspan=2)

# ----- Button
YES = PhotoImage(file=YES_IMAGE)
yes_button = Button(image=YES, command=known_word, highlightthickness=0)
yes_button.grid(row=1, column=0)

NO = PhotoImage(file=NO_IMAGE)
no_button = Button(image=NO, command=next_word, highlightthickness=0)
no_button.grid(row=1, column=1)

next_word()

window.mainloop()
