from sqlalchemy.orm import backref
from app import db
from datetime import datetime

# база данных пользователя
class User(db.Model):
    # создание полей базы данных
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # представление о взаимоотношении между user и post ("один ко многим")
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # сообщает как печатать объекты данного класса (полезно при отладке)
    def __repr__(self):
        return '<User {}>'.format(self.username)

# база данных постов пользователей
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
