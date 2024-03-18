from flask import Flask, render_template
from datetime import datetime
import random
import requests


app = Flask(__name__)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    result = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    json = result.json()
    return render_template("blog.html", posts=json)


@app.route('/guess/<string:name>')
def process(name):
    result = requests.get(f"https://api.genderize.io?name={name}")
    # {
    #   "name": "peter",
    #   "gender": "male",
    #   "probability": 0.99,
    #   "count": 165452
    # }
    json = result.json()

    result = requests.get(f"https://api.agify.io?name={name}")
    # {
    #     "age": 62,
    #     "count": 298219,
    #     "name": "michael"
    # }
    json2 = result.json()

    return render_template("guess.html", name=json['name'], gender=json['gender'], age=json2['age'])

@app.route('/')
def hello_world():
    return render_template("index.html", num=random.randint(0, 10), yyyy=datetime.today().year)


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
