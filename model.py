from sqlalchemy import Column, Integer,String, Date, Float, ForeignKey
#from db import Base, engine
import sqlite3
from constants import dbFile
from sqlalchemy.orm import relationship


class Wallet():
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    reserved_balance = Column(String)
    days_count_to_end = Column(Integer)
    expenses = Column(Float)
    transaction = relationship('Transaction', lazy='joined')

    def __repr__(self):
        return f'Wallet id {self.id}, balance {self.balance}'


class Transaction():
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    #value_id = Column(Integer,ForeignKey(Wallet.id),index=True,nullabel=False)
    value = Column(Float)
    date = Column(Date)
    type_expense = Column(String)
    wallet = relationship('Wallet')


if __name__ == '__main__':
    
    #Base.metadata.create_all(bind=engine)
    conn = sqlite3.connect(dbFile)
    conn.cursor()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Wallet (
            id INT NOT NULL PRIMARY KEY,
            balance FLOAT,
            reserved_balance TEXT,
            days_count_to_end INT,
            expenses FLOAT)''')
        conn.commit()
        conn.execute('''CREATE TABLE IF NOT EXISTS Transactions (
            id INT NOT NULL PRIMARY KEY,
            value FLOAT,
            date DATE,
            type_expense TEXT,
            wallet_id INT NOT NULL,
            FOREIGN KEY (wallet_id) REFERENCES Wallet (id))''')
        
    conn.close()

