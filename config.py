# класс для хранения переменных конфигурации
import os

# Параметры конфигурации определяются как переменные класса внутри класса Config
class Config(object):
    # переменная конфигурации SECRET_KEY используется в качестве криптографического ключа,
    # полезного для генерации подписей или токенов. Flask-WTF использует его для защиты веб-форм
    # от атаки Cross-Site Request Forgery или CSRF (произносится как «seasurf») 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

