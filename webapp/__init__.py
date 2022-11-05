from flask import Flask, render_template  # redirect

from webapp.wallet import Wallet
from webapp.forms import LoginForm, RegistrationForm  # AddTransactionForm

# import model


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

    def load_wallet(wallet_id):
        return Wallet(id=wallet_id)

    @app.route("/wallets/<wallet_id>")
    def get_wallet(wallet_id):
        page_title = "My wallet"
        wallet = load_wallet(wallet_id)
        return render_template(
            "page/index.html", page_title=page_title, wallet=wallet
        )

    # @app.route("wallets/<wallet_id>/add_transaction")
    # def add_transaction(wallet_id, methods=["GET", "POST"]):
    #     page_title = "Add transaction"
    #     transaction_form = AddTransactionForm()
    #     if request.method == "POST":
    #         wallet = model.load_wallet(wallet_id)
    #         wallet_db = model.dump_wallet(wallet)
    #         return redirect("/")
    #     return render_template(
    #         "page/add_transaction.html",
    #         page_title=page_title,
    #         form=transaction_form,
    #     )

    return app
