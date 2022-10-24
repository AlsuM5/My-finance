from datetime import datetime


class Wallet:
    def __init__(
        self, days_count_to_end=30, initial_balance=0, percent_of_savings=10
    ):
        self.expenses = []
        self.transactions = []
        self.balance = initial_balance
        self.reserved_balance = 0
        self.days_count_to_end = days_count_to_end
        self.schedule_expenses = []
        self.percent_of_savings = percent_of_savings

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

    def get_amount_of_savings(self, value_income):
        """метод, который возвращает сумму отложений в зависимости от заданных
        процента (percent_of_savings по умолчанию 10%) отложений,
        (Доход(value_income)-плановые расходы(sum(schedule_expenses)))"""
        if 0 < self.percent_of_savings < 100:
            return (
                self.percent_of_savings
                * (value_income - sum(self.schedule_expenses))
                / 100
            )
        raise PercentError("Процент отложений должен быть от 0 до 100")

    def add_transaction(self, value, type="расходы", date=None):
        transaction_class = 0
        if value > 0:
            transaction_class = Income
        else:
            transaction_class = Expens

        transaction = transaction_class(value)
        self.transactions.append(transaction)
        self.balance += transaction.value


class WalletBaseException(Exception):
    pass


class PercentError(WalletBaseException):
    pass


class Transaction:
    def __init__(self, value, type="расходы", date=None):
        self.value = value
        self.type = type
        self.date = date or datetime.utcnow()
        self.futured = self.date > datetime.utcnow()

    def get_value(self):
        return self.value

    def __add__(self, other):
        return self.value + other.value


class Expens(Transaction):
    pass


class Income(Transaction):
    pass
