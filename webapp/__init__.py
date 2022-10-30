from flask import Flask, render_template
from webapp.wallet import Wallet
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")


    @app.route('/')
    def index():
        page_title = "My wallet"
        wallet = Wallet(initial_balance=10000)
        return render_template('page/index.html', page_title=page_title, wallet=wallet)
    

    @app.route('/login')
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('user/login.html', page_title=title, form=login_form )

    return app
