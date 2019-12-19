from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer,
                   primary_key=True)

    fname = db.Column(db.String(80))

    lname = db.Column(db.String(80))

    email = db.Column(db.String(80),
                      unique=True,
                      nullable=False)

    uname = db.Column(db.String(80),
                      unique=True,
                      nullable=False)

    pword = db.Column(db.String(80),
                      nullable=False)

    created_on = db.Column(db.DateTime,
                           nullable=False)

    active = db.Column(db.Boolean,
                       default=True,
                       nullable=False)

    admin = db.Column(db.Boolean,
                      default=False,
                      nullable=False)

    def __init__(self, uname, pword, email,
                 fname=None, lname=None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.uname = uname,
        self.pword = pword,
        self.created_on = datetime.now()

    def __repr__(self):
        return f'User: {self.uname} <{self.email}> created on \
                {str(self.created_on)}'
