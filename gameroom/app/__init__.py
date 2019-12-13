from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():

        @app.route('/')
        def index():
            return 'Hello World'

        return app
