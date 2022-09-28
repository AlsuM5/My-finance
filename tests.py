from wallet import Wallet, Expens


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expens(Expens(100))
    wallet.add_schedel_expens(199)
    assert wallet.get_daily_allowance() == 330
