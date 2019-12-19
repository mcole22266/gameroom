from flask import Flask, render_template, redirect, url_for, request, flash

from flask_login import current_user, login_required, login_user, logout_user

from .models import User
from .forms import SignInForm, CreateUserForm
from .extensions import database_ready, login_manager


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

        login_manager.init_app(app)

        if database_ready(db, app):
            db.create_all()
            if not User.query.filter_by(uname='admin').first():
                adminUser = User('admin', 'adminpass',
                                 'mcole042891@gmail.com',
                                 is_admin=True)
                db.session.add(adminUser)
            db.session.commit()

        @app.route('/')
        def index():
            return render_template('index.html',
                                   title='Game Room')

        @app.route('/user/signin', methods=['GET', 'POST'])
        def user_signin():
            if current_user.is_authenticated:
                return redirect(url_for('index'))
            form = SignInForm()

            # POST
            if form.validate_on_submit():
                uname = request.form.get('uname')
                pword = request.form.get('pword')
                user = User.query.filter_by(uname=uname).first()
                if not user or not user.pwordCheck(pword):
                    flash('Invalid username or password')
                    return redirect(url_for('user_signin'))
                else:
                    login_user(user)
                    return redirect(url_for('index'))
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
                fname = fname if fname else None  # force null
                lname = request.form.get('lname')
                lname = lname if lname else None  # force null
                email = request.form.get('email')
                uname = request.form.get('uname')
                pword = request.form.get('pword')
                app.logger.info(f'Creating account for {uname} <{email}>')
                user = User(uname, pword, email, fname, lname)
                db.session.add(user)
                db.session.commit()
                flash('Account Created!')
                return redirect(url_for('user_signin'))

            # GET
            return render_template('createuser.html',
                                   title="Game Room - Create Account",
                                   form=form)

        @app.route('/user/logout')
        @login_required
        def user_logout():
            logout_user()
            flash('Successfully logged out')
            return redirect(url_for('index'))

        return app
