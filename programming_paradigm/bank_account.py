class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        return self.amount + self.account_balance
    
    def withdraw(self, amount):
        self.amount = amount
        if self.account_balance <= 0:
            print("No balance in your account!")
        else:
            return self.account_balance - self.amount

    def display_balance(self):
        return self.account_balance
