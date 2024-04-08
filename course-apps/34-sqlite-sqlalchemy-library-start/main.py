from flask import Flask, render_template, request, redirect, url_for
import flask_sqlalchemy
# import sqlite3

app = Flask(__name__)

all_books = []

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute(
#     "CREATE TABLE books "
#     "(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL,"
#     "rating FLOAT NOT NULL)"
# )
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


## CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: silence the deprecation warning in the console.

db = flask_sqlalchemy.SQLAlchemy(app)

# TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


def save(new_book):
    with app.app_context():
        db.session.add(new_book)
        db.session.commit()


@app.route('/')
def home():
    global all_books
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    print(request.form)
    if request.method == "GET":
        return render_template("add.html")
    else:
        new_book = \
            Book(title=request.form["book"], author=request.form["author"], rating=request.form["rating"])
        all_books.append({
            "title": request.form["book"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        })
        save(new_book)
        return render_template("index.html", books=all_books)


if __name__ == "__main__":
    app.run(debug=True)
