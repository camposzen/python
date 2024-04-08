from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def process():
    print(request.form)
    login = request.form['username']
    secret = request.form['password']
    print(f"login:{login} secret:{secret}")
    return render_template("login.html", login=login, secret=secret)


if __name__ == "__main__":
    app.run(debug=True)
