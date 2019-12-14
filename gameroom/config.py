from os import urandom, environ


class Config:

    # app config
    SECRET_KEY = urandom(32)
    FLASK_APP = environ["FLASK_APP"]
    FLASK_ENV = environ["FLASK_ENV"]
    FLASK_DEBUG = environ['FLASK_DEBUG']
    FLASK_HOST = environ['FLASK_HOST']
    FLASK_PORT = environ['FLASK_PORT']

    # mysql config
    MYSQL_DATABASE = environ['MYSQL_DATABASE']
    MYSQL_ROOT_PASSWORD = environ['MYSQL_ROOT_PASSWORD']

    # sqlalchemy config
    SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = environ['SQLALCHEMY_TRACK_MODIFICATIONS']
