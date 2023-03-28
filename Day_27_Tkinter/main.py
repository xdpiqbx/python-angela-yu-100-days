from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("First GUI App")

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.config(padx=100, pady=100)

# ----- Label
my_label = Label(text="The label", font=("Arial", 24, "bold"))
my_label.config(text="New text")  # my_label['text'] = "New text" - same result
# my_label.pack()  # my_label.pack(expand=True)  # alignment my_label.pack(side="left")
# my_label.place(x=100, y=25)
my_label.grid(column=0, row=0)

# ----- Button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# ----- Button
button = Button(text="New button")
# button.pack()
button.grid(column=2, row=0)

# ----- Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=3)

window.mainloop()

# pack - Geometry manager that packs around edges of the cavity
# place - Geometry manager for fixed or rubber-sheet placement
# grid - Geometry manager that arranges widgets in a grid
