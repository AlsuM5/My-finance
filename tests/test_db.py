from model import add_wallet, Wallet, dump_wallet, load_wallet
from webapp.wallet import Wallet as WalletWeb


def test_create_wallet(db_session):
    wallet_db = add_wallet(3000)
    db_session.add(wallet_db)
    db_session.commit()

    assert wallet_db.id == 1

    wallet = Wallet.query.filter_by(id=1).one()

    assert wallet.balance == 3000


def test_dump_wallet(db_session):
    wallet = WalletWeb(initial_balance=2500)
    wallet_db = dump_wallet(wallet)
    db_session.add(wallet_db)
    db_session.commit()

    assert wallet_db.id == 1


def test_load_wallet(db_session):
    wallet_db_test = add_wallet(3000)
    db_session.add(wallet_db_test)
    db_session.commit()

    wallet = load_wallet(wallet_db_test.id)

    assert wallet.balance == 3000
