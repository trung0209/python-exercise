class BankAccount():
    def __init__(self,balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def __str__(self):
        return f"Balance: {self.balance}"

