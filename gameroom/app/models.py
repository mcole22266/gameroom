from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer,
                   primary_key=True)
    col1 = db.Column(db.String(128))
    col2 = db.Column(db.String(128))

    def __init__(self, col1, col2):
        self.col1 = col1
        self.col2 = col2

    def __repr__(self):
        return f'User: {self.col1} {self.col2}'
