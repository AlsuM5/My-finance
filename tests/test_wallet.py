import pytest
from wallet import PercentError, Wallet, Expens


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expenses(Expens(100))
    wallet.add_schedule_expenses(199)
    assert wallet.get_daily_allowance() == 330


def test_amount_of_savings1():
    wallet = Wallet()
    assert wallet.get_amount_of_savings(30000) == 3000


def test_amount_of_saving2():
    wallet = Wallet()
    wallet.percent_of_savings = 120
    with pytest.raises(PercentError) as excinfo:
        wallet.get_amount_of_savings(30000)
    assert isinstance(excinfo.value, PercentError)
