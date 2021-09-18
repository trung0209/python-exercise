from Q2.BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self,balance):
        super().__init__(balance)
        self.transactionCount = 0

    def withdraw(self,amount):
        self.transactionCount += 1
        super().withdraw(amount)

    def deposit(self,amount):
        self.transactionCount += 1
        super().deposit(amount)

    def deductFees(self):
        if (self.transactionCount > 10):
            fees = 1 * (self.transactionCount -10);
            super().withdraw(fees);
        self.transactionCount = 0

    def __str__(self):
        return super().__str__()