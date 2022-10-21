from datetime import datetime


class Wallet:
    def __init__(self, days_count_to_end=30, initial_balance=0):
        self.expenses = []
        self.balance = initial_balance
        self.reserved_balance = 0
        self.days_count_to_end = days_count_to_end
        self.schedule_expenses = []

    def add_expenses(self, expens):
        self.expenses.append(expens)
        self.balance -= expens.value

    def get_balance(self):
        return self.balance

    def get_daily_allowance(self):
        return self.balance / self.days_count_to_end

    def add_schedule_expenses(self, schedule_expens):
        self.schedule_expenses.append(schedule_expens)

    def is_on_trec(self):
        pass


class Expens:
    def __init__(self, value):
        self.value = value
        self.date = datetime.utcnow()


class Transaction:
    def __init__(self, value):
        self.value = value
        self.date = datetime.utcnow()

    def get_value(self):
        return self.value

    def __add__(self, other):
        return self.value + other.value 
