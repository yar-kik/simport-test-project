from wsgi import app
from utils import db

books_list = []

with app.app_context():
    db.session.add_all(books_list)
    db.session.commit()
