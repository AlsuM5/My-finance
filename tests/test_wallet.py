from datetime import datetime, timedelta
from wallet import Wallet, Expens


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expenses(Expens(100))
    wallet.add_schedule_expenses(199)
    assert wallet.get_daily_allowance() == 330


def test_substraction_expens_from_wallet():
    wallet = Wallet(initial_balance=100)
    wallet -= Expens(50)
    assert wallet.get_balance() == 50


def test_expens_date():
    expens = Expens(50, date=datetime.utcnow())
    assert expens.date == datetime.utcnow()


def test_expens_in_the_future():
    date = datetime.utcnow() + timedelta(days=1)
    expens = Expens(50, date=date)
    assert expens.futured is True
