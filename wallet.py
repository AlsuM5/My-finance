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

    def __sub__(self, other):
        self.add_expenses(other)
        return self


class Expens:
    def __init__(self, value, type="расходы", date=None):
        self.value = value
        self.type = type
        self.date = date or datetime.utcnow()
        self.futured = self.date > datetime.utcnow()
