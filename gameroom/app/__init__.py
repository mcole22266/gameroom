from flask import Flask, render_template

from .models import User
from .extensions import database_ready


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        from .models import db
        db.init_app(app)

        if database_ready(db, app):
            db.create_all()
            db.session.commit()

        @app.route('/')
        def index():
            return render_template('index.html', title='Game Room')

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
