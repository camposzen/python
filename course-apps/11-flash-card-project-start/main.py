from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
curr_card = {}


def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=curr_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global curr_card
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=curr_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def mark_known():
    global curr_card
    to_learn.remove(curr_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg="white")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

yes_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=mark_known)
yes_button.grid(row=1, column=1)

next_card()
window.mainloop()
