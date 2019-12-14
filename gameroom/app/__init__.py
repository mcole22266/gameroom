from flask import Flask

from .models import User


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        from .models import db
        db.init_app(app)
        db.create_all()
        db.session.commit()

        user1 = User('Michael', 'Cole')
        user2 = User('Chelsea', 'Givens')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        @app.route('/')
        def index():
            return 'Hello World'

        @app.route('/test/db/view')
        def test_db_view():
            results = User.query.all()
            return f'<p>{results}</p>'

        @app.route('/test/db/add/<col1>/<col2>')
        def test_db_add(col1, col2):
            user = User(col1, col2)
            db.session.add(user)
            db.session.commit()
            return f'test_db_add: col1={col1} col2={col2}'

        return app
