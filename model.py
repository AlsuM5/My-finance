from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

from db import Base, engine
from sqlalchemy.orm import relationship


class Wallet:
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    reserved_balance = Column(String)
    days_count_to_end = Column(Integer)
    transactions = Column(Float)
    transaction_id = relationship("Transaction", lazy="joined")

    def __repr__(self):
        return f"Wallet id {self.id}, balance {self.balance}"


class Transaction:
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    date = Column(Date)
    type_expense = Column(String)
    wallet = relationship("Wallet")

    def __repr__(self):
        return f"Transactions id {self.id}, balance {self.value}"


if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)
