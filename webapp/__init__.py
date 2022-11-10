from flask import Flask, render_template, flash, redirect, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user
)
from model import User
from webapp.decorators import admin_required

from model import load_wallet
from webapp.wallet import Wallet
from webapp.forms import LoginForm, RegistrationForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        page_title = "My wallet"
        wallet = Wallet(initial_balance=121222)
        return render_template(
            "page/index.html", page_title=page_title, wallet=wallet
        )

    @app.route("/login")
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template(
            "user/login.html", page_title=title, form=login_form
        )

    @app.route("/process-login", methods=['POST'])
    def process_login():
        if current_user.is_authenticated:
            return redirect(url_for("index"))
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash("Вы вошли на сайт")
                return redirect(url_for("index"))

        flash("Неправильное имя пользователя или пароль")
        return redirect(url_for("login"))

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("index"))

    @app.route("/admin")
    @admin_required
    def admin_index():
        title = "Панель управления"
        return render_template("admin/index.html", page_title=title)

    @app.route("/register")
    def register():
        form = RegistrationForm()
        title = "Регистрация"
        return render_template(
            "user/registration.html", page_title=title, form=form
        )

    @app.route("/wallets/<wallet_id>")
    def get_wallet(wallet_id):
        page_title = "My wallet"
        wallet = load_wallet(wallet_id)
        return render_template(
            "page/index.html", page_title=page_title, wallet=wallet
        )

    return app
