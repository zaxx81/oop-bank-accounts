from argparse import ArgumentError
from classes.account import Account

class SavingsAccount(Account):

  def __init__(self, id, balance, open_date) -> None:
    super().__init__(id, balance, open_date)
    self.minimum_balance = 10

  def withdraw(self, amount):
    withdraw_fee = 2
    try:
      if (self.balance - amount) < 10 + withdraw_fee:
        raise Exception(f'Withdrawal Error: Balance may not be below ${self.minimum_balance}')
      print(f'Withdrawing ${amount} plus a ${withdraw_fee} fee from your account...')
      self.balance -= (amount + withdraw_fee)
      self.show_balance()
    except:
      print('Invalid withdrawal amount!')
      self.show_balance()
      

  def add_interest(self, rate):
    interest = self.balance * rate
    self.balance += interest
    return interest