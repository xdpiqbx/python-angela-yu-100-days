from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km Converter")

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 150

FONT = ("Arial", 14, "normal")

window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.config(padx=45, pady=30)

# ----- Labels
is_equal_to = Label(text="is equal to:", font=FONT)
is_equal_to.grid(column=0, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)


# ----- Button
def calculate():
    miles = int(input.get())
    res = int(miles * 1.609344)
    result_label.config(text=res)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# ----- Entry
input = Entry(width=10)
# input.pack()
input.grid(column=1, row=0)

window.mainloop()
