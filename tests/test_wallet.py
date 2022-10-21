from wallet import Wallet, Expens, Transaction


def test_wallet():
    wallet = Wallet(initial_balance=10000)
    wallet.add_expenses(Expens(100))
    wallet.add_schedule_expenses(199)
    assert wallet.get_daily_allowance() == 330


def test_sum_transaction():
    transaction = Transaction(10)
    transaction2 = Transaction(20)
    assert transaction + transaction2 == 30
