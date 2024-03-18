import tkinter
from tkinter import *


def button_clicked():
    print("clicked")
    text = input.get()
    label.config(text=f"{text}")


window = tkinter.Tk()
window.title("Tittle oxe")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

button = Button(text="Button", command= button_clicked)
button.grid(column=1, row=1)


button = Button(text="New Button")
button.grid(column=3, row=0)

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()


