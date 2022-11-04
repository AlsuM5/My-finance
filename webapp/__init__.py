from flask import Flask, render_template

from webapp.wallet import Wallet
from webapp.forms import LoginForm, RegistrationForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

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

    @app.route("/register")
    def register():
        form = RegistrationForm()
        title = "Регистрация"
        return render_template(
            "user/registration.html", page_title=title, form=form
        )

    @app.route("/wallets/<wallet_id>")
    def load_wallet(wallet_id):
        page_title = "My wallet"
        wallet_id = load_wallet()
        return Wallet(
            "page/index.html", page_title=page_title, id=wallet_id
        )

    return app
