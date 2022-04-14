from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, \
    BooleanField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Электронная почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    pwcheck = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField('Электронная почта или имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class TeacherForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    patronymic = StringField('Отчество', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class AuditForm(FlaskForm):
    number = IntegerField('Номер', validators=[DataRequired()])
    volume = IntegerField('Вместимость', validators=[DataRequired()])
    submit = SubmitField('Добавить')
