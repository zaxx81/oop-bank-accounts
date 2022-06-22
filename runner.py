from classes.bank import Bank
from classes.account import Account
from classes.owner import Owner
from classes.savings_account import SavingsAccount
from classes.checking_account import CheckingAccount
from classes.money_market_account import MoneyMarketAccount

# ===CSV Test Cases===
# my_bank = Bank("USBB")

# print('\n===Account Test Cases===')
# myAccount = Account(1234, -8.00, "Today")
# myAccount = Account(1234, 8.00, "Today")
# myAccount.withdraw(90)
# myAccount.deposit(500)
# myAccount.withdraw(100)

# print("\n===SavingsAccount Test Cases===")
# mySavingsAccount = SavingsAccount(1234, 8, "Today")
# mySavingsAccount = SavingsAccount(1234, 10000, "Today")
# print('You accrued ${:,.2f} in interest'.format(mySavingsAccount.add_interest(0.0025)))
# mySavingsAccount.show_balance()

# print('\n===Owner Test Cases===')
# myAccount1 = Account(1234, 8.00, "Today")
# owner1 = Owner(14,'Morales','Wanda','9003 Gerald Hill','Honolulu','Hawaii')
# print(owner1)
# myAccount1.owner = owner1
# print(myAccount1.owner)

# print('\n===CheckingAccount Test Cases===')
# myAccount = CheckingAccount(1234, -100, "Today")
# myAccount = CheckingAccount(1234, 100, "Today")
# myAccount.withdraw_using_check(20)
# myAccount.withdraw_using_check(20)
# myAccount.withdraw_using_check(20)
# myAccount.reset_checks()
# myAccount.withdraw_using_check(20)

# print('\n===MoneyMarketAccount Test Cases===')
# myMoneyMarketAccount = MoneyMarketAccount(1234,1000, "Today")
# myMoneyMarketAccount = MoneyMarketAccount(1234,10000, "Today")
# myMoneyMarketAccount.withdraw(1000)
# myMoneyMarketAccount.deposit(5000)
# myMoneyMarketAccount.withdraw(1000)
# myMoneyMarketAccount.deposit(5000)
# myMoneyMarketAccount.deposit(5000)
# myMoneyMarketAccount.deposit(5000)
# myMoneyMarketAccount.withdraw(10000)
# print('You accrued ${:,.2f} in interest'.format(myMoneyMarketAccount.add_interest(0.0025)))