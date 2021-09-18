from Q2.BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, interestRate, balance=0):
        super().__init__(balance)
        self.rate = interestRate

    def addInterest(self):
        interest = super().getBalance() * self.rate / 100;
        super().deposit(interest);

    def __str__(self):
        return super().__str__()
