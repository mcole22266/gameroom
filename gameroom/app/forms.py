from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (InputRequired, Length, Email,
                                EqualTo, Optional, ValidationError
                                )

from .models import User


def usernameTaken(form, field):
    if User.query.filter_by(uname=field.data).first():
        raise ValidationError('That username is already taken.')


def emailExists(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('There is already an account associated with \
                              this email address.')


class SignInForm(FlaskForm):

    uname = StringField('Username', validators=[
        InputRequired(message='A Username is required.'),
        Length(min=5, message='Username must be at least six characters.')
    ])

    pword = PasswordField('Password', validators=[
        InputRequired(message='A password is required.')
    ])

    submit = SubmitField('Sign In')


class CreateUserForm(FlaskForm):

    fname = StringField('First Name', validators=[
        Length(max=50,
               message='First name cannot be longer than 50 characters'),
        Optional()
    ], render_kw={"placeholder": "Optional"})

    lname = StringField('Last Name', validators=[
        Length(max=50,
               message='Last name cannot be longer than 50 characters'),
        Optional()
    ], render_kw={"placeholder": "Optional"})

    email = StringField('Email', validators=[
        InputRequired(message='An Email is required.'),
        Length(min=6, message='Email must be at least six characters.'),
        Email(message='A valid Email is required.'),
        emailExists
    ])

    uname = StringField('Username', validators=[
        InputRequired(message='You must pick a username.'),
        Length(min=6, max=20,
               message='Usernames must be between six and twenty characters.'),
        usernameTaken
    ])

    pword = PasswordField('Password', validators=[
        InputRequired(message='You must pick a password.'),
        EqualTo('pwordConfirm', 'Your passwords do not match.')
    ])

    pwordConfirm = PasswordField('Confirm Password', validators=[
        InputRequired(message='You must confirm your password'),
        EqualTo('pword', 'Your passwords do not match.')
    ])

    submit = SubmitField('Create Account')
