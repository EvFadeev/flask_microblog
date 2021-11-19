from flask.typing import TemplateFilterCallable
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
def index():
    user = {'username':'Evgeny'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # получение данных формы
    if form.validate_on_submit():
        # flash() — полезный способ показать сообщение пользователю
        # Многие приложения используют эту технику, 
        # чтобы сообщить пользователю, было ли какое-либо действие успешным или нет
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


