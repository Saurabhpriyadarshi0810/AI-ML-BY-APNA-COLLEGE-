class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# Python doesn't have true private variables.

class Test:
    def __init__(self):
        self._x = 10

# Single underscore means: "Please don't access directly"


