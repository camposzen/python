import tkinter
from tkinter import *


def button_clicked():
    value = float(input.get()) * 0.25
    label_value.config(text=f"{value}")


window = tkinter.Tk()
window.title("Flour to Coconut Flour converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

input = Entry(width=5)
input.grid(column=1, row=0)

label = tkinter.Label(text="Flour cup(s)", font=("Arial", 14, "normal"))
label.grid(column=2, row=0, sticky="w")

label = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
label.grid(column=0, row=1)

label_value = tkinter.Label(text="value", font=("Arial", 14, "normal"))
label_value.grid(column=1, row=1)

label = tkinter.Label(text="Coconut flour cup(s)", font=("Arial", 14, "normal"))
label.grid(column=2, row=1)

button = Button(text="Calculate", command= button_clicked)
button.grid(column=1, row=3)

window.mainloop()


