from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username =  StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    