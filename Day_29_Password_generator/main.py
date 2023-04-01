from random import randint, choice, shuffle
from tkinter import Tk, PhotoImage, Canvas, Label, Button, Entry, StringVar, messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(0, randint(8, 18))]
    password_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(0, randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit():
    website = website_var.get().strip()
    email_username = email_username_var.get().strip()
    password = password_var.get().strip()

    if not website or not email_username or not password:
        messagebox.showinfo(
            title="Empty fields",
            message="Please don't leave any fields empty"
        )
        return

    is_ok = messagebox.askokcancel(
        title=f"{website}, add?",
        message=f"These are the details entered:\n"
                f"Email: {email_username}\n"
                f"Password: {password}\n"
                f"Is it ok to save?"
    )

    if not is_ok:
        return

    with open("data.txt", "a") as file:
        file.write(str(f"{website} | {email_username} | {password}\n"))
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
WHITE = "#ffffff"

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
CANVAS_CENTER = {"x": int(CANVAS_WIDTH / 2), "y": int(CANVAS_HEIGHT / 2)}

FONT_NAME = "Calibri"
MAIN_LABEL_FONT = (FONT_NAME, 10, "normal")

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg=WHITE)

LOCK_IMAGE = PhotoImage(file="logo.png")

canvas = Canvas(
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    highlightthickness=0,
    bg=WHITE
)
canvas.create_image(
    CANVAS_CENTER["x"],
    CANVAS_CENTER["y"],
    image=LOCK_IMAGE
)
canvas.grid(column=0, row=0, columnspan=3)

# ----- Label
website_label = Label(text="Website", bg=WHITE, font=MAIN_LABEL_FONT)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username", bg=WHITE, font=MAIN_LABEL_FONT)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password", bg=WHITE, font=MAIN_LABEL_FONT)
password_label.grid(column=0, row=3)

# ----- Input Fields
website_var = StringVar()
website_entry = Entry(window, width=35, textvariable=website_var, font=MAIN_LABEL_FONT)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_var = StringVar()
email_username_entry = Entry(window, width=35, textvariable=email_username_var, font=MAIN_LABEL_FONT)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "artem@mail.com")  # default entry

password_var = StringVar()
password_entry = Entry(window, width=18, textvariable=password_var, font=MAIN_LABEL_FONT)
password_entry.grid(column=1, row=3, columnspan=1)

# ----- Button
add_button = Button(text="Add", width=36, command=submit, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(text="Generate password", command=generate_password, highlightthickness=0)
generate_password_button.grid(column=2, row=3)

window.mainloop()
