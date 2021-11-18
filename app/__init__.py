from flask import Flask
from config import Config

app = Flask(__name__)

# добавление конфигурации
""" app.config['SECRET_KEY'] = 'you-will-never-guess' """
# ... add more variables here as needed

# читаем и применяем файл конфигурации
app.config.from_object(Config)

from app import routes