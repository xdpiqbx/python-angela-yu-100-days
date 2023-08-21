from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# with app.app_context():
#     db.create_all()
#     try:
#         new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#         db.session.add(new_book)
#         db.session.commit()
#     except IntegrityError as error:
#         print(error)

# Pride and Prejudice | Jane Austen | 8
# 1984 | George Orwell | 9
# Crime and Punishment | Fyodor Dostoevsky | 8
# Hamlet | William Shakespeare | 7
# One Hundred Years of Solitude | Gabriel García Márquez | 6

@app.route('/')
def home():
    all_books = db.session.execute(
        db.select(Book).order_by(Book.title)
    ).scalars()
    return render_template('index.html', books=list(all_books))


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        db.session.add(Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        ))
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit_rating", methods=['GET', 'POST'])
def edit_rating():
    if request.method == 'POST':
        book_to_update: Book = db.get_or_404(Book, request.form['id'])

        # Old style
        # book_to_update: Book = db.session.execute(
        #     db.select(Book).where(Book.id == request.form['id'])
        # ).scalar()

        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.to_dict().get('id')
    if not book_id:
        return redirect(url_for('home'))

    book = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()

    return render_template('edit_rating.html', book=book)


@app.route("/delete_book", methods=['GET'])
def delete_book():
    book_id = request.args.to_dict().get('id')
    if not book_id:
        return redirect(url_for('home'))

    book_to_delete = db.get_or_404(Book, book_id)

    # Old style
    # book_to_delete = db.session.execute(
    #     db.select(Book).where(Book.id == book_id)
    # ).scalar()

    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
