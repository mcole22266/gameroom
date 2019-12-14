from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():

        @app.route('/')
        def index():
            return 'Hello World'

        @app.route('/test/db/view')
        def test_db_view():
            return 'test_db_view'

        @app.route('/test/db/add/<col1>/<col2>')
        def test_db_add(col1, col2):
            return f'test_db_add: col1={col1} col2={col2}'

        return app
