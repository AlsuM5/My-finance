from sqlalchemy import Column, Integer,String, Date, Float,Boolean
from db import Base, engine


class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    reserved_balance = Column(String)
    days_count_to_end = Column(Integer)
    expenses = Column(Float)

    def __repr__(self):
        return f'Wallet id {self.id}, balance {self.balance}'


class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    value = Column(Float)
    date = Column(Date)
    type_expense = Column(String)
    futured = Column(Boolean)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)