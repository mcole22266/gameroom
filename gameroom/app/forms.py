from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class SignInForm(FlaskForm):

    uname = StringField('Username', validators=[
        InputRequired(message='A Username is required.'),
        Length(min=5, message='Username must be at least six characters.')
    ])

    pword = PasswordField('Password', validators=[
        InputRequired(message='A password is required.')
    ])

    submit = SubmitField('Sign In')
