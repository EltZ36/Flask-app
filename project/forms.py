from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateTimeField, IntegerField, PasswordField,
                     RadioField, StringField, SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length)
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    firstname = StringField('Email',
                        validators=[DataRequired(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
