from flask import Flask
import random

app = Flask(__name__)
current = -1

@app.route('/')
def home():
    global current
    current = random.randint(0, 9)
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Guess a number between 0 and 9!</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route("/<int:number>")
def greet(number):
    if number < current:
        return '<h1 style="text-align: center">Too low! Try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    elif number > current:
        return '<h1 style="text-align: center">Too high! Try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    else:
        return '<h1 style="text-align: center">Found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=False)
