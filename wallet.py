from datetime import datetime


class Wallet:
    def __init__(self, days_count_to_end=30, initial_balance=0):
        self.expenses = []
        self.balance = initial_balance
        self.reserved_balance = 0
        self.days_count_to_end = days_count_to_end
        self.scheduel_expense = []

    def add_expens(self, expens):
        self.expenses.append(expens)
        self.balance -= expens.value

    def get_balance(self):
        return self.balance

    def get_daily_allowance(self):
        return self.balance / self.days_count_to_end

    def add_schedel_expens(self, scheduel_expens):
        self.scheduel_expense.append(scheduel_expens)

    def is_on_trec(self):
        pass


class Expens:
    def __init__(self, value):
        self.value = value
        self.date = datetime.utcnow()


if __name__ == "__main__":
    wallet = Wallet(initial_balance=10000)
    wallet.add_expens(Expens(100))
    wallet.add_schedel_expens(199)
    print(wallet.get_daily_allowance())
