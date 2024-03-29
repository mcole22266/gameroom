from os import urandom, environ


class Config:

    # app config
    SECRET_KEY = urandom(16)
    FLASK_APP = environ["FLASK_APP"]
    FLASK_ENV = environ["FLASK_ENV"]
    FLASK_DEBUG = environ['FLASK_DEBUG']
    FLASK_HOST = environ['FLASK_HOST']
    FLASK_PORT = environ['FLASK_PORT']

    DB_WAIT_INITIAL = environ['DB_WAIT_INITIAL']
    DB_WAIT_MULTIPLIER = environ['DB_WAIT_MULTIPLIER']
    DB_WAIT_MAX = environ['DB_WAIT_MAX']

    # mysql config
    MYSQL_DATABASE = environ['MYSQL_DATABASE']
    MYSQL_ROOT_PASSWORD = environ['MYSQL_ROOT_PASSWORD']

    # sqlalchemy config
    SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = environ['SQLALCHEMY_TRACK_MODIFICATIONS']
