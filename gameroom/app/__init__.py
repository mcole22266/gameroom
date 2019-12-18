from flask import Flask, render_template, redirect, url_for, request

from .models import User
from .forms import SignInForm, CreateUserForm
from .extensions import database_ready


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        from .models import db
        db.init_app(app)

        from flask_wtf.csrf import CSRFProtect
        CSRFProtect(app)

        if database_ready(db, app):
            db.create_all()
            db.session.commit()

        @app.route('/')
        def index():
            return render_template('index.html',
                                   title='Game Room')

        @app.route('/user/signin', methods=['GET', 'POST'])
        def user_signin():
            form = SignInForm()

            # POST
            if form.validate_on_submit():
                uname = request.form.get('uname')
                pword = request.form.get('pword')
                app.logger.info(f'Username: {uname} | Password: {pword}')
                return redirect(url_for('index'))

            # GET
            return render_template('signin.html',
                                   title="Game Room - Sign In",
                                   form=form)

        @app.route('/user/create', methods=['GET', 'POST'])
        def user_create():
            form = CreateUserForm()

            # POST
            if form.validate_on_submit():
                fname = request.form.get('fname')
                lname = request.form.get('lname')
                email = request.form.get('email')
                uname = request.form.get('uname')
                pword = request.form.get('pword')
                app.logger.info(f'Creating account for {uname} <{email}>')
                return redirect(url_for('index'))

            # GET
            return render_template('createuser.html',
                                   title="Game Room - Create Account",
                                   form=form)

        return app
