from argparse import ArgumentError
import csv
import os.path
from classes.owner import Owner

class Account:

  def __init__(self, id, balance, open_date) -> None:
    self.id = int(id)
    self.balance = balance
    self.open_date = open_date
    self.owner = None
    self.minimum_balance = 0
    self.check_min()
    
  def check_min(self):
    try:
      if int(self.balance) < self.minimum_balance:
        raise ArgumentError(f'Opening Balance Error: Balance may not be negative')
    except:
      print('Sorry, you need at least ${:,.2f} to open an account'.format(self.minimum_balance))
  
  def __str__(self) -> str:
    return f'Account ID: {self.id}, Balance: {self.balance}'

  def withdraw(self, amount):
    try:
      if (self.balance - amount) < 0:
        raise Exception(f'Withdrawal Error: Balance may not be negative')
      print(f'Withdrawing ${amount} from your account...')
      self.balance -= amount
      self.show_balance()
    except:
      print('Invalid withdrawal amount!')
      self.show_balance()

  def deposit(self, amount):
    print(f'Depositing ${amount} from your account...')
    self.balance += amount
    self.show_balance()

  def show_balance(self):
    output = '${:,.2f}'.format(self.balance)
    print(f'Your current balance is {output}')

  @staticmethod
  def all_accounts():
    accounts = []

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../support/accounts.csv")
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            accounts.append(Account(*row))
    return accounts
