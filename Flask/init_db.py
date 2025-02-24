from app import app
from models import db, Book

with app.app_context():
    db.create_all()
    # Добавление книг в базу данных
    book1 = Book(title="Варяг", author="Говард Ф.Л.", genre="Историческая фантастика", cost=500)
    book2 = Book(title="Место для битвы", author="Мазин А.В.", genre="Историческая фантастика", cost=400)
    book3 = Book(title="Князь", author="Мазин А.В.", genre="Историческая фантастика", cost=600)
    book4 = Book(title="Кредо Викканки. Знаки и знамения", author="Мара Вульф", genre="Фэнтези", cost=850)
    book5 = Book(title="Кредо Викканки. Вина и грехи", author="Мара Вульф", genre="Фэнтези", cost=900)
    book6 = Book(title="Кредо Викканки. Месть и огонь", author="Мара Вульф", genre="Фэнтези", cost=1050)
    db.session.add_all([book1, book2, book3, book4, book5, book6])
    db.session.commit()