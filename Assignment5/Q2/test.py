from Q2.CheckingAccount import CheckingAccount
from Q2.SavingsAccount import SavingsAccount

mySavings = SavingsAccount(0.5);


accountChecking = CheckingAccount(100);

mySavings.deposit(10000);

# Transfer $2000

# mySavings.withdraw(2000);

accountChecking.deposit(2000);

accountChecking.withdraw(1500);

accountChecking.withdraw(80);

# Transfer $1000

# mySavings.withdraw(1000);

accountChecking.deposit(2000);

accountChecking.withdraw(400);
accountChecking.withdraw(400);


#end of month to test deduct fees and rate
# mySavings.addInterest();
accountChecking.deductFees();

# print(mySavings)
print(accountChecking)