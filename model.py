from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
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
    wallet_db = Wallet(balance=100000, days_count_to_end=30)
    db_session.add(wallet_db)
    db_session.commit()
    assert wallet_db.id == 1
