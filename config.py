# класс для хранения переменных конфигурации
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Параметры конфигурации определяются как переменные класса внутри класса Config
class Config(object):
    # переменная конфигурации SECRET_KEY используется в качестве криптографического ключа,
    # полезного для генерации подписей или токенов. Flask-WTF использует его для защиты веб-форм
    # от атаки Cross-Site Request Forgery или CSRF (произносится как «seasurf») 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # отключить функцию Flask-SQLAlchemy которая должна сигнализировать приложению каждый раз, 
    # когда в базе данных должно быть внесено изменение
    SQLALCHEMY_TRACK_MODIFICATIONS = False

