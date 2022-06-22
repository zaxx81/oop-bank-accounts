from classes.account import Account

class CheckingAccount(Account):

  def __init__(self, id, balance, open_date) -> None:
    super().__init__(id, balance, open_date)
    self.check_counter = 0

  def withdraw(self, amount):
    withdraw_fee = 1
    try:
      if (self.balance - amount) < withdraw_fee:
        raise Exception(f'Withdrawal Error: Balance may be below $10')
      print(f'Withdrawing ${amount} plus a $2 fee from your account...')
      self.balance -= (amount + withdraw_fee)
      self.show_balance()
    except:
      print(f'Invalid withdrawal amount! Your balance is ${self.balance}.')

  def withdraw_using_check(self, amount):
    check_limit = 3
    transaction_fee = 2
    transaction_amount = amount
    self.check_counter += 1
    
    if self.check_counter > check_limit:
      transaction_amount += transaction_fee
      print("made it here")
    
    try:
      if (self.balance - transaction_amount) < -10:
        raise Exception('Check Writing Error: Balance may be overdrafted by more than $10')
      print(f'Writing a check in the ${transaction_amount} from your account...')
      self.balance -= transaction_amount
      self.show_balance()
    except:
      print(f'Invalid withdrawal amount! Your balance is ${self.balance}.')

  def reset_checks(self):
    self.check_counter = 0