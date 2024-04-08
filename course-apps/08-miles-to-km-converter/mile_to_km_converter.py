import tkinter
from tkinter import *


def button_clicked():
    value = round(float(input.get()) * 1.609)
    label_value.config(text=f"{value}")


window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=10)

input = Entry(width=10)
input.grid(column=1, row=0)

label = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
label.grid(column=2, row=0)

label = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
label.grid(column=0, row=1)

label_value = tkinter.Label(text="value", font=("Arial", 14, "normal"))
label_value.grid(column=1, row=1)

label = tkinter.Label(text="Km", font=("Arial", 14, "normal"))
label.grid(column=2, row=1)

button = Button(text="Calculate", command= button_clicked)
button.grid(column=1, row=3)

window.mainloop()


