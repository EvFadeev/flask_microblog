from app import app
from flask import render_template

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

@app.route('/index')
def epta():
    user = {'username':'Pidrilla'}
    posts = [
        {
            'author': {'username': 'PIDARAS'},
            'body': 'ХУЯСЕ!'
        },
        {
            'author': {'username': 'ЕБУ'},
            'body': 'ЕПТАТЬ'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)
