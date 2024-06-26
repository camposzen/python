from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(app)


# create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

    # Create A New Record
    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

    # Read All Records
    all_books = db.session.query(Book).all()
    print(all_books)

    # Read A Particular Record By Query
    # book = Book.query.filter_by(title="Harry Potter").first()
    # print(book.title)

    # Update A Particular Record By Query
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()

    # Update A Record By PRIMARY KEY
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()

    # #Delete A Particular Record By PRIMARY KEY
    # book_id = 1
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()