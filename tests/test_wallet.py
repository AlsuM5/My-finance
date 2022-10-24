import pytest
from wallet import Income, PercentError, Wallet, Expens, Transaction
from datetime import datetime, timedelta


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expenses(Expens(100))
    wallet.add_schedule_expenses(199)
    assert wallet.get_daily_allowance() == 330


def test_sum_transaction():
    transaction = Transaction(10)
    transaction2 = Transaction(20)
    assert transaction + transaction2 == 30


def test_amount_of_savings1():
    wallet = Wallet()
    assert wallet.get_amount_of_savings(30000) == 3000


def test_amount_of_saving2():
    wallet = Wallet()
    wallet.percent_of_savings = 120
    with pytest.raises(PercentError) as excinfo:
        wallet.get_amount_of_savings(30000)
    assert isinstance(excinfo.value, PercentError)


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


def test_transaction():
    wallet = Wallet(initial_balance=100)
    wallet.add_transaction(100)
    transaction = wallet.transactions[0]
    assert isinstance(transaction, Income)
    assert wallet.get_balance() == 200
