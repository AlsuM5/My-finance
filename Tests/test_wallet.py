from wallet import Wallet, Expens


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expense(Expens(100))
    wallet.add_schedel_expense(199)
    assert wallet.get_daily_allowance() == 330
