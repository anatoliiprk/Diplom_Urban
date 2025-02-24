from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Book, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/books')
def books_page():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/add-to-basket/<int:book_id>')
@login_required
def add_to_basket(book_id):
    book = Book.query.get(book_id)
    current_user.basket.append(book)
    db.session.commit()
    return redirect(url_for('basket'))


@app.route('/basket')
@login_required
def basket():
    books = current_user.basket
    total_cost = sum(book.cost for book in books)
    return render_template('basket.html', books=books, total_cost=total_cost)


@app.route('/delete-from-basket/<int:book_id>')
@login_required
def delete_from_basket(book_id):
    book = Book.query.get(book_id)
    current_user.basket.remove(book)
    db.session.commit()
    return redirect(url_for('basket'))


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if len(username) <= 30 and password == confirm_password and len(password) >= 8 and age.isdigit() and len(
                age) <= 3:
            hashed_password = generate_password_hash(password, method='scrypt')
            new_user = User(username=username, password=hashed_password, age=int(age))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('main'))
    return render_template('sign_in.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
