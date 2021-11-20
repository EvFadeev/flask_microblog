from enum import unique
from operator import index
from app import db

# база данных пользователя
class User(db.Model):
    # создание полей базы данных
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # сообщает как печатать объекты данного класса (полезно при отладке)
    def __repr__(self):
        return '<User {}>'.format(self.username)