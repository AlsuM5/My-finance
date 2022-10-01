from wallet import Wallet, Expens


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expenses(Expens(100))
    wallet.add_schedule_expenses(199)
    assert wallet.get_daily_allowance() == 330
