class BankAccount:
    """Управління банківським рахунком"""
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def deposit(self, amount: float):
        """Поповнення банківського рахунку."""
        if amount <= 0:
            raise ValueError("Сума депозиту повинна бути більше нуля.")
        self.balance += amount

    def withdraw(self, amount: float):
        """Зняття готівки з рахунку за умови, наявності коштів."""
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути більше нуля.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Перевірка банансу банківського рахунку."""
        return self.balance
