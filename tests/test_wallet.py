import pytest
from wallet import Income, PercentError, Wallet, Transaction
from datetime import datetime, timedelta


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.create_transaction(-100)
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


def test_transaction_date():
    transaction = Transaction(-50, date=datetime.utcnow())
    assert transaction.date == datetime.utcnow()


def test_transaction_in_the_future():
    date = datetime.utcnow() + timedelta(days=1)
    transaction = Transaction(50, date=date)
    assert transaction.futured is True


def test_transaction():
    wallet = Wallet(initial_balance=100)
    wallet.create_transaction(100)
    transaction = wallet.transactions[0]
    assert isinstance(transaction, Income)
    assert wallet.get_balance() == 200


def test_transaction_total_expense():
    wallet = Wallet(initial_balance=100)
    wallet.create_transaction(100)
    wallet.create_transaction(-19)
    wallet.create_transaction(-20)
    wallet.create_transaction(210)
    assert wallet.total_value_expense == 39
    assert wallet.total_value_income == 310


def test_transaction_total_income():
    pass
