from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(5,20)])
    email=StringField('Emailid',validators=[Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email=StringField('Emailid',validators=[Email()])
    password=PasswordField('Pass',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Login')