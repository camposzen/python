from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave fields empty.")
    else:
        try:
            with open("my_passwords.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("my_passwords.json", "w") as append_file:
                json.dump(new_data, append_file, indent=4)
        else:
            data.update(new_data)
            with open("my_passwords.json", "w") as append_file:
                json.dump(data, append_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search():
    try:
        with open("my_passwords.json", "r") as read_file:
            data = json.load(read_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No passwords found!")
    else:
        website = website_input.get()
        if website in data:
            website_data = data[website]
            username_input.delete(0, END)
            password_input.delete(0, END)
            username_input.insert(0, website_data["email"])
            password_input.insert(0, website_data["password"])
            pyperclip.copy(password_input.get())
            messagebox.showinfo(title="Ok", message="Password ready to CRTL/CMD + V")
            website_input.focus()
        else:
            messagebox.showinfo(title="Oops", message="Website password hasn't been saved yet.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_level = Label(text="Password")
password_level.grid(row=3, column=0)

website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "john.doe@email.com")

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

gen_button = Button(text="Generate", command=generate)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

window.mainloop()