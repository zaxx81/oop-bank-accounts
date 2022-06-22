from argparse import ArgumentError
from classes.account import Account

class MoneyMarketAccount(Account):
  def __init__(self, id, balance, open_date) -> None:
    super().__init__(id, balance, open_date)
    self.minimum_balance = 10000
    self.transactions_counter = 0
    self.check_min()

  def withdraw(self, amount):
    withdraw_fee = 100
    if self.transactions_counter > 5:
      print('Sorry, you have reached the maximum number of transactions this month')
    else:
      try:
        if (self.balance - amount) < self.minimum_balance:
          raise Exception()
        self.balance -= amount
      except:
        self.balance -= (amount + withdraw_fee)
        print(f'Warning: Balances below ${self.minimum_balance} will incur a fee of ${withdraw_fee}')
        print(f'Withdrawing ${amount} plus a ${withdraw_fee} fee from your account...')
      finally:
        self.transactions_counter += 1
        self.show_balance()

  def deposit(self, amount):
    if self.transactions_counter > 5:
      print('Sorry, you have reached the maximum number of transactions this month')
    else:
      print(f'Depositing ${amount} from your account...')
      self.balance += amount
      self.transactions_counter += 1
      self.show_balance()

  def add_interest(self, rate):
    interest = self.balance * rate
    self.balance += interest
    return interest

  def reset_transactions(self):
    self.transactions_counter = 0
      