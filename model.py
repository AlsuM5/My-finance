from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from datetime import datetime
from db import Base, engine, db_session
from sqlalchemy.orm import relationship


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    reserved_balance = Column(String)
    days_count_to_end = Column(Integer)
    transactions = relationship("Transaction", back_populates="wallet")

    def __repr__(self):
        return f"Wallet id {self.id}, balance {self.balance}"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    date = Column(Date)
    type = Column(String)
    wallet_id = Column(Integer, ForeignKey(Wallet.id))
    wallet = relationship("Wallet", back_populates="transactions")

    def __repr__(self):
        return f"Transactions id {self.id}, balance {self.value}"


def create_data_base():

    Base.metadata.create_all(bind=engine)
    wallet_db = Wallet(balance=10000, days_count_to_end=30)
    db_session.add(wallet_db)
    db_session.commit()
    assert wallet_db.id == 1


def add_wallet(balance, days_count_to_end=30, reserved_balance=0):
    wallet_db = Wallet()
    wallet_db.balance = balance
    wallet_db.days_count_to_end = days_count_to_end
    wallet_db.reserved_balance = reserved_balance
    return wallet_db


def add_transaction(value, type, wallet_id, date=None):
    transaction = Transaction()
    transaction.value = value
    if date is None:
        transaction.date = datetime.utcnow()
    else:
        transaction.date = date
    transaction.type = type
    transaction.wallet_id = wallet_id
    return transaction


def dump_wallet(wallet):
    if not wallet.id:
        wallet_db = Wallet.query.filter(Wallet.id == wallet.id).first()
    else:
        wallet_db = add_wallet(
            wallet.balance, wallet.days_count_to_end, wallet.reserved_balance
        )
    for transaction in wallet.transactions:
        if not transaction:
            if not transaction.id:
                transaction = add_transaction(
                    transaction.value,
                    transaction.type,
                    wallet.id,
                    transaction.date,
                )

    return wallet_db


if __name__ == "__main__":
    create_data_base()
