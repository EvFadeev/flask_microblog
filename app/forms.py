# форма входа пользователя
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# форма входа пользователя с вводом имени и пароля
class LoginForm(FlaskForm):
    # Валидатор DataRequired проверяет, что поле не отправлено пустым
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # флажок "Запомнить меня"
    remember_me = BooleanField('Remember Me')
    # кнопка
    submit = SubmitField('Sign In')