
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, validators, BooleanField


class LoginForm(FlaskForm):
	username = StringField('Username',[validators.DataRequired(),validators.Length(min=4, max=25)])
	password = PasswordField('Password',[
        validators.DataRequired(),
		validators.Length(min=8, max=20)
    ])

class RegForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
		validators.Length(min=8, max=20)
    ])
    confirm = PasswordField('Repeat Password',[validators.DataRequired(),validators.Length(min=8, max=20)])